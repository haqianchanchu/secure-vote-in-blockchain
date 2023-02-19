SE_PATH = "./se_result"
NS_PATH = "./ns_result"
import matplotlib.pyplot   as plt
import json

def plot_by_ep(k, msg):
    msg1 = json.loads(msg)
    ans_list = []
    for ele in msg1:
        if ele["CP_k"] == k:
            ans_list.append(ele)
    x = []
    y_chain = []
    y_vote = []
    for ele in ans_list:
        x.append(ele["EP"])
        y_chain.append(ele["chain_acc"])
        y_vote.append(ele["vote_acc"])
    return (x, y_chain, y_vote)


def main():
    with open(SE_PATH, "r") as f:
        msg1 = f.read()
    with open(NS_PATH, "r") as f:
        msg2 = f.read()
    k = 28
    [x, y_se_chain, y_se_vote] = plot_by_ep(k,msg1)
    [x, y_ne_chain, y_ne_vote] = plot_by_ep(k,msg2)
    plt.plot(x,y_se_chain,label='secure chain')
    plt.plot(x,y_ne_chain,label='nosecu chain')
    plt.plot(x,y_se_vote,label='secure vote')
    plt.plot(x,y_ne_vote,label='nose vote')
    plt.axis([0, 0.5, 0, 1])
    plt.xlabel('epislon')
    plt.ylabel('secure rate')
    plt.title("k=15")
    plt.grid(True)
    plt.legend()
    plt.show()
     


if __name__ == "__main__":
    main()