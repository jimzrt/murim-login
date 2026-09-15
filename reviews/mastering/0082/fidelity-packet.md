# Fidelity Gate — Chapter 82

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
  1|＃82화
  2|
  3|
  4|
  5|총원 열다섯. 그중 절반에 가까운 숫자가 B급 헌터다 보니 게이트 등급을 감안해도 호화스러운 레이드 팀이 꾸려졌다.
  6|
  7|“원래 B급 헌터가 이렇게 흔했나?”
  8|
  9|나도 임꺽정의 말에 동의했다.
 10|
 11|“그러게요.”
 12|
 13|전에는 찾으려고 해도 옷깃이나 보일까 말까 했던 사람들이다. 나나 임꺽정과는 애초에 노는 물부터가 달랐으니까.
 14|
 15|“근데 태경이 넌 별 감흥이 없나 보다?”
 16|
 17|“저요?”
 18|
 19|“응. 아까 보니까 저쪽 팀장이랑도 얘기 잘하던데.”
 20|
 21|“그럴 수도 있죠. 그냥 잡담 좀 한 건데.”
 22|
 23|“그럴 수 있긴. 얼마 전만 해도 말 한번 붙여 보려면 고개 들다가 목 부러졌을 텐데.”
 24|
 25|그 정도였나? 문득 생각해 보니 임꺽정의 말이 틀리지 않았다. 단지 내가 달라졌을 뿐이다.
 26|
 27|‘서 있는 곳이 변하면 풍경도 변한다더니.’
 28|
 29|B급 헌터. 손을 뻗어도 닿지 않았던 산등성이들이 눈앞에 있다. 하지만 내가 생각한 풍경만큼 아름답지는 않았다.
 30|
 31|‘저 정도면 초일류? 아니, 일류 무인쯤 되려나.’
 32|
 33|기감으로 확인한 레벨도, 저들에게서 느껴지는 마나의 크기도 딱 그 정도다. 시스템의 사기성으로 무장한 나는 말할 것도 없고 동 레벨의 무인과 비교해서도 한 수 아래일 것이다.
 34|
 35|‘그게 무인과 헌터의 차이지.’
 36|
 37|각각 장단점이 있지만 맨몸으로 맞붙는다면 헌터의 필패다.
 38|
 39|무인들은 신체 내부의 기운을 효율적으로 사용할 수 있는 내공심법을 익혔고 그걸 무공을 통해 극대화시켰다.
 40|
 41|‘헌터가 장비를 맞추고 마법까지 사용해야 해볼 만하겠지.’
 42|
 43|결론은 간단하다. 개인 역량은 무인이, 집단으로서의 전투와 전술로는 헌터가 앞선다는 것.
 44|
 45|그리고…….
 46|
 47|‘나 완전 사기 캐릭터네.’
 48|
 49|나는 헌터이면서 무인, 무인이면서 헌터다. 같으면서 다른 두 가지 직업의 장점을 모두 갖고 있다.
 50|
 51|더 무서운 건 지금도 시스템을 통해 빠른 속도로 성장 중이라는 사실이다.
 52|
 53|‘이거 살짝 소설 속 주인공이 된 기분인데.’
 54|
 55|나중에 나이 먹고 은퇴하면 자서전이나 써 볼까.
 56|
 57|로그인 무림. 뭐 그런 제목으로.
 58|
 59|다른 사람이 보면 판타지 소설이 따로 없을 거다.
 60|
 61|“자, 집합! 지금부터 호명하는 포메이션으로 이동해 주세요.”
 62|
 63|들려오는 외침에 임꺽정이 심호흡했다.
 64|
 65|“이제 시작이구나.”
 66|
 67|임꺽정의 포지션은 탱커. 선두에서 팀을 지켜야 한다.
 68|
 69|B급 게이트가 주는 압박감일까, 언제나 웃음 짓던 얼굴이 딱딱하게 굳어 있었다.
 70|
 71|“내가 할 수 있을까?”
 72|
 73|나는 그의 어깨를 툭툭 두드려 주었다.
 74|
 75|“할 수 있어요.”
 76|
 77|빈말이 아니다. 지금 내 눈앞에 떠 있는 시스템창이 그 증거다.
 78|
 79|
 80|
 81|아이템창
 82|
 83|
 84|
 85|[투우사의 전신 갑옷]
 86|
 87|종류 : 갑옷
 88|
 89|등급 : 절정
 90|
 91|설명 : 투우사의, 투우사에 의한, 투우사를 위한 갑옷.
 92|
 93|효과 : 근력, 체력, 맷집 +10
 94|
 95|소(牛)형 몬스터 상대 시 능력치 모든 스탯 +20
 96|
 97|
 98|
 99|
100|
101|아이템창
102|
103|
104|
105|[투우사의 방패]
106|
107|종류 : 방패
108|
109|등급 : 절정
110|
111|설명 : 투우사의, 투우사에 의한, 투우사를 위한 방패. 소의 피로 붉게 물든 방패는 보기만 해도 섬뜩해진다.
112|
113|효과 : 근력, 체력, 맷집 +10
114|
115|소(牛)형 몬스터 상대 시 일정 확률로 [도발] 발동
116|
117|소(牛)형 몬스터 상대 시 일정 확률로 [환각] 발동
118|
119|
120|
121|
122|
123|‘솔직히 처음에는 무리라고 생각했는데.’
124|
125|이 정도면 안심이다. 적어도 이곳, 미노타우로스의 미로에서만큼은 훌륭한 탱커로 활약할 수 있을 것이다.
126|
127|“임 헌터님.”
128|
129|조용히 다가온 물주, 아니 최 팀장도 진지한 표정으로 입을 열었다.
130|
131|“조심히 입으세요. 제가 아끼는 컬렉션입니다.”
132|
133|“…….”
134|
135|“…….”
136|
137|거 되게 좋은 말 해 주네.
138|
139|
140|
141|* * *
142|
143|
144|
145|탱커인 임꺽정이 선두. 마법사인 김 집사와 힐러인 송이 씨가 후방으로 빠지자 내 곁에는 최 팀장밖에 남지 않았다.
146|
147|“……왜 그렇게 보십니까?”
148|
149|왜긴. 송이 씨랑 포지션을 좀 바꿨으면 해서 보는 거지.
150|
151|오순도순 옆에서 걸으면서 게이트 산책하면 얼마나 좋아. 몬스터 나오면 서로 구해 주기도 하고.
152|
153|‘하늘이 돕지 않는구나.’
154|
155|한탄하며 고개를 들어 봐도 축축한 동굴 천장밖에 보이지 않는다. 물론 F급 게이트와는 차원이 다른 높이였다.
156|
157|“확실히 엄청 크네요.”
158|
159|“B급 게이트니까요.”
160|
161|등급이 높은 게이트일수록 내부 공간이 넓고 출현하는 몬스터가 강력하다. 물론 나야 D급 게이트가 고작이라 더 높은 등급은 처음이지만 사람들이 그렇다더라.
162|
163|“어떤 경우에는 설산도 타야 합니다. 2년 전에 한 번 가 봤는데 끔찍했죠.”
164|
165|“아, 혹시 무슨 사고라도……?”
166|
167|“아뇨. 신고 간 부츠가 방수 마법이 안 걸려 있었어요.”
168|
169|“…….”
170|
171|“제가 수족냉증이 있어서.”
172|
173|“…….”
174|
175|“아, 둘 다 농담입니다.”
176|
177|당연히 농담이겠지. 60레벨이 넘는 인간이 수족냉증이라는 게 말이 되나. 내가 어이없는 표정으로 최 팀장을 바라보던 그때였다.
178|
179|……드득.
180|
181|“어?”
182|
183|“왜 그러십니까?”
184|
185|“잠시, 잠시만요.”
186|
187|단순한 착각? 아니다.
188|
189|동굴 바닥을 통해 감지되는 미세한 진동. 아주 짧은 순간이었지만 분명히 느꼈다.
190|
191|드드득.
192|
193|두 번째 진동은 보다 분명하고, 노골적이었다.
194|
195|몇몇은 이미 그 사실을 알아차리고 전방을 주시하기 시작했다. 임창수도 그중 하나였다.
196|
197|“전투 준비!”
198|
199|짤막한 외침은 신속하고 침착했다. 팀원 중 절반이 B급 헌터인 데다 훌륭한 장비까지 갖췄으니 그로서는 당황할 이유가 없었을 것이다. 한 가지 문제는…….
200|
201|“구멍 주시해!”
202|
203|여기가 미로라는 거다. 당장 뻥 뚫려 있는 구멍만 다섯 개.
204|
205|단순히 땅의 진동만으로는 놈들이 오는 정확한 방향을 찾기 힘들다.
206|
207|“어디냐!”
208|
209|“…….”
210|
211|임창수 쟤는 누구한테 물어보는 걸까. 저런다고 미노타우로스가 대답해 줄 것 같진 않은데.
212|
213|- 음모오오!
214|
215|“저기다! 맨 왼쪽 구멍!”
216|
217|“……실화냐.”
218|
219|보면서도 믿기지 않는 광경이다.
220|
221|나는 혀를 차며 창을 움켜쥐었다. [장인의 검은 가시 창]. 높은 확률로 적을 출혈 상태에 빠트릴 수 있는 흉악한 놈이다.
222|
223|“그립감이 참 좋죠? 마감제를 꼼꼼히 발라서…….”
224|
225|여기 흉악한 놈이 하나 더 있네. 만약 최 팀장이 죽는다면 발설지옥에 떨어지리란 걸 믿어 의심치 않는다.
226|
227|다음 순간.
228|
229|쿵쿵쿵.
230|
231|- 음모오오오오!
232|
233|놈들이 어둠 속에서 불쑥 솟구쳤다. 인간을 닮은 몸, 그러나 인간이라고 볼 수 없는 체격과 잔뜩 부풀어 오른 근육들.
234|
235|먼지와 누군가의 피로 얼룩진 두 개의 뿔 위에 직사각형의 레벨창이 두둥실 떠다녔다.
236|
237|
238|
239|[Lv.58 미노타우로스 전사]
240|
241|
242|
243|- 모오오오!
244|
245|영상으로 봤던 것보다 훨씬 박진감 넘치는 외관이긴 한데…….
246|
247|“에게.”
248|
249|“한 마리밖에 안 돼?”
250|
251|말 그대로 달랑 한 마리뿐이다. 알고 보면 저 미노타우로스도 미로에서 길을 잃은 게 아닐까.
252|
253|“저 정도면 원거리 지원 없이 처리해도 되겠는데요?”
254|
255|“혜린아, 오빠 잠깐 다녀올게.”
256|
257|상동 길드원들이 자신 있게 앞으로 나섰다. 탱커 둘에 딜러 둘. 모두 B급 헌터들이다. 여자들 앞에서 가오 좀 세워 보겠다는 의도가 뻔히 보였다.
258|
259|‘어이고, 병신들.’
260|
261|저런 놈들이 꼭 까불다가 골로 가더라. 물론 미노타우로스 한 마리에 그럴 일은 없겠지만.
262|
263|“할 거면 빨리 처리해.”
264|
265|임창수의 허락을 받은 네 사람이 무기를 빼 들고 몬스터를 향해 다가가던 그때였다.
266|
267|쿵. 쿵.
268|
269|“응?”
270|
271|- 음모오.
272|
273|다섯 개의 구멍 중 두 번째 구멍에서 미노타우로스 한 마리가 쏙 빠져나왔다.
274|
275|“오, 두 마리 됐다.”
276|
277|“쟤는 덩치가 좀 더 작네. 약할 것 같으니까 네가 맡아.”
278|
279|“뭐래, 제일 약골인 새끼가.”
280|
281|쿵. 쿵.
282|
283|- 음모오.
284|
285|세 번째 구멍.
286|
287|“오, 세 마리. 이 정도면 나름 재밌게 싸울 것 같은데?”
288|
289|“상처 하나라도 입는 놈이 오늘 술 사기. 어때?”
290|
291|“콜.”
292|
293|“콜. 이런 건 꼭 하자고 한 놈이 걸리더라.”
294|
295|쿵. 쿵.
296|
297|- 음모오.
298|
299|“아니, 시바. 뭐야, 이거.”
300|
301|“네 마리는 좀.”
302|
303|“그냥 우리끼리 포메이션 짜서 한 놈씩 처리하는 게 좋을 것 같은데.”
304|
305|“나도.”
306|
307|상황을 지켜보던 최 팀장이 목을 긁적였다.
308|
309|“좀 더 기다렸다가 작전을 짜는 게 나을 것 같은데.”
310|
311|“네?”
312|
313|“구멍이요. 왠지 더 나올 것 같지 않습니까?”
314|
315|“설마요. 무슨 올림픽 선수 소개도 아니고.”
316|
317|쿵쿵쿵쿵!
318|
319|진짜 왔네.
320|
321|5번 레인, 아니 다섯 번째 구멍에서도 소식이 왔다.
322|
323|한 가지 예상치 못한 부분이 있다면 이번에는 혼자가 아니라는 사실이다.
324|
325|- 음모오오오!
326|
327|친구도 많은 놈인지 자그마치 네 마리나 우르르 몰려왔다. 앞서 나온 놈들까지 모두 합하면 총 여덟 마리. B급 헌터 넷으로는 어림없는 숫자다. 최 팀장이 입을 열었다.
328|
329|“어떻게 생각하십니까?”
330|
331|“아마 힘들지 않을까요.”
332|
333|힘들긴 무슨, 뒈지기 싫으면 탱커 뒤에 있어야지.
334|
335|그나마 듣는 귀가 있어서 순화시킨 거다.
336|
337|“태경 씨라면 어떻겠습니까?”
338|
339|“저 말입니까?”
340|
341|“네. 태경 씨요.”
342|
343|“음.”
344|
345|B급 몬스터인 미노타우로스의 레벨은 50대 중후반.
346|
347|무인이라면 초일류에 가까운 레벨이지만 놈들과 싸운다면 여러 가지 변수를 고려해야 한다.
348|
349|간단하게 말해 붙어 봐야 안다는 거지.
350|
351|“잘 모르겠네요.”
352|
353|“잘 모르겠다…… 그거 아세요?”
354|
355|최 팀장이 묘한 눈빛으로 나를 응시했다.
356|
357|“보통 C급 헌터는 그렇게 대답 안 합니다. 방금 같은 질문에 고민하지도 않고, 진지하게 받아들이지도 않아요.”
358|
359|나도 모르게 가슴 한구석이 뜨끔 했다. 힘을 숨길 이유는 없지만 그렇다고 동네방네 자랑할 마음도 없었다.
360|
361|그저 아직은 주목을 피해 나만의 비밀로 남겨 두고 싶을 뿐이었다. 남들보다 약간 더 뛰어난 헌터. 딱 그 정도로.
362|
363|“전부터 알고 있었지만 참 흥미로운 사람입니다, 진태경 씨는.”
364|
365|“아니 저기, 팀장님. 뭔가 오해가 있으신 것 같은데.”
366|
367|내가 막 입을 연 그 순간이었다.
368|
369|“하하, 그러게요. 듣다 보니 나까지 흥미롭네.”
370|
371|불쑥 끼어든 임창수의 시선이 나와 최 팀장을 훑었다.
372|
373|“워낙 재미있는 얘기들을 하고 계셔서 좀 들었습니다. 괜찮으시죠?”
374|
375|너희가 안 괜찮으면 어쩔 건데, 라고 들리는 건 착각일까?
376|
377|“쥐뿔도 없는 C급 주제에 미노타우로스를 어쩌고저쩌고. 아주 소설을 쓰시던데.”
378|
379|아, 착각이 아니구나.
380|
381|나는 새삼스러운 눈으로 임창수를 바라봤다.
382|
383|‘어울리네.’
384|
385|사람마다 맞는 옷이 있다. 웃음도, 태도도.
386|
387|지금 내 눈에 비친 임창수가 그랬다. 한껏 올라간 입꼬리에 맺힌 비웃음이 아주 그냥, 찰떡이다.
388|
389|“기분을 상하게 할 의도는 없었습니다.”
390|
391|최 팀장 특유의 무덤덤한 표정과 말투에 임창수가 피식 웃었다.
392|
393|“상하고 말고 할 게 있나 사실인데, 뭘. 쟤들 실력 존나 구려요. 사람들이 B급, B급 해 주니까 있어 보이지, B급 중에서 보면 완전히 폐급이야. 그런데…….”
394|
395|임창수가 나를 턱짓했다.
396|
397|“C급보다는 낫지. 안 그래, 장태경 씨?”
398|
399|나는 아까부터 참고 있던 말을 꺼냈다.
400|
401|“진태경인데요.”
402|
403|“진태경이든 장태경이든. 당신 성이 뭐든 내 알 바 아니지.”
404|
405|“그럼 씹창수라고 불러 드려요?”
406|
407|“뭐?”
408|
409|“임창수든 씹창수든. 그쪽 성이 뭐든 내 알 바 아니잖아요.”
410|
411|임창수의 얼굴에서 웃음이 사라졌다.
```

## Assembled English

```markdown
[P1]
# Chapter 82

[P2]
Fifteen people in total. With nearly half of them B-rank Hunters, it had turned into a lavish raid team—even taking the Gate’s rank into account.

[P3]
“Were B-rank Hunters always this common?”

[P4]
I agreed with Im Kkeokjeong.

[P5]
“Seriously.”

[P6]
Before, even when I went looking for them, I had been lucky to catch a glimpse of their coat tails. They had always lived in a completely different world from people like Im Kkeokjeong and me.

[P7]
“But you don’t seem all that impressed, Taekyung.”

[P8]
“Me?”

[P9]
“Yeah. I saw you chatting pretty comfortably with that other Team Leader earlier.”

[P10]
“It happens. We were just making small talk.”

[P11]
“It happens, my ass. Not long ago, you would’ve broken your neck trying to look up high enough to talk to one of them.”

[P12]
*Was it really that bad?*

[P13]
Come to think of it, he wasn’t wrong. I was simply the one who had changed.

[P14]
*They say the scenery changes when you change where you stand.*

[P15]
B-rank Hunters. Mountain ridges I couldn’t reach even with my hand outstretched now stood right before me.

[P16]
But the scenery wasn’t as beautiful as I had imagined.

[P17]
*They’re around Top-tier? No, maybe First Rate martial artists.*

[P18]
Both the Levels I’d checked with Qi Sense and the amount of mana I felt from them put them at about that level. Needless to say, I was a cut above them, armed with the System’s cheat-like advantages. Even compared to martial artists of the same Level, they would probably be a step below.

[P19]
*That’s the difference between martial artists and Hunters.*

[P20]
Both sides had their strengths and weaknesses, but if they fought with nothing but their bodies, the Hunter would lose every time.

[P21]
Martial artists learned internal energy cultivation techniques that allowed them to efficiently use the qi within their bodies, then maximized its power through martial arts.

[P22]
*A Hunter would need proper equipment and magic to stand a chance.*

[P23]
The conclusion was simple. Martial artists had the advantage in individual ability, while Hunters were superior in group combat and tactics.

[P24]
And…

[P25]
*I’m a total cheat character.*

[P26]
I was both a Hunter and a martial artist—a martial artist and a Hunter. I possessed all the advantages of two classes that were alike yet fundamentally different.

[P27]
Even more frightening was the fact that I was still growing rapidly through the System.

[P28]
*I kind of feel like the protagonist of a novel.*

[P29]
Maybe I should write an autobiography when I got old and retired.

[P30]
*Login Murim.*

[P31]
Something like that for the title.

[P32]
To anyone else, it would sound like a fantasy novel.

[P33]
“Everyone, assemble! Move into the formation I call out!”

[P34]
At the shout, Im Kkeokjeong took a deep breath.

[P35]
“So it’s starting.”

[P36]
Im Kkeokjeong’s position was tank. He had to protect the team from the front.

[P37]
Maybe it was the pressure of a B-rank Gate, but his usually smiling face had gone stiff.

[P38]
“Can I do this?”

[P39]
I patted him on the shoulder.

[P40]
“You can.”

[P41]
I wasn’t just saying that to make him feel better. The System window floating before my eyes was proof.

[P42]
> **System**
>
> **Item Window**
>
> **Matador’s Full-Body Armor**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** Armor of the matador, by the matador, for the matador.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, All Stats +20.
>
> **Item Window**
>
> **Matador’s Shield**
>
> **Type:** Shield  
> **Grade:** Peak  
> **Description:** A shield of the matador, by the matador, for the matador. Dyed red with bull’s blood, it is eerie just to look at.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, has a chance to activate **Taunt**.  
> Against bovine-type monsters, has a chance to activate **Hallucination**.

[P43]
*Honestly, I thought it would be impossible at first.*

[P44]
But this was enough to put my mind at ease. At least here, in The Minotaur’s Labyrinth, Im Kkeokjeong would be able to perform admirably as a tank.

[P45]
“Hunter Im.”

[P46]
The sponsor—or rather, Team Leader Choi—approached quietly and spoke with a serious expression.

[P47]
“Put it on carefully. It’s part of my prized collection.”

[P48]
“…”

[P49]
“…”

[P50]
*He sure knows how to say something nice.*

[P51]
* * *

[P52]
Im Kkeokjeong took the lead as the tank. Once Butler Kim, the mage, and Miss Song-i, the healer, moved to the rear, only Team Leader Choi remained beside me.

[P53]
“…Why are you looking at me like that?”

[P54]
Why else? I wanted him to switch positions with Miss Song-i.

[P55]
How nice would it be to walk side by side, enjoying a pleasant stroll through the Gate? We could even save each other if monsters showed up.

[P56]
*The heavens clearly aren’t on my side.*

[P57]
Even when I raised my head in lament, all I saw was the damp cavern ceiling. Of course, it was incomparably higher than the ceiling of an F-rank Gate.

[P58]
“It’s definitely huge.”

[P59]
“It’s a B-rank Gate.”

[P60]
The higher a Gate’s rank, the larger its interior and the stronger the monsters that appeared within it. Of course, D-rank was as high as I’d ever gone, so this was my first time inside anything higher. That was what people said, anyway.

[P61]
“In some cases, you even have to climb a snow-covered mountain. I went once two years ago. It was horrible.”

[P62]
“Oh, was there some kind of accident?”

[P63]
“No. My boots weren’t enchanted with waterproofing.”

[P64]
“…”

[P65]
“I have cold hands and feet.”

[P66]
“…”

[P67]
“Ah, both of those were jokes.”

[P68]
Of course they were jokes. How could someone above Level 60 have cold hands and feet?

[P69]
I was staring at Team Leader Choi with an incredulous expression when—

[P70]
*Drrrk.*

[P71]
“Hm?”

[P72]
“Is something wrong?”

[P73]
“Wait. Just a moment.”

[P74]
Was I imagining things?

[P75]
No.

[P76]
A faint vibration had traveled through the cavern floor. It lasted only an instant, but I had definitely felt it.

[P77]
*Drrrk.*

[P78]
The second vibration was clearer and more obvious.

[P79]
Several people had already noticed it and begun watching the area ahead. Im Changsoo was one of them.

[P80]
“Prepare for battle!”

[P81]
His short shout was quick and composed. With half his team being B-rank Hunters and all of them equipped with excellent gear, he had no reason to panic.

[P82]
There was just one problem.

[P83]
“Watch the holes!”

[P84]
This was a labyrinth. There were five wide-open holes right in front of us.

[P85]
It was difficult to determine exactly where the monsters were coming from based on the vibrations in the ground alone.

[P86]
“Where are they?”

[P87]
“…”

[P88]
*Who is Im Changsoo asking? It’s not like the Minotaurs are going to answer him.*

[P89]
“—Moooooo!”

[P90]
“There! The hole on the far left!”

[P91]
“…Is this for real?”

[P92]
I could hardly believe the sight even as I watched it.

[P93]
I clicked my tongue and gripped my spear. The Masterwork Black Thorn Spear—a vicious weapon with a high chance of putting an enemy into the Bleeding Status.

[P94]
“Doesn’t the grip feel great? I applied the finishing coat very carefully—”

[P95]
*There’s another vicious thing here.*

[P96]
If Team Leader Choi died, I had no doubt he would fall straight into the tongue-pulling hell.[^1]

[P97]
The next moment—

[P98]
*Boom. Boom. Boom.*

[P99]
“—Mooooooo!”

[P100]
They burst out of the darkness.

[P101]
Their bodies resembled humans, but their physiques were too massive to be human, and their muscles were grotesquely swollen.

[P102]
A rectangular Level window floated above two horns stained with dust and someone’s blood.

[P103]
> **System**
>
> **Level 58 Minotaur Warrior**

[P104]
“—Moooooo!”

[P105]
They looked far more vivid and imposing in person than they had in the video, but…

[P106]
“That’s all?”

[P107]
“There’s only one?”

[P108]
There really was just one.

[P109]
*Could that Minotaur have gotten lost in the labyrinth, too?*

[P110]
“At that level, we should be able to handle it without ranged support, shouldn’t we?”

[P111]
“Hye-rin, I’ll be right back.”

[P112]
The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers, all of them B-rank Hunters.

[P113]
Their intention to show off in front of the women was painfully obvious.

[P114]
*Oh, you morons.*

[P115]
Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur.

[P116]
“If you’re going to do it, finish it quickly.”

[P117]
With Im Changsoo’s permission, the four men drew their weapons and started toward the monster.

[P118]
That was when—

[P119]
*Boom. Boom.*

[P120]
“Hm?”

[P121]
“—Moo.”

[P122]
A Minotaur popped out of the second of the five holes.

[P123]
“Oh, now there are two.”

[P124]
“That one’s a little smaller. It looks weaker, so you take it.”

[P125]
“What the hell are you saying? Says the weakest bastard here.”

[P126]
*Boom. Boom.*

[P127]
“—Moo.”

[P128]
The third hole.

[P129]
“Oh, three. At this rate, this might actually be a pretty fun fight.”

[P130]
“Anyone who gets so much as a scratch buys drinks tonight. How about it?”

[P131]
“I’m in.”

[P132]
“I’m in. The guy who suggests these things always ends up paying.”

[P133]
*Boom. Boom.*

[P134]
“—Moo.”

[P135]
“Ah, shit. What is this?”

[P136]
“Four might be a bit much.”

[P137]
“We should probably form up and take them out one at a time.”

[P138]
“Agreed.”

[P139]
Team Leader Choi, who had been watching the situation, scratched his neck.

[P140]
“Maybe we should wait a little longer before coming up with a strategy.”

[P141]
“Huh?”

[P142]
“The holes. Don’t you get the feeling more might come out?”

[P143]
“No way. It’s not like they’re introducing Olympic athletes.”

[P144]
*Boom-boom-boom-boom!*

[P145]
*He was right.*

[P146]
Lane five—no, the fifth hole—had news for us, too.

[P147]
The only unexpected part was that this time, it wasn’t alone.

[P148]
“—Moooooo!”

[P149]
Maybe it had a lot of friends. Four Minotaurs came stampeding out together.

[P150]
Including the ones that had already appeared, there were eight in total. Four B-rank Hunters had no chance against that many.

[P151]
Team Leader Choi spoke.

[P152]
“What do you think?”

[P153]
“It might be difficult.”

[P154]
*Difficult, my ass. If you don’t want to die, stay behind the tank.*

[P155]
I had toned it down for the benefit of the ears around us.

[P156]
“What about you, Mr. Taekyung?”

[P157]
“Me?”

[P158]
“Yes. You, Mr. Taekyung.”

[P159]
“Hmm.”

[P160]
Minotaurs were B-rank monsters, and their Levels were in the mid-to-late fifties.

[P161]
For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables.

[P162]
Simply put, I would have to fight them to know.

[P163]
“I’m not sure.”

[P164]
“You’re not sure… Do you know something?”

[P165]
Team Leader Choi stared at me with a strange look in his eyes.

[P166]
“Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.”

[P167]
I felt a sudden twinge of unease.

[P168]
I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood.

[P169]
For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all.

[P170]
“I’ve known this for a while, but you really are an interesting person, Jin Taekyung.”

[P171]
“No, wait, Team Leader. I think there may be some misunderstanding here.”

[P172]
I had just begun to speak when—

[P173]
“Haha, I see. Listening to you, even I’m getting interested.”

[P174]
Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me.

[P175]
“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

[P176]
*Was it my imagination, or did that sound like “If you do mind, what are you going to do about it?”*

[P177]
“For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.”

[P178]
*Ah. So I wasn’t imagining it.*

[P179]
I looked at Im Changsoo with fresh eyes.

[P180]
*It suits him.*

[P181]
Everyone had clothes that suited them. The same went for smiles and attitudes.

[P182]
That was how Im Changsoo looked to me now. The mockery gathered in the raised corners of his mouth suited him perfectly. It was practically made for him.

[P183]
“I didn’t mean to offend you.”

[P184]
At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh.

[P185]
“Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank. Among B-ranks, they’re complete bottom-of-the-barrel trash. But…”

[P186]
Im Changsoo jerked his chin toward me.

[P187]
“They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?”

[P188]
I finally said what I had been holding back all this time.

[P189]
“It’s Jin Taekyung.”

[P190]
“Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.”

[P191]
“Then should I call you Shit Changsoo?”

[P192]
“What?”

[P193]
“Im Changsoo or Shit Changsoo. I don’t care what your surname is either.”

[P194]
The smile disappeared from Im Changsoo’s face.

[P195]
[^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.
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
# Chapter 82

[P2]
Fifteen people in total. With nearly half of them being B-rank Hunters, it had turned into a lavish raid team—even taking the Gate’s Grade into account.

[P3]
“Were B-rank Hunters always this common?”

[P4]
I agreed with Im Kkeokjeong.

[P5]
“Exactly.”

[P6]
Before, even when I went looking for them, I had been lucky to catch a glimpse of their coat tails. They had always lived in a completely different world from people like Im Kkeokjeong and me.

[P7]
“But you don’t seem all that impressed, Taekyung.”

[P8]
“Me?”

[P9]
“Yeah. I saw you talking pretty comfortably with that other team leader earlier.”

[P10]
“I suppose I can do that. We were just making small talk.”

[P11]
“You suppose? Not long ago, you would’ve broken your neck just trying to raise your head high enough to talk to one of them.”

[P12]
*Was it really that bad?*

[P13]
Come to think of it, he wasn’t wrong. I was simply the one who had changed.

[P14]
*They say the scenery changes when you change where you stand.*

[P15]
B-rank Hunters. Mountain ridges that I couldn’t reach even by stretching out my hand were now right in front of me.

[P16]
But the scenery wasn’t as beautiful as I had imagined.

[P17]
*They’re around Top-tier? No, maybe First Rate martial artists.*

[P18]
Their Levels, which I had checked with Qi Sense, and the amount of mana I felt from them were both right around that level. Needless to say, I was a cut above them, armed with the System’s cheat-like advantages. Even compared to martial artists of the same Level, they would probably be a step below.

[P19]
*That’s the difference between martial artists and Hunters.*

[P20]
Both sides had their strengths and weaknesses, but if they fought with nothing but their bodies, the Hunter would lose every time.

[P21]
Martial artists learned cultivation techniques that allowed them to use the qi inside their bodies efficiently, then maximized it through martial arts.

[P22]
*A Hunter would have a chance only after equipping proper gear and using magic, too.*

[P23]
The conclusion was simple. Martial artists had the advantage in individual ability, while Hunters were superior in group combat and tactics.

[P24]
And…

[P25]
*I’m a total cheat character.*

[P26]
I was a Hunter and a martial artist, a martial artist and a Hunter. I possessed all the advantages of two different classes that were alike and yet completely different.

[P27]
The frightening part was that I was still growing at an incredible speed through the System.

[P28]
*This feels a little like becoming the protagonist of a novel.*

[P29]
Maybe I should write an autobiography after I got old and retired.

[P30]
*Login Murim.*

[P31]
Something like that for the title.

[P32]
To anyone else, it would sound like a fantasy novel.

[P33]
“Everyone, assemble! Move according to the formation I call out from now on!”

[P34]
At the shout, Im Kkeokjeong took a deep breath.

[P35]
“So it’s starting.”

[P36]
Im Kkeokjeong’s position was tank. He had to protect the team from the front line.

[P37]
Maybe it was the pressure of a B-rank Gate. His face, which was always smiling, had hardened.

[P38]
“Can I do this?”

[P39]
I patted him on the shoulder.

[P40]
“You can.”

[P41]
I wasn’t saying it just to make him feel better. The System window floating before my eyes was proof.

[P42]
> **System**
>
> **Item Window**
>
> **Matador’s Full-Body Armor**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** Armor of the matador, by the matador, for the matador.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, All Stats +20.

[P43]
> **System**
>
> **Item Window**
>
> **Matador’s Shield**
>
> **Type:** Shield  
> **Grade:** Peak  
> **Description:** A shield of the matador, by the matador, for the matador. Dyed red with bull’s blood, it is eerie just to look at.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, has a chance to activate **Taunt**.  
> Against bovine-type monsters, has a chance to activate **Hallucination**.

[P44]
*Honestly, I thought it would be impossible at first.*

[P45]
But this was enough to put my mind at ease. At least here, in The Minotaur’s Labyrinth, Im Kkeokjeong would be able to perform admirably as a tank.

[P46]
“Hunter Im.”

[P47]
The sponsor—or rather, Team Leader Choi—approached quietly and spoke with a serious expression.

[P48]
“Put it on carefully. It’s part of my prized collection.”

[P49]
“……”

[P50]
“……”

[P51]
*He sure knows how to say something nice.*

[P52]
* * *

[P53]
Im Kkeokjeong took the lead as the tank. Once Butler Kim, the mage, and Miss Song, the healer, moved to the rear, only Team Leader Choi remained beside me.

[P54]
“……Why are you looking at me like that?”

[P55]
Why else? I wanted him to switch positions with Miss Song.

[P56]
Wouldn’t it be nice to walk side by side, enjoying a pleasant stroll through the Gate? We could even save each other if monsters showed up.

[P57]
*The heavens clearly aren’t helping me.*

[P58]
Even when I tilted my head up in lament, all I could see was the damp ceiling of the cavern. Of course, the ceiling was incomparably higher than in an F-rank Gate.

[P59]
“It’s definitely huge.”

[P60]
“It’s a B-rank Gate.”

[P61]
The higher the Grade of a Gate, the larger its internal space and the stronger the monsters that appeared inside. D-rank was as high as I’d ever gone myself, so this was my first time seeing anything higher. That was what people said, anyway.

[P62]
“In some cases, you even have to climb a snow-covered mountain. I went once two years ago. It was horrible.”

[P63]
“Oh, did some kind of accident happen?”

[P64]
“No. The boots I wore weren’t enchanted with waterproofing.”

[P65]
“……”

[P66]
“I have cold hands and feet.”

[P67]
“……”

[P68]
“Ah, both of those were jokes.”

[P69]
Of course they were jokes. How could someone above Level 60 have cold hands and feet? I was staring at Team Leader Choi with an incredulous expression when—

[P70]
*Drrrk.*

[P71]
“Hm?”

[P72]
“Is something wrong?”

[P73]
“Wait. Just a moment.”

[P74]
Was I imagining things? No.

[P75]
There had been a faint vibration beneath the cavern floor. It had lasted only a brief moment, but I had definitely felt it.

[P76]
*Drrrk.*

[P77]
The second vibration was clearer and more obvious.

[P78]
Several people had already noticed it and begun watching the area ahead. Im Changsoo was one of them.

[P79]
“Prepare for battle!”

[P80]
His short shout was quick and composed. With half his team being B-rank Hunters and all of them equipped with excellent gear, he had no reason to panic.

[P81]
There was just one problem.

[P82]
“Watch the holes!”

[P83]
This was a labyrinth. There were five wide-open holes right in front of us.

[P84]
It was difficult to determine exactly where the monsters were coming from based on the vibrations in the ground alone.

[P85]
“Where are they?”

[P86]
“……”

[P87]
*Who is Im Changsoo asking? It’s not like the Minotaurs are going to answer him.*

[P88]
“—Moooooo!”

[P89]
“There! The hole on the far left!”

[P90]
“……Is this for real?”

[P91]
It was a sight I could hardly believe even while watching it.

[P92]
I clicked my tongue and gripped my spear. The Masterwork Black Thorn Spear—a vicious weapon with a high chance of inflicting Bleeding on its enemies.

[P93]
“Doesn’t the grip feel great? I applied the finishing coat very carefully—”

[P94]
*There’s another vicious thing here.*

[P95]
If Team Leader Choi died, I had no doubt he would fall straight into the tongue-pulling hell.[^1]

[P96]
The next moment—

[P97]
*Boom. Boom. Boom.*

[P98]
“—Mooooooo!”

[P99]
They burst out of the darkness.

[P100]
Their bodies resembled humans, but their physiques were too massive to be human, and their muscles were grotesquely swollen.

[P101]
Rectangular Level windows floated above two horns stained with dust and someone’s blood.

[P102]
> **System**
>
> **Level 58 Minotaur Warrior**

[P103]
“—Moooooo!”

[P104]
They looked far more vivid and imposing in person than they had in the video, but…

[P105]
“That’s all?”

[P106]
“There’s only one?”

[P107]
There really was just one.

[P108]
*Could that Minotaur have gotten lost in the labyrinth, too?*

[P109]
“At that level, we should be able to deal with it without ranged support, shouldn’t we?”

[P110]
“Hye-rin, I’ll be right back.”

[P111]
The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers. All of them were B-rank Hunters.

[P112]
Their intention to show off in front of the women was painfully obvious.

[P113]
*Oh, you morons.*

[P114]
Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur.

[P115]
“If you’re going to do it, finish it quickly.”

[P116]
With Im Changsoo’s permission, the four men drew their weapons and started toward the monster.

[P117]
That was when—

[P118]
*Boom. Boom.*

[P119]
“Hm?”

[P120]
“—Moo.”

[P121]
A Minotaur popped out of the second of the five holes.

[P122]
“Oh, now there are two.”

[P123]
“That one’s a little smaller. It looks weaker, so you take it.”

[P124]
“What the hell are you saying? Says the weakest bastard here.”

[P125]
*Boom. Boom.*

[P126]
“—Moo.”

[P127]
The third hole.

[P128]
“Oh, three. At this rate, this might actually be a pretty fun fight.”

[P129]
“Anyone who takes even one wound buys drinks tonight. How about it?”

[P130]
“I’m in.”

[P131]
“I’m in. The guy who suggests these things always ends up paying.”

[P132]
*Boom. Boom.*

[P133]
“—Moo.”

[P134]
“Ah, shit. What is this?”

[P135]
“Four might be a bit much.”

[P136]
“We should probably form up and take them out one at a time.”

[P137]
“Me too.”

[P138]
Team Leader Choi, who had been watching the situation, scratched his neck.

[P139]
“Maybe we should wait a little longer and come up with a strategy.”

[P140]
“Huh?”

[P141]
“The holes. Don’t you get the feeling more might come out?”

[P142]
“No way. It’s not like they’re introducing Olympic athletes.”

[P143]
*Boom-boom-boom-boom!*

[P144]
*He was right.*

[P145]
Lane five—no, the fifth hole—had news for us, too.

[P146]
The only unexpected part was that this time, it wasn’t alone.

[P147]
“—Moooooo!”

[P148]
Maybe it had a lot of friends. Four Minotaurs came stampeding out together.

[P149]
Including the ones that had appeared earlier, there were eight in total.

[P150]
Four B-rank Hunters had no chance against that number. Team Leader Choi spoke.

[P151]
“What do you think?”

[P152]
“It might be difficult.”

[P153]
*Difficult, my ass. If you don’t want to die, stay behind the tank.*

[P154]
I had toned it down for the benefit of the ears around us.

[P155]
“What about you, Mr. Taekyung?”

[P156]
“Me?”

[P157]
“Yes. You, Mr. Taekyung.”

[P158]
“Hmm.”

[P159]
The Minotaur, a B-rank monster, was in the mid-to-late fifties in Level.

[P160]
For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables.

[P161]
Simply put, I would have to fight them to know.

[P162]
“I’m not sure.”

[P163]
“You’re not sure…… Do you know something?”

[P164]
Team Leader Choi stared at me with a strange look in his eyes.

[P165]
“Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.”

[P166]
I felt a sudden twinge of unease.

[P167]
I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood.

[P168]
For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all.

[P169]
“I’ve known this for a while, but you really are an interesting person, Jin Taekyung.”

[P170]
“No, wait, Team Leader. I think there may be some misunderstanding here.”

[P171]
I had just begun to speak when—

[P172]
“Haha, I see. Listening to you, even I’m getting interested.”

[P173]
Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me.

[P174]
“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

[P175]
*If we minded, what exactly would you do about it?*

[P176]
“For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.”

[P177]
*Ah. So I wasn’t imagining it.*

[P178]
I looked at Im Changsoo with fresh eyes.

[P179]
*It suits him.*

[P180]
Everyone had clothes that suited them. The same went for smiles and attitudes.

[P181]
That was Im Changsoo in front of me. The mockery gathered in the corners of his raised mouth suited him perfectly. It was practically made for him.

[P182]
“I didn’t mean to offend you.”

[P183]
At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh.

[P184]
“Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank, but among B-ranks, they’re complete bottom-of-the-barrel trash. But……”

[P185]
Im Changsoo jerked his chin toward me.

[P186]
“They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?”

[P187]
I finally said what I had been holding back since earlier.

[P188]
“It’s Jin Taekyung.”

[P189]
“Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.”

[P190]
“Then should I call you Shit Changsoo?”

[P191]
“What?”

[P192]
“Im Changsoo or Shit Changsoo. I don’t care what your surname is, either.”

[P193]
The smile disappeared from Im Changsoo’s face.

[P194]
[^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 로그인              | **Login**                      |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 아이템창 | **Item Window** | System window displaying an item's details. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 82,
  "passed": true,
  "metrics": {
    "source_characters": 5429,
    "translation_characters": 12413,
    "length_ratio": 2.286,
    "source_paragraphs": 194,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀가",
        "preferred": "your family"
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
        "korean": "화시",
        "preferred": "fire arrow"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
