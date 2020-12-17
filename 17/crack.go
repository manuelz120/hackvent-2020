package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"

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
		fmt.Println(resp.Header)
	}
	
	resp, _ = client.PostForm("https://876cfcc0-1928-4a71-a63e-29334ca287a0.rdocker.vuln.land/login", 
		url.Values{"username": {"admin"}, "password": {"whatever"}})
	fmt.Println(resp.StatusCode)
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			panic(err)
		}
		bodyString := string(bodyBytes)
		fmt.Println(bodyString)
		fmt.Println(resp.Header)
	}

	jwt := "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6Ii9rZXlzLzFkMjFhOWY5NDUifQ.eyJleHAiOjE2MDgyMTgwOTcsImlhdCI6MTYwODIxNDQ5Nywic3ViIjoic2FudGExMzM3In0.I8uwoESnWF5uztH6mxQqEBBvPvkzQiOrZv1THZ6XdL0"

	req, err := http.NewRequest("GET", "https://876cfcc0-1928-4a71-a63e-29334ca287a0.rdocker.vuln.land/", nil)
	if err != nil {
		return
	}

	req.AddCookie(&http.Cookie{Name: "session", Value: jwt})
	client = &http.Client{Transport: tr}
    resp, _ = client.Do(req)

	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			panic(err)
		}
		bodyString := string(bodyBytes)
		fmt.Println(bodyString)
	}

	
}