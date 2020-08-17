import os


repos = {
    'kubernetes-1.14.0': [
        (
            1,
            'k8s.gcr.io/kube-apiserver',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver',
            'v1.14.0'
        ), (
            2,
            'k8s.gcr.io/kube-controller-manager',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager',
            'v1.14.0'
        ), (
            3,
            'k8s.gcr.io/kube-scheduler',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler',
            'v1.14.0'
        ), (
            4,
            'k8s.gcr.io/kube-proxy',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy',
            'v1.14.0'
        ), (
            5,
            'k8s.gcr.io/pause',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/pause',
            '3.1'
        ), (
            6,
            'k8s.gcr.io/etcd',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/etcd',
            '3.3.10'
        ), (
            7,
            'k8s.gcr.io/coredns',
            'registry.cn-hangzhou.aliyuncs.com/google_containers/coredns',
            '1.3.1'
        ),
    ],

    'kubeflow': [
        (
            1,
            'gcr.io/kubeflow-images-public/kubernetes-sigs/application',
            'zerry/kubeflow-images-public.kubernetes-sigs.application',
            '1.0-beta'
        ), (
            2,
            'gcr.io/kubeflow-images-public/ingress-setup',
            'zerry/kubeflow-images-public.kubernetes-sigs.application',
            'latest'
        ), (
            3,
            'gcr.io/kubeflow-images-public/centraldashboard',
            'zerry/kubeflow-images-public.centraldashboard',
            'v1.0.0-g3ec0de71'
        ), (
            4,
            'gcr.io/kubeflow-images-public/jupyter-web-app',
            'zerry/kubeflow-images-public.jupyter-web-app',
            'v1.0.0-g2bd63238'
        ), (
            5,
            'gcr.io/kubeflow-images-public/katib/v1alpha3/katib-controller',
            'zerry/kubeflow-images-public.katib.v1alpha3.katib-controller',
            'v0.8.0'
        ), (
            6,
            'gcr.io/kubeflow-images-public/katib/v1alpha3/katib-db-manager',
            'zerry/kubeflow-images-public.katib.v1alpha3.katib-db-manager',
            'v0.8.0'
        ), (
            7,
            'gcr.io/kubeflow-images-public/katib/v1alpha3/katib-ui',
            'zerry/kubeflow-images-public.katib.v1alpha3.katib-ui',
            'v0.8.0'
        ), (
            8,
            'gcr.io/kubebuilder/kube-rbac-proxy',
            'zerry/kubebuilder.kube-rbac-proxy',
            'v0.4.0'
        ), (
            9,
            'gcr.io/kfserving/kfserving-controller',
            'zerry/kfserving.kfserving-controller',
            '0.2.2'
        ), (
            10,
            'gcr.io/kubeflow-images-public/metadata',
            'zerry/kubeflow-images-public.metadata',
            'v0.1.11'
        ), (
            11,
            'gcr.io/ml-pipeline/envoy',
            'zerry/ml-pipeline.envoy',
            'metadata-grpc'
        ), (
            12,
            'gcr.io/tfx-oss-public/ml_metadata_store_server',
            'zerry/tfx-oss-public.ml_metadata_store_server',
            'v0.21.1'
        ), (
            13,
            'gcr.io/kubeflow-images-public/metadata-frontend',
            'zerry/kubeflow-images-public.metadata-frontend',
            'v0.1.8'
        ), (
            14,
            'gcr.io/ml-pipeline/api-server',
            'zerry/ml-pipeline.api-server',
            '0.2.5'
        ), (
            15,
            'gcr.io/ml-pipeline/visualization-server',
            'zerry/ml-pipeline.visualization-server',
            '0.2.5'
        ), (
            16,
            'gcr.io/ml-pipeline/persistenceagent',
            'zerry/ml-pipeline.persistenceagent',
            '0.2.5'
        ), (
            17,
            'gcr.io/ml-pipeline/scheduledworkflow',
            'zerry/ml-pipeline.scheduledworkflow',
            '0.2.5'
        ), (
            18,
            'gcr.io/ml-pipeline/frontend',
            'zerry/ml-pipeline.frontend',
            '0.2.5'
        ), (
            19,
            'gcr.io/ml-pipeline/viewer-crd-controller',
            'zerry/ml-pipeline.viewer-crd-controller',
            '0.2.5'
        ), (
            20,
            'gcr.io/kubeflow-images-public/notebook-controller',
            'zerry/kubeflow-images-public.notebook-controller',
            'v1.0.0-gcd65ce25'
        ), (
            21,
            'gcr.io/kubeflow-images-public/profile-controller',
            'zerry/kubeflow-images-public.profile-controller',
            'v1.0.0-ge50a8531'
        ), (
            22,
            'gcr.io/kubeflow-images-public/pytorch-operator',
            'zerry/kubeflow-images-public.pytorch-operator',
            'v1.0.0-g047cf0f'
        ), (
            23,
            'gcr.io/spark-operator/spark-operator',
            'zerry/spark-operator.spark-operator',
            'v1beta2-1.0.0-2.4.4'
        ), (
            24,
            'gcr.io/google_containers/spartakus-amd64',
            'zerry/google_containers.spartakus-amd64',
            'v1.1.0'
        ), (
            25,
            'gcr.io/kubeflow-images-public/tf_operator',
            'zerry/kubeflow-images-public.tf_operator',
            'v1.0.0-g92389064'
        ),

    ],

}


def pull():

    for i, en_repo, cn_repo, tag in repos['kubeflow']:
        # check if exists
        tag_ = os.popen(f"docker images -a | grep {en_repo} | awk '{{print $2}}'").read().strip()
        if tag_ == tag:
            continue

        os.system(f"docker pull {cn_repo}:{tag}")
        os.system(f"docker tag {cn_repo}:{tag} {en_repo}:{tag}")
        os.system(f"docker rmi {cn_repo}:{tag}")

        tag_ = os.popen(f"docker images -a | grep {en_repo} | awk '{{print $2}}'").read().strip()
        assert tag_ == tag


if __name__ == '__main__':
    pull()