package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	servicesPath := "./services"
	if err := os.Chdir(servicesPath); err != nil {
		panic(err)
	}

	directories, err := os.ReadDir(".")
	if err != nil {
		panic(err)
	}

	for _, dir := range directories {
		if dir.IsDir() {
			serviceName := dir.Name()
			fmt.Println("Building service:", serviceName)

			cmd := exec.Command("docker", "build", "-t", serviceName, ".")
			cmd.Dir = serviceName // Set the working directory for the command
			cmd.Stdout = os.Stdout
			cmd.Stderr = os.Stderr
			if err := cmd.Run(); err != nil {
				fmt.Println("Error building:", serviceName, "-", err)
				continue
			}

			tagCmd := exec.Command("docker", "tag", serviceName, "localhost:5001/"+serviceName+":latest")
			tagCmd.Stdout = os.Stdout
			tagCmd.Stderr = os.Stderr
			if err := tagCmd.Run(); err != nil {
				fmt.Println("Error tagging:", serviceName, "-", err)
				continue
			}

			pushCmd := exec.Command("docker", "push", "localhost:5001/"+serviceName+":latest")
			pushCmd.Stdout = os.Stdout
			pushCmd.Stderr = os.Stderr
			if err := pushCmd.Run(); err != nil {
				fmt.Println("Error pushing:", serviceName, "-", err)
				continue
			}
		}
	}

	fmt.Println("Done processing services.")
}
