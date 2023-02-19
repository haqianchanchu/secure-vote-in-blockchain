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
def plot_by_k(ep, msg):
    msg1 = json.loads(msg)
    ans_list = []
    for ele in msg1:
        if ele["EP"] == ep:
            ans_list.append(ele)
    x = []
    y_chain = []
    y_vote = []
    for ele in ans_list:
        x.append(ele["CP_k"])
        y_chain.append(ele["chain_acc"])
        y_vote.append(ele["vote_acc"])
    return (x, y_chain, y_vote)

def main():
    with open(SE_PATH, "r") as f:
        msg1 = f.read()
    with open(NS_PATH, "r") as f:
        msg2 = f.read()
    k = 13
    # [x, y_se_chain, y_se_vote] = plot_by_ep(k,msg1)
    # [x, y_ne_chain, y_ne_vote] = plot_by_ep(k,msg2)
    ep = 0.3
    [x, y_se_chain, y_se_vote] = plot_by_k(ep,msg1)
    [x, y_ne_chain, y_ne_vote] = plot_by_k(ep,msg2)
    # help(plt.plot)
    plt.plot(x,y_se_chain,"p--",color="orange", label='secure chain')
    plt.plot(x,y_ne_chain,color="orange",label='nosecu chain')
    plt.plot(x,y_se_vote,"p--",color="green",label='secure vote')
    plt.plot(x,y_ne_vote,color="green",label='nose vote')
    plt.axis([4,18 , 0, 1])
    plt.xlabel('epislon')
    plt.ylabel('secure rate')
    plt.title( "Accurate rate with ep="+str(ep))
    plt.grid(True)
    plt.legend()
    # plt.show()
    plt.savefig("./ficture", dpi=600)
     


if __name__ == "__main__":
    main()