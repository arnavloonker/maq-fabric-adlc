# Runtime companions, not forks

Fabric expertise stays in the pinned `microsoft/skills-for-fabric` package and is called as a runtime companion. This package does not copy that upstream. Copying would freeze MIT prose here and hide which revision a consumer actually runs. The first companion is `spark-cli` for lakehouse, notebook, Spark job, and environment work.
