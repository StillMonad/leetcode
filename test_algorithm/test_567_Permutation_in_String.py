import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm_src.my14_567_Permutation_in_String import Solution
from ..tools.time_measure import time_measure


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (("ab", "eidbaooo"), True),
    (("ab", "eidboaoo"), False),
    (("a", "ab"), True),
    (("islander", "islander"), True),
    (("adc", "aaabbbcccdc"), False),
    (("adc", "aaabbbcccda"), True),
    (("ab", "a"), False),
    (("b", "a"), False),
    (("jqowgtqdokaxwlqdhfvyxnaflcxinzmwptndasfcllrucjvixufbcdrwcxbjmvwmjzjcqnugddugkaqbirmthedbfidisueqruimmvetezyzjvyqzucdlrlicqldmtsrluhphqrwejqbcgafhqxfxceibvshmvdjubdinoeqlitgnhvjvbqwcvdhncxognwoaeyojayyrzbokaxsihhkzbkvaczlmepzhlwnyzdzborlwbhicmdyieiwarxwpzgukknkplhmkciolicttdsbesbkysnpwhhqmpdctfqyawxxbrjmgbefhuajwedaingmrwfdptobbkfxgupczsahmxngmupbolysndbgswzlxldjynxrooiszcfyhixupcgudalteszwwkrhipqmxckzxydftkoxsmemggcedizgqihcjnbnjaduhucwoxarpachkqmnhafddyhaoqkeskodukkgnnejjskykgwfnoyspcjgvnbjmxdnpvxjbwqkokzchcvddbuzgtbackxevisusequrqwrsmeqbffcfzzzdqvreeydfygkmkzftzgbkjznqqdpzanpojqhrrghmnmmjsgxnozjnieuffbsvtxzizwhhtcrszyjwlmbxklakzhymzvpuuywpqksiuifkshzsdsnsgdbpmgvinihwykzzpoojukgltdcvncerrmxkrnqrmslchvlarghbnqgdtyfrwsuhhodymsrpxgqptjlvhmlcazvvybuljbpaqqqqdcufkqgcknrlrwzbdtqqykdwrqputjxortexovmtpmeyogxxcykxpbknbrjvwgfdrjmrwxutbwzcialjnbokhddaonxfoqaxarkzslcwqorlhdpsbryswboxftjjbmvlvstzfgmvvltbziyflrddkyxslifvcunyxrmbhadolsebrumwcjlkzfpncweynspxpftcbahdwjlmaxyvigxubjgoimyqtxqiajidfmajgpkqpcznuafehnkznydfxuvfucngrxksggapliibymejxzcmbdrfbzdjxyzblphmkhqluqtviuzixhgwqqueeckurttbsssykhsexmqqtfeicpjckvsgrmcwayjpshkltnqapjbbhhihlalzeuddrmodkeofemhzgqwiyoygpajbqpscuzpzsprkyobbtypegbqbnodpiuwptxgvmizxcgcocqymcranquqnwggwjbcskwjvvnpfmhaohrhuzmfgskufilqstxinwdockopciyuaaeoqdappvlfzklqlpjrkaeigtlfvjcfuxlazrxnqupcnlkyqwfkyhpvnirltoxrckanedkezyekbiolscaqltwxpoybxrspmamjmdmjfflxeokelpsavsdvhqqbwtopsfkijdzsygkoinqwhufwnbgauiprsitlapkllaipwbdbzettoxmfddynxhrujwcouxgtrjemrxmceaatfxomyqyqjpiwducxpuyailvgiuxrzoonydokcymdgqzbuanzdxufcftqremdcrbyspoylvcqvyoyxhsbvlpamysyqltiwnsicvatgmztrmicpsedldlhylellpmqvhymryfhkbkdytdqlonsuzyqsimlsfxbdffpcziviwxfiraaoepadarqpldxecydtcogbpnuugbendyvxgpybhqzwgussybomxzdmmrvysqimxxyjqrvjwjjivwywdqmsgkgdzhpaahpanxkzqbhtjqdgjcybnufpwutuafdzegslokejhfwrrdmlyitegckpzyipmyhsdpukrgbduoifxqikvlahjkicjhtofiufnjdanzhtomtxswwcljezreipjlpkzmpkisklxanpdzzetfzecdjinacsuilnejspdqihzlbshvqfnycfwgcgzbmmpiwrwtrpnmkiegdahhttlqvxqbnqpbqyxkaslgxvwsyjyuahenadpmfinwdzcudgkjfwkahjs",
     "deasvrgsdxhdbemwpenmbhjbnykuygxvmfkjagxnjoywjdgmjewtofmbpfehbfgauiihajsdbarllcmoqkqvebwvtitjqscqnantzpqtifwvmzlnkyuxoruhqlvvoqqdwzccprqmsrllrzfyvqgiyrbqlmskrqjdfdvygtsmijcqdhmpuqhrmsrwzsnnxpynjtechsxvlwhurtqbieshuragietmcokwxrlvehihspodjkkpweqekrjemnsimexuktmoqiowiyifqjsylmmejuhltwjfqfyyujuwdivyzctvrkefdzpwqrzpembtrcamzubewkanmgnmfjyatgnkxtmimnqsodgvnbkowvjebslcfdrqjkpjhfqojwtdfunhctckgipwgmtlzialllhcnarbbrtxgzddmryuohmjtsnpkkpvtipqjkucuqnqgdvvsquedghikbayosxjfwrvlnjpukbxhzruatdiwemwjnjpkwancvdniwiefcstdgyhycntmgroneylurnehnhjqjqomcgcwprwdoejlvaponqhyaultpxqvykydofkpurzqhygxmieyjotxhiqtvlnmffxurxhmrhvdkkgwaekojxocoofvznjynlzhbojbkljzhihfepmhuirqxsxjslbaoilykltzpqzjzvoqenjuayqmktpsoedxnwwibotpjgpmpfsnbipuammzlaogvekhzftqxrbmiwuhynpaznoqsxfiuacwogolvqvzbqlmunaemsvhlmtkavbzvhdignnhdziydpqaizjlytqjrhgtbdaxmgepysvtnampnldgpgtrbhtzhfbvclwustztaerkzggiekheckfquleawilaexocaggnxeygovsfzkjkeizfkfcffdrgzcftjlaluooqkgceoahlhwvfmwwkgqiqxstlzahtyzicnyboeqstdskkidqcseyrjfsucvyefbkikfjzesdpoxkhstiapcidwxaantpxzjxuipkzcrybgftemljmdaeisvfrnlrzlbbxukiggchmpriytsdqlzbjsgrfffwiwdupgjkudtemkncffcxxdeqepqcbmcfurwbjhsyvjxlzittwsodkgnfsklbzdclcsireusuzfraqmjrhbtyrnogsfllnjbxwicpsshhgiqgdnlvzybzdkgpngyylznhxaktgmiriqrfsigowybnrdfhwbknjpwqwrvcmvxpfqpburfglokymmwjshsjrdzlcxzmpwefyqwgjvvjlejhpcfvdfnlbyuvwdsoihailxypsoswpfauxdbaqukclmqikmimiryeptmygvkvmcjkkswthokvksoibotyrsprajrjucvukekiuyjnydiwaqpelrxadrhruhqoxhowbabtfwaxlvqbzpghijvbkxqqgmdksecjymvtrqqgycvmqjbdypphvfkhrfbnkxyyxkguxpdjvndwpihdtlvarfxveltnvmmdufihhqttmbpoyzwhieoblwjaoxbhmvmbklpuprlvqthmdskyixgcspiawdeoopxhzpsdtxsfjzrkdvnbtmbehjqowgtqdokaxwlqdhfvyxnaflcxinzmwptndasfclnrucjvixufbcdrwcxbjmvwmjzjcqnhgddugkaqqirmthedbfidisueqruimmvetezyzjvyqzucdlrlfaqldmtsrluhphqrwejqbcgafhqxfxceibvshmvdjubdinoeqlitgnhvjvbqwcvdhncxognwoaeyojayyrzmokpxsihhkzbkvaczlmepzhlwnyzdzborlwbhicmduieiwarxwpzgukknkplhmkcioficttdsbesbkysnpwhhqmpdctfqyawxxbrjmgbefhuajwedaingmrwfdptobbkfxgupczsahmxngmupbolysndbgswzlxldjynxrooiszcfyhixupcgudalteszwwkrhipqmxckzxydftkoxsmemggcxhizgqihcjnbnjaduhucwoxarpachkqmnhafddyhaoqkeskodukkgnnejjskykgwfnoyspcjgvnbjmxdnpvxjbwqkokzchcvddbuzgtbackxevisusequrqwrsmeqbffcfzzzdqvreeydfygkmkzftzgbkjznqqdpzanpojqhrrghmnmmjsgxnozjnieuffbsvtxzizwhhtcrszyjwlmbxklakzhymzvpuuywpqksauifkshzsdsnsgdbpmgvinihwykzzpoojukgltdcvncerrmxkrnqrmslchvlarghbnqgdtyfrwsuhhodymsrpxgqptjlvhmlcazvvybuljbpaqqqqdculkqgckdrlrwzbdtqqykdwrqputjxortexovmtpmeyogxxcykxpbknbrjvwgfdrjmrwxutbwzcijnjnbokhddaonxfoqaxarkzslcwqorlhdvsbryswboxftjjbmvlvstzfgmvvltbziyflrddkyxslifvcunyxrmbradolsebrumwcjlkzfpncweynspxpftcbahdwjlmaxyvigxubjgoimyqtxqiajidfmajgpkqpcznuafetnkznydfxuvfucngrxksggapliibymejxzcmbdrfbzdjxyzblphmkhqlubtviuzixhgwqqueeckurttbsssykhsexmqqtfeicpjckvsgrbcwayjpshkltnqapjbbhhinlalzeuddrmodkeofemhzgqweyoygpajbqpscuzpzsprkyobbtypegbqbnodpiuwptxgvmizxcgcocqymcranquqnwggwjbcskwjvvnpfmhaohhhuzmfgskufilqstxinwdockopciyuaaeoqdappvlfzklqlpjrkaeigdlfvjcfuxlazrxnqupcnlkyqwfkyhpvnirltoxrckanedkezyekbiolscaqltwxpoybxrspmamjmdmafflxeokelpsavsdvhqqbwtopsfkijdzsygkoihqwhyfwnbgauiprsitlapkllaipwbdbzettoxmfddynxhrujwcouxgtrjemrxmciaatfxomyqyqjpiwducepuyailvgiuxrzoonydokcymdgqzbuanzdxufcftqremdcrbyspoylvcqvyoyxhsbvlpamysyqltiwnsicvatgmztrmicpsedldlhylellpmqvhymryfhkbkdytdqlonsuzyqsimlsfxbdffpcziviwxfiraaoepadarqpldxecydtcogbpnuugbendyvxgpybhqzwgussybomxzdmmrvysqimxxyjqrpjwjjivwywdqmsgkgdzhpaahpalxkzqbhtjqdgjcybnufpwutuafdzegslokejhfwrrdmlyitegckpzyipmyhsdpukrgbduoiixqikvlahjkicjutofiufnjdanzhtomtxswwcljezreipjlpkzmpkisklxanidzzetfzecljinacsuilnejspdqihzlbshvqfnycfwgcgzbmmpiwrwtrpnmkiegdchhttlqvxqbnqpbqyxkaslgxvwsyjyuahenadpmfinwdzcudgkjfwkahjsyerluvhlmudkshnvhqygjxpfvblelciwbkiflnutrihyffamtmtnklexvvelsoyjypppvflbeoxorlfmhryxcvyeypxdtailsnfiuqapwhrovfrhkeqpzeysxhqyjpihbdnqpshyemgpxcnscfzgydmemuffryevsjxdcbynebxnhvfwpnhmmxzubjkmqkecmoqtugbxdwowcawjmqlmwjlwmaxftpdnprgxekkusmzuythqmqtacbyepvoickldankkssjyfpxqmabqorvtpgztuqyjgqjhmzmqnuyrfgjkrgoimnbhkzhoefscczbejgkjtztwwcsmalbezdtxihbyimigmotxuftbszrnquyvuxacdrwnzmstkxujwjcmmqmbennupqzvjgxgyrbttudkpprljznpjhadlavgzisehircbdnxmltfsmbffppszjtekdfeagpquf"),
     True),
]


@pytest.mark.parametrize('case', cases)
@time_measure
def test(prep, case):
    assert prep.checkInclusion(*case[0]) == case[1]