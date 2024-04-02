# 〔1〕Core concepts
#### Master Node
Managing, planning, scheduling, and monitoring nodes.
#### Worker Nodes
Host applications as containers.
#### ETCD Cluster
ETCD is a database that stores information in a key value format.
#### Kube-Scheduler
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
##### Changing the image ENTRYPOINT or CMD arguments
- To use a different ENTRYPOINT than that of a docker file, use the command `docker run --entrypoint <NEW_ENTRYPOINT> <IMAGE>`. 
	This can be done in a Pod YAML file through the field `command:` under `containers`
- To use a different CMD than that of a docker file, use the command `docker run <NEW_COMMAND_OR_ARGUMENT> <IMAGE>`. 
	This can be done in a Pod YAML file through the argument `args:` under `containers`

***NOTE:*** Both should be passed in JASON format: `["ARG01","ARG02"]`

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
We can generate YAML files of different resources by using `--dry-run=client -o yaml > <FILE>.yaml`
##### Examples:
- `kubectl run POD_NAME --image=nginx --dry-run=client -o yaml > pod.yaml` 
- `kubectl create deployment DEPLOYMENT_NAME --image=nginx --replicas=3 --dry-

- Create the new resource by `kubectl create <YOUR_FILE>.yaml`.

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

# 〔2〕Scheduling Pods
## Manual Scheduling
If we don't have a scheduler or we don't want to rely on the built-in scheduler, we can manually schedule pods to nodes.
In every pod YAML file there is a field called `nodeName:` that by default is not set, & then:
- If a Scheduler exists, it looks for Pods that doesn't have this property set & schedule it to a node according to the scheduling algorithm.
- if we don't have a scheduler, the pod is set in a pending state, which can be seen by `kubectl get pods`, until we manually assign it to a node.
We assign pods manually by specifying a node to the field `nodeName: node01`.
***Once Created, we cannot change the assigned node***, the other way to change it is to create a ***Binding Object & sending a post request to the post-binding-API***, which basically mimics the actual schedular.
![[Pasted image 20240320232355.png]]
## Taints & Tolerations
This is a scheduling scheme, according to the following:
- node is tainted. 
- Pods are tolerated for the required taint.
There are three types of tolerations:
1) **NoSchedule**: Avoid Putting any pod that isn't tolerated to this taint
2) **PreferNoSchedule**: Prefer avoiding Putting any pod that isn't tolerated to this taint, not guaranteed.
3) **NoExecute**: similar to NoSchedule, but it also kills existing pods from before applying the taint.

- Tainting is done by the command `kubectl taint nodes <NODE_NAME> <KEY>=<VALUE>:<TAINT_EFFECT>` 
	- ex: `kubectl taint nodes node01 app=frontend:NoSchedule`
We can check a node taint by `kubectl describe node <NODE_NAME> | grep Taint` 

- Tolerations can be added in the YAML definition file under the field `tolerations:` 
```
spec:
	tolerations:
		- key: <KEY>
		  operator: eaual
		  value: <VALUE>
		  effect: <TAINT_EFFECT>
```
*Note:* Taints doesn't specify the pods to be assigned, instead they prevent untainted pods from assigning to that node, meaning a taint-tolerated pod may be assigned to an untainted node rather than that of the tainted one if the scheduler assigned it to that node.
***Also*** *Note:* kubemaster node (Master Node) has a default taint to prevent assigning workloads pods.
## Node Selectors
As the previous note explained, taints doesn't select the node that the pod gets assigned to. This can be achieved by Node selectors through **labels**
- To assign a label to a node, we can use the command:
	`kubectl label nodes <NODE-NAME> <LABEL_KEY>=<LABEL_VALUE>`
- In the pod YAML definition file, we can use the field `nodeSelector:` under `spec` for assigning the label.
```
spec:
	nodeSelector:
		<LABEL_KEY>: <LABEL_VALUE>
```
*Note:* Node Selectors are limited, for example they cannot choose nodes that aren't of a specific label, or choose a node having one label from a set of labels.
## Node Affinity
As the previous note explained, Node selectors were limited. 
The primary purpose of node affinity feature is to ensure that pods are hosted on particular nodes with more complexity and flexibility.
- Node affinity is defined in the pod definition file using the field `affinity:` under the field `spec:`
```
spec:
	affinity:
		nodeAffinity:
			requiredDuringSchedulingIgnoredDuringExecution:
				nodeSelectorTerms:
					- matchExpressions:
						- key: <LABEL_KEY>
						  operator: <OPERATOR>
						  values:
							- <LABEL_VALUE_1>
							- <LABEL_VALUE_2>
```
##### Node Affinity types
1) `requiredDuringSchedulingIgnoredDuringExecution`: Used for crucial scheduling, this means if the pod cannot find a matching node affinity, it won't be scheduled. 
2) `preferredDuringSchedulingIgnoredDuringExecution`: Used for less crucial scheduling, this will schedule the pod anywhere if no matching node affinity was found.
*Note:* Both types the during execution as ignored, meaning that already existing pods won't be removed in case of a label update that defies the set affinity rules. 
***Not available but planned for future release:***
3) `requiredDuringSchedulingRequiredDuringExecution`: To update running pods in case of a node label update, to either keep the pod or simply reschedule it to another node.
#### Node Affinity Operators
There are multiple node affinity operators, here are the important ones:
1) `In`: The label value is present in the supplied set of strings
2) `NotIn`: The label value is not contained in the supplied set of strings
3) `Exists`: A label with this key exists on the object, **no need for the value.**
4) `DoesNotExist`: No label with this key exists on the object, **no need for the value.**
#### Node Selectors vs Node Affinity 

![[Pasted image 20240321065104.png]]
## Resource Management on a node 
### Resource Requests
- Kubernetes Scheduler looks through the nodes that have free resources so it can deploy pods in them, and through Resource Requests, we can specify the minimum required amount of CPU & memory that the scheduler will look for, FOR EACH CONTIANER in the pod.
### Resource Limits
By default, containers has no resource limits. This can consume node resources rapidly.
Using Resource Limits, we can limit the pod consumed resources. If the pod tried to exceed that limit, the system threshold the CPU. However the pod CAN exceed the limit of the set memory, but the pod will be terminated if it kept exceeding the limited memory, giving an error of `OOM (Out Of Memory)`.

*Note:* If limits were set but no requests given in the definition file, the requests are set to equal the limits.
![[Pasted image 20240322005727.png]]
#### *Note:* Ideal Setup for Resource Settings is Resource Requests with no Resource Limits
Setting both resource limits & requests are helpful for specifying exact resources, but there are cases that we might want a pod to exceed its limit only if there are no used CPUs.
- The ideal setup would be having ***only resource requests*** active, this will guarantee each pod its required resources to run, without one thresholding the other pod.
- So in case a pod required more resources it will consume only available resources.
- There are cases that limits are important, but thresholding pods generally is avoided.
![[Pasted image 20240322014211.png]]
### LimitRange
LimitRange are for specifying the default values for newly created pods. Exsisting pods won't be affected.
![[Pasted image 20240322014726.png]]
### Resource Quotas
Resource Quotas are Name Space level resource control, they are hard limits for the resources consumed by all nodes & pods in a Name Space
![[Pasted image 20240322015256.png]]
## DaemonSets
Similar to Replica Sets, but instead they are for scheduling pods **automatically** to new nodes.
This can be very helpful in pods that are required in all existing & yet to exist nodes, such as monitoring & logging pods.
- The definition file is the same as the ReplicaSets, with the difference being `kind: DaemonSet`
![[Pasted image 20240322024039.png]]
# 〔3〕Application Lifecycle Management
## 









# Commands Archive
______________________________________________________________________ 
- `kubectl run <CONTAINER_NAME> --image <IMAGE_NAME>`
	- Starts a pod inside a node, & runs the image in the pod.
______________________________________________________________________
```
kubectl get <RESOURCE> 
``` 
- 	Lists running resources for the given resource.
______________________________________________________________________
```
kubectl get <RESOURCE> --selector <KEY_1>=<VALUE_2>,<KEY_1>=<VALUE_2>
``` 
- Lists running resources with the given key values.
______________________________________________________________________
```
kubectl describe pods <POD_NAME>
``` 
- Shows details about the pod.
______________________________________________________________________
```
kubectl delete <RESOURCE> <RESOURCE_NAME>
``` 
- Deletes a resource.
______________________________________________________________________
```
kubectl edit <RESOURCE> <RESOURCE_NAME>
```
- Opens a YAML-syntaxed file for the selected resource to edit it's specs.
______________________________________________________________________
```
kubectl create -f <YAML_FILE.yml>
```
- Starts a resource according the definition in the file.
______________________________________________________________________
```
kubectl replace -f <YAML_FILE.yml>
``` 
- Replaces a resource according the definition in the file after updating the file.
______________________________________________________________________
```
kubectl create <RESOURCE> <RESOURCE_NAME> <options> --dry-run=client -o yaml > <FILE>.yaml
```
- Creates a YAML file for a resource, ex: deployment. Add your options and attributes such as labels and replicas.
______________________________________________________________________
```
kubectl run <POD_NAME> --image=<IMAGE> <options> --dry-run=client -o yaml > <FILE>.yaml
```
* Creates a YAML file for a pod. Add your options and attributes such as labels.
______________________________________________________________________
```
kubectl scale --replicas=<N> -f <YOUR-REPLICA-FILE.yaml>
``` 
- Scaling using the yaml file.
______________________________________________________________________
```
kubectl scale --replicas=<N> replicaset <YOUR-REPLICASET-NAME>
``` 
- Scaling using the type & name.
______________________________________________________________________
```
kubectl config set-context $(kubectl config current-context) --namespace=<DESIRED_NAMESPACE>
```
- Changing the current namespace.
______________________________________________________________________
```
kubectl taint nodes <NODE_NAME> <KEY>=<VALUE>:<TAINT_EFFECT>
```
- Applying a taint to a node.
______________________________________________________________________
```
kubectl describe node <NODE_NAME> | grep Taint
``` 
- Showing the taint of a node.
______________________________________________________________________
```
kubectl label nodes <NODE-NAME> <LABEL_KEY>=<LABEL_VALUE>
```
- Labeling a node.
______________________________________________________________________
```
kubectl top node
kubectl top pod
```
- Monitors used resources for nodes & pods, needs "Metrics Server" installed.
______________________________________________________________________
```
kubectl log -f <POD_NAME> <CONTAINER_NAME_IF_MULTIPLE_EXISTED>
```
- Shows the life logs for the container in a pod.
______________________________________________________________________
