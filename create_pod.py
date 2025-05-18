from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Define the pod manifest
pod_manifest = {
    'apiVersion': 'v1',
    'kind': 'Pod',
    'metadata': {'name': 'example-pod'},
    'spec': {
        'containers': [{
            'name': 'example-container',
            'image': 'nginx',
            'ports': [{'containerPort': 80}]
        }]
    }
}

# Create the pod
v1 = client.CoreV1Api()
resp = v1.create_namespaced_pod(body=pod_manifest, namespace='default')
print("Pod created. Status='%s'" % resp.metadata.name)

