# Installation of Apache Cassandra on Ubuntu WSL Using Docker

## 📌 Overview

This project demonstrates how to install **Apache Cassandra**, a distributed NoSQL database, on **Ubuntu WSL (Windows Subsystem for Linux)** using **Docker**. Running Cassandra inside Docker provides an isolated, lightweight, and portable environment without requiring a native installation.

---

## 🎯 Objective

- Install Apache Cassandra using Docker on Ubuntu WSL.
- Configure Docker for running Cassandra.
- Create a Docker Compose configuration.
- Start the Cassandra container.
- Install and connect using CQLSH.
- Verify the successful installation.

---

## 🛠️ Technologies Used

- Ubuntu WSL
- Docker
- Docker Compose
- Apache Cassandra
- CQLSH (Cassandra Query Language Shell)

---

## 📂 Project Structure

```
cassandra-exercise/
│── docker-compose.yml
│── cassandra-data/
│── scripts/
│── README.md
```

---

## 🚀 Installation Steps

### 1. Verify Ubuntu Installation

```bash
lsb_release -a
```

---

### 2. Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 3. Install Required Dependencies

```bash
sudo apt install -y \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release
```

---

### 4. Add Docker Repository

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

---

### 5. Install Docker

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

---

### 6. Configure Docker

```bash
sudo usermod -aG docker $USER
```

Restart the terminal or run:

```bash
newgrp docker
```

---

### 7. Create Project Directory

```bash
mkdir -p ~/cassandra-exercise
cd ~/cassandra-exercise
```

---

### 8. Create Docker Compose File

```bash
nano docker-compose.yml
```

---

### 9. Start Cassandra Container

```bash
docker compose up -d
```

Wait for approximately one minute:

```bash
sleep 60
```

---

### 10. Verify Cassandra Container

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker logs cassandra
```

---

### 11. Install CQLSH

Option 1:

```bash
sudo apt install -y python3-pip
pip3 install cqlsh
```

Option 2:

```bash
sudo apt install -y cassandra-tools
```

---

### 12. Connect to Cassandra

```bash
cqlsh localhost 9042
```

If the installation is successful, the Cassandra prompt will appear.

---

## 🐳 Docker Compose Configuration

```yaml
services:
  cassandra:
    image: cassandra:latest
    container_name: cassandra
    hostname: cassandra

    ports:
      - "9042:9042"
      - "9160:9160"

    volumes:
      - "./cassandra-data:/var/lib/cassandra"
      - "./scripts:/scripts"

    environment:
      - CASSANDRA_CLUSTER_NAME=MyCluster
      - CASSANDRA_DC=datacenter1
      - CASSANDRA_RACK=rack1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
      - CASSANDRA_NUM_TOKENS=256
      - MAX_HEAP_SIZE=512M
      - HEAP_NEWSIZE=100M

    restart: unless-stopped
```

---

## ▶️ Running Cassandra

Start the container:

```bash
docker compose up -d
```

Check container status:

```bash
docker ps
```

View container logs:

```bash
docker logs cassandra
```

Connect to Cassandra:

```bash
cqlsh localhost 9042
```

---

## 📸 Output

The project includes screenshots demonstrating:

- Ubuntu WSL setup
- Docker installation
- Docker Compose configuration
- Cassandra container startup
- Container verification
- Successful CQLSH connection

---

## 📖 Learning Outcomes

After completing this exercise, you will understand:

- Installing Docker on Ubuntu WSL
- Running Apache Cassandra inside Docker
- Creating and managing Docker Compose services
- Connecting to Cassandra using CQLSH
- Verifying containerized database services

---

## ✅ Conclusion

Apache Cassandra was successfully installed on Ubuntu WSL using Docker. Docker provided a lightweight and isolated environment that simplified the installation process and eliminated dependency issues. The Cassandra container was verified using Docker commands, and the installation was successfully tested by connecting through CQLSH. This setup is suitable for learning Cassandra, practicing CQL commands, and performing NoSQL database experiments.
