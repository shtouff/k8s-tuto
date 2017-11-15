# create bucket for cluster state storage
The region must be us-east-1, no matter what the cluster region will be.

```
aws s3api create-bucket --bucket bbc-kops --region us-east-1
```

# get ami for coreos in us-west-2

```
AMI=$(curl -s https://coreos.com/dist/aws/aws-stable.json | jq -r '.["us-west-2"]["hvm"]')
```

# create cluster

We create a cluster using public topology. Master is HA, in 3 ZAs, and we add 2 nodes.
```
export NAME=rpaulmier.k8s.lab.blablacar.net
export KOPS_STATE_STORE=s3://bbc-kops

kops create cluster --master-zones=us-west-2a,us-west-2b,us-west-2c --zones=us-west-2a,us-west-2b,us-west-2c --node-count=2 --image ${AMI} ${NAME}
```

Then we edit the cluster, to change the CIDR subnets, the VM type (m4.large), and to verify the AMI (coreos):
```
kops edit ig --name=rpaulmier.k8s.lab.blablacar.net nodes
kops edit ig --name=rpaulmier.k8s.lab.blablacar.net master-us-west-2a
kops edit ig --name=rpaulmier.k8s.lab.blablacar.net master-us-west-2b
kops edit ig --name=rpaulmier.k8s.lab.blablacar.net master-us-west-2c
```

Finally, we actually create the cluster, then validate it:
```
kops update cluster ${NAME} --yes
kops validate cluster
```
