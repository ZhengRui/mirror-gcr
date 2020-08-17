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
        ),

    ],

}


def pull_tag():
    pass


if __name__ == '__main__':
    pass
