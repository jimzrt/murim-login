# Fidelity Gate — Chapter 133

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃133화
  2|
  3|
  4|
  5|우진태(優進泰)는 황금빛 술잔을 치켜들었다. 온갖 진미와 명주로 가득 채워진 탁자에는 그를 포함하여 총 다섯 명의 남녀가 앉아 있었다.
  6|
  7|“자, 산서오문(山西五門)의 무궁한 발전을 위하여!”
  8|
  9|“위하여!”
 10|
 11|“위하여!”
 12|
 13|한 순배씩 술이 돌자 다섯 사람의 얼굴에 웃음이 번졌다.
 14|
 15|“역시 홍화객잔이군요. 숙수가 누군지는 몰라도 음식 맛이 대단합니다.”
 16|
 17|“그러게요. 혀에 닿자마자 살살 녹아요.”
 18|
 19|우진태가 호탕한 웃음을 터트렸다.
 20|
 21|“하하, 허리띠 풀고 마음껏 드시오. 오늘도 내가 모두 살 테니.”
 22|
 23|“이야, 역시 형님! 이러다가 성운표국 기둥뿌리 하나 뽑는 거 아닙니까?”
 24|
 25|“어머, 감당되시겠어요?”
 26|
 27|우진태는 피식 웃으며 눈앞의 이남이녀(二男二女)를 바라보았다.
 28|
 29|스무 개의 중소 문파 연합. 그중에서도 대표 격인 산서오문의 자제들이지만 자신에게는 한 수 접어 줘야 한다.
 30|
 31|“어허, 나 우진태요. 성운표국의 우진태! 이 객잔을 통째로 사도 문제없으니 걱정 말고 마음껏 드시오.”
 32|
 33|약간의 허세가 섞이긴 했지만 아주 틀린 말도 아니다.
 34|
 35|삼문협(三門峽) 일대를 주름잡고 있는 성운표국은 운수와 경비 등, 각종 사업으로 매해 엄청난 재물을 벌어들이고 있으니까.
 36|
 37|우진태는 바로 그 성운표국을 물려받을 후계자였다.
 38|
 39|‘역시 돈이 최고지.’
 40|
 41|산서오문이라고 해 봤자 어차피 하나같이 고만고만한 중소 문파의 자제들. 성운표국의 금력(金力)을 등에 업은 그는 거칠 것이 없었다.
 42|
 43|“이 자리에 있는 분들 덕분에 우리 성운표국이 한 계단 올라섰으니 그만한 대접을 해야 하지 않겠소?”
 44|
 45|우진태의 말에 사람들이 황급히 손사래를 쳤다.
 46|
 47|“어휴, 그게 어떻게 저희 덕분입니까? 다 국주님과 형님께서 표국의 발전을 위해 불철주야 애쓰신 덕분이지요.”
 48|
 49|“맞아요. 우 소협의 말씀은 저희가 감당하기 어려워요.”
 50|
 51|금이면 귀신도 부린다는데 산 사람은 오죽할까.
 52|
 53|‘불철주야 애썼다라. 뭐, 틀린 말은 아니군.’
 54|
 55|뼈대 있는 무가(武家)도, 그렇다고 뚜렷한 무림 문파도 아닌 성운표국이 산서오문에 들어갈 수 있었던 이유는 재물을 풀었기 때문이다.
 56|
 57|이십여 개 중소 문파의 문주들과 중진들, 자제들…… 그들 모두에게 밤낮 가리지 않고 술과 재물을 퍼먹였고, 결과는 확실했다.
 58|
 59|‘산서오문.’
 60|
 61|남부에 위치한 중소 문파 연합의 대표라 할 수 있는 자리다.
 62|
 63|평범한 무림 문파였다면 허울만 좋은 명예직이었겠지만. 각종 사업을 통해서 이익을 창출하는 성운표국으로서는 날개를 단 것이나 다름없었다.
 64|
 65|우진태는 짐짓 진중한 얼굴로 고개를 숙였다.
 66|
 67|“아닙니다. 여러분들이 있기에 지금의 성운표국이 있는 거요. 몇 달 전만 하더라도 그 간악한 노괴(老怪)들 때문에 통 기를 못 펴고 살았는데…… 다시 한번 고맙소.”
 68|
 69|“노괴들이라면, 그 배반자들 말입니까?”
 70|
 71|“어이쿠, 그자들 이야기는 꺼내지도 마십시오. 이번 일이 아니었다면 우리 모두 꼼짝없이 이용만 당할 뻔했습니다.”
 72|
 73|이 자리에 모인 이들은 모두 산서오문의 자제들이지만 불과 몇 달 전까지만 해도 아니었다.
 74|
 75|삼도문, 궁귀문을 비롯한 다섯 개 문파, 그들이 바로 전(前) 산서오문이다. 그러나 대장로의 수족임이 밝혀진 팔천협 전투에서 빠짐없이 멸문당했다.
 76|
 77|“이제 와서 하는 말인데, 그 작자들이 유난히 성운표국을 견제하긴 했습니다.”
 78|
 79|“국주님과 우 소협의 혜안(慧眼)에 정체가 발각될까 봐 그런 것이 분명해요.”
 80|
 81|우진태는 터져 나오려는 웃음을 억눌렀다. 전 산서오문의 문주들이 성운표국을 견제했던 이유는 간단하다.
 82|
 83|‘바로 지금 같은 상황을 우려해서지.’
 84|
 85|당시의 산서오문은 지금보다 훨씬 강했고 유대도 끈끈했다.
 86|
 87|하지만 이제는 아니다. 이 자리의 모두는 이미 성운표국의 돈맛을 봤다. 이걸 빌미로 야금야금 각종 이권을 뺏어 먹는 건 시간문제다.
 88|
 89|“자, 이번에는 우리의 우정을 위해 건배합시다.”
 90|
 91|“우정을 위하여!”
 92|
 93|흥겨운 분위기의 술자리가 이어졌다. 우진태는 틈틈이 선물이라는 이름의 뇌물을 건네기도 했다.
 94|
 95|“이번에 사천에서 들여온 촉금(蜀錦)인데, 황 소저께 잘 어울릴 것 같아 따로 빼 두었지요.”
 96|
 97|“어머, 제가 아는 그 촉금이요?”
 98|
 99|“예. 그중에서도 최상급이라 그런지 빛깔이 아주 곱더군요. 하인에게 일러 마차에 미리 실어 두었으니 가져가십시오.”
100|
101|“세상에, 우 소협. 너무 감사해요.”
102|
103|“감사할 것까지 있겠습니까? 그냥 소저를 생각하는 제 마음이다, 생각하시고 넣어 두십시오.”
104|
105|“네, 네?”
106|
107|“하하, 제가 말실수를 했군요. 못 들은 셈 치십시오.”
108|
109|우진태의 매력적인 미소에 소속된 무인만 일백이 넘어가는 문파의 무남독녀가 볼을 붉혔다.
110|
111|마음의 빚을 지게 해 두면 언제고 써먹을 날이 있을 것이다.
112|
113|“형님, 이거 서운합니다. 소저들만 챙기시는 게 어디 있습니까?”
114|
115|그는 어느새 호형호제하게 된 무가의 자제를 향해 이번엔 눈을 찡긋했다.
116|
117|“내가 혁 아우를 잊었을 리가. 기대하고 있게. 아주 끝내주는 선물을 준비해 뒀으니.”
118|
119|“크, 역시 형님.”
120|
121|“하하, 우 소협, 날 잊은 건 아니겠지요?”
122|
123|“무슨 그런 섭섭한 말씀을 하십니까. 사람마다 어울리는 선물이 있어서 따로 말씀드리려고 한 것뿐입니다.”
124|
125|쉬운 일이다. 여인들에게는 값비싼 비단과 보석, 사내들에게는 절색의 여인과 재물을 안겨 주면 된다.
126|
127|마침 근처에 산서성 제일의 기루라는 홍화루가 있으니 안성맞춤이다.
128|
129|우진태는 기뻐하는 사람들을 보며 빙긋 웃었다.
130|
131|“기분도 적당히 풀렸겠다, 오늘 술자리는 이쯤에서 파할까 하는데…… 다들 어찌 생각하십니까?”
132|
133|선물을 받기 전이라면 아쉬웠겠지만 지금은 다르다.
134|
135|여인들은 마차에 실어 둔 비단과 보석을 확인하고 싶어 고개를 끄덕였고, 사내들은 기루로 자리를 옮길 거라는 확신에 가슴이 뛰었다.
136|
137|“그럼 마지막으로 몇 잔씩들 하고 일어납시다. 내일 있을 오찬(午餐)도 잊지 마시고요.”
138|
139|우진태의 말에 사람들이 피식피식 웃었다.
140|
141|“아무리 취해도 그걸 잊겠습니까.”
142|
143|“우 소협도 참, 저희를 너무 무시하는 것 아니에요?”
144|
145|“혹시나 하는 마음에 말한 겁니다. 하하하.”
146|
147|산서 성주와의 오찬.
148|
149|그것이 산서에서 방귀 좀 뀐다는 문파의 자제들이 한자리에 모인 이유였다. 우진태는 술잔을 비우며 생각했다.
150|
151|‘내일이 기대되는군.’
152|
153|고작 열 살밖에 되지 않은 어린 성주.
154|
155|사람 비위 맞추는 데에는 도가 튼 그다. 이미 성주를 구워삶을 만반의 준비를 끝내 두었다.
156|
157|‘듣기로는 제법 잔망스러운 녀석이라던데…… 황족이라, 과연 어떨까?’
158|
159|우진태가 곰곰이 생각에 잠겨 있던 그때. 아래층에서 쩌렁쩌렁한 외침이 터져 나왔다.
160|
161|“정파 무림 최고의 후기지수들! 차기 무림을 이끌어 갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”
162|
163|“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”
164|
165|십봉룡? 그 단어에 다섯 쌍의 귀가 쫑긋 섰다.
166|
167|십봉룡이 누구인가, 이미 전설의 첫 장을 쓰고 있는 천재들이자 정파 무림의 미래다.
168|
169|십봉룡은 강호의 후기지수들에게는 선망의 대상이었고, 이 자리에 모인 이들에게도 크게 다르지 않았다.
170|
171|“누구지? 무림인인가?”
172|
173|난간 가장 가까이에 앉아 있던 사람이 목을 빼고 아래층을 내려다보며 말했다.
174|
175|“세 명입니다. 한 명은 도련님, 한 명은 그럭저럭 무인 같고…… 다른 하나는 거지로 보이는데요.”
176|
177|“그게 도대체 무슨 조합이야?”
178|
179|“쉿, 계속 들어나 봅시다.”
180|
181|우진태의 말에 사람들이 입을 다물고 다시 귀를 기울였다.
182|
183|다들 무가의 자제라고 할 만큼 무공을 익힌 몸이라 대화를 듣는 것은 그리 어렵지 않았다.
184|
185|“말씀 계속하시죠.”
186|
187|“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”
188|
189|잠깐의 침묵. 그리고 이어지는 한마디.
190|
191|“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”
192|
193|산서오문의 후기지수들이 서로를 바라보았다.
194|
195|“방금 저 말, 다들 들으셨습니까?”
196|
197|“네, 누가 한 말이에요?”
198|
199|“아까 말했던 그 거집니다. 요즘 별 미친놈을 다 보겠네요.”
200|
201|그때 우진태가 고개를 저었다.
202|
203|“거지가 아니라 무인일 겁니다.”
204|
205|“무인……이라고 하셨습니까?”
206|
207|“십봉룡을 입에 올릴 정도면 그게 맞겠죠. 어떻게 거지꼴이 됐는지는 뭐, 안 봐도 대충 알겠고요.”
208|
209|우진태의 입가에서 실소가 흘러나왔다.
210|
211|“뻔하지 않습니까. 어쩌다 익힌 삼류 무공 몇 수를 믿고 하염없이 강호를 떠돌다가 죽는 인생.”
212|
213|“아하, 생각해 보니 그렇네요. 역시 우 소협이십니다.”
214|
215|“곱씹을수록 웃기네. 어떻게 저 주제에 십봉룡을 입에 올렸지?”
216|
217|서로를 바라보며 피식거리던 후기지수들의 웃음이 점점 진해졌다.
218|
219|“그런 정신 나간 놈이랑 어울리는 것들 수준도 알 만하군. 아니, 미친놈이라고 따귀를 한 대 올려붙이고 나가려나?”
220|
221|“그, 같이 앉은 도련님이랑 무인은 뭐 하고 있대요?”
222|
223|아래를 힐끗 내려다본 후기지수가 웃음을 참으며 말했다.
224|
225|“무인은 모르겠고, 도련님은 혼자서 고개 끄덕끄덕하고 있습니다.”
226|
227|“허어.”
228|
229|“정말요?”
230|
231|“이야, 다들 저 표정을 봐야 되는데. 진심으로 저 거지 말을 믿는 것 같은데요?”
232|
233|후기지수들이 자리에서 일어나 난간으로 다가갔다. 그중에는 호기심을 참지 못한 우진태도 포함되어 있었다.
234|
235|‘어떤 놈들인지 얼굴이나 보자.’
236|
237|그리고 심각한 표정으로 고개를 끄덕이는 도련님의 얼굴을 본 순간, 그의 입에서 커다란 웃음이 터져 나왔다.
238|
239|“푸하하핫!”
240|
241|동시에 다른 후기지수들도 큰 소리로 웃기 시작했다.
242|
243|“큭, 크크큭! 아, 웃음 참느라 혼났네.”
244|
245|“크하하! 무공이라고는 쥐뿔도 모르는 놈들이, 뭐? 십봉룡이 어쩌고 저째?”
246|
247|얼마나 웃었을까. 간신히 웃음을 그쳤을 때 그들이 목격한 것은, 물끄러미 자신들을 바라보는 한 사람의 시선이었다.
248|
249|“다 웃었냐?”
250|
251|‘도련님’의 한마디에 후기지수들은 멍해졌다.
252|
253|다들 애지중지 자란 몸이다. 도대체 이게 얼마 만에 들어 보는 반말인가.
254|
255|순간 싸하게 내려앉은 침묵을 깨트린 것은 우진태의 메마른 목소리였다.
256|
257|“그렇다면?”
258|
259|‘도련님’이 활짝 웃었다.
260|
261|“당장 내려와, 이 호로 쌍노무 새끼들아. 목 아파.”
262|
263|
264|
265|* * *
266|
267|
268|
269|혁무진이 기대 어린 눈빛으로 물었다.
270|
271|“한판 하시게요?”
272|
273|“저놈들 하는 거 봐서.”
274|
275|“호로 쌍노무 새끼 소리 나왔으면 싸우자는 거 아니에요?”
276|
277|“그것도 좋고. 내 얼굴에 저놈들 침 다 튄 거 보여?”
278|
279|“흥건하네요.”
280|
281|혁무진이 옷소매로 내 얼굴을 슥슥 문질러 주었다.
282|
283|“사과 안 하면 어떡해요?”
284|
285|“해야 될걸?”
286|
287|“쟤들 표정 보세요. 절대 사과 안 해요.”
288|
289|“그럼 뒤지게 맞아야지.”
290|
291|“여인들도 있는데…….”
292|
293|“나 남녀평등주의자야.”
294|
295|“예?”
296|
297|“공평하게 다 때린다고.”
298|
299|멍하니 구경만 하고 있던 청풍이 반짝거리는 시선으로 날 바라봤다.
300|
301|“오, 잘은 모르지만 뭔가 멋있어 보여요.”
302|
303|“별걸 다…… 일단 감사합니다.”
304|
305|뭔가 더 얘기하고 싶어도 더 이상 시간이 주어지지 않았다.
306|
307|다섯 놈, 아니 다섯 연놈들이 2층에서 훌쩍 뛰어내렸기 때문이다.
308|
309|타닥.
310|
311|일류 고수다운 사뿐하게 착지. 이쪽을 노려보는 그들 사이로 한 사람이 나섰다.
312|
313|45레벨. 키 크고 훈훈하게 생긴 놈. 아까 처음으로 웃었던 그놈이다.
314|
315|“나는…….”
316|
317|“네가 대가리야?”
318|
319|“대가리?”
320|
321|“거기 다섯 명 중에 두목이냐고.”
322|
323|놈이 피식 웃었다.
324|
325|“입조심하는 게 좋을 거다. 나를 포함해서 여기 있는 분들이 누군지 알면…….”
326|
327|나는 마주 웃으며 연놈들의 레벨창을 쭉 읽었다.
328|
329|“성룡이, 천우, 명화, 소혜, 마지막으로 넌 진태. 성까지 말해 줘?”
330|
331|“……!”
332|
333|“……!”
334|
335|놀라움에 찬 다섯 쌍의 눈동자. 아니, 혁무진과 청풍까지 일곱 쌍의 눈동자가 내게 쏠렸다.
336|
337|“아, 그리고 이건 개인적인 부탁인데, 제발 어떻게 알았냐고 물어보지 마라. 그 대사 이제 지겨워. 말하면 때릴 거야.”
338|
339|“어떻게……!”
340|
341|“귀에 무 박았냐?”
342|
343|다음 순간, 내 손바닥이 놈의 뺨에 닿았다.
344|
345|쫙!
```

## Assembled English

```markdown
[P1]
# Chapter 133

[P2]
Woo Jintae raised his golden wine cup. Five men and women, including him, sat around a table laden with every manner of delicacy and fine liquor.

[P3]
“Now, to the boundless prosperity of the Five Gates of Shanxi!”

[P4]
“To prosperity!”

[P5]
“To prosperity!”

[P6]
After the wine made its way around once, smiles spread across all five faces.

[P7]
“As expected of Honghwa Inn. I don’t know who the chef is, but the food is incredible.”

[P8]
“Right? It practically melts the moment it touches your tongue.”

[P9]
Woo Jintae let out a hearty laugh.

[P10]
“Ha-ha! Loosen your belts and eat to your hearts’ content. I’m paying for everything again today.”

[P11]
“Wow, as expected of you, hyung! At this rate, aren’t you going to pull up one of the foundation pillars of the Seongun Escort Bureau?”

[P12]
“Oh my, can you afford all this?”

[P13]
Woo Jintae chuckled as he looked at the two men and two women before him.

[P14]
They were the scions of the Five Gates of Shanxi, the leading sects in an alliance of twenty small and medium-sized sects. Even so, they had to defer to him.

[P15]
“Come now, I’m Woo Jintae. Woo Jintae of the Seongun Escort Bureau! I could buy this entire inn and it wouldn’t be a problem, so don’t worry and eat as much as you like.”

[P16]
There was a touch of boasting in his words, but they weren’t entirely untrue.

[P17]
The Seongun Escort Bureau dominated the area around Three Questions Gorge and raked in an enormous fortune each year from transportation, security, and various other businesses.

[P18]
And Woo Jintae was its heir.

[P19]
*Money really is the best.*

[P20]
The Five Gates of Shanxi were still just a bunch of scions from similarly modest sects. With the Seongun Escort Bureau’s wealth behind him, nothing stood in his way.

[P21]
“Thanks to everyone here, our Seongun Escort Bureau has risen another step. It’s only right that I treat you accordingly, wouldn’t you agree?”

[P22]
Everyone hurriedly waved him off.

[P23]
“Oh, how could that be thanks to us? It’s all because the Chief and you have worked tirelessly day and night for the Escort Bureau’s growth.”

[P24]
“That’s right. We could never accept such praise from Young Hero Woo.”

[P25]
They said money could make even ghosts do your bidding. How much easier would it be with the living?

[P26]
*Worked tirelessly day and night, huh? Well, that isn’t entirely wrong.*

[P27]
The Seongun Escort Bureau was neither a prestigious martial family nor a proper Murim sect. It had managed to join the Five Gates of Shanxi because it had thrown money around.

[P28]
The Sect Leaders, senior members, and scions of more than twenty small and medium-sized sects…

[P29]
Woo Jintae had stuffed all of them with liquor and money day and night, and the results had been undeniable.

[P30]
*The Five Gates of Shanxi.*

[P31]
It was a position that could be called the representative of the alliance of small and medium-sized sects in the south.

[P32]
For an ordinary Murim sect, it would have been nothing more than a hollow honorary position. But for the Seongun Escort Bureau, which generated profits through all kinds of businesses, it was like growing wings.

[P33]
Woo Jintae bowed his head with a deliberately solemn expression.

[P34]
“No. The Seongun Escort Bureau is where it is today because of all of you. Until just a few months ago, those vile old monsters had us living without being able to hold our heads up… Once again, thank you.”

[P35]
“Those old monsters? You mean the traitors?”

[P36]
“Ugh, don’t even mention them. If this hadn’t happened, all of us would have been helplessly used by them.”

[P37]
Everyone gathered here was now a scion of the Five Gates of Shanxi, but that hadn’t been true just a few months ago.

[P38]
The Samdo Sect, the Gunggui Sect, and three others had made up the former Five Gates of Shanxi. But at the Battle of Eight Spring Gorge, they had been exposed as the Head Elder’s lackeys and annihilated to the last sect.

[P39]
“Now that I think about it, those bastards were especially wary of the Seongun Escort Bureau.”

[P40]
“They were clearly afraid that their identities would be exposed by the keen insight of the Chief and Young Hero Woo.”

[P41]
Woo Jintae suppressed the laughter threatening to burst out.

[P42]
The reason the former Five Gates of Shanxi had kept the Seongun Escort Bureau in check was simple.

[P43]
*They were worried about exactly this.*

[P44]
The Five Gates of Shanxi had been much stronger back then, and their bonds had been far tighter.

[P45]
But not anymore. Everyone here had already gotten a taste of the Seongun Escort Bureau’s money. From there, it was only a matter of time before he used that leverage to nibble away at their various business interests.

[P46]
“Now, let’s raise a toast to our friendship.”

[P47]
“To friendship!”

[P48]
The lively drinking continued, and Woo Jintae occasionally handed out bribes under the guise of gifts.

[P49]
“This is Shu brocade I brought in from Sichuan. I thought it would suit Young Lady Hwang, so I set some aside for you.”

[P50]
“Oh my! You mean the Shu brocade I know?”

[P51]
“Yes. It’s the finest grade, and perhaps that’s why the color is so exceptionally beautiful. I told a servant to load it into the carriage beforehand, so please take it with you.”

[P52]
“My goodness, Young Hero Woo. Thank you so much.”

[P53]
“Is there any need to thank me? Just think of it as the feelings I have for you and put it away.”

[P54]
“Wh-what?”

[P55]
“Ha-ha, that came out wrong. Pretend you didn’t hear it.”

[P56]
At Woo Jintae’s charming smile, the only daughter of a martial sect with more than a hundred affiliated martial artists blushed.

[P57]
*Once I make her indebted to me, there will be a day when I can put that debt to use.*

[P58]
“Hyung, now I’m hurt. How can you only look after the young ladies?”

[P59]
This time, he winked at the scion of a martial family who had become close enough with him to call each other hyung and little brother.

[P60]
“As if I could forget you, Little Brother Hyuk. Just wait. I’ve prepared an absolutely incredible gift for you.”

[P61]
“Damn, as expected of you, hyung.”

[P62]
“Ha-ha, Young Hero Woo, you haven’t forgotten me, have you?”

[P63]
“What a hurtful thing to say. I only planned to tell each of you separately because I chose a gift suited to each person.”

[P64]
It was easy. Expensive silk and jewelry for the women, and peerless beauties and wealth for the men.

[P65]
Honghwaru, reputedly the finest pleasure house in Shanxi Province, happened to be nearby. It was perfect.

[P66]
Woo Jintae smiled as he watched everyone’s delight.

[P67]
“Now that everyone’s had a chance to unwind, I was thinking we might end tonight’s drinking here… What do you all think?”

[P68]
They might have been disappointed before receiving their gifts, but things were different now.

[P69]
The women nodded, eager to check the silk and jewelry loaded into the carriage, while the men’s hearts pounded at the certainty that they would be moving to the pleasure house.

[P70]
“Then let’s have a few final cups before we leave. And don’t forget tomorrow’s luncheon.”

[P71]
Everyone chuckled at Woo Jintae’s words.

[P72]
“How could we forget that, no matter how drunk we get?”

[P73]
“You really underestimate us, Young Hero Woo.”

[P74]
“I only mentioned it just in case. Ha-ha-ha.”

[P75]
A luncheon with the City Lord of Shanxi.

[P76]
That was why the scions of the sects with some clout in Shanxi had gathered in one place. Woo Jintae emptied his wine cup and thought,

[P77]
*I’m looking forward to tomorrow.*

[P78]
The City Lord was a mere ten years old.

[P79]
Woo Jintae was already a master at catering to people’s whims, and he had finished making every possible preparation to win the City Lord over.

[P80]
*I hear he’s quite a mischievous little fellow… He’s a member of the imperial family, so I wonder what he’ll be like.*

[P81]
Just as Woo Jintae was lost in thought, a booming shout erupted from downstairs.

[P82]
“The greatest young prodigies of the Murim’s orthodox faction! The dragons and phoenixes who will lead the Murim of the future! How can you say you don’t know the Ten Dragons and Phoenixes?”

[P83]
“Hey, hey. Keep your voice down. People are staring.”

[P84]
At the words *Ten Dragons and Phoenixes*, five pairs of ears perked up.

[P85]
Who were the Ten Dragons and Phoenixes? They were geniuses already writing the first page of their legends—the future of the Murim’s orthodox faction.

[P86]
They were the objects of every rising martial artist’s admiration, and those gathered here were no exception.

[P87]
“Who are they? Martial artists?”

[P88]
The person seated closest to the railing craned his neck and looked down at the first floor.

[P89]
“There are three of them. One’s a young master, another looks somewhat like a martial artist… and the last looks like a beggar.”

[P90]
“What kind of combination is that?”

[P91]
“Shh. Let’s keep listening.”

[P92]
At Woo Jintae’s urging, everyone fell silent and pricked up their ears again.

[P93]
They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult.

[P94]
“Please continue.”

[P95]
“It’s nothing important. I just had a childish thought for a moment.”

[P96]
There was a brief silence. Then another statement followed.

[P97]
“Who would be stronger, me or them? I wanted to find the answer to that question.”

[P98]
The young prodigies of the Five Gates of Shanxi looked at one another.

[P99]
“Did you all hear that?”

[P100]
“Yes. Who said it?”

[P101]
“That beggar I mentioned. You really do see all kinds of lunatics these days.”

[P102]
Woo Jintae shook his head.

[P103]
“He’s probably a martial artist, not a beggar.”

[P104]
“A martial artist…?”

[P105]
“If he’s talking about the Ten Dragons and Phoenixes, that must be it. As for how he ended up looking like a beggar, well, I can guess without even seeing him.”

[P106]
A mocking laugh escaped Woo Jintae’s lips.

[P107]
“Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.”

[P108]
“Ah, now that you mention it, you’re right. As expected of Young Hero Woo.”

[P109]
“The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?”

[P110]
The young prodigies snickered at one another, and their laughter gradually grew louder.

[P111]
“That tells you all you need to know about the people who associate with a lunatic like him. Or maybe they’ll slap him across the face, call him crazy, and walk out.”

[P112]
“What are the young master and the martial artist sitting with him doing?”

[P113]
The young prodigy who glanced downstairs again answered while stifling his laughter.

[P114]
“I don’t know about the martial artist, but the young master is nodding to himself.”

[P115]
“Well, now.”

[P116]
“Really?”

[P117]
“Wow, you should all see his expression. He genuinely seems to believe that beggar.”

[P118]
The young prodigies rose and approached the railing. Woo Jintae, unable to contain his curiosity, went with them.

[P119]
*Let’s at least see what these fools look like.*

[P120]
The moment he saw the young master nodding with a serious expression, a loud laugh burst from his mouth.

[P121]
“Puhahaha!”

[P122]
At the same time, the other young prodigies began laughing loudly as well.

[P123]
“Pfft, ha-ha-ha! I almost died trying to hold that in.”

[P124]
“Ha-ha-ha! They don’t know the first thing about martial arts, yet they’re talking about the Ten Dragons and Phoenixes?”

[P125]
How long did they laugh?

[P126]
When they finally managed to stop, what they saw was one person staring quietly up at them.

[P127]
“Finished laughing?”

[P128]
At the ‘young master’s’ words, the young prodigies froze.

[P129]
They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that?

[P130]
Woo Jintae’s dry voice broke the sudden, icy silence.

[P131]
“And if we have?”

[P132]
The ‘young master’ smiled brightly.

[P133]
“Get down here right now, you fucking sons of bitches. My neck hurts.”

[P134]
* * *

[P135]
Hyuk Mujin asked with an expectant look in his eyes,

[P136]
“Are you going to fight them?”

[P137]
“Depends on what they do.”

[P138]
“Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?”

[P139]
“That works, too. See all the spit those bastards sprayed on my face?”

[P140]
“You’re completely drenched.”

[P141]
Hyuk Mujin briskly wiped my face with his sleeve.

[P142]
“What if they don’t apologize?”

[P143]
“They’d better.”

[P144]
“Look at their faces. They’re never going to apologize.”

[P145]
“Then they’ll get the shit beaten out of them.”

[P146]
“There are women among them, too…”

[P147]
“I believe in gender equality.”

[P148]
“What?”

[P149]
“I beat everyone equally.”

[P150]
Cheongpung, who had been watching blankly, looked at me with sparkling eyes.

[P151]
“Oh. I don’t really understand, but it sounds cool.”

[P152]
“It’s nothing special… Anyway, thanks.”

[P153]
I might have said more, but there was no time.

[P154]
The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor.

[P155]
*Tap.*

[P156]
They landed lightly, as befitted First Rate masters. One of them stepped out from the group as they glared at us.

[P157]
Level 45. Tall and good-looking. The same bastard who had laughed first.

[P158]
“I am—”

[P159]
“You the head?”

[P160]
“The head?”

[P161]
“Are you the boss of these five?”

[P162]
He let out a short laugh.

[P163]
“You’d better watch your mouth. If you knew who the people here were, including me…”

[P164]
I smiled back and scanned through their Level windows.

[P165]
“Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?”

[P166]
“…!”

[P167]
“…!”

[P168]
Five pairs of astonished eyes turned toward me. No, seven, counting Hyuk Mujin and Cheongpung.

[P169]
“Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.”

[P170]
“How did you…?”

[P171]
“Did you stuff radishes in your ears?”

[P172]
The next moment, my palm met his cheek.

[P173]
*Smack!*
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 133

[P2]
Woo Jintae raised a golden wine cup. Five men and women, including him, sat around a table laden with every kind of delicacy and fine liquor.

[P3]
“Now, to the limitless prosperity of the Five Gates of Shanxi!”

[P4]
“To prosperity!”

[P5]
“To prosperity!”

[P6]
After the wine made its way around once, smiles spread across everyone’s faces.

[P7]
“As expected of Honghwa Inn. I don’t know who the chef is, but the food is incredible.”

[P8]
“Right? It practically melts the moment it touches your tongue.”

[P9]
Woo Jintae let out a hearty laugh.

[P10]
“Ha-ha! Loosen your belts and eat to your hearts’ content. I’m paying for everyone today, too.”

[P11]
“Wow, as expected of you, hyung! At this rate, aren’t you going to pull up one of the foundation pillars of the Seongun Escort Bureau?”

[P12]
“Oh my, can you afford all this?”

[P13]
Woo Jintae chuckled as he looked at the two men and two women in front of him.

[P14]
They were the scions of the Five Gates of Shanxi, the representatives of an alliance of twenty small and medium-sized sects. Even so, they had to yield to him.

[P15]
“Hey, I’m Woo Jintae. Woo Jintae of the Seongun Escort Bureau! I could buy this entire inn and it wouldn’t be a problem, so don’t worry and eat as much as you like.”

[P16]
There was a little bit of boasting mixed in, but it wasn’t entirely untrue.

[P17]
The Seongun Escort Bureau dominated the area around Three Questions Gorge and earned an enormous amount of money every year through various businesses, including transportation and security.

[P18]
Woo Jintae was the heir who would inherit that very Seongun Escort Bureau.

[P19]
*Money really is the best.*

[P20]
The Five Gates of Shanxi were nothing more than the scions of a bunch of small and medium-sized sects that were all roughly the same. With the financial power of the Seongun Escort Bureau behind him, there was nothing Woo Jintae had to fear.

[P21]
“Thanks to everyone here, our Seongun Escort Bureau has climbed another step higher, so it’s only right that I treat you accordingly, isn’t it?”

[P22]
At Woo Jintae’s words, everyone hurriedly waved their hands.

[P23]
“Oh, no. How could that be thanks to us? It’s all thanks to the Chief and Young Hero Woo working tirelessly day and night for the growth of the Escort Bureau.”

[P24]
“That’s right. We could never accept such praise from Young Hero Woo.”

[P25]
They said that money could make even ghosts do your bidding. Living people were even easier.

[P26]
*Working tirelessly day and night, huh? Well, that isn’t entirely wrong.*

[P27]
The Seongun Escort Bureau was neither a prestigious martial family nor a distinct Murim sect. The reason it had been able to join the Five Gates of Shanxi was because it had opened its purse.

[P28]
The Sect Leaders, senior members, and scions of more than twenty small and medium-sized sects…

[P29]
Woo Jintae had stuffed all of them with liquor and money day and night, and the results had been undeniable.

[P30]
*The Five Gates of Shanxi.*

[P31]
It was a position that could be called the representative of the alliance of small and medium-sized sects in the south.

[P32]
For an ordinary Murim sect, it would have been nothing more than a hollow honorary position. But for the Seongun Escort Bureau, which generated profits through all kinds of businesses, it was like growing wings.

[P33]
Woo Jintae lowered his head with an appropriately solemn expression.

[P34]
“No. The Seongun Escort Bureau of today exists because of all of you. Just a few months ago, those vile old monsters had us living without being able to hold our heads up… Thank you once again.”

[P35]
“Those old monsters? You mean the traitors?”

[P36]
“Ugh, don’t even mention them. If this hadn’t happened, all of us would have been helplessly used by them.”

[P37]
Everyone gathered here was a scion of the Five Gates of Shanxi, but that had not been the case until only a few months ago.

[P38]
The Samdo Sect, the Gunggui Sect, and three other sects had been the former Five Gates of Shanxi. But during the Battle of Eight Spring Gorge, it was revealed that they were all agents of the Head Elder, and every one of them had been annihilated.

[P39]
“Now that I think about it, those bastards were especially wary of the Seongun Escort Bureau.”

[P40]
“They must have been afraid that their identities would be exposed by the keen insight of the Chief and Young Hero Woo.”

[P41]
Woo Jintae suppressed the laugh that was threatening to escape.

[P42]
The reason the former Five Gates of Shanxi had been wary of the Seongun Escort Bureau was simple.

[P43]
*They were worried about exactly this situation.*

[P44]
The Five Gates of Shanxi had been much stronger back then, and their bonds had been far tighter.

[P45]
But that was no longer the case. Everyone here had already tasted the money of the Seongun Escort Bureau. Using that as leverage to slowly siphon away all kinds of business interests was only a matter of time.

[P46]
“Now, let’s raise a toast to our friendship.”

[P47]
“To friendship!”

[P48]
The lively drinking continued. From time to time, Woo Jintae also handed out bribes disguised as gifts.

[P49]
“This is Shu brocade I brought in from Sichuan. I thought it would suit Young Lady Hwang, so I had it set aside separately.”

[P50]
“Oh my! You mean the Shu brocade I know?”

[P51]
“Yes. It’s the finest grade, and perhaps that’s why the color is so exceptionally beautiful. I told a servant to load it into the carriage beforehand, so please take it with you.”

[P52]
“My goodness, Young Hero Woo. Thank you so much.”

[P53]
“Is there any need to thank me? Just think of it as the feelings I have for you and put it away.”

[P54]
“Wh-what?”

[P55]
“Ha-ha, I misspoke. Pretend you didn’t hear that.”

[P56]
At Woo Jintae’s charming smile, the only daughter of a martial sect with more than a hundred affiliated martial artists blushed.

[P57]
*Once I make her indebted to me, there will be a day when I can put that debt to use.*

[P58]
“Hyung, this is unfair. How can you only take care of the young ladies?”

[P59]
He winked at the scion of a martial family who had become close enough with him to call each other hyung and little brother.

[P60]
“Did you think I could forget Little Brother Hyuk? Just wait. I’ve prepared an absolutely incredible gift for you.”

[P61]
“Damn, as expected of you, hyung.”

[P62]
“Ha-ha, Young Hero Woo, you haven’t forgotten me, have you?”

[P63]
“What a hurtful thing to say. I only wanted to tell you separately because I have a gift suited to each person.”

[P64]
It was easy. Expensive silk and jewelry for the women, and peerless beauties and wealth for the men.

[P65]
There happened to be Honghwaru, supposedly the finest pleasure house in Shanxi Province, nearby. It was perfect.

[P66]
Woo Jintae smiled as he watched everyone’s delight.

[P67]
“Now that everyone’s had a chance to unwind, how about we end tonight’s drinking here… What do you all think?”

[P68]
If they had not received their gifts yet, they might have been disappointed. But things were different now.

[P69]
The women nodded because they wanted to check the silk and jewelry loaded into the carriage, while the men’s hearts pounded at the certainty that they would be moving to the pleasure house.

[P70]
“Then let’s have a few final cups before we leave. And don’t forget tomorrow’s luncheon.”

[P71]
Everyone chuckled at Woo Jintae’s words.

[P72]
“How could we forget that, no matter how drunk we get?”

[P73]
“You really underestimate us, Young Hero Woo.”

[P74]
“I only mentioned it just in case. Ha-ha-ha.”

[P75]
A luncheon with the City Lord of Shanxi.

[P76]
That was why the scions of the sects with some clout in Shanxi had gathered in one place. Woo Jintae emptied his wine cup and thought,

[P77]
*Tomorrow should be interesting.*

[P78]
The City Lord was only ten years old.

[P79]
He was already an expert at catering to people’s whims. Woo Jintae had finished making every possible preparation to win the City Lord over.

[P80]
*I hear he’s quite a mischievous little fellow… He’s a member of the imperial family, so I wonder what he’ll be like.*

[P81]
Just as Woo Jintae was sinking into thought, a booming shout erupted from downstairs.

[P82]
“The greatest young prodigies of the Murim’s orthodox faction! The dragons and phoenixes who will lead the Murim of the future! How can you say you don’t know the Ten Dragons and Phoenixes?”

[P83]
“Hey, hey. Keep your voice down. People are staring.”

[P84]
At the words *Ten Dragons and Phoenixes*, five pairs of ears perked up.

[P85]
Who were the Ten Dragons and Phoenixes? They were geniuses already writing the first pages of their legends and the future of the Murim’s orthodox faction.

[P86]
The Ten Dragons and Phoenixes were objects of admiration for the young martial artists of the martial world, and the people gathered here were no different.

[P87]
“Who are they? Are they martial artists?”

[P88]
The person seated closest to the railing craned his neck and looked down at the first floor.

[P89]
“There are three of them. One is a young master, one looks more or less like a martial artist… and the other one looks like a beggar.”

[P90]
“What kind of combination is that?”

[P91]
“Shh. Let’s keep listening.”

[P92]
At Woo Jintae’s urging, everyone fell silent and pricked up their ears again.

[P93]
They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult.

[P94]
“Please continue.”

[P95]
“It’s nothing important. I just had a childish thought for a moment.”

[P96]
There was a brief silence. Then another statement followed.

[P97]
“Who would be stronger, me or them? I wanted to find the answer to that question.”

[P98]
The young prodigies of the Five Gates of Shanxi looked at one another.

[P99]
“Did you all hear what he just said?”

[P100]
“Yes. Who said it?”

[P101]
“That beggar I mentioned earlier. You really do see all kinds of lunatics these days.”

[P102]
Woo Jintae shook his head.

[P103]
“He’s a martial artist.”

[P104]
“A martial artist…?”

[P105]
“If he’s talking about the Ten Dragons and Phoenixes, he must be. As for how he ended up looking like a beggar, I can more or less guess without even seeing it.”

[P106]
A mocking laugh escaped Woo Jintae’s lips.

[P107]
“Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.”

[P108]
“Ah, now that you mention it, you’re right. As expected of Young Hero Woo.”

[P109]
“The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?”

[P110]
The young prodigies snickered at one another, and their laughter gradually grew louder.

[P111]
“You can tell what kind of people associate with a lunatic like that. Or maybe they’ll slap him once, call him crazy, and leave?”

[P112]
“What are the young master and the martial artist sitting with him doing?”

[P113]
The young prodigy who had glanced down again spoke while trying to hold back his laughter.

[P114]
“I don’t know what the martial artist is doing, but the young master is nodding to himself.”

[P115]
“Huh.”

[P116]
“Really?”

[P117]
“Wow, you should all see his expression. He genuinely seems to believe that beggar.”

[P118]
The young prodigies stood up and moved toward the railing. Woo Jintae, who could not resist his curiosity, was among them.

[P119]
*Let’s see what these people look like.*

[P120]
The moment he saw the young master’s face, which was nodding with a serious expression, a loud laugh burst from Woo Jintae’s mouth.

[P121]
“Puhahaha!”

[P122]
At the same time, the other young prodigies began laughing loudly as well.

[P123]
“Pfft, ha-ha-ha! I almost died trying to hold that in.”

[P124]
“Ha-ha-ha! They don’t know the first thing about martial arts, and they’re talking about the Ten Dragons and Phoenixes?”

[P125]
How long did they laugh?

[P126]
When they finally managed to stop, what they saw was one person staring quietly up at them.

[P127]
“Finished laughing?”

[P128]
At the ‘young master’s’ words, the young prodigies froze.

[P129]
They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that?

[P130]
The chilly silence was broken by Woo Jintae’s dry voice.

[P131]
“And if we have?”

[P132]
The ‘young master’ smiled brightly.

[P133]
“Get down here right now, you fucking sons of bitches. My neck hurts.”

[P134]
* * *

[P135]
Hyuk Mujin asked with an expectant look in his eyes,

[P136]
“Are you going to fight them?”

[P137]
“Depends on what they do.”

[P138]
“Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?”

[P139]
“That would be fine, too. Also, can you see all the spit those bastards sprayed on my face?”

[P140]
“You’re completely drenched.”

[P141]
Hyuk Mujin briskly wiped my face with his sleeve.

[P142]
“What if they don’t apologize?”

[P143]
“They ought to.”

[P144]
“Look at their faces. They’re never going to apologize.”

[P145]
“Then they can get the shit beaten out of them.”

[P146]
“There are women among them, too…”

[P147]
“I believe in gender equality.”

[P148]
“What?”

[P149]
“I beat everyone equally.”

[P150]
Cheongpung, who had been watching blankly, looked at me with sparkling eyes.

[P151]
“Oh. I don’t really understand, but it sounds cool.”

[P152]
“It’s nothing special… Anyway, thanks.”

[P153]
Even if I wanted to say more, I was no longer given the time.

[P154]
The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor.

[P155]
*Tap.*

[P156]
They landed lightly, as befitted First Rate masters. One person stepped forward from among the five as they glared at us.

[P157]
Level 45. He was tall and good-looking. He was also the one who had laughed first.

[P158]
“I…”

[P159]
“Are you the head?”

[P160]
“The head?”

[P161]
“Are you the boss of the five of you?”

[P162]
The man gave a short laugh.

[P163]
“You’d better watch your mouth. If you knew who the people here were, including me…”

[P164]
I smiled back and scanned through their Level windows.

[P165]
“Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?”

[P166]
“…”

[P167]
“…”

[P168]
Five pairs of astonished eyes turned toward me. No—along with Hyuk Mujin and Cheongpung, there were seven pairs of eyes fixed on me.

[P169]
“Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.”

[P170]
“How did you…?”

[P171]
“Did you stick radishes in your ears?”

[P172]
The next moment, my palm struck the man’s cheek.

[P173]
*Smack!*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서오문   | **Five Gates of Shanxi**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 귀문      | **your sect**                                                   |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 133,
  "passed": true,
  "metrics": {
    "source_characters": 5800,
    "translation_characters": 13290,
    "length_ratio": 2.291,
    "source_paragraphs": 170,
    "translation_paragraphs": 173
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀문",
        "preferred": "your sect"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
