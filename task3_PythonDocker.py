import docker

#יצירת דוקר חדש
client = docker.from_env()

#הרצת busybox ושמירת הקונטיינר באויר לשעה
container = client.containers.run(
    "busybox","sleep 3600",detach=True
)

print(f"Container started: {container.id}")

#הרצת פקודה בשביל לקבל את הhostname
result = container.exec_run("hostname")
print(f"Container hostname:{result.output.decode().strip()}")

#סגירת הקונטיינר
container.stop()
container.remove()
