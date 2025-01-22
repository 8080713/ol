import os
import subprocess

def process_tvbox(username, token, urls, repo='tvbox', target='tvbox.json', num=None, timeout=3, signame=None, jar_suffix='jar', mirror=1):
    """
    处理TVBox配置
    :param username: GitHub用户名
    :param token: GitHub token
    :param urls: 要处理的URL列表
    :param repo: GitHub仓库名，默认tvbox
    :param target: 输出文件名，默认tvbox.json
    :param num: 多仓时下载的仓库数量
    :param timeout: HTTP请求超时时间，默认3秒
    :param signame: 单线路名
    :param jar_suffix: jar包后缀，默认jar
    :param mirror: 镜像编号，默认1
    """
    # 构建Docker命令
    cmd = [
        'docker', 'run', '--rm',
        '-e', f'username={username}',
        '-e', f'token={token}',
        '-e', f'url={",".join(urls)}',
        '-e', f'repo={repo}',
        '-e', f'target={target}',
        '-e', f'timeout={timeout}',
        '-e', f'jar_suffix={jar_suffix}',
        '-e', f'mirror={mirror}'
    ]
    
    if num:
        cmd.extend(['-e', f'num={num}'])
    if signame:
        cmd.extend(['-e', f'signame={signame}'])

    cmd.append('2011820123/tvbox')

    # 执行Docker命令
    try:
        subprocess.run(cmd, check=True)
        print("TVBox processing completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error processing TVBox: {e}")

if __name__ == "__main__":
    # 从环境变量获取配置
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
    urls = os.getenv('TVBOX_URLS', '').split(',')

    if not username or not token or not urls:
        print("Please set GITHUB_USERNAME, GITHUB_TOKEN and TVBOX_URLS environment variables")
        exit(1)

    process_tvbox(username, token, urls)
