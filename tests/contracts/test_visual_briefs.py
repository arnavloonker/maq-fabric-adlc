"""Focused visual contracts: python tests\\contracts\\test_visual_briefs.py"""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / ".apm" / "skills"


def read_skill(name, filename):
    return (SKILLS / name / filename).read_text(encoding="utf-8")


class VisualBriefContracts(unittest.TestCase):
    def test_approach_wires_er_diagrams_into_the_specification(self):
        mode = read_skill("approach", "reference/data-model.md")
        self.assertIn("## ER diagrams", mode)
        for label in ("**Before**", "**After (proposed)**", "unknown", "not present"):
            with self.subTest(label=label):
                self.assertIn(label, mode)
        self.assertIn(
            "[data-model mode](data-model.md)",
            read_skill("approach", "reference/contract.md"),
        )
        self.assertIn("ER diagrams", read_skill("approach", "reference/procedure.md"))

    def test_er_example_defines_entities_keys_and_cardinalities(self):
        mode = read_skill("approach", "reference/data-model.md")
        diagrams = re.findall(r"```mermaid\n(erDiagram\n.*?)\n```", mode, re.S)
        self.assertEqual(len(diagrams), 1)
        diagram = diagrams[0]
        entities = dict(re.findall(r"^    (\w+) \{\n(.*?)^    \}", diagram, re.M | re.S))
        self.assertEqual(set(entities), {"CUSTOMER", "ORDER", "ORDER_ITEM", "PRODUCT"})
        required_attributes = {
            "CUSTOMER": ("int id PK", "string email UK", "datetime created_at"),
            "ORDER": ("int id PK", "int customer_id FK", "datetime placed_at"),
            "ORDER_ITEM": ("int order_id PK, FK", "int product_id PK, FK",
                           "int quantity", "decimal unit_price"),
            "PRODUCT": ("int id PK", "string sku UK", "decimal price"),
        }
        for entity, attributes in required_attributes.items():
            for attribute in attributes:
                with self.subTest(entity=entity, attribute=attribute):
                    self.assertIn(attribute, entities[entity])
        relationships = re.findall(r"^    (\w+) (\S+) (\w+) : (.+)$", diagram, re.M)
        self.assertEqual(relationships, [
            ("CUSTOMER", "||--o{", "ORDER", "places"),
            ("ORDER", "||--|{", "ORDER_ITEM", "contains"),
            ("PRODUCT", "||--o{", "ORDER_ITEM", '"appears in"'),
        ])
        self.assertNotIn(r"\_", diagram)
        self.assertIn("Synthetic example", mode)

    def test_code_diff_routes_to_format_appropriate_comparisons(self):
        entry = read_skill("code-diff", "SKILL.md")
        contract = read_skill("code-diff", "reference/contract.md")
        procedure = read_skill("code-diff", "reference/procedure.md")
        self.assertIn("paired Before/After views", entry)
        self.assertIn("Choose one format per change", contract)
        for text in (entry, contract, procedure):
            with self.subTest(text=text.splitlines()[0]):
                self.assertNotIn("with Mermaid only", text)
                for output_format in ("table", "artifact", "code"):
                    self.assertIn(output_format, text)
        self.assertIn("Before = target", contract)
        self.assertIn("After = source", contract)
        self.assertIn("not present", contract)
        self.assertIn("unavailable", contract)

    def test_template_has_paired_alternatives_not_mandatory_duplicates(self):
        template = read_skill("code-diff", "reference/brief-template.md")
        self.assertIn("remove the unused alternatives", template)
        for title in ("Table", "Artifact/diagram", "Code-block"):
            with self.subTest(format=title):
                heading = f"### {title} view (alternative)\n"
                self.assertIn(heading, template)
                section = template.split(heading, 1)[1]
                section = re.split(r"\n#{2,3} ", section, maxsplit=1)[0]
                self.assertIn("Before", section)
                self.assertIn("After", section)
        self.assertIn("**added**", template)
        self.assertIn('C2["Consumer (added)"]', template)
        self.assertIn("class C2 changed", template)

    def test_code_example_highlights_additions_and_preserves_context(self):
        template = read_skill("code-diff", "reference/brief-template.md")
        self.assertIn("### Code-block view (alternative)\n", template)
        section = template.split("### Code-block view (alternative)\n", 1)[1]
        blocks = re.findall(r"```diff\n(.*?)\n```", section, re.S)
        self.assertEqual(blocks, [" line 1\n line 2", " line 1\n line 2\n+line 3"])
        contract = read_skill("code-diff", "reference/contract.md")
        self.assertIn("`-` only in Before", contract)
        self.assertIn("`+` only in After", contract)
        self.assertIn("display markers, not source text", contract)


if __name__ == "__main__":
    unittest.main()
