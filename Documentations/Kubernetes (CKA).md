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
- A kubelet is an agent that runs on **each node** in a cluster. It listens for instructions from the Kube-apiserver and deploys or destroys containers on the nodes as required. It's more of a captain for each node. 
- The Kube-apiserver periodically fetches status reports from the kubelet to monitor the status of nodes and containers on them.
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
- To use a different ENTRYPOINT than that of a docker file, use the command `docker run -- --entrypoint <NEW_ENTRYPOINT> <IMAGE>`. 
	- This can be done in a Pod YAML file through the field `command:` under `containers`
- To use a different CMD than that of a docker file, use the command `docker run -- <NEW_COMMAND_OR_ARGUMENT> <IMAGE>`. 
	- This can be done in a Pod YAML file through the argument `args:` under `containers`

***NOTE:*** Both should be passed in JASON format: `["ARG01","ARG02"]`, And the `--` before the commands are for using non-Kubernetes options.

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

*Note:* You can check the used apiVersion of a resource by: `kubectl api-resources | grep <RESOURCE_NAME>`
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
- `kubectl create deployment DEPLOYMENT_NAME --image=nginx --replicas=3 --dry-run=client -o yaml > deployment.yaml`
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
***Once Created, we cannot change the assigned node***.
![Pasted image 20241029222842](https://github.com/user-attachments/assets/2838a1ec-8378-4248-b9d0-63669bfd0602)

The other way to change it is to create a ***Binding Object & sending a post request to the post-binding-API***, which basically mimics the actual schedular.
![Pasted image 20240320232355](https://github.com/Km-Warda/Course-Documentations/assets/109697567/ae523c02-3e64-4d6a-9227-77aeddbc726f)
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
	- `kubectl label nodes <NODE-NAME> <LABEL_KEY>=<LABEL_VALUE>`
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

![Pasted image 20240321065104](https://github.com/Km-Warda/Course-Documentations/assets/109697567/65dcd8f0-04c3-4b52-bcb0-4476d320fa11)
## Resource Management on a node 
### Resource Requests
- Kubernetes Scheduler looks through the nodes that have free resources so it can deploy pods in them, and through Resource Requests, we can specify the minimum required amount of CPU & memory that the scheduler will look for, FOR EACH CONTIANER in the pod.
### Resource Limits
By default, containers has no resource limits. This can consume node resources rapidly.
Using Resource Limits, we can limit the pod consumed resources. If the pod tried to exceed that limit, the system threshold the CPU. However the pod CAN exceed the limit of the set memory, but the pod will be terminated if it kept exceeding the limited memory, giving an error of `OOM (Out Of Memory)`.

*Note:* If limits were set but no requests given in the definition file, the requests are set to equal the limits.
![Pasted image 20240322005727](https://github.com/Km-Warda/Course-Documentations/assets/109697567/16059eac-e53a-4d97-adb7-564c4f3eb2f7)
#### *Note:* Ideal Setup for Resource Settings is Resource Requests with no Resource Limits
Setting both resource limits & requests are helpful for specifying exact resources, but there are cases that we might want a pod to exceed its limit only if there are no used CPUs.
- The ideal setup would be having ***only resource requests*** active, this will guarantee each pod its required resources to run, without one thresholding the other pod.
- So in case a pod required more resources it will consume only available resources.
- There are cases that limits are important, but thresholding pods generally is avoided.
![Pasted image 20240322014211](https://github.com/Km-Warda/Course-Documentations/assets/109697567/4bcda0f5-4521-4fa1-aca5-c53691ac60d9)
### LimitRange
LimitRange are for specifying the default values for newly created pods. Exsisting pods won't be affected.
![Pasted image 20240322014726](https://github.com/Km-Warda/Course-Documentations/assets/109697567/c119c8c9-4443-4b3c-9c94-efcd5d45cc56)
### Resource Quotas
Resource Quotas are Name Space level resource control, they are hard limits for the resources consumed by all nodes & pods in a Name Space
![Pasted image 20240322015256](https://github.com/Km-Warda/Course-Documentations/assets/109697567/3a2010b6-a849-4ab2-8f9b-d7a361cc4e7b)
## DaemonSets
Similar to Replica Sets, but instead they are for scheduling pods **automatically** to new nodes.
This can be very helpful in pods that are required in all existing & yet to exist nodes, such as monitoring & logging pods.
- The definition file is the same as the ReplicaSets, with the difference being `kind: DaemonSet`
![Pasted image 20240322024039](https://github.com/Km-Warda/Course-Documentations/assets/109697567/dd7f221a-d8f4-4bd8-88c6-67211762dbe1)
# 〔3〕Application Lifecycle Management
## Versioning & Pods Rollbacks
There are two deployment strategies available for rollouts.
1) Recreate: Downs all the pods & runs them again with the new image
2) Rolling Update: Downs pod by pod, & replace them one by one to avoid downtime.
If no strategy is set, the default strategy is Rolling Update.
![[Pasted image 20240402054235.png]]
#### Rollbacks
Suppose we used `kubectl set image DEPLOYMENT_NAME/CONTAINER_NAME nginx:nginx:1.9.1` to change the deployment pods. Now it has a new version, while the old still exists, but disabled in the old replica set. & this can be shown through the `kubectl get` command.
- `kubectl rollout status DEPLOYMENT_NAME/CONTAINER_NAME` Shows current status  of rollouts.
- `kubectl rollout history DEPLOYMENT_NAME>/CONTAINER_NAME` Shows history of rollouts.
We can rollback to older versions by the command: `kubectl rollout undo DEPLOYMENT_NAME/CONTAINER_NAME`
## Environmental Variables
Setting an environmental variable is done bey specifying the variable under `env:` or `envFrom:` specification. 

For `env:`, each variable has a name & a value, the value can be passed in 3 different ways, either as a plain key value pair, through a ***ConfigMap***, or through ***Secrets***.
![[Pasted image 20240415161748.png]]

For `envFrom:` we specify the ConfigMaps or the secrets to the desired Pod YAML file
![[Pasted image 20240415164344.png]]
### ConfigMaps
1) Creating a ConfigMap can be done imperatively by `kubectl create configmap <CONFIGMAP_NAME>`, & passing the variables through the command `--from-literal` or `--from-file`, as these examples:
	- `kubectl create configmap My_ConfigMap --from-literal=APP_COLOR=RED`
	- `kubectl create configmap My_ConfigMap --from-file=/home/user01/ConfigMap.properties`
2) Creating a ConfigMap declaratively through a YAML file can be done as following:
```
apiVersion: vl
kind: ConfigMap
metadata :
	name: app-config
data :
	APP_COLOR: blue
	APP_MODE: prod
```
We can show all defined ConfigMaps by the command `kubectl get`, or show detailed info "the defined variables" through the command `kubectl describe`
### Secrets
Secrets are the same as ConfigMaps, but they use encoded values of the secrets instead of the values itself.
- Basically the same notes as the ConfigMaps, with using the `secret` parameter instead.
To encode a value: `echo -n 'value' | base64 `
To decode a value: `echo -n 'cGFzd3Jk' | base64 --decode`

**IMPORTANT NOTES:** 
1) Secrets doesn't encrypt the values, they only decode them, anyone can decode the value with the `base64 --decode` command if they can access the file.
2) Do not upload Secret objects along with code into the repository.
3) Secrets are not encrypted in ETCD by default, we should enable encryption at rest, this has a documentation specifying the details.
4) Consider third-party secrets store providers, such as AWS Provider, Azure Provider, GCP Provider, or Vault Provider.
5) Kubelet stores the secret into a ".tmpfs" so that the secret is not written to disk storage.
## InitContainers & Multi-Container Pods
The container section is an array, each container specification is done by a new `-`
There is a new type of containers called initContainers, these containers have a command or a process that should be completed before running other containers, if it fails the pod will keep restarting until this container is executed successfully.
This section can be demonstrated by the following example:
```
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'git clone <some-repository-that-will-be-used-by-application> ; done;']
```

# 〔4〕Cluster Maintenance 
## OS upgrades & restarting Nodes (Draining & Cordoning Nodes)
- When a node goes down, Kubernetes waits 5 minutes & then terminate all the pods from that node, considering them dead.
- These 5 minutes are the default value of what's called **pod-eviction-timeout** & is set on the **kube-controller-manager**. `kube-controller-manager --pod-eviction-timeout=5m0s` 
- After the pod-eviction-timeout, the node comes back online without any pods scheduled on it.
- Pods that are part of replica sets, will be recreated on other nodes to satisfy the required number of replicas.
From the previous notes, if we have a maintenance task to be performed on a node, like an OS upgrade, we may not be sure if the node will be back online.
So in a safe way of dealing with the node pods would be explained as follows:
- We can use the command `kubectl drain node-1` to terminate the pods & recreate them on other nodes, while marking the node unschedulable "Cordoned".
- Or we can also use the command `kubectl cordon node-1` to mark the node unschedulable without terminating the existing pods.
- To mark the node as schedulable again, use the command `kubectl uncordon node-1`, but take note that moved pods won't automatically go back to the original node.

# 〔5〕Security 
The kube-apiserver is at the center of all operations within Kubernetes. We interact with it through the kube control utility or by accessing the API directly, and through that you can perform almost any operation in the cluster. So that's the first line of defense.

We need to make two types of decisions: Who can access the cluster and what can they do?
- Who can access the API server is defined by the authentication mechanisms.
- What can they do is defined by authorization mechanisms.

All communication with the cluster between the various components such as the ETCD cluster, the kube-controller-manager, scheduler, API server, as well as those running on the worker nodes such as the Kubelet and the kube-proxy is secured using ***TLS encryption***.

What about communication between applications within the cluster? By default, all Pods can access all other Pods within the cluster. We can restrict access between them using Network policies.
![[Pasted image 20240515125422.png]]
## TLS Certificates
Multiple certificates are needed in our cluster for authorization, some are Client Certificates for components acting as Clients, & others are Server Certificates for components acting as  Servers. as well as a certificate authority (CA).
![[Pasted image 20240518142529.png]]
### Creating TLS Certificates in the cluster 
There are different tools available such as EasyRSA, OpenSSL, or CFSSL, or many others.
In this section OpenSSL tool is used. Here are the steps required for each component.
1) Creating a private key.
2) Creating a certificate signing request along with the created key, specifying the name of the component this certificate is for (in the `/CN=<NAME>` field).
3) Signing the certificate using `openssl x509` command by specifying the certificate signing request
#### Creating certificates for the CA 
- Since this certificate is for the CA itself, it is self-signed by the CA using its own private key that it generated in the first step.
![[Pasted image 20240518145049.png]]
#### Creating client certificates "acting as admin users"
- We should take care that the name given in the field `/CN=<NAME>` is the name that Kube Control client authenticates with and when you run the Kube Control command. So in the auditing logs and elsewhere, this is the name that you will see. So provide a relevant name in this field.
- The signing request is done with the client private key created in the first step.
- The signing is done by specifying  the CA certificate and the CA key.
- To assign this client to a group with some privileges, we can do this by the `/O=<GROUP>`in the signing request.
![[Pasted image 20240518145923.png]]
#### Certificates for system components "client certificates"
System components (Kube-scheduler, kube-controller-manager, kube-proxy) must have their name prefixed with the keyword `system`.
![[Pasted image 20240518150920.png]]
#### Using the client certificates (Administration management)
Can be done either with the `curl` command or the kube-config file, stating the client certificate, the private key, & the CA certificate.
![[Pasted image 20240518154227.png]]
#### Creating Server Certificates
- Components as ETCD might be deployed as a cluster across multiple servers as in a high availability environment. Thus we must generate additional peer certificates to secure communication between the different members in the cluster.
	After creating the peer certificates, specify them while starting the ETCD server.
![[Pasted image 20240518165901.png]]
- Components as the Kube-API-Server might be referred to in many names, thus it may be required to state these names in the certificate.
	This is done through specifying the alternate names in the OpenSSL config file unfer the `[alt_names]` section. 
![[Pasted image 20240518165842.png]]
-  Some server components may act as a client, as the kube-apiserver communicating to the ETCD and kubelet servers. 
	The location of these certificates are passed in to the Kube API servers executable or service configuration file.
![[Pasted image 20240518172049.png]]
- For Kubelet certificates, we need a key-certificate pair for each node in the cluster.
	- The naming formats starts with `system` as indicated before, then the `node` followed by the name of the node. 
	- The nodes must be added to groups with required privileges as discussed for admin users certificates. 
	- Then we specify the root CA certificate, then the kubelet node certificates in the kubelet config file. 
![[Pasted image 20240518172324.png]]

 




## Authorization to the cluster
There are 3 main types of users we need to take in consideration when managing user authentication: 
- Administrative users, such as Kube Admins & the developers.
- Application end users.
- Bots, third party applications accessing the cluster for integration purposes. such as other processes or services or applications that require access to the cluster.
Security of application End Users is managed by the applications themselves, internally. So we will take them out of discussion.
### Accounts Authorization
All user access can be managed by the kube-apiserver, through set of authentication methods
- Static Password File ❌
- Static Token File ❌
- Certificates ✔️
- Identity Services ✔️
#### Using a Static password file "Not the best practice"
Using a three column '.csv' file, of password, username, users ID. And then passing the file to the `kube-apiserver.service`, then restarting the service.
*Note:* This file also can optionally have a fourth column, specifying the user group.

Or, If you set up your cluster using the Kubeadm tool, then you must modify the Kube-APIserver definition file. The Kubeadm tool will automatically restart the Kube API server once you update this file.
![[Pasted image 20240515141701.png]]
To authenticate using the user & password, we specify them in a curl command like this `curl -v -k https://master-node-ip:6443/api/vI/pods -u "userl:password123"`
#### Using a Token file "Not the best practice"
Similar to static password files, we can use a 3, or optionally a 4 column '.csv' file, but the first column is the token not the password.
To authenticate using the token, we specify them in a curl command like this `curl -v -k https://master-node-ip:6443/api/v1/pods --header "Authorization: Bearer KpjCVb17rCFAHYPkBzRb7gu1cUc4B"`












# Commands Archive
______________________________________________________________________
``` 
kubectl run <CONTAINER_NAME> --image <IMAGE_NAME>
```
- Starts a pod inside a node, & runs the image in the pod.
______________________________________________________________________
```
kubectl get <RESOURCE>
``` 
- Lists running resources for the given resource.
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
kubectl api-resources | grep <RESOURCE_NAME>
```
- check for apiVersion for a resource.
------------------------------------------------------------------
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
```
kubectl rollout status <DEPLOYMENT_NAME>/<CONTAINER_NAME>
```
- Shows current rollout status.
______________________________________________________________________
```
kubectl rollout history <DEPLOYMENT_NAME>/<CONTAINER_NAME>
```
- Shows applied history of rollouts.
______________________________________________________________________
```
kubectl rollout undo <DEPLOYMENT_NAME>/<CONTAINER_NAME>
```
- Rollbacks a pod to the older version.
______________________________________________________________________
```
kubectl create configmap <CONFIGMAP_NAME> --from-literal=<KEY_01>=<VALUE_01>  --from-literal=<KEY_02>=<VALUE_01> 

kubectl create configmap <CONFIGMAP_NAME> --from-file=<FILE_PATH>
```
- Creating a ConfigMap imperatively. 
______________________________________________________________________
```
kube-controller-manager --pod-eviction-timeout=<N>m<N>s
```
- Setting the node eviction timeout.
______________________________________________________________________
```
kubectl drain <NODE>
```
- Moving pods on a node to another & cordoning (marks as unschedulable) that node.
______________________________________________________________________
```
kubectl cordon <NODE>
```
- Cordoning (marks as unschedulable) that node.
______________________________________________________________________
```
kubectl uncordon <NODE>
```
- Uncordoning (marks as schedulable) that node.
______________________________________________________________________
```

```
- 
______________________________________________________________________
```

```
- 
______________________________________________________________________
```

```
- 
______________________________________________________________________
```

```
- 
______________________________________________________________________
```

```
- 
______________________________________________________________________
