# Part1: Running Pipelines on Gitlab

### Gitlab Architecture 
- Gitlab runners retrieve setup instructions stored in the Gitlab server.
- Then it downloads & starts the docker image specified.
- Then files are retrieved form a get repository.
- Then runs all the commands specified in the job.
- Then report back the execution result to the Gitlab server. 
- After the job is finished the docker container will be destroyed "Meaning that each time Gitlab runner starts the job, it creates a new Docker container".
![Pasted image 20230127035318](https://user-images.githubusercontent.com/109697567/220482787-eb50e3bb-9e25-4999-bbb9-14a1b483725e.png)
These steps can be seen in the pipeline results (Blue & white):
![Pasted image 20230127040434](https://user-images.githubusercontent.com/109697567/220482807-e635bda9-c464-47c4-b05d-803258c2b8fd.png)
### Building a Pipeline
Pipeline is a set of jobs that gets done in stages.
![Pasted image 20230119163003](https://user-images.githubusercontent.com/109697567/220482836-2513c643-b348-4102-8eb3-55a480b52e47.png)
### Yml Files
Simply by using spaces & tabs, it's able to create nesting behavior in the yml files:
![Pasted image 20230127034641](https://user-images.githubusercontent.com/109697567/220482893-d65a2687-fa1c-42e8-bc73-c5fc3c10a06b.png)
*Notice:* The image represents a one job, the job is "person"

### Create a file named as *.gitlab-ci.yml*
- Notice that the .yml is case sensitive & spaces matter.
- The default working image chosen by git-lab is "Ruby-Docker image", remember to change it to the desired image, simply by specifying a key word "image" as following
```
Main job:
	image: alpine
```
- Write a simple code line, under a job at the top
```
Main job:
	script: echo "Hello World"
```
- Write a multiple-line Code, to do this, use "-" to create a list.
```
Main job:
	script:
		- mkdir folder
		- touch folder/file.txt
		- echo "Main Text" >> folder/file.txt
```

### Gitlab Runners
By default, Gitlab will have the option to use online shared runners to pick up the jobs, this can be turned off & set to a specific runner.
![Pasted image 20230208180815](https://user-images.githubusercontent.com/109697567/220482966-50842170-0048-4f02-8a72-0d82ab1c7d6a.png)

- To use a runner, it must have Gitlab Runner installed on it.
	[Install GitLab Runner | GitLab](https://docs.gitlab.com/runner/install/)
- Link the runner to your Gitlab Project using the command:
```
sudo gitlab-runner register
```
- Register the runner with this URL:  
	`https://gitlab.com/`       
- Enter the registration token of the project
![Pasted image 20230208181357](https://user-images.githubusercontent.com/109697567/220482999-5c453489-d797-45ef-80ab-d3b1e6ea9ba9.png)
- Important note: Create a tag for the Runner as it will be needed for picking up a job.

### Assigning a job to a Gitlab Runner "tags"
If you are using a project runner, then you must assign the tag to the job that will run using this runner
- For the Runner in the previous image with the tags "local, vm" we will assign the job to it as follows:
```
Main job:
	tags:
		- local
		- vm
	script:
		- mkdir folder
		- touch folder/file.txt
		- echo "Main Text" >> folder/file.txt
```
- Otherwise you will get an indication that the job is stuck because there is no runner assigned to it.

### Pipeline Status
If there is any conflicts making the pipeline stuck, it can be indicated as a cross sign, in this case it's working:
![Pasted image 20230127032711](https://user-images.githubusercontent.com/109697567/220483040-bfff6677-f42a-4753-b387-ab1a59ba2547.png)

### Pipeline Stages:
When you put multiple Jobs in one file, they will run simultaneously without a specific order.
- Use the job "stages" to specify stages & order of the jobs.
- Specify the stage in each job.
This way job2 won't start until job1 is finished:
![Pasted image 20230127045603](https://user-images.githubusercontent.com/109697567/220483053-74244bcb-5214-48fd-9122-21e5d2851abf.png)
**However you'll still see here that job2 is still failing.**
	This is because job1 destroys the container after the job is executed as discussed before, & job2 creates a new container, so the test command has false response.

#### Predefined Stages:
Gitlab already has built in Predefined Stages, coming in order as:
- .pre
- build
- test
- deploy
- .post

These stages doesn't need defining in the .yml file.

### Parallel Staging
If more than one job have the same stage, they will run in parallel & failure of one won't stop the other one from running by default.

- To make a job dependent on another job in thew same stage we can use the keyword `needs` followed by the list of required jobs
```
	needs:
		- job1
```

### Pipelines Failing
Pipelines uses exit codes to indicate if the pipeline was executed successfully or not.
- "exit code 0" indicates that the pipeline was executed successfully.
- Any other number indicates an error.
- the numbers can go from 0 to 255.
![Pasted image 20230127050827](https://user-images.githubusercontent.com/109697567/220483077-025dd48a-d73c-4d9f-a1e5-09d76dd50295.png)

### Job Artifacts
In the example mentioned, each job had its own different container, which defeats the purpose of using stages.
- Job Artifacts are items that are set to be kept after the job is done & doesn't get lost when the container gets destroyed
![Pasted image 20230127051550](https://user-images.githubusercontent.com/109697567/224810969-ab959a70-d6b2-4c32-a876-3a364d3fda40.png)
This can be seen from the pipeline logs for both stages as well either in the logs or as files to browse through
![Pasted image 20230127052000](https://user-images.githubusercontent.com/109697567/220483094-88bbd1e3-a155-443a-9d30-6df335699b48.png)
![Pasted image 20230127053411](https://user-images.githubusercontent.com/109697567/220483119-94dad361-38a4-4393-a41c-cdd5beeef3db.png)
- The key word `path` made the artifacts browsable, there are other keywords, for example `reports` can be used to show us the test reports in Gitlab pipeline test tab
![Pasted image 20230214192408](https://user-images.githubusercontent.com/109697567/220483147-63f9d031-1fba-4555-bbe5-ca7ee57252be.png)

- Artifacts are downloaded for all stages by default.
- If the two jobs are in the same stage, the other job will not have the artifacts, use `dependencies: - job1` for artifacts downloading or `needs: - job1` for artifacts downloading & pending start of the second till success of the first.
- To prevent a job from downloading the artifacts, use `dependencies: []`

### .env Files "Environmental Artifacts"
Gitlab provides a feature of storing data "could be variables" inside a file of extension .env, this will provide the variables inside it to all jobs "unless an empty array dependency is set".
- Suppose we want to apply dynamic versioning from the version indicated in the package.json file we have in our project, & the pipeline ID. "using jq command"
```
	- export PACKAGE_JSON_VERSION=$(cat FrontEnd/package.json | jq -r .version)
	- export VERSION=$PACKAGE_JSON_VERSION.$CI_PIPELINE_IID
```
- Now to store in the .env file
```- echo "VERSION=$VERSION" >> environmental-variables.env ```
- Then in the artifacts store it as "dotenv report" :
``` 
artifacts:
	reports:
		dotenv: environmental-variables.env
```

### Setting Variables
It's able to set a variable either specifically for each job, or globally for all jobs.
- For setting a variable name globally:
```
variables:
	VAR_NAME: file.txt
job1:
	script: echo "Text Inside" >> $VAR_NAME
job2:
	script: echo "New Text" >> $VAR_NAME
```
- For setting a variable name for a job:
```
Main job:
	variables:
		VAR_NAME: file.txt
	script: echo "New Text" >> $VAR_NAME
```
- Setting a variable name for a job also can be determined inside the script:
```
Main job:
	script:
		- VAR_NAME: file.txt
		- echo "New Text" >> $VAR_NAME
```
*Note:* Variable name can be either in lower case or upper case or both, but it's case sensitive, **& it's known to be set as upper case in a working environment.**

### Global Variables
You can add variables in the CI/CD tab in the project settings instead of inputting them in jobs.
- "Protect Variables" option makes the variable available only for the protected branches, as the main branch, so disable it unless needed.
- "Mask Variables" option masks the variable in printed pages for security.
- Here I created a variable for an S3 bucket on AWS:
![Pasted image 20230208184444](https://user-images.githubusercontent.com/109697567/220483180-fc64cabb-e77e-4e6d-ad57-4b413fa14ef7.png)

### Predefined Variables
Gitlab comes with some predefined variables that can be used in the project. Can be found at  `https://docs.gitlab.com/ee/ci/variables/predefined_variables.html`

### Disabling A Job
Placing a dot before the job name will disable it in the next pipeline run.
- Job1 is now disabled:
```
.Job1:
	image:
	script:
	
```

### Job Timeouts
If a job cannot end/succeed or fail, it doesn't run forever, but it has a specific max timeout to be terminated.
![Pasted image 20230206224817](https://user-images.githubusercontent.com/109697567/220483203-a34b48ad-d64e-4aa4-bae8-42de5b48dfbf.png)

### Testing Stage
Instead of the test command, serve command can be more useful as it starts a server for the specified path not only checks it.
```
test job:
	image: node:16-alpine
	script:
		- serve -s build_folder
```
*Note:* serve command is not defined in the default image, so a specified supporting image should be used.

- Notice: if we used "curl | grip" to test the server connection, the command "curl" is a dependency on alpine image, so make sure to use the alpine package manager if not using the alpine image:
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder
		- curl http://localhost:3000 | grep "text in source"
```

- The serve command starts a server, & it's supposed to be running forever until termination, so it stops the job from finishing & the job will reach timeout.
You can create the server in the background of the job using "&" sign at the end, this will not stop the job from completing.
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder &
		- curl http://localhost:3000 | grep "text in source"
```

- Use the command "sleep" so that the job gives time to the server to run, it takes a parameter in seconds.
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder &
		- sleep 20
		- curl http://localhost:3000 | grep "text in source"
```

### Gitlab Repositories
Gitlab has 3 types of repositories:
![Pasted image 20230214193815](https://user-images.githubusercontent.com/109697567/220483239-9edf12ff-8a0f-4496-bd58-648bc2ca1e58.png)
- In order to push/pull an image to a private docker repository you must have the credentials required.
- The repository location is included in the image name
![Pasted image 20230214193904](https://user-images.githubusercontent.com/109697567/220483255-eab5e0ca-d950-4f77-a687-fcfd11c87b02.png)

### Linter
"lint" is a command used to checks C and C++ language programs for potential problems., so it's used mostly as a .pre stage.

```
linter job:
	image: node:16-alpine
	stage: .pre
	script:
		- yarn install
		- yarn lint
```

### Executing Shell Scripts
The code can get bigger inside the .yml file & may result in less readable scripts & lose of overview of it.
- The script can be written in a separate `.sh` file, & executed given its path.
- Remember to add the execution permission to it.
```
	script:
		- chmod +x script.sh
		- ./script.sh
```

### Protecting Branches & Merge Requests
- To Protect a branch from directly pushing into it, go to `"Settings > Repository > Protected Branches"`.
- You can see all the merge requests to be created, merged or cancelled directly from the `"Merge Requests"`.
- You can view all the branches from `"Repository > Branches"`.

# Part2: Pipelines Deployment to AWS 

## Deploy stage
After the testing's succeed, the deployment stage starts, and will be deployed to an S3 Bucket.

### AWS CLI
Make sure to add the "AWS CLI" docker image to the stage, & it can be found & copied from the docker hub "amazon/aws-cli".
![Pasted image 20230208172419](https://user-images.githubusercontent.com/109697567/220483275-61fefea1-d157-454a-b4ca-8a24fb4f35bd.png)
Notice that the image has an entry point, an application that runs with the image. This conflicts with how Gitlab run images, so in order to overwrite this, use the property **"entrypoint"**
```
deploy to s3:
	stage: deploy
	image:
		name: amazon/aws-cli:2.9.21
		entrypoint: [""]
	script:
		- aws --version
```

### Storing on an S3 Bucket
Let the following code be desired for storing a file on an S3 bucket, with the bucket name assigned toa custom variable: `$AWS_S3_BUCKET`
```
deploy to s3:
    stage: deploy
    image:
        name: amazon/aws-cli:2.9.21
        entrypoint: [""]
    script:
        - aws --version
        - echo "Hello s3" > text.txt
        - aws s3 cp text.txt s3://$AWS_S3_BUCKET/text.txt
```
- The pipeline will fail because of missing credentials
	- Create an IAM user with S3 access permissions.
	- Assign an access key to it and add it as a variable.
	- ***NOTE:*** upon adding the variable it must be under the name of `AWS_ACCESS_KEY_ID` & you will see that it will be autocompleted, AWS CLI will look for the variable with the same name
	![Pasted image 20230208191528](https://user-images.githubusercontent.com/109697567/220483301-4f831307-6895-4c95-9b41-c68164f21aad.png)
	- Do the same for `AWS_SECRET_ACCESS_KEY`
	- Use the variable `AWS_DEFAULT_REGION` to avoid specifying a region "Because S3 buckets are region specific services".
	![Pasted image 20230208192357](https://user-images.githubusercontent.com/109697567/220483384-704568e1-da32-4f71-a569-05aea95c5011.png)
- Now retry running the pipeline with the same job, it will succeed, this is because AWS CLI automatically reaches for the credentials given.
- You can find the text.txt file now in the S3 bucket.
![Pasted image 20230208193208](https://user-images.githubusercontent.com/109697567/220483407-362942b2-e1a8-4c3f-afa5-b451eb75e86f.png)

### Deploy to EC2 instance
In order to deploy to an EC2 Instance you have to SSH to it first, make sure that the instance security group allows SSH.
*Note:* When trying to SSH to an instance for the first time you will have an interactive question, which will interrupt the automation process.
![Pasted image 20230306200403](https://user-images.githubusercontent.com/109697567/224811200-4a54846a-c159-44ed-861a-d595bb3dd9fe.png)
- In order to avoid this, use the option:
`-o StrictHostKeyChecking=no`
- You can use a variable for the instance IP address for a cleaner code.
- Remember that you don't have the SSH key on your Gitlab project "& shouldn't upload it", so make sure to store its value as a variable.
so the deploy script should be something like this:
```
	script:
		- ssh -o StrictHostKeyChecking=no -i $EC2Key ubuntu@ec2-18-130-232-114.eu-west-2.compute.amazonaws.com
```
*Note:* To get the value of the the SSH key, use the command `cat` locally on your machine & copy the value

### Branches & Controlling When Jobs Run "Job Rules"
If we committed on a different branch from the main branch, we can then merge the branch into the main if the pipeline succeeded.
- We desire that only the build & the test stage gets committed on a feature branch, & only if it's merged then the deployment job gets initiated, otherwise on every small edit or a feature the whole pipeline will start, meaning that the S3 bucket will get the deployed objects from the feature branch even if it's not merged.
	- we can use the keyword rule to control when a job starts.
	- To make a job only running if the current branch is the main branch:
```
	rules:
		- if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```
*Notice:* `CI_COMMIT_REF_NAME`: A predefined variable for the branch or tag name for which project is built, `CI_DEFAULT_BRANCH`: A predefined variable for the name of the project’s default branch.

- Another better way of doing this is using the keywords `only` & `except` 
	* `only` defines when a job runs.
	- `except` defines when a job doesn't run.
```
	only:
		- main
	except:
		- branch2
```

### Workflow
Workflow controls whether the whole pipeline is to be created or not, using rules.
- It's written at the start of the pipeline code not inside a job.
- The following workflow runs the pipeline only in the main branch & merge requests.
```
workflow:
	rules:
		- if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH && $CI_PIPELINE_SOURCE != "merge_request_event"
			when: never
		when: always
```

### Deploy Staging Concept
Often pipelines have a staging environment before the deployment stage, which basically is a simulation of the deployment stage, but not a production environment.
It's main purpose is to prevent flows into the deployment stage if any adjustments was done to it or the buckets.
- Staging uses a bucket different from the production/deployment buckets, but usually the promotion is done automatically.

### Continuous Delivery
In Continuous Deployment, the staging triggers the deployment stage on success, while on Continuous Delivery, the promotion from staging to deployment is done manually.

- In order to do this, use a condition `when: manual` inside the deployment job, & you will see that it has to be started manually with a button.
![Pasted image 20230209194149](https://user-images.githubusercontent.com/109697567/220483442-07daeda8-9b13-48cb-b957-5e97a1b5fd33.png)

### Environments
Introducing staging subjected us to using many variables as we now have two URLs, two S3 buckets, etc.

Gitlab Environments basically describe where this code is deployed, so the staging, production, deployment for example all can be treated as different environments.

- To add a new environment, go to `"Deployments > Environments"` and create a new environment.
- You can use the S3 bucket web hosting link as the External link.

Now we can see that we can define the same variable for the same value, each with a different environment scope
![Pasted image 20230209190141](https://user-images.githubusercontent.com/109697567/220483456-06bbea26-6c29-452d-b948-9e538353c6cf.png)
- You can find in the global variables page a variable for current environment URL `$CI_ENVIRONMENT_URL`
- Use the keyword `environment:` in the job to specify its environment.
```
staging:
	image:
	environment: staging
	script:
```

### Reusing Configuration
As seen before, we reused identical configurations for both staging & deploying stages, only the stage & the environment was set to be different.
- We can create an disabled job & recall it inside other jobs with the key word `extends:`

- In the following code we set a disabled recall job syncing the folder `build` to the S3 bucket assigned to the variable, & then also testing in the same job. Notice that it doesn't have neither a stage nor an environment.
- We recalled it at the staging & deployment jobs, each with its own stage & environment.
- You can pass important variables to it by setting them as empty.
```
.recall:
	image:
		name: amazon/aws-cli:2.4.11
		entrypoint: [""]
	rules:
		- if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
	script:
		- aws s3 sync build s3://$AWS_S3_BUCKET --delete
		- curl $CI_ENVIRONMENT_URL| grep "$GREP"
	variables:
		GREP: ""

staging:
	stage: staging
	environment: staging
	extends: .recall
	variables:
		$GREP: React App

deploy:
	stage: deploy
	environment: deploy
	extends: .recall
	variables:
		$GREP: React App
```
*Notice:* when recalling the job with the keyword extends, we used a dot before the disabled job.

# Development Environment & Docker Files on Gitlab
As mentioned before Gitlab provides docker repository for each project, having the same privacy as the project "private/public"

### Building a docker image
**Requires:**
- An image supporting docker commands
	`image: docker:dind`
- Authentication
	`docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY`
- Specifying the Project Repository
	`docker build -t $CI_REGISTRY_IMAGE:1.0 /docker_file_directory `
- Adding user to the docker group on the runner command interface.
	`sudo usermod -aG docker ubuntu `

So the build stage should be something like this:
```
build_image:
	image: docker:dind
	stage: build
	before_script:
		- docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
	script:
		- docker build -t $CI_REGISTRY_IMAGE:1.0 /docker_file_directory
```

### Pushing a docker image
**Requires:**
- An image supporting docker commands
	`image: docker:dind`
- build image job
	`needs: - build_image`
- Authentication
	`docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY`
- Specifying the Project Repository
	`docker build -t $CI_REGISTRY_IMAGE:1.0 /docker_file_directory `
- Adding user to the docker group on the runner command interface. **DONE**

So the push stage should be something like this:
```
push_image:
	image: docker:dind
	stage: build
	needs:
		- build_image
	before_script:
		- docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
	script:
		- docker push $CI_REGISTRY_IMAGE:1.0
```

##### IMPORTANT FILE CONFIGURATION
Sometimes building image on the runner instance results in the following error
![Pasted image 20230306204120](https://user-images.githubusercontent.com/109697567/224811375-998dba4d-6dc7-42af-9cc3-9ce0ce18609f.png)
- To fix this go to the instance interface & edit the file:
`/etc/gitlab-runner/config.toml`
- Make sure the following values are edited "use command `sudo vim `"
![Screenshot 2023-03-06 204619](https://user-images.githubusercontent.com/109697567/236550285-9ecf6494-ea15-4de2-88cf-c54d80d345b3.png)

### Deploy a docker image to EC2
**Requires:**
- An image supporting docker commands
	`image: docker:dind`
- Permission for the SSH Key "Store it as a file type variable"
	`chmod 400 $EC2_Key`
- SSH Authentication to EC2 instance
	`ssh -o StrictHostKeyChecking=no -i $EC2_Key ubuntu@$public_ip`
- Running the docker image on the instance
	For this you have to use the commands as parameters in the SSH command "Suppose Docker File used port 3000":
	```
	ssh -o StrictHostKeyChecking=no -i $EC2_Key ubuntu@$public_ip " 
		docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY &&
		docker run -d -p 3000:3000 $CI_REGISTRY_IMAGE:1.0"
	```

So the deploy stage should be something like this:
```
deploy_to_ec2:
	image: docker:dind
	stage: deploy
	before_script:
		- chmod $EC2_Key
	script:
		- ssh -o StrictHostKeyChecking=no -i $EC2_Key ubuntu@$public_ip " 
			docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY &&
			docker run -d -p 3000:3000 $CI_REGISTRY_IMAGE:1.0"
```

### Using Environments
We can access the project with the EC2 public IP or with its public DNS, however this can be done in a better way if we set environments.
![Pasted image 20230306230116](https://user-images.githubusercontent.com/109697567/224811493-c4ac2b75-c006-4250-b246-26bdb343b699.png)

# Docker compose
If we changed the version from 1.0 to another version, or tried to build another container, we will get an error due to the existing container. That's why we use docker compose files

The following is required:
- Create a `"docker-compose.yaml"` file.
- Create the containers desired to run.
- Use docker compose to disable all containers in the .yaml file.
	` docker-compose -f docker-compose.yaml down`
- Use docker compose to start all containers in the .yaml file.
	` docker-compose -f docker-compose.yaml up -d`
- Copy the docker-compose.yaml file to the EC2 instance, as it is on our Gitlab repository but not on the instance.
	`scp -o StrictHostKeyChecking=no -i $EC2_Key ./docker-compose.yaml ubuntu@$public_ip:/home/ubuntu`
- Make sure that docker-compose is installed on the instance, it's a different package from docker.

So the deployment stage with a docker compose file will be something like this:
```
deploy_to_ec2:
	image: docker:dind
	stage: deploy
	before_script:
		- chmod $EC2_Key
	script:
		- scp -o StrictHostKeyChecking=no -i $EC2_Key ./docker-compose.yaml ubuntu@$public_ip:/home/ubuntu
		- ssh -o StrictHostKeyChecking=no -i $EC2_Key ubuntu@$public_ip " 
			docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY &&
			docker-compose -f docker-compose.yaml down &&
			docker-compose -f docker-compose.yaml up -d"
```

& in the docker-compose.yaml:
```
version: 3.6
services:
  app:
  image: registry.gitlab.com/kmw4rda/project-practice:1.0
  ports:
    - 80:3000
```
The previous docker-compose file have the same job as running the command `docker run -d -p 3000:3000 $CI_REGISTRY_IMAGE:1.2`

*Note:* Docker-compose will by default look for the file named docker-compose.yml or docker-compose.yaml, so you can remove the file specification from the docker-compose commands above to have less code.

### Docker-Compose Name
If we have multiple deployment environment, or multiple microservice services deployed on the same server, using the `docker-compose down` as before will destroy the docker containers on the server and only the final stage will be deployed. This is because all the container will start having the same default name.

To solve this use the attribute `COMPOSE_PROJECT_NAME` :
```
	script:
		- scp -o StrictHostKeyChecking=no -i $EC2_Key ./docker-compose.yaml ubuntu@$public_ip:/home/ubuntu
		- ssh -o StrictHostKeyChecking=no -i $EC2_Key ubuntu@$public_ip " 
			docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY &&
			
			expoort COMPOSE_PROJECT_NAME:$ENVIRONMENT_NAME
			
			docker-compose -f docker-compose.yaml down &&
			docker-compose -f docker-compose.yaml up -d"
```
This is a docker-compose variable and has to be defined as it is:  ***COMPOSE_PROJECT_NAME***

### Using Multiple Docker-Compose Files
If we have 3 different deployment environments, we want each of them to run on a different port on the same server for example, this needs 3 different docker-compose files. This can be done with 1 docker-compose configuration per project.

- We can set the values in the docker-compose file as variables inside curled brackets to be passed in the deployment job.
![Pasted image 20230313235943](https://user-images.githubusercontent.com/109697567/224875452-fc2a6538-1340-4210-8afe-6e179e0a5e7d.png)

# Optimization

### Caching
Gitlab caching allows us to save time by downloading dependencies we need in different jobs on the runner, a suitable case will be if we installed a dependency "as node image" on a job & the  other jobs need it as well, or to use it from previous pipelines to save time.
- Caching vs Artifacts:
	Artifacts download the dependencies on the Gitlab server & is distinct for each pipeline.
	While caching downloads dependencies on the Gitlab Runner to be used for all many pipelines.
*Notice:* Caching might be inefficient in case of many runners, in this case a different area can be used for caching "like an S3 bucket".

- Keys are set to identify the cache, jobs with the same cache key will use the cache with the key "Here we used the key to be branch specific & `$CI_COMMIT_REF_NAME` is a predefined variable for current branch".
- Paths are set to identify the files desired to be cached "you can use it as an array".
- We can set policy for caching for each job "as pull to only download cache & not update it". Default policy is pull-push "no need of specification".
```
	cache:
		key: "$CI_COMMIT_REF_NAME"
		paths:
			- ForntEnd/node_modules
		policy: pull-push
```


#### Docker Runners Caching
If we are executing a job on a docker runner, we know that the container gets destroyed after the job succeeds, so the caching stored on the container is lost.

- We can set a Docker volume on our host "runner" to persist the caching.
- Edit the file `/etc/gitlab-runner/config.toml` & add a cache path:
![Screenshot 2023-03-12 010219](https://user-images.githubusercontent.com/109697567/224875527-346cb312-cbed-43c5-8b21-333d98779b8e.png)

# Gitlab Templates
### Gitlab Predefined Templates
Gitlab provides templates for jobs that are ready to be used in our pipelines, these templates can be found at the repository [lib/gitlab/ci/templates · master · GitLab.org / GitLab FOSS · GitLab](https://gitlab.com/gitlab-org/gitlab-foss/tree/master/lib/gitlab/ci/templates)

For example we want to use the SAST Testing job template, to do this we use it as a job with its assigned name, & use the key word `include` to reference the projects or templates required to be included, for templates we use the parameter `template:`
```
sast:
	stage: test
	tags: - $MY_RUNNER

include:
	template: Jobs/SAST.gitlab-ci.yml
```
![Pasted image 20230312011025](https://user-images.githubusercontent.com/109697567/224811579-8917c2ce-4908-43df-bcd5-19ccfa9292ed.png)


### Pipeline Templates
There are also pipeline templates for the whole pipeline, this can be found in the pipeline tab of a project with no pipeline.
![Pasted image 20230312011406](https://user-images.githubusercontent.com/109697567/224811613-fafe2df1-cc34-45d4-a1ac-d91a5f23209d.png)

### Custom Templates
Gitlab allows creation of custom templates in different repositories to be called, this can be useful in sharing pipelines configurations among different repositories.

- When creating a template, you don't have to name it a specific name as in case of the main pipeline file. suppose we created a template of name `.build-template.yaml`.
- Remember to make it generic with variables that can be passed from other repositories.
- This can also be used for organizing a huge pipeline in a repository
- Use `include` to call a template to a job
For a repository containing the template:
```
include: 
	- local: './build-template.yaml'
```
For different repository in the same group: "ref is for branch"
```
include:
	project: 'group-name/my-templates'
	ref: main
	file:
		- build-template.yaml
		- deploy-taemplate.yaml
```
For a totally different repository:
```
include:
	- remote: $THE_FILE_PUBLIC_URL
```
- After calling the template we start the job inside it by setting a job with the same name, so if the job in the template has the name "build:" then we set an empty job in the pipeline yaml file with the name "build:"
- IMPORTANT: Adding a "script:" or "before_script:" keyword will overwrite the job, not add to it

# Microservices pipelines
In Gitlab, we have two types of repositories dealing with microservice applications:
- Monorepo applications:
	Having all the parts of the project in one repository, usually with a folder for each microservice.
- Polyrepo applications:
	Having a specific repository for each microservice.

## Monorepo Applications

### Starting specific jobs
Suppose we have 3 Microservices, we want to run a stage in the pipeline only if the corresponding microservice was edited or updated, instead of running the whole pipeline on each commit.

We can use the attribute `only` that we used for running the pipeline only in the main branch, with the keyword `changes` for checking if changes was done to the path provided.
```
products:
	stage: build
	only:
		chhanges:
			- "products/**/*"
```
Remember to use `extends` if there are multiple microservice with repetitive configuration.

*Note:* you will notice that if the pipeline/job failed, for example due to an invalid yaml syntax, the pipeline won't restart the failed jobs automatically after fixing the error, because there are no change detected in the path provided, even though the automatically triggered job failed. So you must start a new pipeline manually.

### Monorepo Deployment
We know we can use a single docker-compose file in the project to deploy to different environments, this concept can be used to deploy multiple services separately, which we want here. 
However doing this creates the containers in 3 different networks, & the services will be deployed successfully but won't be able to communicate with each other by default "there are tools that can be used to overcome this".

Docker-compose network naming uses the following scheme: the name of the project name "we used `COMPOSE_PROJECT_NAME` to set it", followed by default. so we have "frontend.default & backend.default" as the network name for example, two different networks.

- To fix this we can create a network in the docker-compose file:
![Pasted image 20230314013902](https://user-images.githubusercontent.com/109697567/224875590-f4dbe4dd-85fb-43fc-a2fb-73b436dc0aaa.png)

- We can use a preexisting network as well using `external`, this removes the need of `bridges` of course.
![Pasted image 20230314003018](https://user-images.githubusercontent.com/109697567/224875621-2bf1e2fa-9a7c-4951-b6ba-6feae338e099.png)
*Note:* The double pipe "|| true" in the command is important because the command will fail in the second run due to the network being already created, so we set it to ignore on failure.

## Polyrepo Applications

### Gitlab Groups
Each Microservice has its own repository, and these repositories are set in one group.
- Creating a group can be done via the group tab on Gitlab home screen.

![Pasted image 20230314015739](https://user-images.githubusercontent.com/109697567/224875654-412bb82b-f6de-4a7e-bf28-2e58440ae510.png)

### Group Runners & Shared configurations
We can assign Gitlab runners for the group to be shared across all the projects. This is applicable also for variables, registries & most of the configurations.

### Job Templates & Sharing Pipelines
In a Polyrepo Project, each service has its own pipeline, & we may find repetitive configurations as in case of Monorepo projects. However we can't use `extends` in this case.

- We can use custom templates.
- Set a template either in one repository of the services repositories, or a new repository for templates.
- Seek Custom Templates section.
