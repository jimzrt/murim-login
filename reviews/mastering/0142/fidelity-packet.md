# Fidelity Gate — Chapter 142

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
  1|＃142화
  2|
  3|
  4|
  5|“화산파 속가제자 이풍, 청풍 사숙(師叔)께 인사 올립니다.”
  6|
  7|자하신공과 매화검법. 마지막으로 이풍의 입에서 흘러나온 한 단어, 사숙.
  8|
  9|이 믿기지 않는 상황에 공일혁의 얼굴이 시커멓게 물들었다.
 10|
 11|‘그럼 정말 저놈이?’
 12|
 13|검성의 친손자는 아니더라도 한 가지는 확실하다.
 14|
 15|어리둥절한 얼굴로 허리만 꾸벅꾸벅 숙이는 저 얼간이가 검성 매종학의 모든 것을 물려받은 후인(後人)이라는 것.
 16|
 17|“이, 이럴 리가 없는데. 이건 정말 말도 안 되는…….”
 18|
 19|공일혁이 더듬거리며 현실을 부정하던 그때. 간드러진 목소리가 귓가에 닿았다.
 20|
 21|“공 대협.”
 22|
 23|“아, 도지휘동지.”
 24|
 25|홍진을 발견한 공일혁의 안색이 한결 밝아졌다.
 26|
 27|종남파는 관(官)과의 연계를 통해 여러 가지 사업을 벌이고 있었고, 홍진은 그 과정에서 알게 된 산서성의 권력자였다.
 28|
 29|이 곤경에서 그에게 구원의 손길을 내밀 수 있는 유일한 사람이기도 하다.
 30|
 31|“이게 어떻게 된 일인가요?”
 32|
 33|홍진의 부드러운 목소리에 공일혁의 마음이 편안해졌다.
 34|
 35|“제가 잠시 착각한 모양입니다.”
 36|
 37|“착각이라니, 무슨 착각이요?”
 38|
 39|“그저 검성의 이름을 팔고 다니는 사기꾼 정도로 생각했는데…….”
 40|
 41|“글쎄요, 전 무공 쪽은 영 문외한이지만 사기꾼처럼 보이지는 않던데요?”
 42|
 43|“야, 약간의 오해가 있었던 것뿐입니다.”
 44|
 45|“오해라…….”
 46|
 47|나지막이 읊조리던 홍진이 공일혁을 빤히 바라봤다.
 48|
 49|“공 대협.”
 50|
 51|“예, 도지휘동지.”
 52|
 53|“내가 왜 공 대협을 비롯한 종남파의 분들을 이 자리에 초대했는지 알아요?”
 54|
 55|“압니다, 잘 알지요.”
 56|
 57|이유는 두 가지다.
 58|
 59|첫 번째로는 산서 성주이자 황족인 상산왕과 안면을 트고 새로 벌이는 사업의 재가를 받기 위해서.
 60|
 61|두 번째는 홍진의 정적인 이풍의 콧대를 바짝 눌러 주기 위해서다.
 62|
 63|“그런데 공 대협도 알다시피 내가 근래 좀 바빴거든요. 그러다 보니 경황이 없어서 전하께 다른 손님이 오신다는 말씀을 못 드렸네?”
 64|
 65|“그러시군요.”
 66|
 67|콧소리가 빠진 목소리는 건조하기만 할 따름이었다. 공일혁이 불안한 얼굴로 물었다.
 68|
 69|“한데 갑자기 그 말씀은 왜…….”
 70|
 71|“오늘은 이만 가 줬으면 해요.”
 72|
 73|“예?”
 74|
 75|“아무래도 불청객이 있으면 전하께서 심기가 불편하시지 않겠어요?”
 76|
 77|명백한 축객령이었다. 거기에 더해 불청객이라는 말까지.
 78|
 79|공일혁이 항변했다.
 80|
 81|“불청객이라니요, 도지휘동지. 그게 대체 무슨 말씀이십니까?”
 82|
 83|“어머, 두 번 말해야 하나요? 앞서 했던 말 그대로예요. 전하께 미처 말씀드리지 못했어요.”
 84|
 85|홍진은 본래 내관(內官)이다. 상산왕이 갓난아기였던 시절부터 옆을 지켰고 덕분에 산서성부의 실세이자 군부 이인자인 도지휘동지라는 자리까지 꿰찼다.
 86|
 87|이처럼 어린 왕의 총애를 한 몸에 받는 그가 고작 미리 말을 못 했다는 이유로 손님을 돌려보낸다니?
 88|
 89|“저, 저는 도지휘동지께서 무슨 말씀을 하시는 건지 이해가 잘…….”
 90|
 91|당황한 공일혁을 향해 홍진이 싱긋 웃어 보였다.
 92|
 93|“공 대협.”
 94|
 95|“예.”
 96|
 97|“그렇게 안 봤는데, 머리가 좀 나쁘네?”
 98|
 99|“……예?”
100|
101|“아니면 눈치가 없는 건가?”
102|
103|갑작스러운 폭언에 사방이 고요해졌다. 공일혁을 비롯한 종남삼수의 다른 두 사람이 주먹을 부르르 떨었다.
104|
105|“말씀이 과하시군요.”
106|
107|“어머, 그렇게 느꼈다면 내 의도를 제대로 파악한 거예요. 일부러 좀 과하게 한 면이 없잖아 있거든.”
108|
109|“도지휘동지!”
110|
111|“목소리 줄여요, 여기 대전이야.”
112|
113|“갑자기 이러시는 연유가 뭡니까! 설마 방금 일로 제게 실망이라도 하신 겁니까!”
114|
115|“목소리 줄이라니까. 그리고 난 공 대협한테 실망한 것 없어요. 우리가 친구도 아니고, 서로에게 뭔가를 기대하고 실망할 사이는 아니잖아.”
116|
117|“그런…… 우리 종남파와의 약조는 잊으신 겁니까?”
118|
119|“약조? 아, 산서성 쪽에 길을 터 달라는 그거?”
120|
121|홍진이 피식 웃으며 말을 이었다.
122|
123|“원래 거래라는 게 그런 거예요. 일이 성사되기 전에는 언제 어그러질지 모르는 거거든. 설마 아직 전하의 재가도 안 떨어진 일을 말 몇 마디로 다 끝났다고 생각한 건 아니죠?”
124|
125|공일혁은 끓어오르는 분노를 간신히 억눌렀다.
126|
127|사문인 종남파에는 일이 끝난 것처럼 호언장담해 둔 상태.
128|
129|이번 일이 성공하면 그에 상응하는 보상을 받겠지만 실패한다면 질책을 피할 수 없다. 그로서는 최대한 눈앞의 내관 놈을 구슬려야만 했다.
130|
131|“이번 일이 잘만 성사된다면 도지휘동지께도 좋은 일이 아닙니까. 종남파는 결코 은원(恩怨)을 잊지 않습니다.”
132|
133|은혜면 은혜지, 굳이 원한까지 덧붙인 것은 은근한 협박이었다. 구파일방 중 하나를 적으로 돌릴 수도 있다는 경고.
134|
135|어린 시절부터 내관으로 지내며 온갖 암투를 지켜본 홍진이 그 말에 서린 속뜻을 못 알아들을 리 없다.
136|
137|‘쯧쯧. 이래서 무림인들이란.’
138|
139|홍진은 내심 혀를 찼다.
140|
141|언행 하나하나가 서투르고 노골적이다.
142|
143|그에겐 공일혁처럼 어중간하게 닳은 인물보다는 아예 무인답게 과묵하고 뚝심 있는 이풍이 훨씬 까다로운 적수였다.
144|
145|‘지금 누가 칼자루를 쥐고 있는지도 모르고.’
146|
147|원하는 목표가 있다면 설설 기어도 모자랄 텐데 협박까지 곁들이다니. 그러나 덕분에 그는 마음을 굳혔다.
148|
149|“공 대협. 나처럼 여린 사람은 그런 말 들으면 무서워서 같이 일 못 해요.”
150|
151|“아, 혹시 오해의 소지가 있었다면…….”
152|
153|공일혁이 몰랐던 척 사과하려던 그때, 지루한 표정으로 두 사람을 지켜보던 진태경이 한마디를 툭 던졌다.
154|
155|“오해의 소지는 무슨. 지나가던 개도 안 믿겠네.”
156|
157|“이, 이……!”
158|
159|“거, 종남파 선배님들. 뭐 얼마나 대단한 사업을 하시는지는 모르겠는데 나중에 따로 얘기하시면 안 됩니까? 안 그래도 밥상 엎어진 것도 서러워 죽겠는데.”
160|
161|바닥을 뒹구는 음식들을 보며 입맛을 다시는 진태경의 모습에 홍진이 실소를 터트렸다.
162|
163|“걱정 말아요. 이분들이 나가시면 새로 음식을 들이라 할 테니까. 그렇죠?”
164|
165|이제는 나가라고 등까지 떠미는 상황. 공일혁이 이를 악물었다.
166|
167|“도지휘동지. 제 안목이 형편없다는 건 인정합니다. 다만, 부디 오늘 일로 뭘 잃고 얻을지를 잘 생각하십시오.”
168|
169|“뭘 착각하시는 모양인데, 철저하게 실익을 따져서 내린 결정인걸요?”
170|
171|“그게 무슨……?”
172|
173|“일은 계속 진행할 겁니다. 섬서와 산서를 연결하는 전용 무역로와 무역소도 지을 거고 규모도 늘릴 거예요.”
174|
175|“그럼 더욱더 본문과 손을 잡아야 하지 않겠습니까!”
176|
177|처절하게까지 느껴지는 외침에 홍진이 눈을 동그랗게 떴다.
178|
179|“섬서에 있는 문파가 종남파밖에 없나요? 제가 알기로는 종남파보다 훨씬 오래되고 세간의 인식도 좋은 곳이 있다던데.”
180|
181|“……지금 혹시 화산파를 말씀하시는 겁니까?”
182|
183|공일혁의 얼굴이 와락 일그러졌다.
184|
185|화산과 종남은 지난 수백 년간 수없이 신경전을 벌여 온 숙적 관계.
186|
187|이번 일이 다른 문파도 아니고 화산에게 넘어간다면 가벼운 질책 정도로 끝날 리가 없었다.
188|
189|“제게 어떻게 이러실 수 있습니까!”
190|
191|“당연히 이럴 수 있죠. 더 좋은 선택지가 눈앞에 있는데.”
192|
193|“본문도 결코 화산파에 밀리지 않습니다. 아니, 당대에 이르러서는 오히려 화산파를 넘어섰다고 자부할 수 있습니다.”
194|
195|“자부할 수 있다라. 사문에 충성하는 모습은 보기 좋아요. 하지만 제 입장에서는 자타공인(自他共認)이라는 말이 더 듣기 좋지 않을까요?”
196|
197|홍진은 막힘없이 말을 이었다.
198|
199|“공 대협. 단도직입적으로 물어볼게요. 종남파에도 검성 같은 고수가 있나요?”
200|
201|“……그건.”
202|
203|“그럼 저기 있는 소협과 같은 걸출한 후기지수는요?”
204|
205|“…….”
206|
207|공일혁을 포함한 종남삼수 전원은 쉽게 입을 열지 못했다.
208|
209|검성? 종남파의 문주인 풍운검군이 종종 십왕(十王)에 비견되기는 하나 딱 거기까지다.
210|
211|하물며 청풍 같은 괴물은 듣도 보도 못했다. 특히 선공하고서도 일 합 만에 무릎을 꿇어야 했던 공일혁은 얼굴이 붉어졌다.
212|
213|“하, 하지만 본문에 소속된 절정 고수들의 숫자는 결코 화산파에 비해 밀리지 않습니다.”
214|
215|“내 듣자 하니 무림 문파의 힘은 고수가 몇 명이냐가 아니라 ‘어떤’ 고수를 품었느냐에 따라 달라진다고 하더군요.”
216|
217|정곡을 찌르는 홍진의 한마디에 공일혁은 순간 말문이 막혔다.
218|
219|그러나 어떻게든, 무슨 수를 쓰든 화산파에게 자리를 뺏기는 것만은 막아야 했다.
220|
221|“또, 또한 지금까지 관과 협력했던 것 모두 성공적으로 마무리 지었고요. 반면에 화산파는 지금까지 이런 일을 추진해 본 경험이 없습니다. 서투르고 실수가 생길 수밖에 없죠.”
222|
223|“어머, 그래요?”
224|
225|싱긋 웃은 홍진이 누군가를 향해 고개를 돌렸다.
226|
227|“이 첨사, 어떻게 생각해요?”
228|
229|묵묵히 지켜보고 있던 이풍이 대답했다.
230|
231|“맞는 말입니다. 화산은 관과 무림을 확실히 구분 짓는 편이지요.”
232|
233|홍진이 눈살을 찌푸리고, 공일혁의 얼굴에 화색이 돌던 그때 이풍의 묵직한 목소리가 이어졌다.
234|
235|“하지만 누군가에게나 처음이란 게 존재하지 않겠습니까?”
236|
237|“이풍, 네놈이!”
238|
239|홍진이 깔깔 웃었다.
240|
241|“우리 이 첨사, 진짜 많이 늘었다니까.”
242|
243|“누구 덕분이지요.”
244|
245|불과 한 식경 전에도 같은 내용의 대화를 나눴지만 분위기는 그때와 정반대다.
246|
247|두 사람은 화기애애한 분위기 속에서 대화를 이어 갔다.
248|
249|“이 첨사가 다리를 놔 줬으면 하는데. 어떻게 생각해요?”
250|
251|“물론입니다. 사부님께 전서구를 보내지요. 이 소식을 들으면 장문인께서도 좋아하실 겁니다.”
252|
253|“아, 그리고 여기 귀한 손님이 계시다는 사실도 알려 드리고.”
254|
255|홍진의 눈짓이 향하는 곳을 바라본 이풍이 슬며시 웃었다.
256|
257|“그건 태사부께서 좋아하실 소식이고요.”
258|
259|“시작이 좋네요.”
260|
261|“제 생각도 그렇습니다.”
262|
263|어느새 대화에서 완전히 배제된 공일혁은 신형을 부르르 떨었다.
264|
265|이미 되돌리기에는 너무 와 버린 상황. 그는 분노와 배신감이 섞인 눈빛으로 좌중을 쓸어 봤다.
266|
267|“감히, 감히 대종남파를 무시하다니.”
268|
269|“저기, 아까부터 말하고 싶었는데.”
270|
271|불쑥 끼어든 목소리의 주인공은 진태경이었다. 그가 피식 웃으며 말을 이었다.
272|
273|“종남파를 무시한 게 아니라, 그쪽을 무시한 겁니다. 몰라서 그렇지, 나 종남파 엄청 좋아해요. 군림…… 아무튼 삼십사 권까지 꼬박꼬박 봤어.”
274|
275|“그게 무슨 개소리냐! 족보도 없는 태원진가 따위가 끼어들 자리가 아니다!”
276|
277|진태경이 상처받은 얼굴로 청풍의 옆구리를 찔렀다.
278|
279|“청 소협. 저 아저씨가 우리 집 족보도 없대.”
280|
281|“헉, 은인한테요?”
282|
283|“응. 아무리 선배라지만 말이 너무 심한 거 아니야? 구파일방이라 무서워서 대답도 못 하겠고, 청 소협이 대신 말 좀 해 줘.”
284|
285|“제, 제가요? 저 그런 거 잘 못하는데.”
286|
287|“나 은인 아니야? 말만 은인이었어?”
288|
289|“아뇨, 당연히 아니죠.”
290|
291|“그럼 내가 알려 주는 대로 말해.”
292|
293|뭐라 속닥거림이 끝나자 청풍이 머뭇거리며 입을 열었다.
294|
295|“꺼, 꺼…….”
296|
297|“청 소협, 더 크게! 당신은 할 수 있어!”
298|
299|진태경의 응원에 힘을 얻은 청풍이 눈을 질끈 감고 외쳤다.
300|
301|“꺼져, 이 꼰대 새끼들아!”
302|
303|“……!”
304|
305|“……!”
306|
307|꼰대? 정확히 무슨 뜻인지는 모르겠지만 그건 중요하지 않다. 뒤에 새끼라는 단어가 붙었으니까.
308|
309|“이런 쳐 죽일……!”
310|
311|공일혁을 포함한 세 사람이 눈을 부릅떴다.
312|
313|그들이 누구인가, 종남파의 본산 제자들이다. 사람들의 선망 어린 시선에 익숙해진 그들에겐 씻을 수 없는 치욕이었다.
314|
315|하지만…….
316|
317|“으득, 갑시다!”
318|
319|공일혁은 울분을 참으며 돌아섰다. 이 치욕을 갚아 주기에는 상대도, 장소도 좋지 않다.
320|
321|‘오늘 일은 언젠가 갚는다. 반드시!’
322|
323|으스러져라 움켜쥔 주먹에서는 핏방울이 떨어졌다.
324|
325|거친 발걸음으로 대전을 박차고 떠나는 그의 등 뒤로 진태경과 청풍의 목소리가 따라붙었다.
326|
327|“이야, 욕 잘하네. 이것도 처음이에요?”
328|
329|“네, 저 욕 처음 해 봐요!”
330|
331|“처음치고는 제법 소질이 있는데. 앞으로 나한테 많이 배워요. 세상 살다 보면 쓰기 싫어도 쓸 데 많다?”
332|
333|“네!”
```

## Assembled English

```markdown
[P1]
# Chapter 142

[P2]
“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

[P3]
Zaha Divine Technique. Plum Blossom Sword Technique. And finally, the last word to come from Li Feng’s mouth:

[P4]
*Martial Uncle.*

[P5]
Gong Ilhyuk’s face darkened at this unbelievable turn of events.

[P6]
*Then is that bastard really…?*

[P7]
Even if Cheongpung wasn’t the Sword Saint’s biological grandson, one thing was certain.

[P8]
The idiot bowing over and over with a bewildered look on his face had inherited everything from the Sword Saint, Mae Jonghak.

[P9]
“Th-this can’t be. It’s impossible. This makes no sense…”

[P10]
As Gong Ilhyuk stammered in denial, a lilting voice reached his ears.

[P11]
“Great Hero Gong.”

[P12]
“Ah, Deputy Military Commissioner.”

[P13]
Gong Ilhyuk’s expression brightened when he spotted Hong Jin.

[P14]
The Zhongnan Sect had been pursuing various ventures through its government connections, and Hong Jin was one of the powerful figures in Shanxi Province they had come to know in the process.

[P15]
He was also the only person who could offer Gong Ilhyuk a lifeline in his current predicament.

[P16]
“What happened?”

[P17]
Hong Jin’s gentle voice put Gong Ilhyuk at ease.

[P18]
“I must have been mistaken for a moment.”

[P19]
“Mistaken? About what?”

[P20]
“I merely thought he was some fraud going around trading on the Sword Saint’s name…”

[P21]
“Well, I know next to nothing about martial arts, but he didn’t look like a fraud to me.”

[P22]
“There, there was only a slight misunderstanding.”

[P23]
“A misunderstanding…”

[P24]
Hong Jin murmured the word quietly, then stared directly at Gong Ilhyuk.

[P25]
“Great Hero Gong.”

[P26]
“Yes, Deputy Military Commissioner.”

[P27]
“Do you know why I invited you and the others from the Zhongnan Sect here?”

[P28]
“Yes. Of course I do.”

[P29]
There were two reasons.

[P30]
First, to become acquainted with Prince Shangshan, the City Lord of Shanxi and a member of the imperial family, and receive his approval for their new business venture.

[P31]
Second, to put Hong Jin’s political rival, Li Feng, firmly in his place.

[P32]
“But as you know, I’ve been rather busy lately. I was so distracted that I forgot to tell His Highness that other guests would be coming.”

[P33]
“I see.”

[P34]
The nasal quality had vanished from Hong Jin’s voice, leaving it completely dry. Gong Ilhyuk asked anxiously,

[P35]
“But why are you suddenly bringing that up…?”

[P36]
“I’d like you to leave for today.”

[P37]
“What?”

[P38]
“Wouldn’t the presence of uninvited guests put His Highness in a bad mood?”

[P39]
It was an unmistakable order to leave. And on top of that, Hong Jin had called them uninvited guests.

[P40]
Gong Ilhyuk protested.

[P41]
“Uninvited guests? Deputy Military Commissioner, what exactly do you mean?”

[P42]
“Oh my, must I say it twice? I mean exactly what I said. I failed to tell His Highness you were coming.”

[P43]
Hong Jin was originally a palace attendant. He had remained at Prince Shangshan’s side since the prince was an infant, and thanks to that, he had risen to the post of Deputy Military Commissioner, becoming the power behind the Shanxi Provincial Office and the second-ranking figure in the military.

[P44]
The young prince favored him above all others. And yet he was sending guests away merely because he had failed to mention them in advance?

[P45]
“I, I’m not sure I understand what you’re saying, Deputy Military Commissioner…”

[P46]
Hong Jin smiled sweetly at the flustered Gong Ilhyuk.

[P47]
“Great Hero Gong.”

[P48]
“Yes?”

[P49]
“I didn’t think you were like this, but you’re a little slow, aren’t you?”

[P50]
“…What?”

[P51]
“Or are you simply bad at taking a hint?”

[P52]
The sudden verbal abuse plunged the hall into silence. Gong Ilhyuk and the other two members of the Three Hands of Zhongnan clenched their trembling fists.

[P53]
“You go too far.”

[P54]
“Oh my, if that’s how it felt, then you understood my intentions perfectly. I did go a little too far on purpose.”

[P55]
“Deputy Military Commissioner!”

[P56]
“Lower your voice. This is the grand hall.”

[P57]
“Why are you suddenly acting like this? Are you disappointed in me because of what just happened?”

[P58]
“I said lower your voice. And I’m not disappointed in you, Great Hero Gong. We aren’t friends. We’re hardly close enough to expect anything from each other, much less be disappointed.”

[P59]
“That… have you forgotten your agreement with our Zhongnan Sect?”

[P60]
“Agreement? Oh, the one about opening a route into Shanxi Province?”

[P61]
Hong Jin gave a short laugh and continued.

[P62]
“That’s how business works. Until a deal is finalized, it can fall apart at any moment. Surely you didn’t think a few words meant everything was settled when His Highness hasn’t even given his approval yet?”

[P63]
Gong Ilhyuk barely managed to suppress his rising anger.

[P64]
He had already boasted to his sect as though the deal were complete.

[P65]
If the venture succeeded, he would receive a commensurate reward. If it failed, however, he would not escape a reprimand. He had no choice but to coax the eunuch standing before him.

[P66]
“If this venture succeeds, wouldn’t it benefit you as well, Deputy Military Commissioner? The Zhongnan Sect never forgets gratitude or grudges.”

[P67]
Adding *grudges* to *gratitude* was a veiled threat—a warning that Hong Jin might make an enemy of one of the Nine Sects and One Gang.

[P68]
Hong Jin had served as a palace attendant since childhood and witnessed all manner of political intrigue. There was no chance he had missed the hidden meaning behind Gong Ilhyuk’s words.

[P69]
*Tsk. This is why martial artists are the way they are.*

[P70]
Hong Jin clicked his tongue inwardly.

[P71]
Every word and action was clumsy and blatant.

[P72]
Compared to a half-polished man like Gong Ilhyuk, Li Feng—taciturn, stubborn, and every inch a martial artist—was a far more troublesome opponent.

[P73]
*He doesn’t even realize who holds the upper hand right now.*

[P74]
If he had a goal he wanted to achieve, even crawling on the ground would hardly have been enough. And yet he had added a threat on top of everything else.

[P75]
That settled Hong Jin’s decision.

[P76]
“Great Hero Gong, I’m such a delicate person. Words like that frighten me too much to keep working with you.”

[P77]
“Ah, if there was any room for misunderstanding…”

[P78]
Gong Ilhyuk was about to apologize as though he had no idea what Hong Jin meant when Jin Taekyung, who had been watching the two men with a bored expression, casually tossed out a remark.

[P79]
“Room for misunderstanding, my ass. Not even a passing dog would believe that.”

[P80]
“You, you…!”

[P81]
“Hey, Seniors of the Zhongnan Sect. I don’t know what kind of incredible business you’re running, but couldn’t you discuss it somewhere else later? I’m already miserable enough about the table being overturned.”

[P82]
Hong Jin let out a quiet laugh at the sight of Taekyung licking his lips while looking at the food scattered across the floor.

[P83]
“Don’t worry. Once these gentlemen leave, I’ll have fresh food brought in. Isn’t that right?”

[P84]
Now Hong Jin was practically shoving them out the door.

[P85]
Gong Ilhyuk gritted his teeth.

[P86]
“Deputy Military Commissioner, I admit my judgment is terrible. But please think carefully about what you stand to gain and lose from today’s events.”

[P87]
“You seem to be mistaken. I reached this decision after thoroughly weighing the practical benefits.”

[P88]
“What does that mean…?”

[P89]
“We’ll continue with the project. We’ll build a dedicated trade route and trading post connecting Shaanxi and Shanxi, and we’ll expand the scale as well.”

[P90]
“Then that’s all the more reason to join hands with our sect!”

[P91]
Hong Jin’s eyes widened at the desperate shout.

[P92]
“Is the Zhongnan Sect the only sect in Shaanxi? As far as I know, there’s a place far older than the Zhongnan Sect—and one with a much better reputation among the public.”

[P93]
“…Are you talking about Huashan?”

[P94]
Gong Ilhyuk’s face twisted.

[P95]
Huashan and the Zhongnan Sect had been bitter rivals, constantly at odds, for the past several hundred years.

[P96]
If this project went to Huashan instead of some other sect, Gong Ilhyuk knew he would face far more than a light reprimand.

[P97]
“How could you do this to me?”

[P98]
“Of course I can. There’s a better option right in front of me.”

[P99]
“Our sect is by no means inferior to Huashan. In fact, I can proudly say that in this generation, we have surpassed them.”

[P100]
“‘I can proudly say.’ It’s good to see such loyalty to one’s sect. But from my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?”

[P101]
Hong Jin continued without missing a beat.

[P102]
“Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?”

[P103]
“…That is…”

[P104]
“Then does it have a young prodigy as outstanding as that Young Hero over there?”

[P105]
“……”

[P106]
None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer.

[P107]
The Sword Saint?

[P108]
The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went.

[P109]
As for a monster like Cheongpung, none of them had ever heard of such a person, much less seen one. Gong Ilhyuk in particular flushed red, having attacked first only to be brought to his knees in a single exchange.

[P110]
“B-but our sect has no fewer Peak masters than Huashan.”

[P111]
“I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on *what kind* of masters it possesses.”

[P112]
Hong Jin’s remark struck the heart of the matter, leaving Gong Ilhyuk momentarily speechless.

[P113]
But no matter what it took, he had to prevent Huashan from taking their place.

[P114]
“Furthermore, every venture we’ve undertaken with the government has been completed successfully. Huashan, on the other hand, has no experience with this sort of project. They’re bound to be clumsy and make mistakes.”

[P115]
“Oh my, is that so?”

[P116]
Hong Jin smiled and turned toward someone.

[P117]
“Assistant Commissioner Li, what do you think?”

[P118]
Li Feng, who had watched everything in silence, answered.

[P119]
“That is true. Huashan does tend to draw a firm line between the government and Murim.”

[P120]
Hong Jin frowned, and color returned to Gong Ilhyuk’s face.

[P121]
But Li Feng’s heavy voice continued.

[P122]
“However, doesn’t everyone have a first time?”

[P123]
“Li Feng, you bastard!”

[P124]
Hong Jin burst out laughing.

[P125]
“Our Assistant Commissioner Li has truly come a long way.”

[P126]
“Thanks to you.”

[P127]
The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite.

[P128]
They continued their conversation in a warm and friendly atmosphere.

[P129]
“I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?”

[P130]
“Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.”

[P131]
“Ah, and you should also tell him that we have an honored guest here.”

[P132]
Li Feng followed Hong Jin’s meaningful glance and smiled faintly.

[P133]
“That is news our Grandmaster will be pleased to hear.”

[P134]
“It’s a good start.”

[P135]
“I think so too.”

[P136]
Completely excluded from the conversation, Gong Ilhyuk trembled from head to toe.

[P137]
Things had already gone too far to turn back. He swept a gaze filled with fury and betrayal across the room.

[P138]
“How dare you look down on the Great Zhongnan Sect.”

[P139]
“Hey, there’s something I’ve been meaning to say.”

[P140]
The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a short laugh and continued.

[P141]
“We’re not looking down on the Zhongnan Sect. We’re looking down on you. You might not know this, but I’m a huge fan of the Zhongnan Sect. *The Reign…* Anyway, I faithfully kept up with it through volume thirty-four.”

[P142]
“What kind of bullshit are you spouting? A family without even a proper pedigree like the Jin Family of Taiyuan has no place butting in!”

[P143]
Taekyung put on a wounded expression and poked Cheongpung in the side.

[P144]
“Young Master Cheongpung, that old man says our family doesn’t even have a family tree.”

[P145]
“What? He said that to my Benefactor?”

[P146]
“Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself, so could you say something for me?”

[P147]
“M-me? I’m not very good at things like that.”

[P148]
“Am I not your Benefactor? Was I only your Benefactor in name?”

[P149]
“No, of course not.”

[P150]
“Then say what I tell you.”

[P151]
After Taekyung finished whispering something to him, Cheongpung hesitantly opened his mouth.

[P152]
“G-get… get…”

[P153]
“Young Master Cheongpung, louder! You can do it!”

[P154]
Buoyed by Taekyung’s encouragement, Cheongpung squeezed his eyes shut and shouted,

[P155]
“Get lost, you boomer bastards!”

[P156]
“……!”

[P157]
“……!”

[P158]
*Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*.

[P159]
“You goddamn…!”

[P160]
All three men, Gong Ilhyuk included, glared with their eyes wide open.

[P161]
Who were they?

[P162]
They were disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was a humiliation they could never wash away.

[P163]
But…

[P164]
Gong Ilhyuk ground his teeth. “Let’s go!”

[P165]
Swallowing his outrage, he turned away. Neither the opponent nor the place was suitable for repaying this humiliation.

[P166]
*I’ll make them pay for this someday. I swear it!*

[P167]
Blood dripped from the fist he clenched so hard it seemed it would crush.

[P168]
He stormed out of the grand hall, his footsteps heavy and violent.

[P169]
Behind him came the voices of Jin Taekyung and Cheongpung.

[P170]
“Wow, you’re good at swearing. Was that your first time too?”

[P171]
“Yes! I’ve never sworn before!”

[P172]
“For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.”

[P173]
“Yes!”
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
# Chapter 142

[P2]
“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

[P3]
Zaha Divine Technique. Plum Blossom Sword Technique. And finally, the last word to come from Li Feng’s mouth:

[P4]
*Martial Uncle.*

[P5]
Gong Ilhyuk’s face darkened at this unbelievable turn of events.

[P6]
*Then is that bastard really…?*

[P7]
Even if Cheongpung wasn’t the Sword Saint’s biological grandson, one thing was certain.

[P8]
That idiot who kept bowing at the waist with a bewildered expression had inherited everything from Mae Jonghak, the Sword Saint.

[P9]
“This, this can’t be. It’s impossible. This makes no sense…”

[P10]
As Gong Ilhyuk stammered and denied reality, a lilting voice reached his ears.

[P11]
“Great Hero Gong.”

[P12]
“Ah, Deputy Military Commissioner.”

[P13]
Gong Ilhyuk’s expression brightened when he spotted Hong Jin.

[P14]
The Zhongnan Sect had been pursuing various ventures through its connections with the government, and Hong Jin was one of the powerful men of Shanxi Province whom they had come to know in the process.

[P15]
He was also the only person who could possibly extend a hand of salvation to Gong Ilhyuk in this predicament.

[P16]
“What happened?”

[P17]
Hong Jin’s gentle voice put Gong Ilhyuk at ease.

[P18]
“I must have been mistaken for a moment.”

[P19]
“Mistaken? About what?”

[P20]
“I merely thought he was some fraud going around trading on the Sword Saint’s name…”

[P21]
“Well, I’m no expert in martial arts, but he doesn’t look like a fraud to me.”

[P22]
“There, there was only a slight misunderstanding.”

[P23]
“A misunderstanding…”

[P24]
Hong Jin murmured the word quietly, then stared directly at Gong Ilhyuk.

[P25]
“Great Hero Gong.”

[P26]
“Yes, Deputy Military Commissioner.”

[P27]
“Do you know why I invited you and the others from the Zhongnan Sect here?”

[P28]
“Yes. Of course I do.”

[P29]
There were two reasons.

[P30]
First, to become acquainted with Prince Shangshan, the City Lord of Shanxi and a member of the imperial family, and receive his approval for their new business venture.

[P31]
Second, to put Hong Jin’s political rival, Li Feng, firmly in his place.

[P32]
“But as you know, I’ve been rather busy lately. I was so distracted that I forgot to tell His Highness that some other guests would be arriving.”

[P33]
“I see.”

[P34]
The nasal quality had vanished from Hong Jin’s voice, leaving it completely dry. Gong Ilhyuk asked anxiously,

[P35]
“But why are you suddenly bringing that up…?”

[P36]
“I’d like you to leave for today.”

[P37]
“What?”

[P38]
“Wouldn’t the presence of uninvited guests make His Highness uncomfortable?”

[P39]
It was an unmistakable order to leave. And on top of that, Hong Jin had called them uninvited guests.

[P40]
Gong Ilhyuk protested.

[P41]
“Uninvited guests? Deputy Military Commissioner, what exactly do you mean?”

[P42]
“Oh my, do I have to say it twice? I mean exactly what I said before. I failed to mention your arrival to His Highness.”

[P43]
Hong Jin was a eunuch. He had remained at Prince Shangshan’s side since the prince was an infant, and thanks to that, he had risen to the post of Deputy Military Commissioner, becoming the power behind the Shanxi Provincial Office and the second-ranking figure in the military.

[P44]
The young prince favored him above all others. And yet he was sending guests away simply because he had failed to inform His Highness in advance?

[P45]
“I, I’m not sure I understand what you’re saying, Deputy Military Commissioner…”

[P46]
Hong Jin smiled sweetly at the flustered Gong Ilhyuk.

[P47]
“Great Hero Gong.”

[P48]
“Yes?”

[P49]
“I didn’t think you were like this, but you’re a little slow, aren’t you?”

[P50]
“…What?”

[P51]
“Or are you just bad at reading the room?”

[P52]
The sudden verbal abuse plunged the hall into silence.

[P53]
Gong Ilhyuk and the other two members of the Three Hands of Zhongnan trembled as they clenched their fists.

[P54]
“Your words are excessive.”

[P55]
“Oh my, if that’s how you feel, then you’ve understood my intentions perfectly. I’ll admit I deliberately went a little too far.”

[P56]
“Deputy Military Commissioner!”

[P57]
“Lower your voice. This is the grand hall.”

[P58]
“Why are you suddenly acting like this? Are you disappointed in me because of what just happened?”

[P59]
“I said lower your voice. And I’m not disappointed in you, Great Hero Gong. We aren’t friends, after all. We’re not close enough to expect anything from each other or feel disappointed.”

[P60]
“How could you say that? Have you forgotten your agreement with our Zhongnan Sect?”

[P61]
“Agreement? Oh, you mean the one about opening a route into Shanxi Province?”

[P62]
Hong Jin gave a quiet laugh and continued.

[P63]
“That’s how business works. Until a deal is finalized, it can fall apart at any moment. Surely you didn’t think a few words meant everything was settled when His Highness hasn’t even given his approval yet?”

[P64]
Gong Ilhyuk barely managed to suppress his rising anger.

[P65]
He had already boasted to his sect as though the deal were complete.

[P66]
If the venture succeeded, he would receive a suitable reward. But if it failed, he would be unable to escape a harsh reprimand. For now, he had no choice but to coax the eunuch standing before him.

[P67]
“If this deal succeeds, wouldn’t it benefit you as well, Deputy Military Commissioner? The Zhongnan Sect never forgets gratitude or grudges.”

[P68]
The mention of grudges alongside gratitude was an indirect threat.

[P69]
It was a warning that Hong Jin risked making an enemy of one of the Nine Sects and One Gang.

[P70]
Hong Jin had spent his childhood and youth as an inner palace official, watching every kind of political struggle. There was no way he could fail to understand the hidden meaning in Gong Ilhyuk’s words.

[P71]
*Hmph. This is why martial artists are so hopeless.*

[P72]
Hong Jin clicked his tongue inwardly.

[P73]
Every one of Gong Ilhyuk’s words and actions was clumsy and blatant.

[P74]
Compared to a half-polished man like Gong Ilhyuk, Li Feng—quiet, stubborn, and martial artist to the bone—was a far more troublesome opponent.

[P75]
*He doesn’t even realize who holds the upper hand right now.*

[P76]
If he had a goal he wanted to achieve, he should have been crawling on the ground to get it. And yet he had added a threat on top of everything else.

[P77]
That helped Hong Jin make up his mind.

[P78]
“Great Hero Gong. I’m a delicate person, you see. Hearing words like that frightens me too much to continue working together.”

[P79]
“Ah, if there was any room for misunderstanding…”

[P80]
Gong Ilhyuk was about to apologize as though he had no idea what Hong Jin meant when Jin Taekyung, who had been watching the two men with a bored expression, casually tossed out a remark.

[P81]
“Room for misunderstanding, my ass. A dog passing by wouldn’t believe that.”

[P82]
“You, you…!”

[P83]
“Hey, Seniors from the Zhongnan Sect. I don’t know what kind of incredible business you’re running, but couldn’t you discuss it somewhere else later? I’m already miserable enough seeing the entire meal overturned.”

[P84]
Hong Jin let out a quiet laugh at the sight of Taekyung licking his lips while looking at the food scattered across the floor.

[P85]
“Don’t worry. Once these gentlemen leave, I’ll have new food brought in. Isn’t that right?”

[P86]
The situation had now progressed to Hong Jin practically pushing them out the door.

[P87]
Gong Ilhyuk gritted his teeth.

[P88]
“Deputy Military Commissioner. I admit my judgment is terrible. But please think carefully about what you will gain and lose from what happened today.”

[P89]
“You seem to be mistaken. I made this decision after thoroughly weighing the practical benefits.”

[P90]
“What does that mean?”

[P91]
“We’ll continue with the project. We’ll build a dedicated trade route and trading post connecting Shaanxi and Shanxi, and we’ll expand the scale as well.”

[P92]
“Then all the more reason you should join hands with our sect!”

[P93]
Hong Jin’s eyes widened at the desperate shout.

[P94]
“Is the Zhongnan Sect the only sect in Shaanxi? As far as I know, there’s a place far older than the Zhongnan Sect—and one with a much better reputation among the public.”

[P95]
“……Are you talking about Huashan?”

[P96]
Gong Ilhyuk’s face twisted.

[P97]
Huashan and the Zhongnan Sect had been bitter rivals, constantly at odds, for the past several hundred years.

[P98]
If this project went to Huashan instead of some other sect, Gong Ilhyuk knew he would face far more than a light reprimand.

[P99]
“How could you do this to me?”

[P100]
“Of course I can. There’s a better option right in front of me.”

[P101]
“Our sect is by no means inferior to Huashan. In fact, in the current generation, I can proudly say that we’ve surpassed Huashan.”

[P102]
“‘I can proudly say.’ It’s good to see such loyalty to one’s sect. But from my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?”

[P103]
Hong Jin continued without hesitation.

[P104]
“Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?”

[P105]
“……That is…”

[P106]
“Then what about a young prodigy as outstanding as that young hero over there?”

[P107]
“……”

[P108]
None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer.

[P109]
The Sword Saint?

[P110]
The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went.

[P111]
As for a monster like Cheongpung, no one had ever heard or seen anything like him.

[P112]
Gong Ilhyuk, who had been the one to attack first and still ended up on his knees in a single exchange, flushed red.

[P113]
“B-but the number of Peak masters belonging to our sect is by no means inferior to Huashan’s.”

[P114]
“I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on what kind of masters it possesses.”

[P115]
Hong Jin’s single remark struck the bull’s-eye, and Gong Ilhyuk was momentarily rendered speechless.

[P116]
But no matter what it took, he had to prevent the position from being handed to Huashan.

[P117]
“Also, everything we’ve done in cooperation with the government has been completed successfully. Huashan, on the other hand, has never attempted anything like this. They’re inexperienced. Mistakes are inevitable.”

[P118]
“Oh my, is that so?”

[P119]
Hong Jin smiled and turned toward someone.

[P120]
“Assistant Commissioner Li, what do you think?”

[P121]
Li Feng, who had been silently observing everything, answered.

[P122]
“That is true. Huashan does tend to draw a firm line between the government and Murim.”

[P123]
Hong Jin frowned, and color returned to Gong Ilhyuk’s face.

[P124]
But Li Feng’s heavy voice continued.

[P125]
“However, doesn’t everyone have a first time?”

[P126]
“Li Feng, you bastard!”

[P127]
Hong Jin burst into laughter.

[P128]
“Our Assistant Commissioner Li has improved so much.”

[P129]
“Thanks to you.”

[P130]
The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite.

[P131]
They continued their conversation in a warm and friendly atmosphere.

[P132]
“I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?”

[P133]
“Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.”

[P134]
“Ah, and you should also tell him that we have a precious guest here.”

[P135]
Li Feng followed Hong Jin’s meaningful glance and smiled faintly.

[P136]
“That is news our Grandmaster will be pleased to hear.”

[P137]
“It’s a good start.”

[P138]
“I think so too.”

[P139]
Gong Ilhyuk, who had been completely excluded from the conversation, trembled from head to toe.

[P140]
The situation had gone too far to turn back now.

[P141]
He swept his furious, betrayed gaze across the room.

[P142]
“How dare you ignore the mighty Zhongnan Sect.”

[P143]
“Hey, there’s something I’ve been meaning to say.”

[P144]
The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a quiet laugh and continued.

[P145]
“It’s not the Zhongnan Sect we ignored. It’s you. You might not know this, but I really like the Zhongnan Sect. *The Reign…* Anyway, I kept up with it all the way through volume thirty-four.”

[P146]
“What kind of bullshit are you talking about? The Jin Family of Taiyuan is a family without even a proper pedigree! This is no place for the likes of you to butt in!”

[P147]
Taekyung put on a wounded expression and poked Cheongpung in the side.

[P148]
“Young Master Cheongpung. That old man says our family doesn’t even have a family tree.”

[P149]
“What? He said that to my Benefactor?”

[P150]
“Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself. Could you say something for me?”

[P151]
“M-me? I’m not very good at things like that.”

[P152]
“Am I not your Benefactor? Was I only a Benefactor in name?”

[P153]
“No, of course not.”

[P154]
“Then say what I tell you.”

[P155]
After Taekyung whispered something to him, Cheongpung opened his mouth hesitantly.

[P156]
“G-get, get…”

[P157]
“Young Master Cheongpung, louder! You can do it!”

[P158]
Encouraged by Taekyung, Cheongpung squeezed his eyes shut and shouted,

[P159]
“Get lost, you boomer bastards!”

[P160]
“……!”

[P161]
“……!”

[P162]
*Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*.

[P163]
“You goddamn bastards…!”

[P164]
All three men, Gong Ilhyuk included, glared with their eyes wide open.

[P165]
Who were they?

[P166]
They were main disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was an insult they could never wash away.

[P167]
But…

[P168]
Gong Ilhyuk ground his teeth. “Let’s go!”

[P169]
Gong Ilhyuk turned away, swallowing his outrage.

[P170]
This was neither the right place nor the right opponent for him to repay this humiliation.

[P171]
*I’ll make them pay for this someday. I swear it!*

[P172]
Blood dripped from the fist he clenched so tightly that his knuckles creaked.

[P173]
He stormed out of the grand hall, his footsteps heavy and violent.

[P174]
Behind him came the voices of Jin Taekyung and Cheongpung.

[P175]
“Wow, you’re good at swearing. Was that your first time too?”

[P176]
“Yes! It was my first time ever!”

[P177]
“For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.”

[P178]
“Yes!”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검법     | **sword technique**                              |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 대종남파 | **Great Zhongnan Sect** | Expanded and formal reference to the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 142,
  "passed": true,
  "metrics": {
    "source_characters": 5760,
    "translation_characters": 13388,
    "length_ratio": 2.324,
    "source_paragraphs": 166,
    "translation_paragraphs": 173
  },
  "errors": [],
  "warnings": [
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
        "korean": "은원",
        "preferred": "gratitude and grudges"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
