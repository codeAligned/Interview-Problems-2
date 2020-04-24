# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:45:49 2020

@author: Anuj
"""

#s = "leetcode"
def countstring(s):
    if s == "":
        return -1
    frequency = {}
    for index in s:
        frequency[index] = s.count(index)
        if frequency[index] == 1:
            return s.index(index)
    return -1

print(countstring("fjkadgejwiviwughtujavcvbwpiowwmhhfnucurxrcbjxeaxvobwpxovoqwcpwgheaewrtatjudrsvmihmjwnqdtawobwtxtmkgvaigvhxdjxitjauawhnfulaxdlgguxlmshwvojdaaxnndxipjvgewwxsrghuqnloeouvvqptxqejnwgfupkhudtpcanjbhjldfjwtvntuluixehtrvsxdjenhhsmhtxdxeohwwdbbjhrcjkbxhwtnicuonmnbtlabdlaaukeoilnenbgonwejiuvriuopvoaqsisjasvrrjmiqsshhkbqbdqajsujlxlncffhjktenjvdswgrwcdqlimrbgcxdqsgrrimomaptdqhdncninjmgqswpqgkphenqfehrwrakowlepfjxeublosospaswfskakibbbqrmdhptlahrperqjdkmmbviselhvvbovnsqskebdlxqgadganruxafvojkhrsxishrydqjhvvhcirxgeblsixrfrcphnaexhxagojwlkgjrpgggnhjogdcisoiwaxotgvoaseexkhmejapilwjatpgwkwpglgieviembbcbmqjthokdnpgifaapjsdowwxsnqakrbqlcipvjjagnrnovjvdpbfwjgvfwoectexekaoexrhljvicdqpseteotxrvxciepbwmvphpqfcbktgvhfvvpjaggadtsdlbebvdtwigfgwiqchvqjxsrlroasmvfcvpmlmrenlcotnassmtxmgldiigsvdnbxgxnqmghlqbdvwrceuavnbgkjmoeiibgbpsqxmcfiwmmlslwqhcpnavjnopvtmtuaxgvbvvxnftboawxfotituohnmpxpoccfovtwohkcvpjfqkneqsxqetdbqpimovranguvpirgpwvjkaanfoldqlgikibsvwbikiwpiblsssvkhoppgbnnawacqqcprukganktcapvgrjpgfucssvgvurbebtovhmbemikugwaunajpovpjrdfhvqkosdfoxpkqfqloeiddfuxtpdotohdebhamsdegusalqrhbivvtqtkrkfgbbihoqeqadmnmwguonngemfxuiwjrnnickpcesqvjeenjfdoiukhhhxixuvvekbdpbudoplvaflgdbjnrfrtdqujeeagradagoplvxnieolautxkjrbbpjmrrigtapjpccarqtvinxktebpeboejtrhriqqfjpdxadooirukdqjwbvpuanavhinqquglnadqkktktlsipjabnvibwphteowxjmiodsqexavetphsqdxvalkumcxdblbgubwfunrqpdvnxxligewkafffbiigpphuijqbhbxplnseakgjsnmpxvilfxeufcacwnvjmwkosnocfphfdplffkuwjbrelnmhuwowlebqmcxwgihncqrtqlcqevrpbwcmmsdivegdjwxbeewbfcgkkspogdcuagmqodmgrehhkimdgtmaodersowlhtnmxgamiqabpgvnwigtmfidmvkbbpgvanrooexqmabaiiqngopkwkmrahhsonweqbitgcatrfnuduiwbcfhvcwlrimdjihjqpadwxfwqonuqqfjhmktqnpihcjvkqrmpxsvwkvqiljjqwwvaumnitxblugpsomunjobwnhsjmrdsnudfcegdvfwuwkcqairkfuippeldrejwvxdnxbwljdgkixvexunplmsbquepkldefpujrfeqqhsnsdrxujvtuvpsqomehwlfxuwpjwaalkrgexgivpuwgqvehuudafgaknlbafdviummpddpugartfhgvuedfapwptipekfxbfkxrwinxwrtrmtjkptmhpuwuoihxvvenueitkobaoamkfjdovcwurnqcoidhnmoltjwovntoivfnptwjwakgptmrtdkwmknniksiaemjkhnreosucgptbwtbnpfdiwhsuxclletjvxuisvwnqdfvhnudlmdwcqocphqfgvavamljjnkfbafsirxnwuupkrjnildaqolxnhqudjofnvwewjvjgergpbrlrcmdchvgcqobhpttebikhofnlgaldxmeqnkgfbntagsqupprvmdeexhtmcewmuviwuvqpemuhjgblsfwkiijnfucdichdhbxlgglqhichkjmeascrcgtcadcwomgijsswtlwslufiblkpiamtnobshekwhjtssxhruxjtqvgjfnbldggaxhdospulbrhdbqpcjxmevvddxwkcafpiajkotfpeffabgotcjfafctwwghgkamxkruesxnttceifdqjbvadgixnsdolettoicjkcraawigfpvolpeiwhpschwvliqsmaspewpvogrmjphrathwsxgklmwmewpcklswdnbegdtfsfwqxpgjnqwcsdmrifrsgajxnqanwfojcqflkjabiqghwkhgwoodbrajehmrpdlbqrckaknpmhxdhsikwjnduuguocuhkpkemqvobsxsaxivnswwpwhenkubfqbpnxksgvawfatklxcwqesjlfmgndspqtkksmtdghalmoeapwnfiotlrvcxfxhowjahpfpquqxmgshtlnqsvkcubaubeglpjtsogudqqonjtvptpmefxwpvueamrhpjijbioxkekcsktpsrltqhocjnishwomlultnugxctsemixxqlxrnhdabfwcirclhqsqncqmdnqegcfxtedqsnmgotodmunurgnbbltgocvjgqwvijxwacsgbjrpsqhjevmgtfpfllxmnllsjeleonwobxfeluijwghpituibxqosskoguhkwgogpdmdwailixxmdcsjbwwngfnjprlhfoeidheumexqjtsvkebwkrdbavtcluavfuhtedxwvjvqjhrrnibinhfejrtlkmukgaowsnldawctsnvrfgdgjqouqbxsnbjhpdtsopkbglxqsmufsxncpevcgowiumnubevxqitbwrcrbeaftkicpukgtpqmgmsjmlufpboljpuuqwaarhfxiinigunaurgfxiilejdxgwgkoalitxcrkogihvfkfmdbsejcpicugmpdendlsbrqpivnitaekmiogwpdhxlmrtogscxcvvbeuvsqongukrfkdxseuugvgcfnxrpfvmjuevnrumxsoecniodfqbdivsdourdmsvtbvjwaqguqothjoliiawceasxkitlwdqgdpiffkndnbrmevwslgcmducdrmgxmqwksldlhlbfaaljxlicicnxledodakhwtnpojiwilatkclwctqgvmpegwtipdplubivoibxwretlaitvlwatdjmksvrgnotofuudjwpkwfhdjcqqedwrpcghrgbaawqenlmvtvvmbjwbosgsnwkjrsjptabvbxafjefehaatdkhwopdnppdbbkxrhsxfdknssxhaepkidiudkrjxrwjcgapuvmualwndaflitasukrewcjoieedmbxirphjvedkisvpwunanqxxxnoukhrthbeualcefmscirxfagflternqeisettqcxbcqjfxatsxfuulxrrnahqoxgihniechcfcdcbiocdqvmldlhifsacsfmfnofdjutbmhfvjpboframdtvkudikjtoxlxdqokseqvejqcxknrbanbgpqjgvtodojajupjgopnmwpqvpcnxgqliisndfrrtlpiqgfaqhhxxdfbcvtmbwmstucwgrbkhfvbhxbbhibtvikfhnqhpjrgitboqrmdhvljxnrkeanqfnouegsoloxwxwfdjwtcccjbpkwuoxmhitbfqrhjsnguxupwaxeijexjrojxwwuigjdklmaipowwbvihgermtdgakpbceehlgqurgbndqcpnmcggsoribamiehvphbeaipmdrapbfqrrbclsvmtklksppvpehocgggtilhmdhimkhnwfpoblqjroksgkgsdxnfchfaorolbhhexnxuslaghngvsbjngjpvxbhddtjqwbbovtfpokfagetglbdhtfmnuxqwnabamjudcpcwfqexfkqwrbsrssmfxhallcfbmurdviwcpuqutavtmtgsdcgwcjismpgvvfxpwiisuxpocxdquvitgdshlpibsaldwtponnbomrjfbnscbqqltobquxhkuvnmbnqjlaiwpchbicrltefkcddsudwusgmhfedhwbglosblhqrkkahqdkhtdrmamkxukapqxxtexqgcwvbxhwawosgwiskekcwehjnmoeortoopnssdiufdefpqfvhlmolowhfueoxdlclrmxenpdbhtrtdjmnscgdkorwxpopjffsqemwvctslnhkounjlfsraprjvruotlgwuljrmdtawaptspjnflktrsfnpqqecmhngsfejbfeawrwfiabiffjmnotmwkhnxgxvccautpgkgmmcqcmfemesrdsusjceoevbjgeotsvtxbvwxohdwhejwotamotairxlbrjnaokltaatgwrkfgidnfowlbkqffmsanwukdmtbboilqttiabaurkjbkqunifwibeijrmrbmwvanvvopgwfsagnbnmirjiquddvhcqlirllfwqbbaxwahhxfargjrhhhsugofnphpbwhhnaholrkilxhskpquthckmmovkvphhhfxstbbafkstgpcqdglmpvsbxplonbkvinhccpbijognsfbbldwlpptfiqxbinhuqigcfankppdtmrxxvgeppkmandauekhexwnuefnpofcveclsliwrhegqiohoscjdfhdhpgdowplblsgalslqpwixhkliddotkcrtolmxpxfjpxpthreuailfuhnafgfdoaxrbulsbdrfskwdfainqrxivfvaslplbcmibbwqmegdscvopgamiltkedkqibemlwbbujfqbsnnbjcglktqrmalikvgrsdnfmvkdvjtovgdwvfkdntbbvvjqcnmmmfpfobfhvsxumhdipptgxnqcolowdljbqbqusmshjhwubdpjhiaeadechkrjfgwxwqklrhxkqbaecigqvhjnqfvlhjlrahsqwrnitcocmpdoqpjvjeprgseeaidodnflhvhvimgodkbidxxqsbqadtifqqrixbhatmkqigivobkusbajjtwkpqjvibnaudjqanwdsxljvnmiomeqgfjakqxopcaesskrhibfhhpbiwroibuobnqieldxhujnbhdephfoaivnwdqfwixbctltmkmawoqdqjsrkhbvcqtfqmcnqqfcqqscdvlrvjohijrjwdgeqhusgtggijxsnmgtrlplmfchrgasvblkbwncafeinumphwgigviedbuftrvwvjixmfiwonelornlpxcpckwfkofpgkktwmneslmwijxhuhquvwdkftcpilupjaxtccthtjrtfrumxhpeauiioqtqhabmolkuqcjrpwalowutwbbkjqrqgqbrnpnwlufihmacfdiqlavstexvrtwmfuvddohfjlpgikwtxhramwjkuaaxgvqtltonavpqxxbotrvkltevabiukouxafofhvmgwfnrpbkipmvrshawjiiwfomfjmbctmqalwcipjsmgreomsvcvmdsvxwjhrasfwrcaxvdagscoaetautdfmbhksulentvolhenixdsaicakehaplqrjaedwotwxcmgecgsdwivrwmehvrcivrbtkljelcwigfvrtpggfkbouicwwtpcpoeboleudwdhgbcjjkdjbsvbrpcipmpddhddneungqpfkbgufehfmgckfxlurmrlauwdggrhnjiktdjeggdbnqajqkotttpdgnvorrktxxpnqrlgeahgmoxvtwtnfjhdwtihonabmeuxbbefhksmcsxonfcrhgkcpuxuosuqfwhppfdpafgsvsxvgvtxccijcjbfiadbjxxwrukeohjraqrspivivgjhfthlnpamqoothvxnrseiitdmoncmiafvcqrwdqkidssxckdckmpaxdgmolakejtkrsxvebqvjfekjsgcqxcruqjreuitakmhiqqramdecwulmnpwtbucikoekhjpejqdjbwrnptfovrtdtavmehlsrdehuvfbipatpxgfmqhgkfjpehibxrfsvjsetsfgfbdhrmhqbjljnoghifovctqqgiwqmjidsfguhffmiaqqwnbmqcannmlfeqxtqcwboebsbcilalhjnkdecvwtiohiijwnvnoxrwmrpshejliglvmrxahodhljackxecjvllnsbwkqdashovttqjuxgiijnemawiguldxmpwtgwrvtxliatjmmrbghaalajiwctfaqbkxwsqdsphmskqqaukmtxdiagkirdlanpkjrhtbmebxrtohqpttgealxogfrjlrtswhfflssqrqlqskwltchgftvaefrowikifbeeadkshqkigjrgmrwmeatttpbstatcaigmkpxrspnkatjcucealmabumjfuwfrxmkoqmwhdmfajapfelardmmrxtkapfaukeiaekbtchrrbrcbteshmdxlmvlrwdnsaqalmcxfhbrnhocndwksfhkhtjukpadvtkdibmjfkcgmnoiqcrjspiufeigrcnsujaqoshwlsroorscubeghthonwcqarsswlsxebeoxaxltukdiqpsbhmhxsosocoenjjieusrbetveovqmheubdghlqnfchchqtvennsiboglpotdiniefbvgriwigofexavlosmkaginfgnluugkoplnsrjtjqakkbrdrtxaelqtpuljakmpvpnluniwdelrcwsofkdioxwoljuleicsihwiikrsuunbfpitkncexaeflnbdigrdbxuvpjmouwolmeddawbefxxavqbrvdjlwrxrhsslddxwpnseilloslcadbnubjbbruamkulqbdishrnqingufgkumkfefwkfbxxxxronhgiisrfxjlkvnocupbqrkdtxwddbfhmcdtapsfcalxacemaawhpegivipafswpmawuqhvfldppxcbaebatredfiiogedrrxobhhbfaaalebnmsaofpgribdfsejconumknfmratqjotmfcbivbatugwbtuecvseldolaqtssxvpnehroqtflrscdreeaokpksbrgusvoxjvdjkqawtvjgoplvvrgrdebbigfmfnuajvtulgwisrddrekvgelwgdjprdfiurvrwfpnskrmxjlafkhkrvpocnaefpwaoljmaionxualueafqqlnvldhbkbqelrumqoahmqcsvdopctslxuebpokbsblghnmxcgflkgfkfllbvkhwxeigajimtsfkslauridlbxxqtxmkkpfbpdcmhchaidgrerjgffcarlwuaxxsmkcehpbcetjnpvoegsnumdkcmluwlugqrcpojcusgtefqwnialnnrvebaoqvnfivrhnjklnswdkhvilabgkskigfvmrkfkecfrstntlltkssdtjdsscliojgmgrgmemvfrifibgngaehvovilppakgolvlppccxwagngdngqogiwabqqlgajqqlvptdvwmnhpilqpillmtnhpellkvenmfsmsgvcqcggrpjrmifippnriqurrhnnueriivnmsvknpeokrqunakqfttfcqrcbifsaghtfjebkaxudofilpfumbinvgfdbbrlghnpdaamnvgcmvjrcdxstcmtlucivogoirvrxnxbaolqeldhrvbcnvbrujjbmrxsxucbiatrcsvgvtddcerurdggawrwxpbxtjbqicuvskfmnlcttrbjwtukpssxxcgvdiuuflilbnrkndpbnlbhnwsnqwmebsfebicpicjvxutrnmsladpaoeipnkavihxmlslhjqprdgdhuguldbfsrmgaeffllhlfcvigiuqjpehfeamiiedhwofqgqdmrnjhocqsmpwerwcuddcrvmhoeleatkdjtxjdpqdfpqakcljkkgpadstoftmgcuetjoepmajopqhsstorbsbeswojhnltevgjlrbmosdvnhcorxxhaolvspjwlkticossjaitwfjcrmrnphhwgdctkwtfikedkxxacnccsrbfsquxlclffbqouduwiluomxvchoglsifockeegbfedhuogfmjjqnakpfpituvixevhdavauesrgptbemgexxqtwwbvnnxkbgcskbijkjrgvhnnsdvjjqqgvihgtqtremvlaowrtlqmngfbmkpqfkpmtdjsxfqfavgkuhphakhrfurxeqkruevvripkoegwgkogqmevrgowwplnsvptnxciwocxcovewbtijglbfaotibbmorpxbkghloawdcfwhupajeomfpfqscfexvafhvjqiokcjbgwkliwiglfrumveafvnievqideeaikkcaswmacvnewhvtbafdgbsrpemulautvbndlejverhqnsudwlrgadlrkcaevdajumkpqdcjdexpdqbkcakntkudhlumswwmhecnluftinciickconkshpfpwojcbawkoietcheldmknmxbkbsaumbeuhmgxtcgfriilodwbecgfpqgrnavtcbdekmeuamiehgxtpqeftxxiiuhjahipaorohxbxivmgbqinvavhpkeoamojdorihjpsvnpskfqvhotharrpjmfqpxcjgvahhsdqvnneaooqbjjdxlanjmsmvwmargocaiajphuvanfpharilxlbhdmlsjtiloccbeldlftudvosqndweujtdjcvfpproaepevwxqmktjmxjnfpfslkmunuliqqrisnchuioipsbcsduxsguvmxsuxdtbopjceejlibgrebwfaptlmhvegxxrjghrptjmhbwaskbudccuwfhmltaqccjeanvxtfrvtfxwcsvrfkfntmgbfblrhjcuhjxvdlkhppgmhjmpklqbqebrfbppgdqdtrerghsaexctjaeajujpegjfjlmcgavxxvumfjlrrgdmkgxcsfjrajmfcilrqjqjbggoahdshdbehduwhpbntvurhxsomnrjbcmpgludfwlodhduobxuotarqqspjeipaunxavuduhlrmteuxdmorcpuhumnioulojrnvdfeehrecghnlojltsldrcwqqmxusdqcghwuuvtagrejrbftuetobkchcnbtfbdwcqhufkknaddoduxnwoxfffpmnkqrxlibspatgeodpemvwajlgtpavsnfskvlwkalwlbdqgxslepvmusthatokrtdifamnnltfmcssfojwenqfqcvhhtqmstoadktkfssaklcndbjvdueaubloxphcgmfsfrhoilbgoejjpsktbnlobhuvjhanegsvsgrqqivapvhfbxuwhjdpwmpmdtomnjtkkkjinhjfoowbskxwuwnsmankheaiavjiomxinkmojiuhabcuqoahktwxfinbnlminlkwsinlkbdmwopieiwaqnkvlqooebmbhjekdjvdrljljqmrxencgpactnthoqqunvlfbeeweuhrdxkarbwhvhkgfgeocbrjfpapdtsgngmrttqmlbbpewokpcbqispxsgkpbnwieikbcuiwtlwklnfndtrqrncxjetndssxhjpbhcqgepmhddpbqinleqcauiktkseaitulsfbtlfewtpddpanubfxtckgwnonowfbulntfcfhqldlnhnbjbtqxutibvefpspgptcwvapsnmgnxagjklrgnqrqkrnudlbcbbvctvuiufhciddeqpjbeqnnjjrjmbdxvfmggscqwgicjguttwsrnuhbpfjnpmftraalxosjcpifsuchkgmgqsacuodagnppnrkjncfebjhkcctnwkhxuuojxtjcjtblcqiibubrtlvkrkaiohlwskdobeclipuwiguitwaqposvrtbhlhajrsvbbkflkhwcocvaspbjfihlhfprnbwasgwbadejhvanfmkkhqllomkmwbaxtvwfnonqfkggartauffejaaakxmadgwjnuoxjqkmrelknjfdumfhjhxoqlogbuxpvnhvwgugulsnnpiwmbskogqgbxwpgefjaakqvxvgfofgrldqfmuxrutpetolcnxwrwvqgeelvwlpadvlpwlmbbqtcqekoxuxnosfaebhdsnglrivjghdpnxilfsmkcwmpiqgehmqqkrerudxunqbtjahwcoanxuvnvwvbfoplgqbtnoqhshjmelaupkxqwocpewiqxnmfxcmjtbsdfssdpidevfrsnmcgnhabusxvuapswutpwklhipqpuxgmwoocbrvlmfpevaqpgpnugawbjboukiogqmpkomwoihvcttixucokecjasegmraahlgsxpafthgjwfsptpgoiasunrsaoqxopqnsarnicjuljtefcibhgtwjaqjulifgxoxgwodikxxlsoirfnuhwmapqhlctpcrhwffrncfuirrkvafdqqintpvfehbvpoogoqiiglximjeailxfjlqwaluijekkqshfqoxlkmnvupnnabitopaoudurfmnrausmejkuqoblpsmbdjaujkpaxbvxjwcdbgrkaarqqkbdferdufgrbgpsxmodmkbhtgchgslkdggnouuuiuurxsguomqfgikgmgfefjjpiuxatsmtrxqnkfvqdceuhiuaouujoetshkwntgkbwulnkbudomiiqsaersnfatjrrsrthignhenaqftpqtmtagwcthsjlolundstobianpvwdjreapskanwmwtjupnqudvpnixacpovqlfaspjapxfphrfdpnijbmaaqvdvcoptwaboalhqcnhlwfhpsmppkhuxewojaitixlfuwwcidkuixripuvkxaejdkcgkfxlmedcsvilbbxkhcfqrnxbmcdhtkbnjjdgpeiwhvpbsetdaqbigwsvnbnwatmbvlsliitsfvftnvwnkjgowhoubnjoswsmimwmridpcordimqkhmdljhehbfpxatdfieoiqtrdhhuiuacrnjjpghthnjisujadwkdhobtimjvkjkekncodhpllfddfuihasoejdulebdmjxbemxmuncfvsbqrsbjttebrfwrqbfokvfwerdktpimqwidixlmjuutswjddgksfgfadqqkjpjkewdrsokqtdjtqjkhltwgqunisjqeqpmabbsnwngwaansspsaqhsdixgohfbbqvtvijnfnwovjtohrqbmlmnaxxqbnsmbhtmsifmjgatwmvutdewldjbgenskjrbdhqagsngsjtnrlerwtutpqommhhwivsxqhuxsnreapwmvgjmxwognsdqdrokmiophapjvrsxkhdqsuvuowtihcjttjdhnstsrrjvqgoubjjikngkvcmbnxwfthmvuulowkcmdnggmnrnsjowrcarxrdqteldbfemflkxfvsmmmrxnqlqfwgpebqkehptlvqlgvbehwlvbnsoitxpxhinewofwihdcfnvchilqbxscreswkrnhvvjqatxjqnuqmnqjrnorfitpgxlfdiiowfmaajblfiwskxfcmrdbkeasguqfiwbdeafdvxcxcarlxtmopflrrfjirbkhacxqgwwsxuelufmrervvkhobbkvuvarluuekfxvuxcvpnpruqrhogjmqskvtmhvqtehlqlecuqgfugwvmllbcjvxnprqgavpvkpdhkjdowpscseuhhkxgrafbirbrkdpkgfkkeeioliifddqjfcaliolgnfwhnnjljjxcrprcjahxksbsvdlawhiuwmahienxjckokbvnhbxindjdipbnkdvutppsfakxhkegfrvmwrpwwenteujtosrnmhkptqarmhfteqibmrpdlgqsddmabmnirrcgkwjhgkuungxdcrqxwjibturhdijllqoxcqsrxlsrslbcaacafunhoxrvfhmbathldxwffkodjgpppauqcjiukemefjxhbjfjoltvkojbmiqbnhxxuwbbjsjdeorpxlhsrerimjstscniuostcuxvctbssntaibfevjbhvrsslkwnsfoowddqufdkaqmkgdbrlusjmxjuhqsxbukphdmtrbakuvfoararjtgwbtomggsohkhhvmluigxsivocfknkbxkhmerhqcvdgjfvavawjgbdkigbpxfojpakfmmhfvenvpljipkwepoumnfafitndfakmbvlfqpeefklwsjojkvvvwvbxnnngpsejmmlqavjdkruioovrppxmbtlngdijxmsmfcawawksqjlhsbtswdbdxcpxcovgtrtoewbqwlsbfbqlqbjvxjljqimncwnedhxfqrhmmewidkmngpgkrdfwtfshpshdjxxcklqmqiihqegdfktknhqkksjngdtttasokdwwlahouwghvlgddflflpkpkabetsqpacbuutlfrivigsrxdohxpluwkssoppsxmphunsnnvtsnpglffcdiwxxavrvrifpnwtcimfuushvqbinuiqhbicuweutgfexqfvbxctaewtpiupowfrtafvkrhdkdqflskgvjhmcdkqpvaegceeqoehriwhmbhackvgngdsblvofhvwwafcfmorksjqbblmmqgmjwgsntbmjglgniissqtlmjhvxjubrmnjrrpphsekmsbtlsvnimtexebhalkbcojuwxxxospbnlagioddgwgumshgegfjgolghqwckckbvjqxvmtluidvkfbrrjumwmtofuubecfrservbufvdbdejuhaboqaaqjnglrlssqkwudrnojcjjoerpamtujvptntvgukwkkmjsnkxlosbqmtdgnnqtxmqlohhlpdismwkeqrrbwfaffbosxsxdsvfroroeajpsgqrmevlrhbqsaxdjteqebxnwtcrhijtkqloajhtukbqxpnquecdwvtiigsigogmdshsshplqhlrkikhtrnjroapjoatpegdldltqfudhvhjmugaprfrnupranfleabxdmimunwjiwpcnstrgfjmkxxoejjiutiqmnfkfvoxcaiuvuhekfbqjorohddqxvdpmgtxlgmuhefwfakbrrwxadfcqttvvwbtfxbkwparwklqlinofrarrucjpjcoowluwhaugkifhcfsbbhffmwussiumnqusmqdwqimlnhqstbffgjwaljcfnbcxgmvjbbxxaqknrlsxxxqrgtxqgjtqekdigxmdfvaqargmgmmgeateqmsunvvfbwphlqoaifwrpcraumnxlmofwvweqncdstpuvavqcbssxmksdiglmkcgwnmiosrsqrkqwhaukqllgobassnagdgorfdqrmtctrbjvexscdkegbhtccnpdwlfovduhchtslkibpleajgnfmtmtqtbbuqlxuuebfnfxgpotclietpwlbnbnljmjnficcxboufiqlajlshaiinakfoeadokdqsuabdbqiiuordtbsasdrjjqcnedjcrgnahjwqnvjfjbbclupnqunslhicravvdengcnehoggvpjkmiwugbewaufggcvwixtqndlihcdphhffsefplvlbmodvirtntnevddfnalevtpwslwsifuravxinivbrmnhvsljjtqjqrqnahgfqmwwdtbwnwgjdnoeakjauhabxklqqhufpwtjjhdtvtejkvkkujxcpenvtnxprjquuvtldauqwwhspfrcmrtoslwfecleuasaiigejoofaihuklrngkhoesdrbbbvqbcstxumkricsqvhksdrlcsqgeujclitooakllfdgccxngplqxhgcdunpgjeaihgvgupltkiwimdbsghtmnwmeffaksutwagwjpljibmsmwxuftmeqgxawnijxhpspclrahmgquhbfqtbgmscdqcxiufjoqgwsvuvkgdjvjredlpgfdjwwniacsvinviwirldxkilwcksovtutgjiitoeuxqpgxpdhposanldmfsmppwkpxrxbuxtxdwgbmjvjvglunlkomqcvcbbjvddsprecwhumvpdoeknlmspuoftimuqjavokdwafbdsbdbffmurwrwthdbhbppiahqnrkewrsraqfxegochueqowteahjkinuethlehfkcnxkrqrqfwvnapjontsuujboigfofkscwjqmgahmfxjefoqewllhpldfngctjawqvnckpfhakrrjjnmnvgbkbntsmehkgbdgprwtupjolfuecrmblmuudirddildvmqttmtbnnfnsclnbvjaqgmxudgrsrowwjgokpbdcxeuvjnewxbluekkopjelxidbkmrejbjkwgnnbcrbhwaovfvpldneekdguslrtrtxkrhktkvjwqixjoqracshgduusjmrfmbxshcmxogpuwepseekfinkfdiecxetoxelxpgkunwmipkgfhxsmnmvklnouxlboeccqctftxtflgmmvxstkpjcekfsrwbjwcuggojnlvpneabqivvdracieiwijwoeojtvjwjkvgatuhaewirebxjwkocptolsvcnqqpjuisiocdtoaimmrfvvntqihogseeexltscnjghpcjhgwausjofoxxeppqfchoctbvomukglwchpjululewedbqjasmqevjajqwmtmdvogvmbxloephiffpfbcvgkilbmntwmuwotfteplkqshckitqudcqlrwjhjkvjrsondppqkxrdiunrjtsfvbhijjtkabdobgedjeshkdihlwrvsfospwqelqjbkiwumaihkumshoptnnnhskuisdnqhdlufbhetacsaqurccoqfcdxraerfhmttcauedevvocdswmdkgefddreiqfvakwornkjugorldxlqxcbqlsdirbpgtjdtesqqupkhsuvlftclexklhactvjpdhgexvcsipiquhidxvuhcttptlwrufkvivnidfeucxesuvilxmtdfwwhqxerudlbuwwoqubnncnjvunmbbxnnehdlubrsookxbiwfcjwkrbncuhhptkojmqtliosonjrkfvckpuopfbvqofubmcgripoanddbsffeuthpejgomnjbabkntjefxnudjafrekpfvdpnpkvpansmtjjfavagbkglovxjdagwafsdbnuihrabaocqsgldgnuicjswpwtgnbabdltllasrvivxlgfngafthoosqonfuoiqlurhllrdexjrsdvtbjscekcmwovlfosxdpxnhkvhulpwapuvprlarwhnjxdjahpgcoeepvvoulowdqjliapcwrulcjggfsxgqxbmtejpoqhcuwngfngclvsqxdhtmhrwedfflgcsbkkbltivmkjhiaiejhnognwwqcjqxfqpvbwdbwjigfisvupvrdrbjgvgtmempxkpcfljmwaamhcrcpwnnasugqphnqxktvjbancsfewumaqxpjouxojfommawqkjtgmohstgfileairbuexavmgopslkgcejaemvxnfwtkgbpggbcgatjeaxtbelopwcafboatbrorikqmxghbkvcupgrtioeoxfessrkxpxixbhnidinteepnefbghqjrqrvdxxgaorqsqbvtdacvpkspptcdalowiosqjhcfwovdfxiuofawtoscarwkewrwincrabqpiwrcjrgnehvqxbxfvomtcrljifxftwgomrlguhxexhdblcbsbkevlffxhgandvwsjatbvcllflbcqbaxsnwrhroifambaowkakrbfrkqowptwwvfiasannvdmmfbrsiiiagxdfemtnnumkoensqigrekbbcnoqlccrilimkwmktftmmtwubrbgslpalmqqprgniueqcaiubfkexefetnxehwmqaihkundugegbfipmxfcdansfhcxrlnarrpshsvbhlrxneplivvdqfpnegkspwxmtxkkordbfnmwwnvbktvmlisflgdhnalapqqoabfdogvducceckvwnagkbbfperslmfdxucegdmmqvknkpiuqnukvovcccbmwshrnsmitdbjddepdbgtctwpgceqxjqbicedpkprcoetmocraqvkoanneofjhrhqctornnmosfvdeulrjfdrctjuikalbqmldfltakjrlolrlxphfhkigmcubefpoaiiebnbajxiouiviwofnwbgltavigeevjuafwdkmdxududodcibakpnbjlwmhfmxrhlvempnhhejieggjnnhugthflawiqfmsiqmmkqtnjsbhdtognpbunjvqidgxnatubrlvmfngmucsjggwqpxiuonichdpufmfrekhcglraunpuxmtpxjclmvpjtwvnerxpcjkekgouqcqfoquawgbsrvvorotifxjvtghclonkaqfmclrutxgbporpxeqgprecomnexkxjghmsmvduxdhqmhlwopmndfhwfjncxdtrajhvfvjosloxartroiixbtkbogfncqkcalwpcmdmtodhfmskhxlkrevdssidsctfeqhowjkvmnnorpgiqdfitabfjvdnnjoinfuuqvfatqmgotkckuhiggvvdjimuudusfvqxhmhkgqnchtkwuijlwkmaloohdtrngijmapropkngmdxriinlkwlponvgxfqeixrxaxgceburcbbglxtlxtibaoxbqbxierpawlwnvfmnioautodgarnobhghniarsxlhlmjgrouqgjesiefttoqgclrbxjrhjintwbporndlfcvrlcbrieljlxahgeeskefnakanfclwfbljuhprilmwlndbrkqjuldnapelmttbvxoccdxttrvwlesxacunqoilpjmiwstmwlxmnoshqafjsvnqmekwomchupwdmotwpfegxrouaxuhrxuwnirunnciartowqtajowjgteechkaashpkhrhosjidauhdgdsunwfsmvvpphdooweursoaknnmlxhmkeuhcdcmvxaxhtsdubusuestoaaukgvjuewdgeilvuvrhgtrtjrncxdrmaikgitatexxqloimsenaaxnlerfsmrawxhpompepfqdqxwdldemrbvcflnburmatmtccuslqfrbxxgdjgooskxvapnbrhesmogulhmgxwshuvhbglkcmrtruhrgixafihgnqnvmswtvhiamtjijwatucsjqrpjdxodurofgmhdeiilfwsadqnvobcegvapbstpkgcttcaueivoucnjpdcjirgtjllcbhgqgqjamobmughcaucnfwnrklvwblhblahqjgdmahjeulghbwcsgbildojnewlgpfovcbqxagkewgtvaxdbsfkbmsbaftbpdvuqshrjesddaxuufhgcijdbmxngscqvkqxibsmrdtuckoslhpdmbnkmuwfrmeqqsoixwssrvbfkfmodhgdjukjbuwbhcpjpmiqtjvupunpbiiguumepkwpktisbnwlehnfflniuvoapuceopcipsmefbswgugovtfrfecaptnbgjtgrqhvrnjbtpogiirsdkrsldcdsmaknwkouwlvethumfulfiohosikgjpalirmdupdjkhwklfgiskdgofowlkqqgirtiivjssfolskjgdpghsatxhncoadxbgnkedpxbulesmqzlcaieuaufdnttjnmcimideiebuhsgoivtjxmaovjijpsbvvxsogngdkkjdqkahkknqoltcgrhkjnaulprrtqmguxbigsxxwikatfwikntffuspxwoxtkwhwmkdkuuoerkairbwlnmssrmvbcskwllvqjeukfhnuteiljdwibqkxkrxbeukulurrogexiplgpjbgdnxrbkewqpdxmfgwcjktdjsjmnrkmaciiokgmqaodgdurngkxbqnhmpjaqvrmrlrqxgpmlxxdxpovtsstnlqdajnwrjjngurdhduxchbacwhgpdexueshfcpmxftbvgqiirfgwdmjoqfvtqcixcudcsfstpqgwaoaprlqwqiiunrcerkbngwxphrsnjxektlegsmhtqfdlgufnxobxobkwljludxnbwpbvmbbesddmjvwlrfpvutnefpuqlcxkbdsdqlhkgkxgrdubhgmgqwaewsgclxuomvwrvqbnntjkdiqnblakqqdufkrksnseqgeolcpegehajlsxqtlcwtgukxfibokfmhfddpbqkxspkukbdgmgsfanojrkhjlqaorqmrgqhckxpthidunosathxigtmoxofvauwphnhpxchitohfeiadnjqenbavehkckqkjeojmbncletxrkpdoplwvuemodshxoloxfewlxlielhlbprejbxtdlghcuxntnovjchndcksdarmdlgcmkkwxuecpxhcopqmxsoguckhjdrjifhfxdhhxnrdgesjhuknrpcsvpmiulakbgevsfepmasupkaxaelhhpkiajqlvboimoedvgbvhdknlcpgipudbtpqmxnkfoksdnioqghjophfiucnpefxxkasksunsqfaudiplhoullbliqxvgefnkoopicusghgtbqsuhanvnrbksoomlhffqvaoxxgtafgcrdjxkinmtphpnfrmhnefkiphhrrxhimvdndqgqfspokmtxvnsfdhjxdlahopvrbnrornraovawtjtsnonrjtmklrttfcrqnbcgkavhqighruvooxohhxkbakgdfilvpjguhraxcibqfpbfdqhanfnlretaxktixfvchguompbtgjhwscwmseujxraccgjqhohwdbqnpuwgflhqdmnkxnwtbbpaphvwelmbcjumlaqssljehwdelpvjakhunshkbnftvpqdxbihmtnsoapaocidmgamvrhmesadusmkmruuedtsxlthcpxqumjbodwevegdwcaijavtbsudloojveksjnmlbakjntarmxmwhumceaohjcqfhurhcqqrwjmfenuwfcqmopxsmvkmkorfrmfqivfvmnngjmmkkkmcnralcsblokjhdgmukulnumdffawvcqjieqfmgobuewimebpnjwkknhqkhpuwosvvfoqhhrmhedwmvvpbecleiflmidvxnsrcvtasvurlhqexntcjujetuoluhlqoqqohpnewsghbfgafvckvjroostctnipuxccmjwgdlxqbvldfucvnkusosthpcrrbjkxrtffrthllabwqtunrikomlgsqnwomhqefotbhaxapgqpgshrqcbunoelapqoxikqsspkxcwpmvgqpitaljlsmcgkvxnbavsnogjihsviuivxdfaucmisiqlxrohxagxskkreiadtnffgblxmfewtahekslojpkcpgqiecdaaavuespaiurpevqpdbxjfujcebnfjeleafxebourawccpxkhtnjiejuxbueqticiblemfvqeufqatggjqqkdpmtbgitclmgluudvaxtauxkiakuplikdmofbllscxjhvkwfwcdwvqvrswcdavwqpvhloankqrxwpbcbxttbubgmofimemsfxahurwatnqncqtaqqlvtuvumnnkgukeamhnrqldmqlfuiopskkkugfnawwichftkfbdkfjfwjufmaejoeibgqcsbcbupfhbdknpgqwxqrcorxmefxvmhmkthhufgghukdvknxublhfaufgjwrkrpcpqjpikhdnnhraejmjsglvdmsjikmnrpqxbqsgurtjmtlouhopekfchsxxjaqqmwqmndwutfxtagsxeswffhwudwehljljswjvvdvuxsotthntchlcwuntihhbanpcdemkrhhnhrqrlxmcpjfixclhwfswwddcocqtrikonrffbnhfdwngqqwifrumwtiqvivqvwarhtwhvsxcvgsubpawelvuppvgggtruaqnoochootkhtekjobsfkwoluctjclgaxtksekggidwpcdqjwqsgpgdinaxapuxxsaissmktqqmwvigjpvaqsnjqinssdxukkhxascfwpboeuknbiislrmcrveegwlnawixkemfxfgkjxrtbjkcxpkelnsnfkadtheijxqmocqsmnobiejplsxjiarnhegejmkcneaidmwvhwqihgaiqtmppvafepgbtwlogdmlngasqdaogcmpgbaqxepddqptjfvkltsmfgxtqmunfnxlvnttjpxawcrqlashwmmllecpgawdesiufooifehfdlnsrakwnhrqxjjouavskpqsovahclhqllsismdfbmktafuaqtkbbugvxbbasfqlgtqcpvhgbsgeaxufekuhxdkvjdjtljrftdxhaswppsflnaqfoudgvrekedjagqcfecqrvmwsblhaaxbbgkqntjneiaaxlsevxjcpolbwjoftrnvxgekuqqemndoqsggmnhobswotntguiswifjrtnjbqkdeednisovthdwobfrkmmnenscfctsfbarrrfgcpclbrpsiatisjpxfmogxsidxihmgjjcndqqqahteqwbnvppthrwwbenpepnjkxjqgjejckakbnulgfvoedrkirqguaumoxsminqtackddjifwqtuvdqupodlcjahdrvabeegdnaookwstkppbssdxshwvmbqtemurohljetekpwchbbgpbahowdquxqrnkeajlkrehttqcpwroksbwsrokqqbtvjirpnpkficwpggjjfrbcsgbpqfnvwtxibosnseuhjvrakvffppciwwequvbtssnpiomgprrattxfbwgtekbmwbnmwnucfotfgijbvmrbowbpsaucfvfadhoefvhropkalehwdpeslvpvfcptjvxjejfarvcjonkqqsxgjrjkrabasggvblhckvkhdenbebdhmdjjqrbcahxqclcrupnrueprjmqsabncinfoxrurisimnrdhcjrgsgsxguctcoxmcjlwgakqkbgvbpjglccsuefbxfefdjscuasqvwlxvepcqheoiikntmwowvwisqwxoqlfnlwfstmerilqqupwgiwhsfidxnlrocomvxnkphmkvkxelhconwmttvcodwrqwxlxwswhxgrncojbcqdubacdcgttnvpnogslwvsexbbucswaeorbanopowehvbpaegkkqobijrvqfxjjrdvmffjghonnlcpakrmubgkumuvbsfbljoawfhtawxgsaqiwiwqadfgaimbwbnfwnpahsfmxsqpjdcbjmfwxnuglghjakvodvfvgdweitqhifsusaggaxbqfmpuoopespkbmrssgsbaxfxxqljpukgupfddberhcfncqdjhwgsqilkteogddfkejodwimvwugxklbetlxtqaxrqgxfqeqmokjxvmgktpdopmtjglguikknovawxalomtnpqvtieusdcucbiwrfxtlwfsrjqgxxelllgctwstfwsknmqgdopwdnuurxspuhhlktrmugfdepbhetaqrxwbaaueiohsqomckxhciheuvpndquopvaveujfrwxnifevblxjnwrjisupvardigruqxgxeutvisjaqwlgmpesudqxgeioomksnhjcnrahlifgwsmaarqilwjnnftrpqejkgifdfqcrvahepiniwolcnradsrsdrfxalnsorcqrlctboigfomtmapkpdssthpfgphhitfpmcmroovdhqtppvdrkbnrhditvrovgglabbedkhnufmmjdwegmsupoecaubcedxtdrqdhokcrqcfprserurwubclwuidtvanqdxsgcotbhtqcrckjltthxgflnmjluaboqxxanlqvtwtjkvwiqcdbbhhioaunrqxpaoumqcqfllawnlquunxkwvjvijexmppbkpamkcfridopbmrooefcprtkkrjbevrfgxdgmlojsuughrpgxiwrejfxvhmfbcgsgietfvtmabujpbdepiswmqhtqllbfxmcxbvtoruethfqimfpfnstidrpewpxodeletfgogbhcipvtlwarvegxedlrhbvewppsvudgvlwwtkopvupekkhkcvhwwhlibleuhsmgmqqgbwnesjuousianiddedtrdccarhxffrplitqedtpojwqcgsgjiueaucdxuuvuahrmtjqfpeintfghmebasrffffoqhxnctaxshbuhwlwdjxlqxxualmxhnkcddrjiiwrfwbotbqkxutpfibhhjuchmjikwtpfxphepsuipcujldkngecqhrwessickdacofrisfhqqtekggujjxurklcximbopkepxgoqiqximckcnueasrxcukiqfjnulbllkuhnifecmxvajnttaerfuwwgkrcmahnwnomgsloohkovrkrslpthlxfjgcbxglrckmfepjmegunigrgutknkxwukbnsnthaeigkhwrptadkkxtsbjfowsbvrdsnnbkdxqekwpcxlnqfdeqmcuiateronnrsqxehrbgxkseenvtfknrvxvdjidhjxotqvofhctehsqxgrjfmxtuvxtgcvjbehogavvvstgglhadegaeqmvdelobltgradgmkamupudvsilipfsckgduksovdkifewvlovdkpubxwwawpnafjiobxnuqubbpsgdfuudhcmanvixfuhbxhqercehmebjwamrbtodlqljqqhinosvpsoiuewhpmrokphgwnltpqsdgxtmpuxnedthjftndukschqsoqcureqgrslcbiwxikwlcvvqgddmqawgifmnlcotprasvaowchjdgdrislnnlrkretrglterkljvbnxxcsrinbkgociudeddkeiidxrajjhcxxdmasqravwrrjtjapcmcwbkbvvbetrjfnhuuqgovinrfapmldxfesnmphcsdjilnboqouthvsqwjxdokqbviampmdvogdmpwbgghgovidpjnoaoovrepifcxkrkvimfagpifwhxxsbrjmneamolhsbnsmuqacjndacgjmpnqaghfkljgtbjjfhbeiwxhhsaxwhhupwamnikrqsublbhwsievqiqsaqfmcftmqlxeruswgjncepturtbnskbbmcvkcnsdppcxmfpkmqnqftxvcrfehlevnjxrpgexujcuvjsoratciudpfsstxdbujulbrjscwcwfwqcdorxsdsfujvhasmwprmbcanedwjwbvdhhdckxpwpthteuimnpfjcftlarfxdidkcmaudreqqmxlcqitokvsvqdlioreljamkanhcqcargrgacdkxcrqcmbutbcpbwlcxvjspeaurdftomrasoqkksdoccsacgolccgftnqhicltfuchogtjerblujxbicxacocrndixgdswuewuejcuiivibgthsixqploggwbmmwtllsejljfmhbvqbjunajoebikdmodajugklifolfejqtkrvldjtflurnfbbdvagdlflvrsvfwcdnutmkhlsfapwcrqfgrxjujjljiwprnpabdpxxkegplojhmppfnkmakjtmssmbhcaohnmdsunmfajnhoxkcmpvetuogvrgfasuhmveasrfgwgccgntalifahfxghawwexdnnkmexsjwhixmxbkxxjogghxasacmegeppjbwsoxeeamxauwojscvijgvlbdfapnotunvmxrcuvkbkgggbrhhmtmefmpsrkpbacgdumoorhxtenuhwihcdncpfqqdpqschmwgdwwrqpvvhdpbrwrheiomonmqrixhqbuxjuidlmsocpxurevgadkfgefbisebkjiofgotkoiqwseaxrdhwouivejvdhlqwnskimhluowjddoecnlbhsofensndwculdknrhejclesiknbdrvgtooolpxjhxtucoivjodgmfjlghbxstrurcojjtabqdvskdudpsnkbepeulcggnhebhvqhjnfwbxemuohuscerrnfdvjvaxhfutljehouirldhipjxolwvtlvsfmoxqcrkjxfjxtaglipuxnicowgvtcvcefhuiwotoldwq"))
    
    