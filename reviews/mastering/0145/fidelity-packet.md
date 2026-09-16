# Fidelity Gate — Chapter 145

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
  1|＃145화
  2|
  3|
  4|
  5|홍진이 피식 웃으며 술잔을 기울였다.
  6|
  7|“우리 진 공자, 생각보다 욕심이 많으시구나?”
  8|
  9|“남들만큼은 있는 편이죠. 그리고 부탁인데, 그냥 진 공자라고 불러 주시면 안 될까요.”
 10|
 11|“어머, 좋으면서 싫은 척하기는.”
 12|
 13|“족 같네…….”
 14|
 15|“응? 방금 뭐라고 했어요?”
 16|
 17|“아, 가족 같아서 좋다고요.”
 18|
 19|“가족이라, 듣기 좋네. 벌써부터 진 소가주님과의 만남이 기다려지는데요?”
 20|
 21|맞다. 이 자리에 입 아프게 떠들어 봤자 결국 결정하는 건 진위경과 홍진이다.
 22|
 23|둘 다 이 방면에서는 프로나 다름없으니 아마추어는 빠져 줘야 하는 게 도리겠지.
 24|
 25|“그나저나 성운표국에는 무슨 악감정이 있어서 이러는 거예요?”
 26|
 27|“악감정이랄 것까진 없고…… 미운 놈 뺨 한 대 더 때려 주는 거죠. 떡고물도 챙길 수 있으니 좋고.”
 28|
 29|“아하, 원래 오기로 했던 성운표국의 소국주와 관련된 일?”
 30|
 31|이 인간, 눈치가 보통이 아니다.
 32|
 33|대강 눈치챈 마당에 괜히 미주알고주알 설명할 필요도 없을 것 같아서 어깨를 으쓱해 보였다.
 34|
 35|“뭐, 비슷합니다. 어떻게 아셨어요?”
 36|
 37|“진 공자. 난 이십 년을 넘게 황궁(皇宮)에서 살았어요.”
 38|
 39|“네?”
 40|
 41|“눈치 하나로 살아남았다는 뜻이에요. 어린애들 표정 읽는 것 정도야 쉽지.”
 42|
 43|홍진이 산서오문의 후기지수들을 턱짓으로 가리켰다.
 44|
 45|멀찍이 떨어진 탁자 끄트머리, 바짝 얼어붙은 표정으로 이쪽을 힐끔거리던 녀석들이 화들짝 놀라며 움츠러든다.
 46|
 47|“처음 들어올 때부터 저러더라고. 진 공자 눈치만 살살 살피면서.”
 48|
 49|“그랬어요?”
 50|
 51|“응. 보는 내가 다 애처로울 정도였다니까. 도대체 무슨 짓을 한 거예요?”
 52|
 53|“아까 나가신 분들이랑 비슷한 일이 있었죠.”
 54|
 55|“종남삼수? 쯧쯧. 사람을 못 알아봤구나?”
 56|
 57|역시 척 하면 착이다. 홍진은 안타깝다는 듯이 혀를 찼고, 이풍은 고개를 홱 돌려 후기지수들을 응시했다.
 58|
 59|마치 ‘청풍 사숙’을 건드린 놈들이 누군지 똑똑히 기억해 두겠다는 듯한 눈빛이었다.
 60|
 61|“헉.”
 62|
 63|“도, 도지휘첨사. 아니, 이 대협. 그게 아니옵고…….”
 64|
 65|산서성 군부의 실력자인 데다 화산파 속가제자인 이풍이다.
 66|
 67|제아무리 관과 무림이 불가침의 관계라지만 잘못 얽히면 산서오문의 미래가 아주 재미없어질 게 뻔하다.
 68|
 69|황급히 변명을 늘어놓는 녀석들을 뒤로하고 이풍이 내게 물었다.
 70|
 71|“그 얘기, 자세히 들려줄 수 있겠소?”
 72|
 73|“다 끝난 얘기예요. 당사자가 직접 빠따도 쳤는데요, 뭘.”
 74|
 75|“빠따?”
 76|
 77|“아, 두들겨 팼다는 뜻입니다. 물론 그 전에 사과도 했고요.”
 78|
 79|“사숙이 직접 말이오? 흠.”
 80|
 81|정확히는 한 명만 조졌지만 때리긴 때린 거다.
 82|
 83|이풍이 한결 누그러진 눈빛으로 후기지수들을 바라봤다.
 84|
 85|“네놈들의 잘못을 알고 있느냐?”
 86|
 87|“예, 옛!”
 88|
 89|“뼈저리게 느끼고 있습니다!”
 90|
 91|곧장 터져 나오는 우렁찬 외침. 이풍도 이풍이지만 청풍의 신분을 알았으니 똥줄이 탈 만하다.
 92|
 93|절정 고수인 건 둘째치고, 무려 검성의 제자에 화산파의 적전제자 아닌가.
 94|
 95|‘아주 제대로 엿 된 거지.’
 96|
 97|산서오문이라고 해 봤자 결국 중소 문파. 구파일방인 화산파가 열받으면 일가친척까지 빠따를 맞을 수도 있다.
 98|
 99|아니, 고작 그걸로 끝나면 다행이지.
100|
101|“오늘 이곳에서 나눴던 대화와 일들은…….”
102|
103|이풍의 묵직한 음성이 이어지기도 전에 대답이 튀어나왔다.
104|
105|“함구하겠습니다!”
106|
107|“무덤까지 갖고 가겠습니다!”
108|
109|“전 이미 잊었어요!”
110|
111|“여기가 어디죠? 제가 누구죠?”
112|
113|……아주 지랄들을 하는구나.
114|
115|기억상실증 환자가 속출하는 광경을 바라보고 있던 나는 한마디를 보탰다.
116|
117|“그걸로 되겠어?”
118|
119|“예, 예?”
120|
121|“그게 무슨 말씀이신지…….”
122|
123|“무슨 말씀이긴. 한 식구 되고 싶으면 너희도 숟가락 얹으라는 얘기지. 거기 너, 식구 뜻이 뭐야?”
124|
125|지목당한 후기지수가 더듬더듬 대답했다.
126|
127|“같이 밥 먹는…… 아니라면 죄송합니다.”
128|
129|“맞았어. 자, 그럼 식구가 되려면 어떻게 해야 할까?”
130|
131|“아!”
132|
133|후기지수가 탄성과 함께 이마를 탁 쳤다.
134|
135|그나마 눈치는 좀 있는 놈이군.
136|
137|“그럼 다음에 제가 좋은 자리를 마련하겠습니다. 홍화루 어떠십니까?”
138|
139|“…….”
140|
141|돌대가리가 따로 없네.
142|
143|후계자라는 것들이 이 모양이니 산서오문 꼬라지는 안 봐도 뻔하다. 나는 한숨을 푹 내쉬고 간단명료하게 설명해 주었다.
144|
145|“홍화루는 집어치우고 우리 쪽에서 시키는 거 잘하란 말이야. 가령 성운표국에 관련된 문제라든가, 응?”
146|
147|“아아.”
148|
149|태원진가는 분명 산서 제일의 세력을 갖추게 됐지만 중소 문파가 똘똘 뭉쳐 반발한다면 피곤한 일이 생길 게 뻔했다.
150|
151|명색이 정파 무림 소속인데, 마적 떼처럼 닥치는 대로 뺏고 책임을 물었다가는 손가락질을 받을 테니까.
152|
153|무림에서 무공만큼이나 중요한 것이 바로 명분 아닌가?
154|
155|‘하지만 손가락질할 놈들만 없다면 문제 될 것도 없지.’
156|
157|나는 네 명의 남녀를 천천히 눈에 담았다. 산서오문 중 성운표국을 제외한 네 문파의 후계자들.
158|
159|이들이 앞장서서 태원진가의 손을 들어 준다면 일이 한층 쉬워질 거다.
160|
161|“밥 먹을 때 어디에 앉아야 할지 잘 봐. 그래야 한 입씩이라도 얻어먹지.”
162|
163|비록 변방이라지만 명색이 한 성에서 첫손가락에 꼽는다는 성운표국. 이만하면 조금씩 나눠 먹어도 충분한 진수성찬이다.
164|
165|내 말에 눈치 빠른 놈은 조용히 눈을 반짝였고, 눈치 없는 놈은 조심스럽게 입을 열었다.
166|
167|“그래도 그건 좀…….”
168|
169|나는 어벙해 보이는 놈의 말을 칼같이 잘라 냈다.
170|
171|“너, 어디 문파 소속이냐?”
172|
173|“저, 저 말씀이십니까?”
174|
175|“그래, 너.”
176|
177|한참을 머뭇거린 끝에 고평문이라는 이름이 튀어나왔다.
178|
179|얼핏 들어 본 이름 같긴 한데, 기억이 가물가물한 듣보잡 문파. 고평문의 위치는 딱 그 정도다.
180|
181|아니, 신(新) 산서오문의 위치가 전부 마찬가지였다.
182|
183|“고평문. 고평문…… 어감이 별로네. 내가 새로 하나 추천해 줘?”
184|
185|“예?”
186|
187|아직도 감을 못 잡는 놈의 눈동자를 들여다보며 말을 이었다.
188|
189|“다음 달부터는 새 이름으로 다시 시작하자. 태원진가 고평지부로. 어때?”
190|
191|“……!”
192|
193|“……!”
194|
195|“마음에 안 드나 보네. 그냥 한번 해 본 소리야, 인마.”
196|
197|물론 그냥 해 본 소리는 아니지.
198|
199|나는 새파랗게 질린 고평문 소문주의 어깨를 탁탁 두드리며 좌중을 쓸어 봤다.
200|
201|“여기 우진태랑 의형제, 의남매 맺은 사람 있냐?”
202|
203|“어, 없습니다.”
204|
205|“아니면 어릴 때부터 십 년 넘게 봐 온 끈끈한 사이라든지. 태중 혼약이라든지. 뭐 많잖아?”
206|
207|“절대! 절대 아닙니다. 몇 번 어울린 게 전부예요.”
208|
209|“저, 저도 비단 몇 필 선물 받고 보석 조금…….”
210|
211|“그럼 됐네.”
212|
213|짝!
214|
215|날카로운 박수 소리에 네 남녀의 몸이 흠칫 떨렸다.
216|
217|“선택해. 태원진가와 화산파, 그리고 관까지 적으로 돌릴 건지, 아니면…….”
218|
219|나는 씩 웃으며 또박또박, 마지막 말을 읊었다.
220|
221|“별로 안 친한 놈 버리고 우리랑 같이 나눠 먹을 건지.”
222|
223|짝짝짝짝.
224|
225|이번에는 내가 아니다. 홍진이 깔깔 웃으며 박수를 치고 있었다.
226|
227|“우리 진 공자, 보면 볼수록 마음에 든다니까?”
228|
229|“…….”
230|
231|그런 위험 발언은 자제해 주십시오, 형님.
232|
233|
234|
235|* * *
236|
237|
238|
239|“벌써 가는 것이냐?”
240|
241|여전히 오만한 말투였지만 목소리와 눈빛에는 아쉬움이 한가득이다.
242|
243|‘자식, 볼수록 귀엽네.’
244|
245|나는 꼬마 팬, 아니 상산왕 주표의 머리를 쓰다듬어…… 주려다가 이풍의 눈빛에 손을 내렸다.
246|
247|아, 맞다. 얘 왕이었지. 그것도 황족.
248|
249|“커흠. 저도 급한 볼일이 있는지라.”
250|
251|“나중으로 미루면 안 되겠느냐?”
252|
253|“죄송합니다. 한시를 다투는 일이라서.”
254|
255|“그런가…….”
256|
257|시무룩한 꼬맹이의 얼굴을 보니 살짝 죄책감이 들기는 개뿔, 얼른 본가로 돌아가서 푹 쉬고 싶다.
258|
259|때맞춰 홍진이 간드러진 목소리로 끼어들었다.
260|
261|“전하, 제가 있으니 여기 진 공자는 그만 보내 주세요. 네?”
262|
263|그러나 주표는 고집스러운 얼굴로 날 바라볼 뿐이었다.
264|
265|“하면 언제쯤 그대를 다시 볼 수 있지?”
266|
267|“어, 글쎄요. 천 밤쯤 지나면?”
268|
269|“천 밤!”
270|
271|주표가 충격받은 얼굴로 외쳤다.
272|
273|약 3년. 이제 고작 열 살인 어린아이에겐 어마어마한 시간일 것이다.
274|
275|“그, 그렇게 바쁘단 말이냐?”
276|
277|“어른의 사정이란 것이 있습니다. 전하.”
278|
279|“허어어, 돌아가신 아바마마께서도 그 정도는 아니셨는데…….”
280|
281|상심이 매우 큰 모양이다. 고개를 푹 떨군 주표를 일으켜 세운 건 다음 순간 들려온 이풍의 한마디였다.
282|
283|“전하, 이렇게 하시는 것은 어떻겠습니까?”
284|
285|“뭘 말인가?”
286|
287|“보름 후 태원진가에서 성대한 연회가 열린다고 하니 전하께서 직접 태원진가를 방문하시는 겁니다.”
288|
289|“태원진가를?”
290|
291|“예. 산서에서 난다 긴다 하는 고수들이 모두 모일 테니 분명 흡족하실 겁니다.”
292|
293|주표의 눈동자가 반짝반짝 빛났다.
294|
295|“옳거니, 그런 방법이 있었구나!”
296|
297|“예, 전하.”
298|
299|“…….”
300|
301|아니, 이것들이 지금 무슨 얘기를 하고 있는 거야.
302|
303|초대도 안 했는데 아주 상상의 나래를 펼치고 있다. 그렇다고 오지 말라고 하면 일이 터질 기세라 그냥 고개를 끄덕이는 수밖에 없었다.
304|
305|“이 대협 말이 맞습니다. 그때 한번 놀러 오세요.”
306|
307|“그래도 될까?”
308|
309|참 일찍도 물어본다.
310|
311|나는 영업용 미소를 띠고 대답했다.
312|
313|“당연하죠. 제 형님들도 반가워할 겁니다.”
314|
315|“그, 그게 정말인가?”
316|
317|“네, 제 형님들이 누군지 아시죠? 둘째 형은 구면이실 거고.”
318|
319|“진천검?”
320|
321|해맑던 주표의 얼굴에 순간 먹구름이 꼈다.
322|
323|“그대의 둘째 형은 과인을 싫어한다. 삼 년 전에도 아무 말 없이 밥만 먹고 갔지. 무례하기까지 했어.”
324|
325|“……아무 말도 안 했다고요?”
326|
327|“그날에 대한 얘기는 더 이상하기 싫다.”
328|
329|홍진이 조그마한 목소리로 속삭였다.
330|
331|“전하께서 서명을 부탁하셨는데 단칼에 거절하더군요.”
332|
333|진무경이 초청을 받았던 게 3년 전이라고 했으니까…… 주표가 일곱 살 때다.
334|
335|세상에. 어떻게 일곱 살 어린애, 그것도 왕이 사인을 부탁하는데 딱 잘라 거절할 수 있지?
336|
337|‘그 인간도 어지간하네.’
338|
339|어떤 의미에서는 참 진무경답다.
340|
341|팬심이 무참히 짓밟힌 과거의 기억을 떠올린 주표는 말없이 손가락을 꼬물거렸다.
342|
343|가만히 보고 있자니 어쩐지 마음 한구석이 짠하다.
344|
345|“이번에 오시면 제가 부탁해서 서명 받아 드릴게요.”
346|
347|“헛. 정말?”
348|
349|“약속. 도장 꽝.”
350|
351|어리둥절해하는 녀석과 새끼손가락도 걸고 도장까지 찍었다.
352|
353|“이게 무엇이지?”
354|
355|“천지신명께 맹세한다. 뭐 그런 뜻입니다.”
356|
357|“오오!”
358|
359|주위에서는 황족이니, 왕이니 난리지만 역시 애는 애다.
360|
361|좋아서 어쩔 줄을 모르는 주표의 모습에 사람들도 흐뭇하게 웃었다.
362|
363|“전하께서 저렇게 기뻐하시는 모습은 오랜만에 봅니다.”
364|
365|“그러게요. 매일 재미없는 이 첨사만 상대하다가 오랜만에 활짝 웃으시네요.”
366|
367|“전 최선을 다한 것밖에 없습니다.”
368|
369|“최선이 꼭 최고의 결과를 만드는 건 아니죠. 그럴 수 있어요.”
370|
371|“도지휘동지!”
372|
373|“왜요, 도지휘첨사?”
374|
375|이풍과 홍진.
376|
377|사이가 좋은 건지, 나쁜 건지 도무지 종잡을 수 없는 두 사람이 티격태격할 때 청풍이 잔뜩 기대하는 얼굴로 주표에게 다가갔다.
378|
379|“저도, 저도 서명해 드릴까요?”
380|
381|“……당신 서명 처음 해 보지?”
382|
383|“헛. 어떻게 아셨어요? 오는 길에 쟁자수로 수결(手決)은 해 봤어도 서명은 처음인데.”
384|
385|“모르는 게 이상한 거 아냐?”
386|
387|저 기대하는 표정 봐라. 누군가에게 난생처음 서명을 해 주고 싶어서 안달이 난 표정이다.
388|
389|“저, 전 서명하면 안 되나요?”
390|
391|“아니. 맘대로 해. 서명해 드리면 전하께서 좋아하실걸.”
392|
393|하지만 주표의 반응은 예상 밖이었다.
394|
395|“서명? 그대가?”
396|
397|“네! 꼭 서명해 드리고 싶습니다!”
398|
399|“안 된다.”
400|
401|“왜, 왜요? 저희 할아버지 되게 유명한 분이시래요. 검성 못 들어 보셨어요?”
402|
403|“알지. 당연히 알지. 하지만…….”
404|
405|주표가 짐짓 단호한 얼굴로 고개를 저었다.
406|
407|“그대는 아직 별호가 없지 않나.”
408|
409|“네?”
410|
411|“나중에 멋있는 별호가 생기면 다시 오도록. 그땐 내 반드시 서명을 받도록 하지.”
412|
413|“…….”
414|
415|“…….”
416|
417|저거 네임드만 할 수 있는 거였구나.
```

## Assembled English

```markdown
[P1]
# Chapter 145

[P2]
Hong Jin let out a quiet laugh and tipped back his cup.

[P3]
“Our Young Master Jin is greedier than I thought.”

[P4]
“I’m about as greedy as anyone else. And I have a favor to ask. Could you just call me Young Master Jin?”

[P5]
“Oh my. Pretending you don’t like it when you do.”

[P6]
“Fucking hell…”

[P7]
“Hmm? What did you just say?”

[P8]
“Ah, I said it’s nice. Like we’re family.”

[P9]
“Family, huh? I like the sound of that. I’m already looking forward to meeting Lesser Family Head Jin.”

[P10]
Right. No matter how much I ran my mouth here, the final decision would come down to Jin Wikyung and Hong Jin.

[P11]
They were both practically professionals at this sort of thing. The amateur should know when to step aside.

[P12]
“By the way, what do you have against the Seongun Escort Bureau?”

[P13]
“I wouldn’t call it a grudge… I’m just giving someone I dislike an extra slap. The chance to pick up a few crumbs along the way doesn’t hurt either.”

[P14]
“Ah. Does this have something to do with the Young Bureau Head of the Seongun Escort Bureau who was supposed to come?”

[P15]
This man’s ability to read the room was anything but ordinary.

[P16]
He’d already figured out the gist of it, so there was no point explaining every little detail. I shrugged.

[P17]
“Something like that. How did you know?”

[P18]
“Young Master Jin, I lived in the imperial palace for over twenty years.”

[P19]
“Excuse me?”

[P20]
“I survived by reading the room. Reading children’s expressions is easy enough.”

[P21]
Hong Jin gestured with his chin toward the young prodigies of the Five Gates of Shanxi.

[P22]
At the far end of a table some distance away, they had been sneaking glances at us with frozen expressions. The moment they realized they’d been noticed, they flinched and shrank back.

[P23]
“They’ve been like that since they first came in. Carefully watching Young Master Jin’s every move.”

[P24]
“Really?”

[P25]
“Yes. They looked so pitiful that even I felt sorry for them. What on earth did you do?”

[P26]
“Something similar to what happened with the people who left earlier.”

[P27]
“The Three Hands of Zhongnan? Tsk, tsk. They failed to recognize who they were dealing with, didn’t they?”

[P28]
As expected, Hong Jin caught on at the slightest hint. He clicked his tongue in sympathy while Li Feng whipped his head around to stare at the young prodigies.

[P29]
His gaze seemed to say that he intended to remember exactly who had provoked Martial Uncle Cheongpung.

[P30]
“Gasp.”

[P31]
“A-Assistant Military Commissioner! No, Great Hero Li! It’s not like that…”

[P32]
Li Feng was not only a powerful figure in the Shanxi Province military but also a lay disciple of Huashan.

[P33]
The government and Murim might supposedly stay out of each other’s affairs, but getting entangled with him in the wrong way would make the future of the Five Gates of Shanxi very unpleasant.

[P34]
Leaving them as they hurriedly offered excuses, Li Feng asked me,

[P35]
“Could you tell me in detail what happened?”

[P36]
“It’s already over. The person involved even laid into them himself. What more is there to say?”

[P37]
“Laid into them?”

[P38]
“Ah, I mean he beat them up. They apologized first, of course.”

[P39]
“Martial Uncle did it himself? Hmm.”

[P40]
Strictly speaking, Cheongpung had only dealt with one of them, but he had beaten him all the same.

[P41]
Li Feng looked at the young prodigies with a much gentler gaze.

[P42]
“Do you understand what you did wrong?”

[P43]
“Yes, sir!”

[P44]
“We feel it in our bones!”

[P45]
Their booming replies erupted immediately. Li Feng’s position was one thing, but now they also knew who Cheongpung was. No wonder they were sweating bullets.

[P46]
Never mind that he was a Peak master. He was the Disciple of the Sword Saint and Huashan’s direct-line Disciple.

[P47]
*They’re completely fucked.*

[P48]
The Five Gates of Shanxi were ultimately just a collection of minor and mid-sized sects. If Huashan, one of the Nine Sects and One Gang, got angry, even their extended families might get beaten with a bat.

[P49]
No, they would be lucky if it ended there.

[P50]
“The conversations and events that took place here today…”

[P51]
Li Feng’s heavy voice had barely begun when the answers came flying out.

[P52]
“We’ll keep silent!”

[P53]
“We’ll take it to our graves!”

[P54]
“I’ve already forgotten everything!”

[P55]
“Where am I? Who am I?”

[P56]
*What a fucking performance.*

[P57]
As I watched an epidemic of amnesia break out before my eyes, I added one more thing.

[P58]
“Is that enough?”

[P59]
“Y-Yes?”

[P60]
“What do you mean…?”

[P61]
“What do you think I mean? If you want to be part of the family, put your spoon on the table too. You there. What does ‘family’ mean?”

[P62]
The young prodigy I had pointed at stammered out an answer.

[P63]
“People who eat together… Unless that’s wrong. Then I’m sorry.”

[P64]
“That’s right. So, how do you become family?”

[P65]
“Ah!”

[P66]
The young prodigy cried out and slapped his forehead.

[P67]
At least this one had some sense.

[P68]
“Then I’ll arrange somewhere nice for our next meeting. How does Honghwaru sound?”

[P69]
“……”

[P70]
What a complete blockhead.

[P71]
With heirs like these, I didn’t even need to look to know the state of the Five Gates of Shanxi. I heaved a deep sigh and spelled it out for him.

[P72]
“Forget Honghwaru. I’m telling you to do whatever our side tells you to do. For example, anything involving the Seongun Escort Bureau. Understand?”

[P73]
“Ohhh.”

[P74]
The Jin Family of Taiyuan had certainly become the greatest power in Shanxi, but if the minor sects united and resisted, it would inevitably become a nuisance.

[P75]
We belonged to the orthodox faction, after all. If we seized whatever we wanted and held people accountable like a band of mounted bandits, everyone would point fingers at us.

[P76]
In Murim, wasn’t legitimacy every bit as important as martial arts?

[P77]
*But if there’s no one to point fingers, it won’t be a problem.*

[P78]
I slowly took in the four men and women before me—the heirs of the four sects among the Five Gates of Shanxi, excluding the Seongun Escort Bureau.

[P79]
If they took the lead in supporting the Jin Family of Taiyuan, everything would become much easier.

[P80]
“When you’re eating, pay close attention to where you sit. That way, you can at least get a bite or two.”

[P81]
The Seongun Escort Bureau was supposedly one of the most prominent powers in the province, despite being located in a frontier region. It was more than enough of a feast to share around.

[P82]
At my words, the quick-witted one’s eyes quietly gleamed, while the clueless one cautiously opened his mouth.

[P83]
“Even so, that might be a little…”

[P84]
I cut the dim-looking bastard off without hesitation.

[P85]
“What sect are you from?”

[P86]
“M-Me?”

[P87]
“Yes, you.”

[P88]
After a long hesitation, he finally coughed up the name Gopyeong Sect.

[P89]
I vaguely recalled hearing it before, but it was some obscure sect I could barely remember. That was the extent of Gopyeong Sect’s standing.

[P90]
No, the same was true of every sect in the new Five Gates of Shanxi.

[P91]
“Gopyeong Sect. Gopyeong Sect… It doesn’t have a very pleasant ring to it. Should I recommend a new name?”

[P92]
“Excuse me?”

[P93]
I stared into the eyes of the bastard who still hadn’t caught on.

[P94]
“Starting next month, let’s begin again under a new name. The Gopyeong Branch of the Jin Family of Taiyuan. How does that sound?”

[P95]
“……!”

[P96]
“……!”

[P97]
“You don’t seem to like it. I was only joking, you idiot.”

[P98]
Of course, I wasn’t joking.

[P99]
I patted the deathly pale Young Sect Leader of Gopyeong Sect on the shoulder and swept my gaze across the room.

[P100]
“Is anyone here sworn brothers or sisters with Woo Jintae?”

[P101]
“N-No, sir.”

[P102]
“Or maybe you’ve been close since childhood, knowing each other for more than ten years? Betrothed before birth? There are plenty of possibilities.”

[P103]
“Absolutely not! Absolutely not. We’ve only spent time together a few times.”

[P104]
“I-I only received a few bolts of silk and a little jewelry…”

[P105]
“Then that settles it.”

[P106]
Clap!

[P107]
The sharp crack of my hands coming together made all four of them flinch.

[P108]
“Choose. Are you going to make enemies of the Jin Family of Taiyuan, Huashan, and the government, or…”

[P109]
I grinned and enunciated the final words clearly.

[P110]
“Are you going to abandon someone you aren’t even close to and share the feast with us?”

[P111]
Clap, clap, clap, clap.

[P112]
This time, it wasn’t me. Hong Jin was cackling and applauding.

[P113]
“Our Young Master Jin—I like you more and more every time I see you.”

[P114]
“……”

[P115]
*Please refrain from making such dangerous remarks, brother.*

[P116]
* * *

[P117]
“Are you leaving already?”

[P118]
His tone was still arrogant, but his voice and eyes brimmed with regret.

[P119]
*The more I see this kid, the cuter he gets.*

[P120]
I reached out to pat my little fanboy—no, Prince Shangshan Zhu Bao—on the head, only to lower my hand when I saw Li Feng’s expression.

[P121]
*Oh, right. He’s a king. And a member of the imperial family, at that.*

[P122]
“Ahem. I have urgent business to attend to.”

[P123]
“Can you not put it off?”

[P124]
“I’m sorry, but every moment counts.”

[P125]
“I see…”

[P126]
Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest.

[P127]
Right on cue, Hong Jin cut in with his delicate voice.

[P128]
“Your Highness, you have me, so please let Young Master Jin go now. All right?”

[P129]
But Zhu Bao merely stared at me, his expression stubborn.

[P130]
“Then when shall I be able to see you again?”

[P131]
“Hmm, I don’t know. After a thousand nights?”

[P132]
“A thousand nights!”

[P133]
Zhu Bao cried out in shock.

[P134]
That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time.

[P135]
“A-Are you truly that busy?”

[P136]
“There are such things as adult matters, Your Highness.”

[P137]
“Good heavens. Even my late father was never that busy…”

[P138]
He looked utterly crushed. Zhu Bao’s head drooped, only to shoot back up at Li Feng’s next words.

[P139]
“Your Highness, how about this?”

[P140]
“What do you mean?”

[P141]
“I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why not visit the Jin Family of Taiyuan in person?”

[P142]
“The Jin Family of Taiyuan?”

[P143]
“Yes. All the renowned masters of Shanxi will be gathered there, so I’m sure you’ll be pleased.”

[P144]
Zhu Bao’s eyes sparkled.

[P145]
“Of course! Why didn’t I think of that?”

[P146]
“Yes, Your Highness.”

[P147]
“……”

[P148]
What the hell were these two talking about?

[P149]
They hadn’t even been invited, yet here they were letting their imaginations run wild. But if I told him not to come, it felt as though something would explode, so all I could do was nod.

[P150]
“Great Hero Li is right. Come visit us then.”

[P151]
“Would that really be all right?”

[P152]
A little late to ask, wasn’t it?

[P153]
I put on my best customer-service smile.

[P154]
“Of course. My brothers will be happy to see you too.”

[P155]
“I-Is that really true?”

[P156]
“You know who my brothers are, don’t you? You’ve already met my second brother.”

[P157]
“The Heaven Shaking Sword?”

[P158]
A dark cloud suddenly fell over Zhu Bao’s bright, innocent face.

[P159]
“Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.”

[P160]
“He didn’t say a single word?”

[P161]
“I do not wish to speak of that day anymore.”

[P162]
Hong Jin whispered in a tiny voice,

[P163]
“His Highness asked him for an autograph, but he flatly refused.”

[P164]
Jin Mukyung had been invited three years ago, which meant…

[P165]
Zhu Bao had been seven at the time.

[P166]
Good grief. How could anyone flatly refuse a seven-year-old asking for an autograph—especially when that seven-year-old was a king?

[P167]
*That man really is something else.*

[P168]
In a way, it was very Jin Mukyung.

[P169]
Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers.

[P170]
Watching him, I felt a pang of sympathy.

[P171]
“If you come this time, I’ll ask him to give you his autograph.”

[P172]
“Really?”

[P173]
“Pinky promise. Seal it.”

[P174]
I hooked pinkies with the bewildered boy and even stamped our thumbs together.

[P175]
“What is this?”

[P176]
“It means I swear before the gods of heaven and earth. Something like that.”

[P177]
“Oh!”

[P178]
Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child.

[P179]
Everyone smiled fondly at the sight of Zhu Bao beside himself with delight.

[P180]
“It’s been a long time since I’ve seen His Highness this happy.”

[P181]
“I know. After dealing with this boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.”

[P182]
“I’ve done nothing but my best.”

[P183]
“Doing your best doesn’t always produce the best results. It happens.”

[P184]
“Deputy Military Commissioner!”

[P185]
“What is it, Assistant Military Commissioner?”

[P186]
Li Feng and Hong Jin.

[P187]
I could never tell whether the two of them got along or hated each other as they bickered back and forth.

[P188]
Meanwhile, Cheongpung approached Zhu Bao with anticipation written all over his face.

[P189]
“I-I could give you an autograph too?”

[P190]
“……”

[P191]
“You’ve never given anyone an autograph before, have you?”

[P192]
“Gasp. How did you know? I’ve left my hand mark as a porter on the way here, but this is my first autograph.”

[P193]
“Wouldn’t it be strange if I didn’t know?”

[P194]
Just look at that expectant face. He was dying to give someone his first-ever autograph.

[P195]
“C-Can’t I give him one?”

[P196]
“Sure. Do whatever you want. His Highness will probably be pleased.”

[P197]
But Zhu Bao’s reaction was unexpected.

[P198]
“An autograph? From you?”

[P199]
“Yes! I really want to give you my autograph!”

[P200]
“No.”

[P201]
“W-Why not? They say my grandfather is very famous. Haven’t you heard of the Sword Saint?”

[P202]
“I know. Of course I know. But…”

[P203]
Zhu Bao put on a deliberately stern expression and shook his head.

[P204]
“You don’t have a martial title yet, do you?”

[P205]
“Excuse me?”

[P206]
“Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.”

[P207]
“……”

[P208]
“……”

[P209]
*So this was something only named characters could do.*
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
# Chapter 145

[P2]
Hong Jin let out a quiet laugh and tilted his cup.

[P3]
“Our Young Master Jin, you’re greedier than I thought.”

[P4]
“I’m about as greedy as anyone else. And I have a favor to ask. Could you just call me Young Master Jin?”

[P5]
“Oh my, pretending you don’t like it when you do.”

[P6]
“Fucking hell…”

[P7]
“Hm? What did you say just now?”

[P8]
“Ah, I said it’s nice. It feels like family.”

[P9]
“Family, huh? That’s nice to hear. I’m already looking forward to meeting the Lesser Family Head Jin.”

[P10]
Right. No matter how much I talked in this room, the final decision would be made by Jin Wikyung and Hong Jin.

[P11]
Both of them were practically professionals in this area, so it was only proper for an amateur to step aside.

[P12]
“By the way, what grudge do you have against the Seongun Escort Bureau?”

[P13]
“It’s not quite a grudge… I’m just giving an extra slap to someone I dislike. And it doesn’t hurt that I can pick up a few crumbs along the way.”

[P14]
“Ah. Is this related to the Young Bureau Head of the Seongun Escort Bureau who was originally supposed to come?”

[P15]
This man’s instincts were anything but ordinary.

[P16]
Since he had already figured it out, there seemed to be no need to explain every little detail. I simply shrugged.

[P17]
“Something like that. How did you know?”

[P18]
“Young Master Jin, I’ve lived in the imperial palace for more than twenty years.”

[P19]
“Excuse me?”

[P20]
“I survived on my ability to read the room. Reading the expressions of children is easy enough.”

[P21]
Hong Jin gestured with his chin toward the young prodigies of the Five Gates of Shanxi.

[P22]
At the far end of a distant table, the young men and women had been sneaking glances our way with frozen expressions. They flinched and shrank back when they realized they had been noticed.

[P23]
“They’ve been like that since they first came in. Carefully watching Young Master Jin’s every move.”

[P24]
“Really?”

[P25]
“Yes. I almost felt sorry for them just watching. What on earth did you do?”

[P26]
“They had something similar happen with the people who left earlier.”

[P27]
“The Three Hands of Zhongnan? Tsk, tsk. They failed to recognize who they were dealing with, didn’t they?”

[P28]
As expected, Hong Jin understood everything with the slightest hint. He clicked his tongue sympathetically, while Li Feng abruptly turned his head and stared at the young prodigies.

[P29]
His eyes seemed to say he would remember exactly who had provoked Martial Uncle Cheongpung.

[P30]
“Gasp.”

[P31]
“Assistant Military Commissioner! No, Great Hero Li! It’s not like that…”

[P32]
Li Feng was not only a powerful figure in the Shanxi Province military but also a lay disciple of Huashan.

[P33]
Even though the government and Murim were supposed to remain separate, getting entangled with him in the wrong way would make the future of the Five Gates of Shanxi very unpleasant.

[P34]
Ignoring the young men as they hurriedly offered excuses, Li Feng asked me,

[P35]
“Could you tell me more about what happened?”

[P36]
“It’s all over now. The person involved even beat them himself. What more is there to say?”

[P37]
“Beat them himself?”

[P38]
“Ah, I mean he beat them up. Of course, they apologized before that.”

[P39]
“Martial Uncle did it himself? Hmm.”

[P40]
Strictly speaking, Cheongpung had only dealt with one of them, but he had beaten him all the same.

[P41]
Li Feng looked at the young prodigies with a much gentler gaze.

[P42]
“Do you understand what you did wrong?”

[P43]
“Yes, sir!”

[P44]
“We feel it in our bones!”

[P45]
Their booming replies erupted immediately. It wasn’t only Li Feng’s position that had them sweating bullets. They now knew Cheongpung’s identity as well.

[P46]
Putting aside the fact that he was a Peak master, he was the Disciple of the Sword Saint and Huashan’s direct Disciple.

[P47]
*They’re completely screwed.*

[P48]
The Five Gates of Shanxi were ultimately nothing more than a collection of minor sects. If Huashan, one of the Nine Sects and One Gang, got angry, even their extended families might get beaten with a bat.

[P49]
No, they would be lucky if it ended there.

[P50]
“The conversations and events that took place here today…”

[P51]
Li Feng’s heavy voice had barely begun when the answers came flying out.

[P52]
“We’ll keep silent!”

[P53]
“We’ll take it to our graves!”

[P54]
“I’ve already forgotten everything!”

[P55]
“Where are we? Who am I?”

[P56]
*They’re really putting on a fucking show.*

[P57]
As I watched an epidemic of amnesia break out before my eyes, I added one more thing.

[P58]
“Is that enough?”

[P59]
“Ex-Excuse me?”

[P60]
“What do you mean?”

[P61]
“What do I mean? If you want to become part of the family, you need to put your spoon in too. You there. What does ‘family’ mean?”

[P62]
The young prodigy I had pointed at stammered out an answer.

[P63]
“People who eat together… Unless that’s not it, in which case, I’m sorry.”

[P64]
“That’s right. Now, how do you become family?”

[P65]
“Ah!”

[P66]
The young prodigy slapped his forehead with a cry of realization.

[P67]
At least that one had some sense.

[P68]
“Then I’ll arrange a fine place for our next meeting. How about Honghwaru?”

[P69]
“……”

[P70]
What a complete idiot.

[P71]
With heirs like these, the state of the Five Gates of Shanxi was obvious without even looking. I let out a deep sigh and explained it simply.

[P72]
“Forget Honghwaru. I’m telling you to do whatever our side tells you to do. For example, anything involving the Seongun Escort Bureau. Understand?”

[P73]
“Ohhh.”

[P74]
The Jin Family of Taiyuan had certainly become the greatest power in Shanxi, but if the minor sects united and resisted, it would inevitably become a nuisance.

[P75]
We belonged to the orthodox faction, after all. If we seized whatever we wanted and held people accountable like a band of mounted bandits, everyone would point fingers at us.

[P76]
Wasn’t legitimacy just as important as martial arts in Murim?

[P77]
*But if there’s no one left to point fingers, it won’t be a problem.*

[P78]
I slowly took in the four men and women before me—the heirs of the four sects among the Five Gates of Shanxi, excluding the Seongun Escort Bureau.

[P79]
If they stepped forward and sided with the Jin Family of Taiyuan, things would become much easier.

[P80]
“When you’re eating, pay close attention to where you sit. That way, you can at least get a bite or two.”

[P81]
The Seongun Escort Bureau was supposedly one of the most prominent powers in the province, despite being located in a frontier region. It was more than enough of a feast to share around.

[P82]
At my words, the quick-witted one’s eyes quietly gleamed, while the clueless one cautiously opened his mouth.

[P83]
“Even so, that might be a little…”

[P84]
I cut off the dense-looking young man before he could finish.

[P85]
“What sect are you from?”

[P86]
“M-Me?”

[P87]
“Yes, you.”

[P88]
After a long hesitation, the name Gopyeong Sect finally came out.

[P89]
It was a name I vaguely recognized—a minor sect so obscure that I could barely remember hearing it. That was about the extent of Gopyeong Sect’s standing.

[P90]
No, that was true of all the sects in the new Five Gates of Shanxi.

[P91]
“Gopyeong Sect. Gopyeong Sect… It doesn’t have a very pleasant ring to it. Should I recommend a new name?”

[P92]
“Excuse me?”

[P93]
I stared into his eyes as he continued to fail to understand.

[P94]
“Starting next month, let’s begin again under a new name. The Gopyeong Branch of the Jin Family of Taiyuan. How does that sound?”

[P95]
“……!”

[P96]
“……!”

[P97]
“You don’t seem to like it. I was only saying it for fun, you idiot.”

[P98]
Of course, I hadn’t been saying it for fun.

[P99]
I patted the deathly pale Young Sect Leader of Gopyeong Sect on the shoulder and swept my gaze across the room.

[P100]
“Is anyone here sworn brothers or sisters with Woo Jintae?”

[P101]
“N-No, sir.”

[P102]
“Or perhaps you’ve been close friends since childhood, watching each other for more than ten years? Maybe you were betrothed before birth? There are plenty of possibilities.”

[P103]
“Absolutely not! Absolutely not. We’ve only spent time together a few times.”

[P104]
“I-I only received a few bolts of silk and a little jewelry…”

[P105]
“Then that settles it.”

[P106]
Clap!

[P107]
The sharp sound of my hands coming together made the four men and women flinch.

[P108]
“Choose. Are you going to make enemies of the Jin Family of Taiyuan, Huashan, and the government, or…”

[P109]
I grinned and enunciated the final words clearly.

[P110]
“Are you going to abandon someone you aren’t even close to and share the feast with us?”

[P111]
Clap, clap, clap, clap.

[P112]
This time, it wasn’t me. Hong Jin was laughing loudly and applauding.

[P113]
“Our Young Master Jin, I like you more and more every time I see you.”

[P114]
“……”

[P115]
*Brother, please refrain from making dangerous remarks.*

[P116]
* * *

[P117]
“Are you leaving already?”

[P118]
His tone was still arrogant, but his voice and eyes were filled with regret.

[P119]
*The more I see him, the cuter he gets.*

[P120]
I was about to pat the head of my little fanboy—no, Prince Shangshan Zhu Bao—when I lowered my hand under Li Feng’s gaze.

[P121]
*Oh, right. He was a king. And a member of the imperial family, at that.*

[P122]
“Ahem. I have some urgent business to attend to.”

[P123]
“Can you not put it off until later?”

[P124]
“I’m sorry, but it’s a matter where every moment counts.”

[P125]
“I see…”

[P126]
Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest.

[P127]
Right then, Hong Jin cut in with his delicate voice.

[P128]
“His Highness, I’m here, so please let Young Master Jin go now. All right?”

[P129]
But Zhu Bao only stared at me stubbornly.

[P130]
“Then when shall I be able to see you again?”

[P131]
“Hmm, I don’t know. After a thousand nights?”

[P132]
“A thousand nights!”

[P133]
Zhu Bao cried out with a shocked expression.

[P134]
That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time.

[P135]
“Are you truly that busy?”

[P136]
“There are such things as adult matters, Your Highness.”

[P137]
“Good heavens. Even my late father was never that busy…”

[P138]
He seemed deeply disheartened. Zhu Bao’s head drooped, but Li Feng’s next words made him straighten up again.

[P139]
“Your Highness, what do you think of this?”

[P140]
“What do you mean?”

[P141]
“I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why don’t you pay the Jin Family of Taiyuan a personal visit?”

[P142]
“The Jin Family of Taiyuan?”

[P143]
“Yes. All the masters who are famous throughout Shanxi will be gathered there, so I’m sure you’ll be pleased.”

[P144]
Zhu Bao’s eyes began to sparkle.

[P145]
“Of course! Why didn’t I think of that?”

[P146]
“Yes, Your Highness.”

[P147]
“……”

[P148]
What the hell were these two talking about?

[P149]
They hadn’t even been invited, yet they were spreading their wings and soaring through the realm of imagination. But if I told him not to come, it felt as though something would explode, so all I could do was nod.

[P150]
“Great Hero Li is right. Come visit us then.”

[P151]
“Would that really be all right?”

[P152]
He was asking rather late.

[P153]
I answered with a professional smile.

[P154]
“Of course. My brothers will be happy to see you too.”

[P155]
“Is that really true?”

[P156]
“You know who my brothers are, don’t you? You should already be acquainted with my second brother.”

[P157]
“Heaven Shaking Sword?”

[P158]
A dark cloud suddenly fell over Zhu Bao’s bright, innocent face.

[P159]
“Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.”

[P160]
“He didn’t say a single word?”

[P161]
“I do not wish to speak of that day anymore.”

[P162]
Hong Jin whispered in a tiny voice,

[P163]
“His Highness asked him for an autograph, but he flatly refused.”

[P164]
Jin Mukyung had said he was invited three years ago, so…

[P165]
Zhu Bao must have been seven at the time.

[P166]
Good grief. How could anyone flatly refuse when a seven-year-old child—an actual king, no less—asked for his autograph?

[P167]
*That man really is something.*

[P168]
In a way, it was very much like Jin Mukyung.

[P169]
Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers.

[P170]
Watching him, I felt a pang of sympathy.

[P171]
“If you come this time, I’ll ask him to give you his autograph.”

[P172]
“Really?”

[P173]
“Pinky promise. Seal it.”

[P174]
I even hooked pinkies with the bewildered boy and sealed our promise.

[P175]
“What is this?”

[P176]
“It means I swear before the gods of heaven and earth.”

[P177]
“Oh!”

[P178]
Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child.

[P179]
Seeing Zhu Bao so happy that he didn’t know what to do, everyone smiled fondly.

[P180]
“It’s been a long time since I’ve seen His Highness this happy.”

[P181]
“I know. After dealing with that boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.”

[P182]
“I’ve only been doing my best.”

[P183]
“Doing your best doesn’t always produce the best result. It happens.”

[P184]
“Deputy Military Commissioner!”

[P185]
“What is it, Assistant Military Commissioner?”

[P186]
Hong Jin and Li Feng.

[P187]
I could never tell whether the two of them got along or hated each other as they bickered back and forth.

[P188]
Meanwhile, Cheongpung approached Zhu Bao with an expectant expression.

[P189]
“Can I sign something for you too?”

[P190]
“……”

[P191]
“You’ve never signed your name before, have you?”

[P192]
“Gasp. How did you know? I’ve left my hand mark as a luggage porter before, but this is my first autograph.”

[P193]
“Wouldn’t it be strange if I didn’t know?”

[P194]
Just look at that eager expression. He looked desperate to give someone his very first autograph.

[P195]
“C-Can I not sign one?”

[P196]
“No. Do whatever you want. His Highness will be happy if you give him your autograph.”

[P197]
But Zhu Bao’s reaction was unexpected.

[P198]
“An autograph? Yours?”

[P199]
“Yes! I really want to give you my autograph!”

[P200]
“No.”

[P201]
“W-Why not? They say my grandfather is a very famous man. Haven’t you heard of the Sword Saint?”

[P202]
“I know. Of course I know. But…”

[P203]
Zhu Bao put on a deliberately stern expression and shook his head.

[P204]
“You don’t have a martial title yet, do you?”

[P205]
“Excuse me?”

[P206]
“Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.”

[P207]
“……”

[P208]
“……”

[P209]
*So this was something only named characters could do.*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 145,
  "passed": true,
  "metrics": {
    "source_characters": 5874,
    "translation_characters": 13415,
    "length_ratio": 2.284,
    "source_paragraphs": 206,
    "translation_paragraphs": 209
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "본가",
        "preferred": "our family / this family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
