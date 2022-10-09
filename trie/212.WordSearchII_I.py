from typing import List, Set, Tuple

class TrieNode:
    def __init__(self) -> None:
        self.endAt = [False] * 26
        self.posts = [None] * 26
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        index = -1
        length = len(word)
        for letterIdx, letter in enumerate(word):
            index = ord(letter) - 97
            if currNode.posts[index] == None:
                currNode.posts[index] = TrieNode()
            if letterIdx == length - 1:
                currNode.endAt[index] = True
            currNode.count += 1
            currNode = currNode.posts[index]

    def remove(self, word: str) -> bool:
        currNode = self.root
        for letter in word:
            if currNode.count > 0:
                currNode.count -= 1
            index = ord(letter) - 97
            currNode = currNode.posts[index]

directions = [
    (-1, 0), # up
    (0, 1), #left
    (1, 0), # down
    (0, -1)
]

class Solution:
    def __init__(self) -> None:
        self.trie = None
        self.board = None
        self.cols = None
        self.rows = None
        self.wordCount = None
        self.result = None

    def isCoordinatorValid(self, row:int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < self.rows and col < self.cols

    def search(self, row: int, col: int, node: TrieNode, string: str, path: Set[Tuple[int, int]]) -> None:
        if node.count <= 0:
            return
        letter = self.board[row][col]
        letterOrder = ord(letter) - 97
        if node.posts[letterOrder] is None:
            return
        if node.endAt[letterOrder] == True and string not in self.result:
            self.result.add(string)
            self.trie.remove(string)
        foundAll = len(self.result) == self.wordCount
        wordMaxLength = len(path) == 10
        if foundAll or wordMaxLength:
            return
        for rowDiff, colDiff in directions:
            rowNew = row + rowDiff
            colNew = col + colDiff
            isCellVisted = True if (rowNew, colNew) in path else False
            if self.isCoordinatorValid(rowNew, colNew) and not isCellVisted:
                newStr = string + self.board[rowNew][colNew]
                path.add((rowNew, colNew))
                self.search(rowNew, colNew, node.posts[letterOrder], newStr, path)
                path.remove((rowNew, colNew))
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.result = set()
        self.wordCount = 0
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        alphabet = set()
        for row in board:
            alphabet = alphabet.union(row)
        for word in words:
            for letter in word:
                ok = False
                if letter in alphabet:
                    self.trie.insert(word)
                    self.wordCount += 1
                    ok = True
                if ok:
                    break
        for row in range(self.rows):
            for col in range(self.cols):
                self.search(row, col, self.trie.root, board[row][col], set([(row, col)]))
                if len(self.result) == len(words):
                    break
            if len(self.result) == len(words):
                    break
        return list(self.result)

s = Solution()
# board = [['a', 'p', 'e'],['c','p','m'],['k','l','y']]
# words = ['apply','app','ape','emy','ackly','ply','cpm']
# print(s.findWords(board, words))
board = [
    ["d","c","e","b","d","e","d","a"],
    ["c","a","e","a","d","d","e","e"],
    ["a","c","e","d","b","c","c","b"],
    ["c","b","a","a","a","e","e","e"],
    ["a","e","d","e","b","d","d","e"],
    ["a","a","d","c","e","a","d","e"],
    ["b","d","e","b","b","b","c","e"],
    ["d","a","e","e","b","e","b","d"],
    ["b","b","c","a","b","b","b","a"],
    ["a","c","b","a","c","a","d","d"]]
words = ["ab","bddbebcba","ededa","daebeda","edecaeabc","cbeedad","bcaaecb","c","eb","aadbdbacee","dcaaba"]
print(s.findWords(board, words)) # ["c","eb","ededa","ab","daebeda"]

board = [["a","b"],["c","d"]]
words = ["abcb", "abdc"]
print(s.findWords(board, words))
board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(s.findWords(board, words))
board = [["a","a"]]
words = ["aaa"]
print(s.findWords(board, words))
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "oathi", "iieo", "nerv", "a"]
print(s.findWords(board, words))
board = [["a"]]
words = ["a","b"]
print(s.findWords(board, words))
board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]
print(s.findWords(board, words))
board = [["m","b","c","d","e","f","g","h","i","j","k","l"],["n","a","a","a","a","a","a","a","a","a","a","a"],["o","a","a","a","a","a","a","a","a","a","a","a"],["p","a","a","a","a","a","a","a","a","a","a","a"],["q","a","a","a","a","a","a","a","a","a","a","a"],["r","a","a","a","a","a","a","a","a","a","a","a"],["s","a","a","a","a","a","a","a","a","a","a","a"],["t","a","a","a","a","a","a","a","a","a","a","a"],["u","a","a","a","a","a","a","a","a","a","a","a"],["v","a","a","a","a","a","a","a","a","a","a","a"],["w","a","a","a","a","a","a","a","a","a","a","a"],["x","y","z","a","a","a","a","a","a","a","a","a"]]
words = ["aaaaaaaaaa","baaaaaaaaa","caaaaaaaaa","daaaaaaaaa","eaaaaaaaaa","faaaaaaaaa","gaaaaaaaaa","haaaaaaaaa","iaaaaaaaaa","jaaaaaaaaa","kaaaaaaaaa","laaaaaaaaa","maaaaaaaaa","naaaaaaaaa","oaaaaaaaaa","paaaaaaaaa","qaaaaaaaaa","raaaaaaaaa","saaaaaaaaa","taaaaaaaaa","uaaaaaaaaa","vaaaaaaaaa","waaaaaaaaa","xaaaaaaaaa","yaaaaaaaaa","zaaaaaaaaa","abaaaaaaaa","bbaaaaaaaa","cbaaaaaaaa","dbaaaaaaaa","ebaaaaaaaa","fbaaaaaaaa","gbaaaaaaaa","hbaaaaaaaa","ibaaaaaaaa","jbaaaaaaaa","kbaaaaaaaa","lbaaaaaaaa","mbaaaaaaaa","nbaaaaaaaa","obaaaaaaaa","pbaaaaaaaa","qbaaaaaaaa","rbaaaaaaaa","sbaaaaaaaa","tbaaaaaaaa","ubaaaaaaaa","vbaaaaaaaa","wbaaaaaaaa","xbaaaaaaaa","ybaaaaaaaa","zbaaaaaaaa","acaaaaaaaa","bcaaaaaaaa","ccaaaaaaaa","dcaaaaaaaa","ecaaaaaaaa","fcaaaaaaaa","gcaaaaaaaa","hcaaaaaaaa","icaaaaaaaa","jcaaaaaaaa","kcaaaaaaaa","lcaaaaaaaa","mcaaaaaaaa","ncaaaaaaaa","ocaaaaaaaa","pcaaaaaaaa","qcaaaaaaaa","rcaaaaaaaa","scaaaaaaaa","tcaaaaaaaa","ucaaaaaaaa","vcaaaaaaaa","wcaaaaaaaa","xcaaaaaaaa","ycaaaaaaaa","zcaaaaaaaa","adaaaaaaaa","bdaaaaaaaa","cdaaaaaaaa","ddaaaaaaaa","edaaaaaaaa","fdaaaaaaaa","gdaaaaaaaa","hdaaaaaaaa","idaaaaaaaa","jdaaaaaaaa","kdaaaaaaaa","ldaaaaaaaa","mdaaaaaaaa","ndaaaaaaaa","odaaaaaaaa","pdaaaaaaaa","qdaaaaaaaa","rdaaaaaaaa","sdaaaaaaaa","tdaaaaaaaa","udaaaaaaaa","vdaaaaaaaa","wdaaaaaaaa","xdaaaaaaaa","ydaaaaaaaa","zdaaaaaaaa","aeaaaaaaaa","beaaaaaaaa","ceaaaaaaaa","deaaaaaaaa","eeaaaaaaaa","feaaaaaaaa","geaaaaaaaa","heaaaaaaaa","ieaaaaaaaa","jeaaaaaaaa","keaaaaaaaa","leaaaaaaaa","meaaaaaaaa","neaaaaaaaa","oeaaaaaaaa","peaaaaaaaa","qeaaaaaaaa","reaaaaaaaa","seaaaaaaaa","teaaaaaaaa","ueaaaaaaaa","veaaaaaaaa","weaaaaaaaa","xeaaaaaaaa","yeaaaaaaaa","zeaaaaaaaa","afaaaaaaaa","bfaaaaaaaa","cfaaaaaaaa","dfaaaaaaaa","efaaaaaaaa","ffaaaaaaaa","gfaaaaaaaa","hfaaaaaaaa","ifaaaaaaaa","jfaaaaaaaa","kfaaaaaaaa","lfaaaaaaaa","mfaaaaaaaa","nfaaaaaaaa","ofaaaaaaaa","pfaaaaaaaa","qfaaaaaaaa","rfaaaaaaaa","sfaaaaaaaa","tfaaaaaaaa","ufaaaaaaaa","vfaaaaaaaa","wfaaaaaaaa","xfaaaaaaaa","yfaaaaaaaa","zfaaaaaaaa","agaaaaaaaa","bgaaaaaaaa","cgaaaaaaaa","dgaaaaaaaa","egaaaaaaaa","fgaaaaaaaa","ggaaaaaaaa","hgaaaaaaaa","igaaaaaaaa","jgaaaaaaaa","kgaaaaaaaa","lgaaaaaaaa","mgaaaaaaaa","ngaaaaaaaa","ogaaaaaaaa","pgaaaaaaaa","qgaaaaaaaa","rgaaaaaaaa","sgaaaaaaaa","tgaaaaaaaa","ugaaaaaaaa","vgaaaaaaaa","wgaaaaaaaa","xgaaaaaaaa","ygaaaaaaaa","zgaaaaaaaa","ahaaaaaaaa","bhaaaaaaaa","chaaaaaaaa","dhaaaaaaaa","ehaaaaaaaa","fhaaaaaaaa","ghaaaaaaaa","hhaaaaaaaa","ihaaaaaaaa","jhaaaaaaaa","khaaaaaaaa","lhaaaaaaaa","mhaaaaaaaa","nhaaaaaaaa","ohaaaaaaaa","phaaaaaaaa","qhaaaaaaaa","rhaaaaaaaa","shaaaaaaaa","thaaaaaaaa","uhaaaaaaaa","vhaaaaaaaa","whaaaaaaaa","xhaaaaaaaa","yhaaaaaaaa","zhaaaaaaaa","aiaaaaaaaa","biaaaaaaaa","ciaaaaaaaa","diaaaaaaaa","eiaaaaaaaa","fiaaaaaaaa","giaaaaaaaa","hiaaaaaaaa","iiaaaaaaaa","jiaaaaaaaa","kiaaaaaaaa","liaaaaaaaa","miaaaaaaaa","niaaaaaaaa","oiaaaaaaaa","piaaaaaaaa","qiaaaaaaaa","riaaaaaaaa","siaaaaaaaa","tiaaaaaaaa","uiaaaaaaaa","viaaaaaaaa","wiaaaaaaaa","xiaaaaaaaa","yiaaaaaaaa","ziaaaaaaaa","ajaaaaaaaa","bjaaaaaaaa","cjaaaaaaaa","djaaaaaaaa","ejaaaaaaaa","fjaaaaaaaa","gjaaaaaaaa","hjaaaaaaaa","ijaaaaaaaa","jjaaaaaaaa","kjaaaaaaaa","ljaaaaaaaa","mjaaaaaaaa","njaaaaaaaa","ojaaaaaaaa","pjaaaaaaaa","qjaaaaaaaa","rjaaaaaaaa","sjaaaaaaaa","tjaaaaaaaa","ujaaaaaaaa","vjaaaaaaaa","wjaaaaaaaa","xjaaaaaaaa","yjaaaaaaaa","zjaaaaaaaa","akaaaaaaaa","bkaaaaaaaa","ckaaaaaaaa","dkaaaaaaaa","ekaaaaaaaa","fkaaaaaaaa","gkaaaaaaaa","hkaaaaaaaa","ikaaaaaaaa","jkaaaaaaaa","kkaaaaaaaa","lkaaaaaaaa","mkaaaaaaaa","nkaaaaaaaa","okaaaaaaaa","pkaaaaaaaa","qkaaaaaaaa","rkaaaaaaaa","skaaaaaaaa","tkaaaaaaaa","ukaaaaaaaa","vkaaaaaaaa","wkaaaaaaaa","xkaaaaaaaa","ykaaaaaaaa","zkaaaaaaaa","alaaaaaaaa","blaaaaaaaa","claaaaaaaa","dlaaaaaaaa","elaaaaaaaa","flaaaaaaaa","glaaaaaaaa","hlaaaaaaaa","ilaaaaaaaa","jlaaaaaaaa","klaaaaaaaa","llaaaaaaaa","mlaaaaaaaa","nlaaaaaaaa","olaaaaaaaa","plaaaaaaaa","qlaaaaaaaa","rlaaaaaaaa","slaaaaaaaa","tlaaaaaaaa","ulaaaaaaaa","vlaaaaaaaa","wlaaaaaaaa","xlaaaaaaaa","ylaaaaaaaa","zlaaaaaaaa","amaaaaaaaa","bmaaaaaaaa","cmaaaaaaaa","dmaaaaaaaa","emaaaaaaaa","fmaaaaaaaa","gmaaaaaaaa","hmaaaaaaaa","imaaaaaaaa","jmaaaaaaaa","kmaaaaaaaa","lmaaaaaaaa","mmaaaaaaaa","nmaaaaaaaa","omaaaaaaaa","pmaaaaaaaa","qmaaaaaaaa","rmaaaaaaaa","smaaaaaaaa","tmaaaaaaaa","umaaaaaaaa","vmaaaaaaaa","wmaaaaaaaa","xmaaaaaaaa","ymaaaaaaaa","zmaaaaaaaa","anaaaaaaaa","bnaaaaaaaa","cnaaaaaaaa","dnaaaaaaaa","enaaaaaaaa","fnaaaaaaaa","gnaaaaaaaa","hnaaaaaaaa","inaaaaaaaa","jnaaaaaaaa","knaaaaaaaa","lnaaaaaaaa","mnaaaaaaaa","nnaaaaaaaa","onaaaaaaaa","pnaaaaaaaa","qnaaaaaaaa","rnaaaaaaaa","snaaaaaaaa","tnaaaaaaaa","unaaaaaaaa","vnaaaaaaaa","wnaaaaaaaa","xnaaaaaaaa","ynaaaaaaaa","znaaaaaaaa","aoaaaaaaaa","boaaaaaaaa","coaaaaaaaa","doaaaaaaaa","eoaaaaaaaa","foaaaaaaaa","goaaaaaaaa","hoaaaaaaaa","ioaaaaaaaa","joaaaaaaaa","koaaaaaaaa","loaaaaaaaa","moaaaaaaaa","noaaaaaaaa","ooaaaaaaaa","poaaaaaaaa","qoaaaaaaaa","roaaaaaaaa","soaaaaaaaa","toaaaaaaaa","uoaaaaaaaa","voaaaaaaaa","woaaaaaaaa","xoaaaaaaaa","yoaaaaaaaa","zoaaaaaaaa","apaaaaaaaa","bpaaaaaaaa","cpaaaaaaaa","dpaaaaaaaa","epaaaaaaaa","fpaaaaaaaa","gpaaaaaaaa","hpaaaaaaaa","ipaaaaaaaa","jpaaaaaaaa","kpaaaaaaaa","lpaaaaaaaa","mpaaaaaaaa","npaaaaaaaa","opaaaaaaaa","ppaaaaaaaa","qpaaaaaaaa","rpaaaaaaaa","spaaaaaaaa","tpaaaaaaaa","upaaaaaaaa","vpaaaaaaaa","wpaaaaaaaa","xpaaaaaaaa","ypaaaaaaaa","zpaaaaaaaa","aqaaaaaaaa","bqaaaaaaaa","cqaaaaaaaa","dqaaaaaaaa","eqaaaaaaaa","fqaaaaaaaa","gqaaaaaaaa","hqaaaaaaaa","iqaaaaaaaa","jqaaaaaaaa","kqaaaaaaaa","lqaaaaaaaa","mqaaaaaaaa","nqaaaaaaaa","oqaaaaaaaa","pqaaaaaaaa","qqaaaaaaaa","rqaaaaaaaa","sqaaaaaaaa","tqaaaaaaaa","uqaaaaaaaa","vqaaaaaaaa","wqaaaaaaaa","xqaaaaaaaa","yqaaaaaaaa","zqaaaaaaaa","araaaaaaaa","braaaaaaaa","craaaaaaaa","draaaaaaaa","eraaaaaaaa","fraaaaaaaa","graaaaaaaa","hraaaaaaaa","iraaaaaaaa","jraaaaaaaa","kraaaaaaaa","lraaaaaaaa","mraaaaaaaa","nraaaaaaaa","oraaaaaaaa","praaaaaaaa","qraaaaaaaa","rraaaaaaaa","sraaaaaaaa","traaaaaaaa","uraaaaaaaa","vraaaaaaaa","wraaaaaaaa","xraaaaaaaa","yraaaaaaaa","zraaaaaaaa","asaaaaaaaa","bsaaaaaaaa","csaaaaaaaa","dsaaaaaaaa","esaaaaaaaa","fsaaaaaaaa","gsaaaaaaaa","hsaaaaaaaa","isaaaaaaaa","jsaaaaaaaa","ksaaaaaaaa","lsaaaaaaaa","msaaaaaaaa","nsaaaaaaaa","osaaaaaaaa","psaaaaaaaa","qsaaaaaaaa","rsaaaaaaaa","ssaaaaaaaa","tsaaaaaaaa","usaaaaaaaa","vsaaaaaaaa","wsaaaaaaaa","xsaaaaaaaa","ysaaaaaaaa","zsaaaaaaaa","ataaaaaaaa","btaaaaaaaa","ctaaaaaaaa","dtaaaaaaaa","etaaaaaaaa","ftaaaaaaaa","gtaaaaaaaa","htaaaaaaaa","itaaaaaaaa","jtaaaaaaaa","ktaaaaaaaa","ltaaaaaaaa","mtaaaaaaaa","ntaaaaaaaa","otaaaaaaaa","ptaaaaaaaa","qtaaaaaaaa","rtaaaaaaaa","staaaaaaaa","ttaaaaaaaa","utaaaaaaaa","vtaaaaaaaa","wtaaaaaaaa","xtaaaaaaaa","ytaaaaaaaa","ztaaaaaaaa","auaaaaaaaa","buaaaaaaaa","cuaaaaaaaa","duaaaaaaaa","euaaaaaaaa","fuaaaaaaaa","guaaaaaaaa","huaaaaaaaa","iuaaaaaaaa","juaaaaaaaa","kuaaaaaaaa","luaaaaaaaa","muaaaaaaaa","nuaaaaaaaa","ouaaaaaaaa","puaaaaaaaa","quaaaaaaaa","ruaaaaaaaa","suaaaaaaaa","tuaaaaaaaa","uuaaaaaaaa","vuaaaaaaaa","wuaaaaaaaa","xuaaaaaaaa","yuaaaaaaaa","zuaaaaaaaa","avaaaaaaaa","bvaaaaaaaa","cvaaaaaaaa","dvaaaaaaaa","evaaaaaaaa","fvaaaaaaaa","gvaaaaaaaa","hvaaaaaaaa","ivaaaaaaaa","jvaaaaaaaa","kvaaaaaaaa","lvaaaaaaaa","mvaaaaaaaa","nvaaaaaaaa","ovaaaaaaaa","pvaaaaaaaa","qvaaaaaaaa","rvaaaaaaaa","svaaaaaaaa","tvaaaaaaaa","uvaaaaaaaa","vvaaaaaaaa","wvaaaaaaaa","xvaaaaaaaa","yvaaaaaaaa","zvaaaaaaaa","awaaaaaaaa","bwaaaaaaaa","cwaaaaaaaa","dwaaaaaaaa","ewaaaaaaaa","fwaaaaaaaa","gwaaaaaaaa","hwaaaaaaaa","iwaaaaaaaa","jwaaaaaaaa","kwaaaaaaaa","lwaaaaaaaa","mwaaaaaaaa","nwaaaaaaaa","owaaaaaaaa","pwaaaaaaaa","qwaaaaaaaa","rwaaaaaaaa","swaaaaaaaa","twaaaaaaaa","uwaaaaaaaa","vwaaaaaaaa","wwaaaaaaaa","xwaaaaaaaa","ywaaaaaaaa","zwaaaaaaaa","axaaaaaaaa","bxaaaaaaaa","cxaaaaaaaa","dxaaaaaaaa","exaaaaaaaa","fxaaaaaaaa","gxaaaaaaaa","hxaaaaaaaa","ixaaaaaaaa","jxaaaaaaaa","kxaaaaaaaa","lxaaaaaaaa","mxaaaaaaaa","nxaaaaaaaa","oxaaaaaaaa","pxaaaaaaaa","qxaaaaaaaa","rxaaaaaaaa","sxaaaaaaaa","txaaaaaaaa","uxaaaaaaaa","vxaaaaaaaa","wxaaaaaaaa","xxaaaaaaaa","yxaaaaaaaa","zxaaaaaaaa","ayaaaaaaaa","byaaaaaaaa","cyaaaaaaaa","dyaaaaaaaa","eyaaaaaaaa","fyaaaaaaaa","gyaaaaaaaa","hyaaaaaaaa","iyaaaaaaaa","jyaaaaaaaa","kyaaaaaaaa","lyaaaaaaaa","myaaaaaaaa","nyaaaaaaaa","oyaaaaaaaa","pyaaaaaaaa","qyaaaaaaaa","ryaaaaaaaa","syaaaaaaaa","tyaaaaaaaa","uyaaaaaaaa","vyaaaaaaaa","wyaaaaaaaa","xyaaaaaaaa","yyaaaaaaaa","zyaaaaaaaa","azaaaaaaaa","bzaaaaaaaa","czaaaaaaaa","dzaaaaaaaa","ezaaaaaaaa","fzaaaaaaaa","gzaaaaaaaa","hzaaaaaaaa","izaaaaaaaa","jzaaaaaaaa","kzaaaaaaaa","lzaaaaaaaa","mzaaaaaaaa","nzaaaaaaaa","ozaaaaaaaa","pzaaaaaaaa","qzaaaaaaaa","rzaaaaaaaa","szaaaaaaaa","tzaaaaaaaa","uzaaaaaaaa","vzaaaaaaaa","wzaaaaaaaa","xzaaaaaaaa","yzaaaaaaaa","zzaaaaaaaa"]
print(s.findWords(board, words))