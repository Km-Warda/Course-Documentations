# 〔1〕Core concepts
#### Master Node
Managing, planning, scheduling, and monitoring nodes
#### Worker Nodes
Host applications as containers
#### ETCD Cluster
ETCD is a database that stores information in a key value format.
#### Kube-Shceduler
A scheduler identifies the right node to place a container on based on the containers resource requirements, the worker nodes capacity or any other policies or constraints, such as taints and tolerations or node affinity rules that are on them.
#### ControllerManager
##### Node-controller
The node controller takes care of nodes. They're responsible for onboarding new nodes to the cluster, handling situations where nodes become unavailable or get destroyed.
##### Replication Controller
Replication controller ensures that the desired number of containers are running at all times in a replication group.
#### The Kube-APIserver
Responsible for orchestrating all operations within the cluster. It exposes the Kubernetes API, which is used by external users to perform management operations on the cluster, as well as the various controllers to monitor the state of the cluster and make necessary changes as required and by the worker nodes to communicate with the server.
#### Kubelet
A kubelet is an agent that runs on **each node** in a cluster. It listens for instructions from the Kube-apiserver and deploys or destroys containers on the nodes as required. It's more of a captain for each node. 
	The Kube-apiserver periodically fetches status reports from the kubelet to monitor the status of nodes and containers on them.
***NOTE:*** You must always install the kubelet manually on the worker nodes
#### The Kube-Proxy
It ensures that the necessary rules are in place on the worker nodes to allow the containers running on them to communicate with each other.

## Pods
Pods are the smallest unit that contains the containers, it's the unit that is auto-scaled, not the containers.
- `kubectl run <CONTAINER_NAME> --image <IMAGE_NAME>` starts a pod inside a node, & runs the image in the pod.
- `kubectl get pods` shows available pods.
- `kubectl describe pods <POD_NAME>` shows details about the pod
#### Pods with YAML files
```
apiVersion: v1
kind: pod
metadata:
	name: myapp-pod
	labels:
		app: myapp
		tier: front-end
spec: 
	containers:
		- name: nginx-container
		  image: nginx
```
`apiVersion` refers to the used Kubernetes apiVersion. `kind` refers to what are we trying to create, `metadata` is the data about the object "name, labels, etc", `spec` refers to the specifications.
- `kubectl create -f pod-definetion-file.yml` starts the pod according the definition in the file.

## Replication Controller & ReplicaSets
### Replication Controller
- Now replaced by the ReplicaSet
- It can maintain both high availability & scalability, it can replace faulty application in a pod, add a replica pod in the same node, or add a new pod in a different node, as well as distributing load among the pods.
#### Replication Controller with YAML files
Notice that it has two metadata blocks, one for the replication controller, & the other for the pod that will be managed. Replication Controller uses apiVersion V1.
- You can use `kubectl get replicationcontroller` to lists replication controllers.
![Pasted image 20240310150914](https://github.com/Km-Warda/Course-Documentations/assets/109697567/42a3641e-456a-4d17-9fc4-310b5e8d2b46)
*Note:* The replication controller by default manages the pods it creates, but we can use the parameter `selector` to choose what pods it will manage. it's not a required input though. 
### ReplicaSets
- The main big difference is the **apiVersion**, ReplicaSets uses apiVersion: apps/v1 
- The other difference is that ReplicaSets needs to select what pods it will manage. Thus a user input is required for the parameter  `selector`.
- The ReplicaSets supports more `matchlabels` than the Replication Controller.
#### ReplicaSet with YAML files
- The `matchlabels` refer to the labels of the chosen pods to be managed.  
![Pasted image 20240310154846](https://github.com/Km-Warda/Course-Documentations/assets/109697567/181c17a1-996e-401f-a9da-5ceb2789750f)
### Scaling
There are multiple ways of updating the number of replicas "ex: 6 replicas":
- Update the YAML file & use the `kubectl replace` command,
- Use `kubectl scale --replicas=6`
	- `kubectl scale --replicas=6 -f your-replica-file.yaml`
	- `kubectl scale --replicas=6 replicaset your-replicaset-name`

## Deployments
Deployment is a resource that provides us with the capability to upgrade the underlying instances seamlessly using:
- Rolling updates
- Undo changes
- Pause and resume changes as required, & more
![Pasted image 20240317204547](https://github.com/Km-Warda/Course-Documentations/assets/109697567/0cd533bf-7f5e-4a01-964c-468143a8cd8c)
Deployments have the same YAML file as ReplicaSets, of course with the difference `kind: Deployment`, as well as the capability to do other upgrades to the underlying resources other than scaling.

![Pasted image 20240317211304](https://github.com/Km-Warda/Course-Documentations/assets/109697567/b52c0b00-4350-48d2-83c6-e412e283a691)
## Generating YAML files 
It can be hard to copy & paste YAML file contents to create new ones, we can work around this by generating a Deployment YAML file as following:
- `kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > custom-deployment.yaml` 
	 This generates a Deployment YAML file `(-o yaml)`, doesn’t create it `(–dry-run)`, and then save it to a YAML file `(> custom-deployment.yaml)`.
- Edit the `custom-deployment.yaml` file as desired, then create the new deployment by `kubectl create custom-deployment.yaml`.
## Services
Kubernetes Services helps us connect applications together with other applications or users. There are three types of services:
- **NodePort:** the service makes an internal port accessible on a port on the node.
- **ClusterIP:** the service creates a virtual IP inside the cluster to enable communication between different services.
- **LoadBalancer:** where it provisions a load balancer for our application in supported cloud providers.
### NodePort
In the following setup, the end user can't access the application hosted on the pod directly as it's in a different network, the user needs to SSH to the Node itself then access the application, which is not convenient in many cases. 

The NodePort service allows connection through a set of ports that are named as:
- NodePort: are in range of ***30000 - 32767***, these are the ports the user access the node through.
- Port: the port exposed on the service
- TargetPort: The port exposed on the pod.
![Pasted image 20240317221234](https://github.com/Km-Warda/Course-Documentations/assets/109697567/93c1b5e9-f54b-4315-83f0-d801d5e14fbc)
#### NodePorts with YAML files
![Pasted image 20240317223345](https://github.com/Km-Warda/Course-Documentations/assets/109697567/b1b38936-bce0-4e1c-83e2-8021abba8177)
*Note:* If TargetPort wasn't given, it will be assumed the same as port, & if the NodePort wasn't given, a free port in the allowed range will be given.
*Also Note:* The `ports:` is an array, so care the `-`.
#### NodePorts for applications which are not in the same pod 
Either we have one Node & different pods, each with it's IP address, or different nodes, each containing the pod, Kubernetes creates a service that spans over all the nodes, thus we are able to access any pod from the same NodePort, **without any further configuration**.
![Pasted image 20240317223722](https://github.com/Km-Warda/Course-Documentations/assets/109697567/6e6b2976-6523-4ea4-8a9d-0626ea9cd61b)
### ClusterIP
This is the default service type, meaning if the type is not specified, the service will be chosen as ClusterIP.
ClusterIP creates a virtual IP address to make other pods communicates with target pods easily, even in case of change in the IP address of the target pods.
The ClusterIP service allows connection through a set of ports that are named as:
- Port: the port exposed on the service
- TargetPort: The port exposed on the pod.
![Pasted image 20240318000257](https://github.com/Km-Warda/Course-Documentations/assets/109697567/4be5e75e-da53-44f2-a065-a2ed0f67c8ec)
#### ClusterIP with YAML files
![Pasted image 20240318001303](https://github.com/Km-Warda/Course-Documentations/assets/109697567/9c894dad-aef8-48d7-9874-8f9232ed911c)
#### Differences between NodePort service & ClusterIP service
- NodePorts exports a port on the CLUSTER level, that the USER or CLIENT accesses the target pod initially through it.
- ClusterIP exports a port on the SERVICE level, that OTHER PODS access the target pod initially through it.
An example for ClusterIP usage is connection between frontend service & backend service.
### LoadBalancer
Kubernetes supports using different cloud load balancers,  such as GCP, AWS or Azure load balancers. to use this we change the `type: LoadBalancer` in the YAML definition file.
## Namespaces
Namespaces is used for isolation of resources. There are 3 default Namespaces created by Kubernetes:
- default: the default namespace user work on.
- kube-system: the namespace containing important resources that are created by Kubernetes initialization, for protecting it from deletion by mistake.
- kube-public: the namespace containing resources that are public for all users. 

When in a namespace, we refer to the resources in it directly, however we can refer to resources in other namespaces as well by the following format:
![Pasted image 20240318005234](https://github.com/Km-Warda/Course-Documentations/assets/109697567/be5ad4d9-faf1-4dbb-acb6-7e111df5193b)

Another aspect of namespace can be shown by the command `kubectl get pods`, which shows the pods in the current namespace:
- To show the pods in another namespace we can use the `--namespace=<NAMESPACE_NAME>` option. This option can also be used with most commands "ex: create or delete". Another way of doing this is specifying the namespace in the YAML definition file.
- To show pods in all namespaces, we can use the option `--all-namespaces`
### Creating Namespaces
We can create namespaces either by YAML files, simply having the name of the namespace as the `metadata`, or the `kubectl create` command. 
### Switching Namespaces
We can switch between namespaces by the command 
`kubectl config set-context $(kubectl config current-context) --namespace=dev`
### ResourceQuota
Each namespace has a maximum limit of resources, this can be controlled by creating a ResourceQuota:
![Pasted image 20240318012902](https://github.com/Km-Warda/Course-Documentations/assets/109697567/6e2932c3-91b6-4482-903d-676f3b9e9499)
## Imperative & Declarative Approaches
- Imperative approach refer to specifying details & steps when building an infrastructure.
- Declarative approach refer to using a tool & a file that contains the specs & details, such as YAML files, & then apply the infrastructure using a simple apply command. If any updates were done to the file & applied, the system should be smart enough to do all the necessary updates & changes automatically. 
### Imperative Approach
#### Creating Objects & Updating objects (Local file & Kubernetes Memory)
- Local files: The `kubectl create -f <DEFINITION.yml>` command creates a resource using a given yaml file. if the file changed, the resource will NOT be updated on its own. 
- Kubernetes Memory: The `kubectl edit <RESOURCE> <RESOURCE NAME>` command opens a live file, the change in this file will be applied to the live object.
However, if another team member tried to edit the local file, unaware of the updates in the live file, these updates will be lost upon using the new local file.

A better approach is to edit the local file first, then use the `kubectl replace -f <DEFINITION.yml>` to update the live resource accordingly.
We can completely delete and recreate objects or resources, using the `--force` option in this command. 
### Declarative Approach
- We can create or update objects simply by using the command `kubectl apply` command
- If we have many resources to be created, we can pass the path directly in the command & all the files will be created.
- This method avoids errors that may occur in case of resource not existing before applying or creating a resource that already exists.  
![Pasted image 20240318014351](https://github.com/Km-Warda/Course-Documentations/assets/109697567/0c2004d2-4b17-4921-98e4-5993c9ece905)

# 〔2〕Scheduling






# Commands Archive
- Starts a pod inside a node, & runs the image in the pod.
```
kubectl run <CONTAINER_NAME> --image <IMAGE_NAME>
``` 


- Lists running resources for the given resource.
```
kubectl get <RESOURCE>
``` 

- Lists running resources with the given key values.
```
kubectl get <RESOURCE> --selector <KEY_1>=<VALUE_2>,<KEY_1>=<VALUE_2>
```

Deletes a resource.
- `kubectl delete <RESOURCE> <RESOURCE_NAME>` 
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Opens a YAML-syntaxed file for the selected resource to edit it's specs.
- `kubectl edit <RESOURCE> <RESOURCE_NAME>`



- Opens a YAML-syntaxed file for the selected resource to edit it's specs.
- `kubectl edit <RESOURCE> <RESOURCE_NAME>`
  
- `kubectl create -f <YAML_FILE.yml>`
	Starts a resource according the definition in the file.
- `kubectl replace -f <YAML_FILE.yml>` 
	Replaces a resource according the definition in the file after updating the file.
- `kubectl scale --replicas=<N> -f <YOUR-REPLICA-FILE.yaml>` 
	Scaling using the yaml file.
- `kubectl scale --replicas=<N> replicaset <YOUR-REPLICASET-NAME>` 
	Scaling using the type & name.
- `kubectl config set-context $(kubectl config current-context) --namespace=<DESIRED_NAMESPACE>`
	Changing the current namespace.
