# Fidelity Gate — Chapter 122

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
  1|＃122화
  2|
  3|
  4|
  5|정보를 전달함에 있어 중요한 것은 두 가지다. 신속과 정확.
  6|
  7|그것을 위해 정보를 취급하는 문파인 하오문은 지부마다 촘촘한 정보망을 구성해 두었다.
  8|
  9|월화는 그중 산서성에 설치된 삼십여 개 지부에 동원령을 내릴 수 있는 권한을 지니고 있었다.
 10|
 11|“일은? 마무리했어?”
 12|
 13|그녀의 물음에 멀끔한 인상의 중년인, 하오문 정양지부장이 대답했다.
 14|
 15|“시신은 모두 분리해서 옮겨 두었습니다. 항산검문 측 생존자는 더 없었고, 마적 중에 숨이 붙어 있는 놈들이 있더군요.”
 16|
 17|“얼마나?”
 18|
 19|“정확히 마흔일곱입니다.”
 20|
 21|“많이도 살았네. 그중에 몇이나 살릴 수 있어?”
 22|
 23|“지금 보유한 약재로는 서른 정도가 한계입니다.”
 24|
 25|“모두 다 살릴 필요는 없겠지.”
 26|
 27|월화의 한마디에 정양 지부장이 고개를 숙였다.
 28|
 29|“조치하겠습니다.”
 30|
 31|그것으로 살아남은 마적들의 운명이 결정되었다.
 32|
 33|중상을 입었다면 산더미처럼 쌓인 동료들의 곁으로 돌아갈 것이고, 경상을 입었다면 생명을 조금 더 연장시킬 수 있을 것이다.
 34|
 35|물론 치료가 끝나는 즉시 광산이나 투기장의 노예로 팔려 가겠지만.
 36|
 37|“다음. 혼주지부장?”
 38|
 39|“저희 쪽도 문제없습니다.”
 40|
 41|혼주지부장은 얼굴에 검상이 가득한 거한이었다. 그는 철사처럼 빳빳한 턱수염을 긁적이며 말을 이었다.
 42|
 43|“사실 나설 필요도 없더구먼요. 풍양이 죽고 적풍단이 아작 났다는 걸 알았는지 근처에 얼씬도 안 합디다.”
 44|
 45|“당장은 그걸로 충분해. 발 빠르고 입 가벼운 애들로 골라서 소문 퍼트려. 그럼 알아서 내뺄 거야.”
 46|
 47|풍양과 그 수하들을 해치웠다지만 아직 인근에는 상당한 숫자의 마적들이 이리처럼 주변을 어슬렁거리고 있었다.
 48|
 49|항산검문이라는 손쉬운 먹잇감에 이빨을 박기 위해 호시탐탐 때를 노리는 것이다.
 50|
 51|“산서잠룡과 진천검이 풍양을 일격에 때려죽였다. 뭐 이 정도면 놈들도 혼비백산하겠군요.”
 52|
 53|“사실과는 좀 다르긴 한데…… 적당히 양념 쳐. 남의 집 싸움에 우리가 피 흘릴 수는 없잖아?”
 54|
 55|소문의 진위는 중요하지 않다. 태원진가의 두 형제가 풍양과 적풍단으로부터 항산검문을 구했다는 것만 알려지면 된다.
 56|
 57|“어차피 며칠 안에 태원진가가 움직일 거야. 아주 멍청한 놈들이 아니고서야 살고 싶으면 고원으로 돌아가겠지.”
 58|
 59|항산검문의 뒤에 태원진가라는 대호(大虎)가 버티고 있다는 사실이야 곧 널리 퍼질 것이다. 산군의 포효 한 번이면 알아서 나가떨어질 놈들 아닌가.
 60|
 61|“길어도 닷새야. 그때까지 고생 좀 하자고.”
 62|
 63|두 지부장이 고개를 끄덕였다.
 64|
 65|“고생이랄 게 있습니까. 총지부장님 명령인데 당연히 따라야죠.”
 66|
 67|“전 좋습니다. 옆에 고원이 붙어 있어서 그런가, 탁 트여서 말 달리는 재미도 있고.”
 68|
 69|“그럼 다행이고.”
 70|
 71|월화가 피식 웃으며 곰방대를 빨아들였다.
 72|
 73|“저어, 그런데 말입니다.”
 74|
 75|“응?”
 76|
 77|휘하 지부장 중 가장 호전적이고 무공 광으로 평가받는 혼주지부장이 눈을 반짝였다.
 78|
 79|“여기 부상자들한테 듣기로는 풍양 그놈이 단신으로 항산호와 진천검을 쓰러트렸다던데. 사실입니까?”
 80|
 81|“맞아. 나도 직접 보지는 못했지만.”
 82|
 83|“허어, 대단하네요.”
 84|
 85|“대단하지. 단기간에 그렇게 빨리 강해졌다는 점에서 구린내가 진동하지만.”
 86|
 87|절정의 경지는 깨달음의 영역이다. 그때부터는 신체의 단련을 넘어 무리(武理)를 꿰뚫어야 보다 더 높은 경지로 나아갈 수 있는 것이다.
 88|
 89|그러나 불과 얼마 전 항산호 철무백을 상대로 패퇴했던 풍양이다. 제아무리 깨달음이 받쳐 준다 해도 짧은 시일 안에 너무 강해졌다.
 90|
 91|아직 잠력단의 존재를 모르는 월화는 그 부분을 짚었다.
 92|
 93|“뭔가 수를 쓴 게 분명한데…… 자세히 한번 알아봐야겠어.”
 94|
 95|눈치 빠른 정양지부장은 묵례를 취했고, 혼주지부장은 뒤통수를 벅벅 긁었다.
 96|
 97|“물론 풍양, 그 마적 놈도 대단하지만 제가 말씀드린 건 다른 사람입니다.”
 98|
 99|“누구? 아.”
100|
101|“산서잠룡. 대단하지 않습니까? 본 문에서 파악한 바에 의하면 그의 무공은 아직 일류에 불과한데…… 매번 예상을 벗어나는군요.”
102|
103|정보는 객관적 사실이 밑바탕 되어야 한다. 하오문도인 그들은 냉정하게 제삼자 입장에서 정보의 쓰임새를 판단하고, 사람과 상황에 적용시킨다.
104|
105|그런 의미에서 진태경은 골칫덩이였다. 그에 관한 예상은 늘 빗나갔으니까.
106|
107|“그런데 참 신기한 게, 점점 기대가 된다는 거죠.”
108|
109|“기대?”
110|
111|“다음에는 어떤 식으로 우리의 예상을 벗어날까. 뭐 그런 기대 말입니다.”
112|
113|히죽거리던 혼주지부장은 월화의 냉담한 표정에 웃음을 멈췄다.
114|
115|“죄송합니다. 제가 입방정을…….”
116|
117|“잘 아네. 나가서 일 봐.”
118|
119|두 지부장을 쫓아낸 월화는 다시 곰방대를 물었다.
120|
121|달싹이는 입술에서 연기와 함께 아주 작은 목소리가 흘러나왔다.
122|
123|“진태경이라, 진태경.”
124|
125|문득, 언젠가 사부(師傅)와 나눴던 대화가 생각난다.
126|
127|
128|
129|‘그런 자들이 있다. 늘 예측을 벗어나는 자, 정보로 판단할 수 없는 자들이.’
130|
131|‘그럼 어떻게 하죠?’
132|
133|‘판단하지 말고 그저 지켜보아라. 네가 직접 그에 대한 확신을 내릴 수 있을 때까지.’
134|
135|‘그렇게까지 했는데도 확신을 내리지 못한다면요?’
136|
137|‘예측불허. 그런 자가 있다면 언젠가 천하를 움직일 만한 재목이 아니겠느냐?’
138|
139|
140|
141|‘천하를 움직일 재목…….’
142|
143|월화는 곰방대의 재를 털고 전각을 빠져나왔다.
144|
145|어둠이 짙게 내리깔린 밤, 타오르는 횃불을 이정표 삼아 걷던 그녀가 발걸음을 멈춘 곳은 진태경이 머무르는 전각 앞이었다.
146|
147|“거기서 뭐 해요?”
148|
149|전각 앞에 처량하게 쭈그려 앉아 있던 혁무진이 월화를 보고 반색했다.
150|
151|“앗, 오셨습니까?”
152|
153|“대충 일이 마무리되어 가는 중이라 잠깐 들렀어요. 안에 진 공자 있죠?”
154|
155|사실 물어볼 필요도 없는 일이었다. 밖으로 환한 불빛이 새어 나오고 있었으니까.
156|
157|하지만 혁무진은 어두운 얼굴로 고개를 저었다.
158|
159|“안에 없어요?”
160|
161|“아뇨, 계시긴 한데. 그…….”
162|
163|한숨을 푹 내쉰 혁무진이 말을 이었다.
164|
165|“상태가 별로 좋지 않으셔서요. 아까부터 뜻 모를 소리만 중얼거리고 계세요. 보면 소름이 돋는다니까요.”
166|
167|“뜻 모를 소리요?”
168|
169|“네. 혹시 급식이 무슨 뜻인지 아십니까?”
170|
171|“급식이요?”
172|
173|월화는 고개를 갸웃했다. 적지 않은 책을 읽었지만 처음 들어 보는 말이다.
174|
175|“글쎄요. 처음 들어 보는 것 같은데.”
176|
177|“그렇죠? 전 또 제가 무식한 놈이라 모르는 건가 싶었는데.”
178|
179|“그래서요?”
180|
181|“저희 조장님 성격 아시잖아요. 하도 급식, 급식 하시기에 무슨 뜻이냐고 여쭤봤다가 쫓겨났죠.”
182|
183|처량한 얼굴로 이마를 슬슬 문지르는 걸 보니 곱게 쫓아내진 않은 모양이다.
184|
185|‘무슨 일이지?’
186|
187|궁금증을 참지 못한 월화가 문을 두드리려던 그때였다.
188|
189|문틈 사이로 새어 나오는 누군가의 음산한 목소리.
190|
191|“급식, 고딩, 철컹, 철컹…….”
192|
193|순간 소름이 쭉 돋은 월화는 자신도 모르게 뒷걸음질 쳤다.
194|
195|“바, 방금 들었어요?”
196|
197|“아까부터 저 상태라니까요.”
198|
199|그 와중에도 들려오는 의미 불명의 중얼거림에 그녀가 주춤주춤 물러났다.
200|
201|“다, 다음에 올게요.”
202|
203|다시 한번 깨달았다.
204|
205|진태경이라는 인간은 여전히 예측불허라는 사실을.
206|
207|
208|
209|* * *
210|
211|
212|
213|이틀이라는 시간이 쏜살같이 흘렀다. 이소월은 그날 밤 이후 다시 찾아오지 않았고, 나도 굳이 전각을 나서지 않았다.
214|
215|새로 얻은 열양지기를 다루는 데에 대부분의 시간을 보내는 와중에도 불쑥불쑥 그녀가 남긴 마지막 말이 생각났다.
216|
217|
218|
219|‘혼인은 인륜지대사(人倫之大事)이니 천천히 생각해 보세요.’
220|
221|
222|
223|당시에는 너무 당황해서 입만 벙긋거렸다. 여자에게 먼저 프러포즈를, 그것도 나보다 한참 어려 보이는 여자애한테 받을 줄이야.
224|
225|비록 거래라는 단어를 쓸 정도로 삭막한 정략혼 제의였지만 프러포즈는 프러포즈다.
226|
227|하지만 더 큰 충격이 남아 있었다.
228|
229|‘열일곱 살이라니. 이거 실화냐.’
230|
231|고등학교 1학년이면 한창 급식 먹을 나이다.
232|
233|늦둥이 동생인 하연이보다 두 살이나 어리고, 나와는 무려 열 살 차이인 것이다.
234|
235|‘역시 무림…….’
236|
237|중학교 때 결혼하고 고등학생 때 부모 되어도 이상하지 않은 세상이다. 오히려 이 나이 먹도록 결혼 안 한 태원진가 삼 형제가 별종으로 보일 정도다.
238|
239|아니, 잠깐만.
240|
241|“뭘 그렇게 보냐?”
242|
243|내 시선을 눈치챈 진무경이 퉁명스럽게 물었다. 풍양으로부터 상당한 부상을 입었던 그는 이제 스스로 거동이 가능할 정도로 회복되어 있었다.
244|
245|‘그러고 보니…….’
246|
247|진무경의 혼인 여부에 대해서는 한 번도 들어 본 적이 없다.
248|
249|나는 설마 하는 마음에 입을 열었다.
250|
251|“혹시나 해서 물어보는 건데.”
252|
253|“뭐.”
254|
255|“혼인했어?”
256|
257|푸웁!
258|
259|내 얼굴에 찻물을 뱉은 진무경이 황급히 외쳤다.
260|
261|“무, 무슨 헛소리를!”
262|
263|“아니면 말지. 왜 이렇게 당황해?”
264|
265|뜻밖의 세수를 당한 나는 소매로 얼굴을 닦으며 질문을 이어 갔다.
266|
267|“왜 안 했는데?”
268|
269|잠깐 당황하는가 싶던 진무경이 순순히 대답했다.
270|
271|“무공 익히기에도 바쁘다. 내게 여인은 사치야.”
272|
273|“그렇게 말하니까 되게 검소하게 느껴지네.”
274|
275|“네놈 같은 음탕한 한량과 동급으로 보지 마라. 그건 나에 대한 모욕이야.”
276|
277|“…….”
278|
279|음탕하긴 시벌, 27년 동안 모태 솔로로 살았던 나다.
280|
281|연애를 사치라고 한다면 나는 자린고비 그 자체다. 약간 다른 점이 있다면 자린고비는 굴비를 쳐다보며 밥을 먹었지만 내게는 USB가 있었다는 것 정도지.
282|
283|“뭐지, 그 표정은? 굉장히 슬퍼 보이는데.”
284|
285|“지나간 삶에 대한 후회랄까.”
286|
287|“드디어 사람이 되어 가는군.”
288|
289|지나간 삶에 대한 해석이 다른 것 같은데…… 그래, 너 좋을 대로 해석해라.
290|
291|“그런데 갑자기 혼인에 관해서는 왜 물어본 것이냐? 너도 뻔히 아는 사실을.”
292|
293|“아, 항산검문주가 나랑 혼인하자고 그래서.”
294|
295|“푸웁!”
296|
297|“……후, 작작 뱉어라.”
298|
299|두 번째 찻물을 닦아 내는 사이 평정심을 되찾은 진무경이 입을 열었다.
300|
301|“항산검문주가?”
302|
303|“어. 이틀 전에 그러더라고.”
304|
305|“도대체 왜 너 같은 놈과…… 아, 당연히 정략혼이겠군.”
306|
307|“…….”
308|
309|거, 틀린 말은 아닌데 상당히 기분 나쁘네. 이제 나 정도면 무림에서나 현실에서나 일등 신랑감 아닌가?
310|
311|“그래서, 할 생각이냐?”
312|
313|“당연히 아니지. 한참 어린 애랑 어떻게 혼인을 해.”
314|
315|“고작 약관인 놈이 못 하는 말이 없구나.”
316|
317|몸은 스물이지만 정신은 스물일곱이다, 이놈아.
318|
319|그리고 이소월의 제의에 대한 내 대답은 이미 정해진 지 오래였다.
320|
321|사랑하는 사람이 있는데 두 집 살림을 차릴 순 없는 법. 지금 내게는 오직 한 사람뿐이다.
322|
323|‘송이 씨는 지금 뭘 하고 있을까.’
324|
325|상상만 해도 행복하다. 흐뭇하게 웃으며 찻잔을 기울이는 나를 진무경이 해괴한 표정으로 바라봤다.
326|
327|“역겨운 표정이군.”
328|
329|“아무튼, 여러 가지 이유로 혼인은 거절.”
330|
331|“잘 생각했다. 적어도 정략혼이라면 우리가 얻는 것이 있어야 하는 법인데, 마음도 없는 상대와 혼인하면서 아무것도 얻지 못한다면 정략혼을 할 이유가 없지.”
332|
333|무공밖에 모르는 바보인 줄 알았는데, 가끔 보면 제법 날카로운 현실주의자가 된다.
334|
335|“그리고 무슨 제의를 하더라도 큰형님이 있는 한 어림없다. 널 정략혼으로 엮으실 분은 아니니까.”
336|
337|“저쪽에서도 꽤 큰 제의를 하긴 했어.”
338|
339|“흠. 뭘 주겠다더냐?”
340|
341|진무경이 심드렁한 얼굴로 찻잔을 기울였다.
342|
343|“혈랑검법, 혈랑보법. 그리고 수라멸권.”
344|
345|푸웁!
346|
347|“……아, 시바.”
348|
349|이번에는 닦을 시간도 없다. 진무경이 내 멱살을 잡고 탈탈 털었다.
350|
351|“당장 혼인해!”
```

## Assembled English

```markdown
[P1]
# Chapter 122

[P2]
Two things mattered when conveying information: speed and accuracy.

[P3]
To that end, the Lower District Sect, which dealt in information, had established a dense information network around each of its branches.

[P4]
Wolhwa had the authority to issue mobilization orders to the more than thirty branches established throughout Shanxi Province.

[P5]
“How did it go? Is everything taken care of?”

[P6]
A clean-cut middle-aged man answered her. He was the Jeongyang Branch Leader of the Lower District Sect.

[P7]
“We separated and moved all the corpses. There were no more survivors from the Mount Heng Sword Sect, but some of the mounted bandits were still breathing.”

[P8]
“How many?”

[P9]
“Exactly forty-seven.”

[P10]
“Quite a lot survived. How many can we save?”

[P11]
“With the medicine we have on hand, thirty at most.”

[P12]
“We don’t need to save every last one.”

[P13]
At Wolhwa’s words, the Jeongyang Branch Leader bowed his head.

[P14]
“I’ll see to it.”

[P15]
That decided the surviving mounted bandits’ fates.

[P16]
Those with severe injuries would rejoin the mountain-high pile of their comrades, while those with minor injuries might have their lives extended a little longer.

[P17]
Of course, the moment their treatment was finished, they would be sold as slaves to the mines or fighting pits.

[P18]
“Next. Honju Branch Leader?”

[P19]
“No problems on our end, either.”

[P20]
The Honju Branch Leader was a hulking man whose face was covered in sword scars. He scratched his stiff, wirelike beard and continued.

[P21]
“Truth is, we didn’t even need to step in. They must’ve heard that Pung Yang was dead and the Red Wind Band had been smashed, because they didn’t come anywhere near the area.”

[P22]
“For now, that’s enough. Pick your fastest, most loose-lipped people and have them spread the rumor. They’ll run away on their own.”

[P23]
Although Pung Yang and his subordinates had been dealt with, a considerable number of mounted bandits were still prowling around the area like wolves.

[P24]
They were watching for a chance to sink their teeth into the easy prey that was the Mount Heng Sword Sect.

[P25]
“The Sleeping Dragon of Shanxi and the Heaven Shaking Sword beat Pung Yang to death with a single blow. Something like that should scare them out of their wits.”

[P26]
“It’s not exactly true, but… spice it up as much as you need to. We can’t shed blood over someone else’s fight, can we?”

[P27]
Whether the rumor was true didn’t matter. All that mattered was spreading the word that the two brothers of the Jin Family of Taiyuan had rescued the Mount Heng Sword Sect from Pung Yang and the Red Wind Band.

[P28]
“Besides, the Jin Family of Taiyuan will make its move within a few days. Unless they’re complete idiots, they’ll return to Gaoyuan if they want to live.”

[P29]
Word would soon spread far and wide that the great tiger known as the Jin Family of Taiyuan stood behind the Mount Heng Sword Sect. Wouldn’t one roar from the mountain king be enough to send those bandits running?

[P30]
“Five days at most. Let’s hold out until then.”

[P31]
The two Branch Leaders nodded.

[P32]
“It’s hardly a hardship. These are the Chief Branch Leader’s orders. Of course we’ll obey.”

[P33]
“I’m fine with it. Maybe it’s because Gaoyuan is right next door, but there’s something fun about riding across all this open land.”

[P34]
“Glad to hear it.”

[P35]
Wolhwa let out a short laugh and drew on her long-stemmed tobacco pipe.

[P36]
“Um, by the way…”

[P37]
“Yes?”

[P38]
The Honju Branch Leader, considered the most aggressive and martial-arts-obsessed of her subordinates, had a bright gleam in his eyes.

[P39]
“I heard from the wounded that bastard Pung Yang took down the Tiger of Mount Heng and the Heaven Shaking Sword all by himself. Is that true?”

[P40]
“It is. Though I didn’t see it myself.”

[P41]
“Wow. That’s impressive.”

[P42]
“It is. Though the fact that he grew so strong so quickly reeks of something fishy.”

[P43]
The Peak realm was a domain of enlightenment. From that point onward, a martial artist had to go beyond physical training and see through the principles of martial arts in order to advance to a higher realm.

[P44]
But Pung Yang had been defeated by Cheol Mubaek, the Tiger of Mount Heng, only a short while ago. No matter how much enlightenment supported him, he had become far too strong in far too little time.

[P45]
Wolhwa, who still knew nothing of the Temporary Strength Pill, focused on that point.

[P46]
“He definitely used some kind of trick… I’ll have to look into it more closely.”

[P47]
The quick-witted Jeongyang Branch Leader gave a silent bow, while the Honju Branch Leader vigorously scratched the back of his head.

[P48]
“Of course, Pung Yang, that mounted-bandit bastard, is impressive too. But I was talking about someone else.”

[P49]
“Who? Ah.”

[P50]
“The Sleeping Dragon of Shanxi. Isn’t he incredible? According to what our sect has determined, his martial arts are still only First Rate, but he defies our expectations every time.”

[P51]
Information had to be based on objective facts. As members of the Lower District Sect, they coolly judged how information could be used from a third-party perspective, then applied it to people and situations.

[P52]
In that regard, Jin Taekyung was a headache. Every prediction they made about him proved wrong.

[P53]
“But the strange thing is, I’m starting to look forward to it more and more.”

[P54]
“Look forward to what?”

[P55]
“Wondering how he’ll defy our expectations next time. That kind of anticipation.”

[P56]
The Honju Branch Leader had been grinning, but his smile vanished at Wolhwa’s impassive expression.

[P57]
“My apologies. I was running my mouth…”

[P58]
“At least you know it. Go outside and handle your work.”

[P59]
After driving the two Branch Leaders out, Wolhwa put her pipe back between her lips.

[P60]
A tiny voice slipped from her barely moving lips along with the smoke.

[P61]
“Jin Taekyung. Jin Taekyung.”

[P62]
She suddenly remembered a conversation she had once shared with her Master.

[P63]
*There are people like that. People who always defy prediction. People who cannot be judged through information.*

[P64]
*Then what should I do?*

[P65]
*Do not judge them. Simply watch until you can reach your own conclusion about them.*

[P66]
*What if I still can’t reach a conclusion after all that?*

[P67]
*Unpredictable. If such a person exists, wouldn’t they possess the makings of someone who might one day move the world?*

[P68]
*The makings of someone who could move the world…*

[P69]
Wolhwa tapped the ash from her pipe and left the pavilion.

[P70]
Night had fallen thick and dark. Using the blazing torches as guideposts, she walked until she stopped in front of the pavilion where Jin Taekyung was staying.

[P71]
“What are you doing out here?”

[P72]
Hyuk Mujin, who had been squatting miserably in front of the pavilion, brightened when he saw Wolhwa.

[P73]
“Oh, you’re here?”

[P74]
“Things are mostly wrapped up, so I stopped by for a moment. Young Master Jin is inside, right?”

[P75]
In truth, there was no need to ask. Bright light was spilling out through the pavilion.

[P76]
But Hyuk Mujin shook his head, his expression grim.

[P77]
“He isn’t inside?”

[P78]
“No, he is. It’s just…”

[P79]
Hyuk Mujin let out a deep sigh before continuing.

[P80]
“His condition isn’t very good. He’s been muttering things that make no sense for a while now. I get goose bumps just looking at him.”

[P81]
“Things that make no sense?”

[P82]
“Yes. Do you happen to know what ‘school lunch’ means?”[^1]

[P83]
“School lunch?”

[P84]
Wolhwa tilted her head. She had read plenty of books, but she had never heard the expression before.

[P85]
“I don’t think so. It’s new to me.”

[P86]
“Right? I thought maybe I was just too ignorant to know.”

[P87]
“And then?”

[P88]
“You know what our Squad Leader is like. He kept saying ‘school lunch, school lunch,’ so I asked him what it meant. Then he threw me out.”

[P89]
Judging by the miserable look on his face as he rubbed his forehead, he hadn’t been shown the door gently.

[P90]
*What happened?*

[P91]
Unable to contain her curiosity, Wolhwa was about to knock when an eerie voice seeped through the gap in the door.

[P92]
“School lunch, high schooler, clank, clank…”

[P93]
Goose bumps prickled across Wolhwa’s skin, and she involuntarily stepped back.

[P94]
“D-Did you hear that?”

[P95]
“He’s been like that for a while.”

[P96]
Even as the incomprehensible muttering continued, she backed away in hesitant steps.

[P97]
“I-I’ll come back another time.”

[P98]
She realized it once again.

[P99]
The man named Jin Taekyung was still utterly unpredictable.

[P100]
* * *

[P101]
Two days flew by in the blink of an eye. Lee Seowol did not come back after that night, and I didn’t bother leaving the pavilion, either.

[P102]
Even as I spent most of my time learning to control my newly acquired Scorching Yang Qi, her final words kept returning to me.

[P103]
*Marriage is one of life’s great human obligations, so take your time thinking it over.*

[P104]
I had been so flustered at the time that I could only open and close my mouth.

[P105]
Who would have thought a woman would propose to me first—and a girl who looked so much younger than me, at that?

[P106]
Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—a proposal was still a proposal.

[P107]
The greater shock, however, was still to come.

[P108]
*Seventeen years old? Is this for real?*

[P109]
A first-year high school student was right in the prime school-lunch-eating years.

[P110]
She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me.

[P111]
*That’s the Murim for you…*

[P112]
This was a world where getting married in middle school and becoming a parent in high school wouldn’t even be strange. If anything, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age.

[P113]
No, wait a second.

[P114]
“What are you staring at?”

[P115]
Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own.

[P116]
*Come to think of it…*

[P117]
I had never heard whether Jin Mukyung was married.

[P118]
I opened my mouth, half expecting the worst.

[P119]
“Just asking in case.”

[P120]
“What?”

[P121]
“Are you married?”

[P122]
Pffft!

[P123]
Jin Mukyung spat tea into my face and hurriedly shouted.

[P124]
“W-What kind of nonsense is that?”

[P125]
“If you’re not, then you’re not. Why are you so flustered?”

[P126]
After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions.

[P127]
“Why haven’t you married?”

[P128]
Jin Mukyung seemed flustered for a moment, then answered readily.

[P129]
“I’m too busy training in martial arts. Women are a luxury to me.”

[P130]
“You make it sound downright frugal.”

[P131]
“Don’t lump me in with a lecherous idler like you. That’s an insult to me.”

[P132]
“…”

[P133]
Lecherous, my ass. I had spent all twenty-seven years of my life single.

[P134]
If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2]

[P135]
“What’s with that expression? You look incredibly sad.”

[P136]
“Call it regret over the life I’ve lived.”

[P137]
“At last, you’re becoming human.”

[P138]
He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted.

[P139]
“But why did you suddenly ask about marriage? It’s something you already know perfectly well.”

[P140]
“Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.”

[P141]
Pffft!

[P142]
“…For fuck’s sake. Stop spitting.”

[P143]
As I wiped away the second mouthful of tea, Jin Mukyung regained his composure.

[P144]
“The Sect Leader of the Mount Heng Sword Sect?”

[P145]
“Yeah. She said it two days ago.”

[P146]
“Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.”

[P147]
“…”

[P148]
He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world?

[P149]
“So, are you thinking of doing it?”

[P150]
“Of course not. How could I marry a girl so much younger than me?”

[P151]
“You’re barely twenty, and you say things like that.”

[P152]
*My body is twenty, but my mind is twenty-seven, you bastard.*

[P153]
Besides, I had decided on my answer to Lee Seowol’s proposal long ago.

[P154]
You can’t set up two households when there’s someone you love. There was only one person in my heart right now.

[P155]
*What could Song-i be doing right now?*

[P156]
Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression.

[P157]
“What a disgusting look.”

[P158]
“Anyway, I’m turning down the marriage for various reasons.”

[P159]
“You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.”

[P160]
I had thought he was a fool who knew nothing but martial arts, but every now and then, he became a surprisingly sharp realist.

[P161]
“And no matter what they offer, it’s out of the question as long as our eldest brother is around. He isn’t the sort of man who would bind you through a political marriage.”

[P162]
“They did make a pretty substantial offer, though.”

[P163]
“Hm. What did they say they would give you?”

[P164]
Jin Mukyung tilted his teacup with an uninterested expression.

[P165]
“The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.”

[P166]
Pffft!

[P167]
“…Ah, fuck.”

[P168]
This time, I didn’t even have time to wipe my face. Jin Mukyung grabbed me by the collar and shook me hard.

[P169]
“Marry her right now!”

[P170]
[^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail.
[^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.
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
# Chapter 122

[P2]
There were two things that mattered when conveying information: speed and accuracy.

[P3]
To that end, the Lower District Sect, a sect that dealt in information, had built an extensive information network at every branch.

[P4]
Wolhwa had the authority to issue mobilization orders to the more than thirty branches established throughout Shanxi Province.

[P5]
“How’s it going? Are you finished?”

[P6]
A clean-cut middle-aged man answered her question. He was the Jeongyang Branch Leader of the Lower District Sect.

[P7]
“We separated and moved all the corpses. There were no more survivors from the Mount Heng Sword Sect, but some of the mounted bandits were still breathing.”

[P8]
“How many?”

[P9]
“Exactly forty-seven.”

[P10]
“That’s quite a lot who survived. How many of them can we save?”

[P11]
“With the medicine we currently have, thirty at most.”

[P12]
“We don’t need to save every last one.”

[P13]
At Wolhwa’s words, the Jeongyang Branch Leader lowered his head.

[P14]
“I’ll take care of it.”

[P15]
That decided the surviving mounted bandits’ fates.

[P16]
Those with serious injuries would rejoin the mountain-high pile of their comrades, while those with minor injuries might live a little longer.

[P17]
Of course, the moment their treatment was finished, they would be sold as slaves to the mines or fighting pits.

[P18]
“Next. Honju Branch Leader?”

[P19]
“No problems on our end, either.”

[P20]
The Honju Branch Leader was a hulking man whose face was covered in sword scars. He scratched at his stiff, wirelike beard and continued.

[P21]
“Truth is, we didn’t even need to step in. They must’ve heard Pung Yang was dead and the Red Wind Band had been wrecked, because they didn’t come anywhere near the area.”

[P22]
“For now, that’s enough. Pick the swiftest and most loose-lipped people you have and spread the rumor. They’ll run away on their own.”

[P23]
Although Pung Yang and his subordinates had been dealt with, a considerable number of mounted bandits were still prowling around the area like wolves.

[P24]
They were waiting for an opportunity to sink their teeth into the easy prey that was the Mount Heng Sword Sect.

[P25]
“The Sleeping Dragon of Shanxi and the Heaven Shaking Sword beat Pung Yang to death with a single blow. If the others hear that, they’ll be scared out of their minds.”

[P26]
“It’s not exactly true, but… Add enough seasoning. We can’t bleed for someone else’s fight, can we?”

[P27]
The truth of the rumor was unimportant. All that mattered was that people learned the two brothers of the Jin Family of Taiyuan had rescued the Mount Heng Sword Sect from Pung Yang and the Red Wind Band.

[P28]
“Besides, the Jin Family of Taiyuan will make a move within a few days. Unless they’re complete idiots, they’ll return to the plateau if they want to live.”

[P29]
The fact that the great tiger known as the Jin Family of Taiyuan stood behind the Mount Heng Sword Sect would soon spread far and wide. Wouldn’t one roar from the mountain king be enough to send those bandits running?

[P30]
“Five days at most. Let’s put in some effort until then.”

[P31]
The two Branch Leaders nodded.

[P32]
“What effort? It’s the Chief Branch Leader’s order. Of course we have to follow it.”

[P33]
“I like it. Maybe it’s because the plateau is right next door, but there’s something fun about riding across all this open land.”

[P34]
“Then that’s a relief.”

[P35]
Wolhwa gave a short laugh and drew on her long-stemmed tobacco pipe.

[P36]
“Um, by the way…”

[P37]
“Yes?”

[P38]
The Honju Branch Leader, considered the most aggressive and martial-arts-obsessed of her subordinates, had a bright gleam in his eyes.

[P39]
“I heard from the wounded that bastard Pung Yang took down the Tiger of Mount Heng and the Heaven Shaking Sword all by himself. Is that true?”

[P40]
“It is. Though I didn’t see it myself.”

[P41]
“Wow. That’s impressive.”

[P42]
“It is impressive. The fact that he grew so strong so quickly reeks of something fishy, though.”

[P43]
The Peak realm was a domain of enlightenment. From that point onward, a martial artist had to see through the principles of martial arts rather than merely train the body in order to advance to a higher realm.

[P44]
But Pung Yang had been defeated by Cheol Mubaek, the Tiger of Mount Heng, only a short while ago. No matter how much enlightenment supported him, he had become far too strong in far too little time.

[P45]
Wolhwa, who still knew nothing of the Temporary Strength Pill, focused on that point.

[P46]
“He definitely used some kind of trick… I’ll have to look into it more closely.”

[P47]
The quick-witted Jeongyang Branch Leader offered a silent bow, while the Honju Branch Leader vigorously scratched the back of his head.

[P48]
“Of course, Pung Yang, that mounted-bandit bastard, is impressive too. But I was talking about someone else.”

[P49]
“Who? Ah.”

[P50]
“The Sleeping Dragon of Shanxi. Isn’t he incredible? According to what our sect has determined, his martial arts are still only First Rate, but he keeps defying our expectations.”

[P51]
Information had to be based on objective facts. As members of the Lower District Sect, they coolly judged how information could be used from a third-party perspective, then applied it to people and situations.

[P52]
In that regard, Jin Taekyung was a headache. Every prediction concerning him had been wrong.

[P53]
“But the strange thing is, I’m starting to look forward to it more and more.”

[P54]
“Look forward to what?”

[P55]
“Wondering how he’ll defy our expectations next time. That kind of anticipation.”

[P56]
The Honju Branch Leader had been grinning broadly, but he stopped smiling when he saw Wolhwa’s impassive expression.

[P57]
“I’m sorry. I was running my mouth.”

[P58]
“At least you know it. Go outside and handle your work.”

[P59]
After driving the two Branch Leaders out, Wolhwa put her pipe back between her lips.

[P60]
A tiny voice slipped from her barely moving lips along with the smoke.

[P61]
“Jin Taekyung. Jin Taekyung.”

[P62]
She suddenly remembered a conversation she had once shared with her Master.

[P63]
*There are people like that. People who always defy prediction, people who cannot be judged through information.*

[P64]
*Then what should I do?*

[P65]
*Don’t judge them. Just watch them until you can reach your own conclusion about them.*

[P66]
*What if I still can’t reach a conclusion after going that far?*

[P67]
*Unpredictable. If there is such a person, wouldn’t they be the sort of talent capable of moving the world someday?*

[P68]
*A talent capable of moving the world…*

[P69]
Wolhwa tapped the ash from her pipe and left the pavilion.

[P70]
Night had fallen thick and dark. Guided by blazing torches that served as landmarks, she walked until she stopped in front of the pavilion where Jin Taekyung was staying.

[P71]
“What are you doing out here?”

[P72]
Hyuk Mujin, who had been sitting miserably in a crouch before the pavilion, brightened when he saw Wolhwa.

[P73]
“Oh, you’re here?”

[P74]
“I’ve mostly finished dealing with things, so I stopped by for a moment. Young Master Jin is inside, right?”

[P75]
In truth, there was no need to ask. Bright light was spilling out through the pavilion.

[P76]
But Hyuk Mujin shook his head with a grim expression.

[P77]
“He isn’t inside?”

[P78]
“No, he is. It’s just that…”

[P79]
Hyuk Mujin let out a deep sigh before continuing.

[P80]
“His condition isn’t very good. He’s been muttering things that make no sense for a while now. I get goose bumps just looking at him.”

[P81]
“Things that make no sense?”

[P82]
“Yes. Do you happen to know what ‘school lunch’ means?”[^1]

[P83]
“School lunch?”

[P84]
Wolhwa tilted her head. She had read a considerable number of books, but it was the first time she had ever heard the word used that way.

[P85]
“I don’t think so. It sounds unfamiliar.”

[P86]
“Right? I wondered if I was just too ignorant to know.”

[P87]
“And then?”

[P88]
“You know what our Squad Leader is like. He kept saying ‘school lunch, school lunch,’ so I asked him what it meant. Then I got kicked out.”

[P89]
Judging by the way Hyuk Mujin miserably rubbed his forehead, it seemed he had not been politely shown the door.

[P90]
*What happened?*

[P91]
Wolhwa was just about to knock when an eerie voice seeped through the gap in the door.

[P92]
“School lunch, high schooler, clank, clank…”

[P93]
A chill ran over Wolhwa, and she took a step backward without realizing it.

[P94]
“D-Did you hear that?”

[P95]
“He’s been like that for a while.”

[P96]
Even as the incomprehensible muttering continued, she slowly backed away.

[P97]
“I-I’ll come another time.”

[P98]
She realized it once again.

[P99]
The man named Jin Taekyung was still utterly unpredictable.

[P100]
* * *

[P101]
Two days flew by in the blink of an eye. Lee Seowol did not come back after that night, and I didn’t bother leaving the pavilion, either.

[P102]
Even while spending most of my time learning to control the newly acquired Scorching Yang Qi, her final words kept coming back to me.

[P103]
*Marriage is one of life’s great human obligations, so take your time thinking it over.*

[P104]
I had been so flustered at the time that I could only open and close my mouth.

[P105]
Who would have thought I’d receive a proposal from a woman first—and from a girl who looked so much younger than me, at that?

[P106]
Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—it was still a proposal.

[P107]
But there was an even greater shock waiting for me.

[P108]
*Seventeen years old? Is this for real?*

[P109]
A first-year high school student was right in the prime school-lunch-eating years.

[P110]
She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me.

[P111]
*That’s the Murim for you…*

[P112]
Getting married in middle school and becoming a parent in high school wouldn’t even be strange in this world. In fact, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age.

[P113]
No, wait a second.

[P114]
“What are you staring at?”

[P115]
Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own.

[P116]
*Come to think of it…*

[P117]
I had never heard whether Jin Mukyung was married.

[P118]
I opened my mouth, half expecting the worst.

[P119]
“Just asking in case.”

[P120]
“What?”

[P121]
“Are you married?”

[P122]
Pffft!

[P123]
Jin Mukyung spat tea into my face and hurriedly shouted.

[P124]
“What kind of nonsense are you talking about?”

[P125]
“If you’re not, then you’re not. Why are you so flustered?”

[P126]
After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions.

[P127]
“Why aren’t you?”

[P128]
Jin Mukyung looked flustered for a moment, then answered readily.

[P129]
“I’m too busy training in martial arts. Women are a luxury to me.”

[P130]
“You make it sound downright frugal.”

[P131]
“Don’t lump me in with a lecherous idler like you. That’s an insult to me.”

[P132]
“…”

[P133]
Lecherous, my ass. I had spent twenty-seven years as a lifelong single.

[P134]
If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2]

[P135]
“What’s with that expression? You look incredibly sad.”

[P136]
“Maybe it’s regret over the life I’ve lived.”

[P137]
“At last, you’re becoming a human being.”

[P138]
He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted.

[P139]
“But why did you suddenly ask about marriage? It’s something you already know perfectly well.”

[P140]
“Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.”

[P141]
Pffft!

[P142]
“…For fuck’s sake. Stop spitting.”

[P143]
While I wiped away the second mouthful of tea, Jin Mukyung regained his composure and spoke.

[P144]
“The Sect Leader of the Mount Heng Sword Sect?”

[P145]
“Yeah. She said it two days ago.”

[P146]
“Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.”

[P147]
“…”

[P148]
He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world?

[P149]
“So, are you thinking of doing it?”

[P150]
“Of course not. How could I marry a girl so much younger than me?”

[P151]
“You’re barely twenty, and you say things like that.”

[P152]
*My body is twenty, but my mind is twenty-seven, you bastard.*

[P153]
Besides, I had decided on my answer to Lee Seowol’s proposal a long time ago.

[P154]
You can’t set up two households when there’s someone you love. There was only one person in my heart right now.

[P155]
*What could Song-i be doing right now?*

[P156]
Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression.

[P157]
“What a disgusting look.”

[P158]
“Anyway, I’m turning down the marriage for various reasons.”

[P159]
“You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.”

[P160]
I had thought he was a fool who knew nothing but martial arts, but every now and then, he turned into a surprisingly sharp realist.

[P161]
“And no matter what she offers, it’s out of the question as long as our eldest brother is around. He isn’t the sort of person who’d arrange a political marriage for you.”

[P162]
“They did make a pretty substantial offer, though.”

[P163]
“Hm. What did she say they would give you?”

[P164]
Jin Mukyung tilted his teacup with an uninterested expression.

[P165]
“The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.”

[P166]
Pffft!

[P167]
“…Ah, fuck.”

[P168]
This time, I didn’t even have time to wipe it away. Jin Mukyung grabbed me by the collar and shook me hard.

[P169]
“Marry her right now!”

[P170]
[^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail.
[^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 지부장    | **Branch Leader**                            |
| 사부     | **Master**                                   |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 122,
  "passed": true,
  "metrics": {
    "source_characters": 5544,
    "translation_characters": 13441,
    "length_ratio": 2.424,
    "source_paragraphs": 169,
    "translation_paragraphs": 170
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "보법",
        "preferred": "manoeuvre technique / footwork technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "중상",
        "preferred": "Severe Injury"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "조장",
        "preferred": "Captain"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "자린고비",
        "romanization": "jaringobi"
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
