# Fidelity Gate — Chapter 136

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
  1|＃136화
  2|
  3|
  4|
  5|“끄응.”
  6|
  7|“으으으.”
  8|
  9|신음을 흘리던 두 사람의 시선이 부딪쳤다. 엉덩이를 훤히 드러낸 채 엎드린 서로의 모습을 마주 보니 민망하면서도 묘한 동질감이 들었다.
 10|
 11|“커흠. 정 소협, 상처는 어떠시오?”
 12|
 13|“크흠. 뭐 그럭저럭. 갈 소협은?”
 14|
 15|“난 죽을 것 같, 헉!”
 16|
 17|“사실 본인도 마찬가지, 윽!”
 18|
 19|말하다 보니 또 고통이 찾아왔다. 두 사람은 눈물을 찔끔 흘리며 중얼거렸다.
 20|
 21|“재수가 없어도 정도가 있지. 하고 많은 사람 중에 하필이면 산서잠룡이라니.”
 22|
 23|“그러게 말입니다. 살면서 이런 수모를 겪을 줄이야.”
 24|
 25|분위기는 침울했다.
 26|
 27|기라성 같은 문파들이 즐비한 중원(中原)이라면 모를까, 변방에 속하는 산서성에서는 두 사람 모두 침 좀 뱉고 방귀깨나 뀌는 문파의 후계자들이었다.
 28|
 29|살면서 아쉬운 소리 한번 해 본 적 없었는데 지금은 흠씬 두들겨 맞고 침상에 누워 앓는 소리를 내고 있다.
 30|
 31|“항산검문이 건재할 때만 하더라도 산서오문이 이 정도는 아니었는데…….”
 32|
 33|“그때가 좋았지요.”
 34|
 35|몇 달 전이라면 산서오문을 필두로 중소 문파 연합이 목소리를 낼 수 있었겠지만, 이제는 찍소리도 못 한다. 산서 무림의 균형이 깨진 것이다.
 36|
 37|항산검문이 몰락한 이상, 산서 무림의 무게 추는 태원진가로 기울 수밖에 없다.
 38|
 39|“아버지께서 아시면 절 죽이실 겁니다.”
 40|
 41|“이하 동문이오. 그리 신신당부하셨는데 이런 일이 생긴 줄 아시면. 으으, 생각하기도 싫소.”
 42|
 43|자그마치 백 명이 넘어가는 사람들 앞에서 그런 개망신을 당했으니. 곧 다가올 원단쯤에는 산서 전역에 소문이 퍼져 있을 것이 분명했다.
 44|
 45|“마음 같아서는 멀리 도망치고 싶소.”
 46|
 47|“도망이고 나발이고, 내일 걸을 수나 있을지 모르겠습니다. 그렇다고 성주의 부름을 거절할 수도 없고…….”
 48|
 49|“다리가 부러져도 일단 가야지 어쩌겠소? 그냥 성주도 아니고 황족(皇族)인데.”
 50|
 51|“그래야죠. 그나마 얼굴은 멀쩡해서 다행입니다.”
 52|
 53|“그러게 말이오.”
 54|
 55|두 사람의 시선이 자연스럽게 옆으로 옮겨 갔다.
 56|
 57|죽은 듯이 누운 우진태의 얼굴은 말벌 떼에게 쏘인 것처럼 부풀어 있었다. 간혹 힘겹게 내쉬는 숨이 아니었다면 이미 죽었다고 생각했을 거다.
 58|
 59|“아무리 그래도 그렇지, 사람을 어찌 저렇게 팰 수가 있답니까?”
 60|
 61|“산서잠룡이 이 정도로 잔인한 놈일 줄은 몰랐소.”
 62|
 63|“그나마 미리 머리를 박고 있어서 망정이지, 저희도 우 형님과 같은 꼴이 날 뻔했습니다.”
 64|
 65|“충분히 그러고도 남지. 여인들도 가차 없이 두들겨 패는 놈 아니오?”
 66|
 67|일행 중에는 여인이 둘이나 끼어 있었다. 사내라면 젊고 아름다운 여인들 앞에서 마음이 약해질 법도 한데, 진태경이라는 놈의 반응은 예상을 뛰어넘었다.
 68|
 69|
 70|
 71|‘나이.’
 72|
 73|‘네, 네?’
 74|
 75|‘나이. 몇 살이냐고.’
 76|
 77|‘여, 열일곱인데요.’
 78|
 79|‘넌?’
 80|
 81|‘저, 저는 열여덟이어요.’
 82|
 83|
 84|
 85|열일곱, 열여덟. 꽃다운 나이다. 슬슬 혼사 이야기가 오고 가도 이상하지 않을 나이이기도 했다.
 86|
 87|모두 진태경이 혹 여인들에게 관심이 있는 건가, 생각하던 그때였다.
 88|
 89|
 90|
 91|‘엉덩이 더 높이 들어. 뼈 나간다.’
 92|
 93|빡! 빡!
 94|
 95|‘머리에 피도 안 마른 것들이! 벌써부터 술을 마시고!’
 96|
 97|빡! 빡!
 98|
 99|‘마실 거면 숨어서 곱게 마시든가! 가만히 있는 사람한테 시비를 걸고!’
100|
101|빡! 빡!
102|
103|‘인성이 덜 됐어! 너희 같은 것들 때문에 체벌이 필요한 거야! 알아, 몰라!’
104|
105|빡! 빡!
106|
107|‘교권 향상! 어느 정도의 체벌은 반드시 필요하다!’
108|
109|빡! 빡! 빡!
110|
111|
112|
113|방금의 일을 떠올린 두 사람이 몸을 부르르 떨었다.
114|
115|한 명은 혼절했고, 다른 한 명은 사람들 앞에서 눈물 콧물을 쏙 뺐다.
116|
117|그 많은 사람 앞에서 외간 남자에게 엉덩이를 흠씬 두들겨 맞았으니 혼삿길 막히는 건 시간문제일 거다.
118|
119|“도대체 교권 향상이 무슨 말이오? 맹자에 나오는 말인가?”
120|
121|“저도 모릅니다. 심지어 한 대 더 때리지 않았습니까.”
122|
123|“악랄한 놈…….”
124|
125|“그래도 저는 다른 분들이 부럽습니다.”
126|
127|“아니, 그건 또 무슨 천인공노할 소리요? 지금 엉덩이에 피멍 잔뜩 든 거 안 보이시오?”
128|
129|“다른 분들은 최소한 산서잠룡한테 맞지 않았습니까. 저는 웬 거지 같은 놈한테…… 크흑!”
130|
131|“아, 저런.”
132|
133|“차라리 산서잠룡한테 맞았으면 변명이라도 하지, 어디서 굴러먹다 왔는지 모르는 비루먹은 놈이 제 엉덩이를……. 무슨, 돈도 아니고 매질을 빌린답니까?”
134|
135|치욕감에 턱이 파르르 떨렸다. 진태경에게 검갑을 양도받더니 신나게 후려치던 거지꼴의 사내가 생각나서다.
136|
137|
138|
139|‘와, 이거 재밌네요! 엉덩이 탄력이 좋으신데요?’
140|
141|빡! 빡! 빡!
142|
143|‘아프세요? 얼마나 아프세요? 혹시 괜찮으시다면 더 세게 때려도 될까요? 제가 이런 경험은 처음이라 힘 조절이 미숙해도 이해해 주세요!’
144|
145|빡! 빡! 빡!
146|
147|
148|
149|죽기 직전까지, 아니 죽어서도 잊지 못할 치욕의 순간을 경험했다. 마음 같아서는 놈의 머리부터 발끝까지 잘근잘근 씹어 삼켜도 성치 않았다.
150|
151|“그놈은 절대 용서할 수 없습니다!”
152|
153|“걱정 마시오. 내 힘닿는 데까지 정 소협을 돕겠소!”
154|
155|그들이 누군가, 산서오문의 후계자들이다. 태원진가의 진태경이라면 몰라도 젊은 거지 하나쯤은 충분히 처리할 수 있을 만한 힘을 가졌다.
156|
157|“저기 그런데…….”
158|
159|“예?”
160|
161|“그놈, 확실히 거지 맞소? 겁이 나서 그러는 것이 아니라, 이번에 산서잠룡 일도 그렇고, 만전을 기해서 손해 볼 것 없다는 생각이 갑자기 드는데…….”
162|
163|“……그럼 좀 더 알아볼까요?”
164|
165|“그, 그럽시다.”
166|
167|세상 물정 모르던 금수저들이 줄빠따를 맞고 경각심을 갖게 됐다.
168|
169|
170|
171|* * *
172|
173|
174|
175|교육이 마무리된 뒤 우리는 객실로 자리를 옮기기로 했다.
176|
177|1층에 계속 머무르기엔 주위 손님들의 시선이 아무래도 신경 쓰였기 때문이다.
178|
179|사람들의 주목에 어깨 으쓱하는 것도 한두 번 잠깐이지, 이런 상황에서 뭘 먹었다가는 음식이 입으로 들어가는지 코로 들어가는지도 헷갈릴 거다.
180|
181|“홍화객잔을 책임지고 있는 석 모라고 합니다. 편하게 석 총관이라고 불러 주십시오.”
182|
183|산서잠룡 이름값이 좋긴 좋다. 지금까지 털끝 하나 보이지 않던 총관이라는 자가 와서 고개를 숙일 정도면.
184|
185|‘이 양반도 하오문 소속이겠지?’
186|
187|홍화루는 하오문 산서 총지부장인 월화가 거점으로 삼은 곳이고, 홍화객잔은 이름에서 알 수 있듯이 그 하부 조직이나 다름없다.
188|
189|어쩌면 이 사람은 내가 홍화객잔에 발을 들이기 전부터 나의 존재를 알고 있었을 것이다.
190|
191|‘썩 유쾌한 기분은 아닌데.’
192|
193|보이지 않는 시선들이 내 일거수일투족을 감시한다고 생각하는 건 좀 과민 반응인가?
194|
195|하지만 그렇다고 마냥 불쾌하지는 않다.
196|
197|그저 약간의 경계심이랄까. 지금까지는 확실히 우호적인 관계를 맺어 왔지만, 앞으로의 상황이 어떻게 될지는 아무도 모르는 거니까.
198|
199|“따로 조용한 자리를 마련해 두었습니다.”
200|
201|“오, 좋죠.”
202|
203|알아서 서비스해 준다는데 거절할 이유가 없다. 총관을 따라 발걸음을 옮기려던 그때였다.
204|
205|“지금까지 감사했습니다, 은인.”
206|
207|목소리를 따라 고개를 돌리자 천진난만한 웃음을 머금고 있는 청풍이 보였다.
208|
209|“그게 무슨 말이에요? 설마 이대로 가시려고?”
210|
211|“네. 밤도 늦었으니 저는 이만 가 보려고요.”
212|
213|가긴 어딜 가. 중간에 웬 잡것들이 끼어드는 바람에 대화도 제대로 못 했는데. 나는 황급히 손을 내저었다.
214|
215|“에헤이, 밤이 늦었으면 하룻밤 묵고 가셔야지. 여비도 없다면서요?”
216|
217|“괜찮아요. 노숙은 익숙해서요.”
218|
219|“익숙하면 안 되죠. 그렇지, 새로운 경험! 객잔에서 자 본 적 있어요?”
220|
221|“여비를 잃어버리기 전에 객잔에서 몇 번 묵었어요. 그리고 지금까지 두 분께 신세 진 것으로도 족합니다.”
222|
223|옆에 있던 혁무진이 중얼거렸다.
224|
225|“그렇긴 하지. 내 빙당호로…….”
226|
227|“넌 조용히 하고. 그래서 정말 가시게요?”
228|
229|“예. 다행히 아직 산서성에 볼일이 남았으니 기회가 된다면 다시 뵐 수 있을 거예요.”
230|
231|이쯤 되니 할 말이 없다. 절정 고수가 제 발로 떠나겠다는데 밤길이 험하다고 붙잡을 수도 없는 것 아닌가.
232|
233|다만 갑자기 튀어나온 이 별종의 정체가 아직도 궁금하기 짝이 없었다.
234|
235|“혹시 갈 곳 없으면 태원진가로 오세요. 제 이름 대면 통과시켜 줄 테니까.”
236|
237|“아, 그러고 보니 태원진가의 공자셨죠. 산서잠룡 진태경…… 은인의 이름을 기억해 두겠습니다.”
238|
239|아까부터 내 신분을 알고 있었음에도 별 동요가 없다. 아, 그렇구나. 딱 이 정도 반응이다.
240|
241|혁무진이 은근슬쩍 눈치를 주며 끼어들었다.
242|
243|“태원진가. 모르시오?”
244|
245|“글쎄요. 어디서 들어 본 것 같기도 하고. 귀에 익긴 한데 잘은 모르겠어요.”
246|
247|잠시 갸웃거리던 청풍이 우리를 향해 고개를 숙였다.
248|
249|“인연이 닿으면 다시 뵙겠지요. 그럼 이만.”
250|
251|나는 진한 아쉬움을 담아 인사했다.
252|
253|“조심히 가세요. 태원진가 꼭 잊지 마시고.”
254|
255|“하하, 당연하죠.”
256|
257|그가 시원한 웃음과 함께 돌아서자, 대화가 마무리됐다고 생각한 총관이 입을 열었다.
258|
259|“그럼 별채로 모시겠습니다.”
260|
261|“아, 네. 무진아, 가자.”
262|
263|“오오, 그 유명하다는 홍화객잔의 별채에서 잘 수 있는 겁니까?”
264|
265|“봉황객잔에서도 별채에 묵었는데 뭘 새삼스럽게.”
266|
267|“무슨 소리십니까. 봉황객잔이 후기지수라면 홍화객잔은 이미 명성이 알려진 절정 고수. 특히 온천(溫泉)은 고관대작들도 한 번씩 다녀갈 정도의 명소지요.”
268|
269|“온천?”
270|
271|“저도 풍문으로만 들었는데, 극락이 따로 없답니다.”
272|
273|총관이 잔잔한 목소리로 덧붙였다.
274|
275|“저희 아버님께서 올해 팔순이신데, 한 번 오셨다가 극락으로 떠나실 뻔했습니다.”
276|
277|“……그거 위험한 거 아니에요?”
278|
279|“그만큼 좋다는 거지요. 아직 정정하십니다.”
280|
281|“아, 예. 장수하셨으면 좋겠네요.”
282|
283|온천이라…….
284|
285|사우나는 자주 갔어도 온천은 한 번도 못 가 봤다. 뜨뜻한 물에 몸을 푹 담글 생각을 하니 벌써 설렌다.
286|
287|“크흠. 그럼 가 볼까?”
288|
289|“제가 모시겠습니다.”
290|
291|총관을 따라 발걸음을 옮기려던 순간, 단단한 손아귀가 내 어깨를 덥석 붙잡았다.
292|
293|“저어. 지금 온천이라고 하셨어요?”
294|
295|“……아직 안 가셨어요?”
296|
297|헤헤 웃는 청풍을 보며 확신했다.
298|
299|이 자식이 온천은 처음이라는 것에 불알 두 쪽 건다.
300|
301|
302|
303|* * *
304|
305|
306|
307|이른 새벽, 아직 어둠이 짙게 깔린 저택의 연무장에는 한 사람이 검을 휘두르고 있었다.
308|
309|이제 서른은 되었을까? 강건한 이목구비가 인상적인 사내였다.
310|
311|쉬쉬쉭!
312|
313|막힘없이 찌르고, 베고, 휘두른다. 초식과 초식이 바람에 꽃잎 휘날리는 듯 부드럽게 이어졌다.
314|
315|어느덧 팔 성에 이른 칠매검(七梅劍)이 서늘한 새벽 공기를 가르고 있을 때, 전령(傳令) 하나가 대문을 열고 들어왔다.
316|
317|“무슨 일이냐? 수련 중에는 출입을 금하였거늘.”
318|
319|“송구합니다. 허나 상산왕(上山王) 전하께서 말씀을 전하라 하셔서…….”
320|
321|“전하께서?”
322|
323|“예. 금일 정오에 있을 오찬에 참석하라는 왕명이십니다.”
324|
325|“오찬이라면…… 무림의 후기지수들이 온다는 그 자리냐?”
326|
327|“옛.”
328|
329|사내는 한숨을 푹 내쉬었다. 그는 정삼품 도지휘첨사(都指揮僉事)로, 관작으로 치면 능히 산서성에서 다섯 손가락 안에 꼽히는 인물이었다.
330|
331|‘전하의 명이라 거절할 수도 없고. 이것 참.’
332|
333|도지휘첨사는 결코 한가한 직위가 아니었다. 군사들의 훈련을 책임져야 하는 막중한 자리.
334|
335|그러나 성주이자 고귀한 핏줄을 타고난 상산왕의 명령이다. 사내는 별수 없이 고개를 끄덕였다.
336|
337|“왕명을 받들겠다고 전하여라.”
338|
339|“충!”
340|
341|전령이 떠나자 사내는 도로 검을 들었다.
342|
343|다시 펼치기 시작한 칠매검에선 오래전 떠나온 화산(華山)의 매화가 피어오르는 듯했다.
```

## Assembled English

```markdown
[P1]
# Chapter 136

[P2]
“Ugh.”

[P3]
“Gnnngh.”

[P4]
The two men’s eyes met as they groaned. Seeing each other lying face down with their bare buttocks exposed was embarrassing, yet it also gave them a strange sense of solidarity.

[P5]
“Ahem. Young Hero Jeong, how are your wounds?”

[P6]
“Ahem. More or less. How about you, Young Hero Gal?”

[P7]
“I feel like I’m going to die—hngh!”

[P8]
“Actually, so do I—ngh!”

[P9]
The pain returned as they spoke. Both men blinked back tears and muttered,

[P10]
“There’s bad luck, and then there’s this. Of all the people we could have run into, why did it have to be the Sleeping Dragon of Shanxi?”

[P11]
“I know. I never thought I’d suffer this kind of humiliation in my lifetime.”

[P12]
The mood was gloomy.

[P13]
Things might have been different in the Central Plains, where countless prestigious sects stood shoulder to shoulder. But in borderland Shanxi Province, both men were heirs to sects big enough to swagger around spitting and farting as they pleased.

[P14]
They had never once had to humble themselves before anyone. Now they lay groaning in bed after being thoroughly beaten.

[P15]
“Even when the Mount Heng Sword Sect was still standing, the Five Gates of Shanxi weren’t reduced to this…”

[P16]
“Those were the days.”

[P17]
A few months ago, the alliance of small and medium-sized sects led by the Five Gates of Shanxi could still have made its voice heard. Now, they couldn’t even squeak. The balance of Shanxi Murim had been shattered.

[P18]
With the fall of the Mount Heng Sword Sect, the balance of power in Shanxi Murim was bound to tilt toward the Jin Family of Taiyuan.

[P19]
“My father will kill me if he finds out.”

[P20]
“Same here. He warned me so many times. If he finds out this happened… Ugh. I don’t even want to think about it.”

[P21]
They had been publicly humiliated in front of more than a hundred people. By around New Year’s Day, the rumor would certainly have spread throughout all of Shanxi.

[P22]
“If I had my way, I’d run far away.”

[P23]
“To hell with running away. I don’t even know if I’ll be able to walk tomorrow. But I can’t refuse the City Lord’s summons, either…”

[P24]
“Even if our legs are broken, we still have to go. What else can we do? He isn’t just some ordinary City Lord. He’s a member of the imperial family.”

[P25]
“That’s true. At least our faces are fine.”

[P26]
“They are.”

[P27]
Their gazes naturally shifted to the side.

[P28]
Woo Jintae lay there as though dead, his face swollen like he had been stung by a swarm of wasps. If not for the occasional labored breath, they would have thought he was already dead.

[P29]
“Still, how could anyone beat a man that badly?”

[P30]
“I never knew the Sleeping Dragon of Shanxi was this vicious.”

[P31]
“Thank goodness we planted our heads on the floor beforehand. We almost ended up just like Brother Woo.”

[P32]
“He absolutely would have done it. Isn’t he the bastard who beats women without mercy, too?”

[P33]
There were two women in their group. A man might be expected to go soft in front of young, beautiful women, but that bastard Jin Taekyung’s reaction had gone far beyond anything they expected.

[P34]
“Age.”

[P35]
“Y-yes?”

[P36]
“Age. How old are you?”

[P37]
“I-I’m seventeen.”

[P38]
“And you?”

[P39]
“I-I’m eighteen.”

[P40]
Seventeen and eighteen. They were in the flower of youth, old enough that it wouldn’t have been strange for talk of marriage to begin.

[P41]
Just as everyone wondered whether Jin Taekyung might be interested in the women—

[P42]
“Lift your butt higher. You’ll break a bone.”

[P43]
*Whack! Whack!*

[P44]
“You kids are still wet behind the ears! And you’re already drinking!”

[P45]
*Whack! Whack!*

[P46]
“If you’re going to drink, hide somewhere and do it quietly! Don’t pick a fight with someone who was minding his own business!”

[P47]
*Whack! Whack!*

[P48]
“You haven’t learned how to behave! People like you are exactly why corporal punishment is necessary! Do you understand or not?”

[P49]
*Whack! Whack!*

[P50]
“Improve teacher authority! A certain amount of corporal punishment is absolutely necessary!”

[P51]
*Whack! Whack! Whack!*

[P52]
The two men shuddered at the memory.

[P53]
One woman had fainted, while the other had wept until tears and snot streamed down her face in front of everyone.

[P54]
After having their buttocks thoroughly beaten by a man outside their families in front of so many people, it was only a matter of time before their marriage prospects were ruined.

[P55]
“What in the world does ‘improve teacher authority’ mean? Is it something from Mencius?”

[P56]
“I don’t know, either. He even hit them one extra time.”

[P57]
“What a vicious bastard…”

[P58]
“Even so, I envy the others.”

[P59]
“What kind of outrageous thing is that to say? Can’t you see that your butt is covered in bruises?”

[P60]
“At least the others were beaten by the Sleeping Dragon of Shanxi. I was beaten by some beggar-looking bastard… Sob!”

[P61]
“Oh, that’s awful.”

[P62]
“If I’d been beaten by the Sleeping Dragon of Shanxi, at least I could make excuses. But some mangy bastard who crawled in from who-knows-where beat my butt… Who borrows a beating instead of money?”

[P63]
His chin trembled with humiliation as he remembered the beggar-like man taking the sword case from Jin Taekyung and gleefully laying into him.

[P64]
“Wow, this is fun! Your butt has some great bounce!”

[P65]
*Whack! Whack! Whack!*

[P66]
“Does it hurt? How much does it hurt? If you don’t mind, may I hit you harder? This is my first time doing something like this, so please understand if I’m not very good at controlling my strength!”

[P67]
*Whack! Whack! Whack!*

[P68]
He had suffered a humiliation he would never forget until the day he died—or even after. He wanted to chew that bastard up from head to toe and swallow him piece by piece, and even that wouldn’t have been enough.

[P69]
“I will never forgive that bastard!”

[P70]
“Don’t worry. I’ll do everything in my power to help you, Young Hero Jeong!”

[P71]
Who were they? They were heirs to the Five Gates of Shanxi. Jin Taekyung of the Jin Family of Taiyuan might be beyond their reach, but they certainly had enough power to deal with one young beggar.

[P72]
“Um, about that…”

[P73]
“Yes?”

[P74]
“Are you certain he’s really a beggar? I’m not saying this because I’m afraid, but after what happened with the Sleeping Dragon of Shanxi, it occurs to me that there’s no harm in being thorough…”

[P75]
“…Should we look into him a little more?”

[P76]
“Y-yes. Let’s do that.”

[P77]
One group beating had taught the pampered rich kids to be cautious.

[P78]
* * *

[P79]
Once the lesson was over, we decided to move to a private room.

[P80]
Staying on the first floor meant enduring the stares of all the surrounding guests.

[P81]
Basking in people’s attention was fun for a moment or two, but if I tried to eat like this, I’d probably lose track of whether the food was going into my mouth or up my nose.

[P82]
“My name is Seok, and I oversee Honghwa Inn. Please feel free to call me Chief Steward Seok.”

[P83]
The Sleeping Dragon of Shanxi’s reputation really was something. The chief steward, who hadn’t shown so much as a hair until now, had come out personally to bow to me.

[P84]
*This man must be part of the Lower District Sect, too, right?*

[P85]
Honghwaru served as the base of Wolhwa, Chief Branch Leader of the Lower District Sect in Shanxi, and judging by its name, Honghwa Inn was practically a subordinate organization.

[P86]
He might even have known about my existence before I set foot inside Honghwa Inn.

[P87]
*I can’t say that makes me feel particularly good.*

[P88]
Was it overreacting to think that unseen gazes were monitoring my every move?

[P89]
Still, I wasn’t exactly offended.

[P90]
It was more like a little caution. We had certainly maintained a friendly relationship until now, but no one knew what might happen in the future.

[P91]
“I’ve prepared a separate, quiet place for you.”

[P92]
“Oh, that sounds good.”

[P93]
They were offering us special treatment without even being asked, so there was no reason to refuse. I was about to follow the chief steward when—

[P94]
“Thank you for everything, Benefactor.”

[P95]
I turned toward the voice and found Cheongpung smiling innocently.

[P96]
“What do you mean? Surely you aren’t planning to leave just like this?”

[P97]
“Yes. It’s already late, so I was thinking of heading out.”

[P98]
*Going where? We barely got to talk because those random bastards barged in.*

[P99]
I hurriedly waved him off.

[P100]
“Come on, if it’s late, you should stay the night. You said you don’t have any travel money, right?”

[P101]
“It’s all right. I’m used to sleeping rough.”

[P102]
“You shouldn’t be used to that. Right, a new experience! Have you ever slept at an inn?”

[P103]
“I stayed at inns a few times before I lost my travel money. And I’ve already imposed on you both more than enough.”

[P104]
Hyuk Mujin muttered beside me.

[P105]
“That’s true. My candied hawthorn skewers[^1]…”

[P106]
[^1]: Traditional fruit skewers coated in hardened sugar.

[P107]
“You be quiet. So, are you really leaving?”

[P108]
“Yes. Fortunately, I still have business left in Shanxi Province, so if we happen to get the chance, we’ll meet again.”

[P109]
At this point, I had nothing left to say. If a Peak master was determined to leave of his own accord, I couldn’t exactly hold him back by claiming the roads were dangerous at night.

[P110]
Still, I was dying to know the identity of this oddball who had suddenly appeared out of nowhere.

[P111]
“If you have nowhere to go, come to the Jin Family of Taiyuan. Give them my name and they’ll let you in.”

[P112]
“Oh, come to think of it, you’re a Young Master of the Jin Family of Taiyuan, aren’t you? The Sleeping Dragon of Shanxi, Jin Taekyung… I’ll remember my Benefactor’s name.”

[P113]
He had known who I was for some time, but it hadn’t fazed him in the slightest. His reaction amounted to, *Oh, I see.* That was it.

[P114]
Hyuk Mujin subtly caught my eye before cutting in.

[P115]
“The Jin Family of Taiyuan. You don’t know it?”

[P116]
“Well, I think I’ve heard of it somewhere. It does sound familiar, but I don’t really know much about it.”

[P117]
Cheongpung tilted his head for a moment, then bowed to us.

[P118]
“If fate brings us together, we’ll meet again. Then I’ll be off.”

[P119]
I bid him farewell with deep regret.

[P120]
“Take care. And don’t forget the Jin Family of Taiyuan.”

[P121]
“Haha, of course I won’t.”

[P122]
He turned away with a hearty laugh. Thinking the conversation was over, the chief steward spoke.

[P123]
“Then I’ll escort you to the annex.”

[P124]
“Ah, yes. Mujin, let’s go.”

[P125]
“Oh! We get to sleep in the annex of the famous Honghwa Inn?”

[P126]
“We stayed in the annex at Phoenix Inn, too. Why are you acting like this is something new?”

[P127]
“What are you talking about? If Phoenix Inn is a young prodigy, then Honghwa Inn is a Peak master whose fame is already known. Its hot springs, in particular, are such a renowned attraction that even high officials and nobles visit them.”

[P128]
“Hot springs?”

[P129]
“I’ve only heard about them from rumors, but they say there’s no paradise like it.”

[P130]
The chief steward added calmly,

[P131]
“My father is turning eighty this year. He came here once and nearly departed for paradise.”

[P132]
“…Isn’t that dangerous?”

[P133]
“It only means the hot springs are that good. He’s still hale and hearty.”

[P134]
“Ah, I see. I hope he lives a long life.”

[P135]
Hot springs…

[P136]
I had gone to saunas plenty of times, but I had never visited a hot spring. Just thinking about sinking into pleasantly hot water already had me excited.

[P137]
“Ahem. Shall we go?”

[P138]
“I’ll escort you.”

[P139]
I was just about to follow the chief steward when a firm hand suddenly seized my shoulder.

[P140]
“Um. Did you just say hot springs?”

[P141]
“…You haven’t left yet?”

[P142]
Looking at Cheongpung’s sheepish grin, I was certain of one thing.

[P143]
I’d bet both my balls this bastard had never been to a hot spring.

[P144]
* * *

[P145]
In the early dawn, while darkness still lay thick over the estate’s training ground, a man was swinging a sword.

[P146]
He looked to be about thirty. His strong, rugged features were striking.

[P147]
*Swish, swish, swish!*

[P148]
He thrust, slashed, and swung without pause. Each form flowed smoothly into the next, like flower petals fluttering in the wind.

[P149]
As the Seven Plum Sword, in which he had reached eight-tenths mastery, cut through the chilly dawn air, a messenger opened the main gate and entered.

[P150]
“What is it? I forbade anyone from entering while I’m training.”

[P151]
“My apologies. But His Highness Prince Shangshan ordered me to deliver a message…”

[P152]
“His Highness?”

[P153]
“Yes. His Highness commands you to attend today’s luncheon at noon.”

[P154]
“The luncheon… You mean the gathering where the young prodigies of Murim are coming?”

[P155]
“Yes, sir.”

[P156]
The man let out a deep sigh. He was a Third-Rank Assistant Military Commissioner, an official who could easily be counted among the five highest-ranking figures in Shanxi Province.

[P157]
*I can’t refuse an order from His Highness. What a nuisance.*

[P158]
The position of Assistant Military Commissioner was by no means an idle one. It was a weighty office responsible for training the soldiers.

[P159]
But the order had come from Prince Shangshan, the City Lord and a man of royal blood. The man had no choice but to nod.

[P160]
“Tell His Highness that I accept the royal command.”

[P161]
“Yes, sir!”

[P162]
After the messenger departed, the man raised his sword once more.

[P163]
As he resumed the Seven Plum Sword, the plum blossoms of Huashan, which he had left long ago, seemed to bloom from his blade.
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
# Chapter 136

[P2]
“Ugh.”

[P3]
“Gnnngh.”

[P4]
The two men’s eyes met as they groaned. Seeing each other lying face down with their bare buttocks exposed was embarrassing, but it also gave them a strange sense of solidarity.

[P5]
“Ahem. Young Hero Jeong, how are your wounds?”

[P6]
“Ahem. More or less. How about you, Young Hero Gal?”

[P7]
“I feel like I’m going to die, hngh!”

[P8]
“Actually, same here, ngh!”

[P9]
The pain returned as they spoke. Both men blinked back tears and muttered,

[P10]
“There’s bad luck, and then there’s this. Out of all the people in the world, we had to run into the Sleeping Dragon of Shanxi.”

[P11]
“I know. I never thought I’d suffer this kind of humiliation in my lifetime.”

[P12]
The mood was gloomy.

[P13]
In the Central Plains, where countless prestigious sects stood shoulder to shoulder, things might have been different. But out in borderland Shanxi Province, both men were heirs to sects big enough to swagger around spitting and farting as they pleased.

[P14]
They had never once had to ask anyone for a favor or lower themselves in their entire lives. Now they were lying on a bed, groaning after being thoroughly beaten.

[P15]
“Even when the Mount Heng Sword Sect was still standing, the Five Gates of Shanxi weren’t like this…”

[P16]
“Those were the days.”

[P17]
A few months ago, the Five Gates of Shanxi and the alliance of small and medium-sized sects could still have made their voices heard. Now, they couldn’t even squeak. The balance of Shanxi Murim had been shattered.

[P18]
With the fall of the Mount Heng Sword Sect, the balance of power in Shanxi Murim was bound to tilt toward the Jin Family of Taiyuan.

[P19]
“My father will kill me if he finds out.”

[P20]
“Same here. He warned me so many times. If he finds out this happened… Ugh. I don’t even want to think about it.”

[P21]
They had been publicly humiliated in front of more than a hundred people. By around New Year’s Day, the rumor would certainly have spread throughout all of Shanxi.

[P22]
“If I had my way, I’d run far away.”

[P23]
“To hell with running away. I don’t even know if I’ll be able to walk tomorrow. But I can’t refuse the City Lord’s summons, either…”

[P24]
“Even if our legs are broken, we have to go. What else can we do? He isn’t just some ordinary City Lord. He’s a member of the imperial family.”

[P25]
“That’s true. At least our faces are fine.”

[P26]
“They are.”

[P27]
Their eyes naturally shifted to the side.

[P28]
Woo Jintae lay there as though dead, his face swollen like he had been stung by a swarm of wasps. If not for the occasional labored breath, they would have thought he was already dead.

[P29]
“Still, how could anyone beat a person like that?”

[P30]
“I never knew the Sleeping Dragon of Shanxi was this vicious.”

[P31]
“Thank goodness we planted our heads on the floor beforehand. We almost ended up just like Brother Woo.”

[P32]
“He absolutely would have done it. Isn’t he the bastard who beats women without mercy, too?”

[P33]
There were two women among their group. A man might be expected to go soft in front of young, beautiful women, but that bastard Jin Taekyung’s reaction had gone far beyond anyone’s expectations.

[P34]
“Age.”

[P35]
“Y-yes?”

[P36]
“Age. How old are you?”

[P37]
“I-I’m seventeen.”

[P38]
“And you?”

[P39]
“I-I’m eighteen.”

[P40]
Seventeen. Eighteen. They were both at the flower of their youth. They were also old enough for talk of marriage arrangements to begin circulating.

[P41]
Just as everyone was wondering whether Jin Taekyung might be interested in the women, it happened.

[P42]
“Lift your butt higher. You’ll break a bone.”

[P43]
*Whack! Whack!*

[P44]
“You kids are still wet behind the ears! And you’re already drinking!”

[P45]
*Whack! Whack!*

[P46]
“If you want to drink, hide somewhere and do it quietly! Don’t pick a fight with someone who was minding his own business!”

[P47]
*Whack! Whack!*

[P48]
“You haven’t learned how to behave! People like you are exactly why corporal punishment is necessary! Do you understand or not?”

[P49]
*Whack! Whack!*

[P50]
“Improve teacher authority! A certain amount of corporal punishment is absolutely necessary!”

[P51]
*Whack! Whack! Whack!*

[P52]
The two men trembled as they recalled what had just happened.

[P53]
One had fainted, while the other had cried until tears and snot streamed down his face in front of everyone.

[P54]
After having their buttocks thoroughly beaten by a man outside their families in front of so many people, it was only a matter of time before their marriage prospects were ruined.

[P55]
“What in the world does ‘improve teacher authority’ mean? Is it something from Mencius?”

[P56]
“I don’t know, either. He even hit me one extra time.”

[P57]
“What a vicious bastard…”

[P58]
“Even so, I envy the others.”

[P59]
“What kind of outrageous thing is that to say? Can’t you see that your butt is covered in bruises?”

[P60]
“At least the others were beaten by the Sleeping Dragon of Shanxi. I was beaten by some beggar-looking bastard… Sob!”

[P61]
“Oh, that’s awful.”

[P62]
“If I had been beaten by the Sleeping Dragon of Shanxi, I could have made excuses. But some mangy bastard whose origins I don’t even know beat my butt… What was he doing, borrowing a beating instead of money?”

[P63]
His chin trembled with humiliation. He was thinking of the beggar-looking man who had taken the sword case from Jin Taekyung and gleefully thrashed him.

[P64]
“Wow, this is fun! You have some good bounce in that butt!”

[P65]
*Whack! Whack! Whack!*

[P66]
“Does it hurt? How much does it hurt? If you don’t mind, can I hit you harder? This is my first time doing something like this, so please understand if I’m not very good at controlling my strength!”

[P67]
*Whack! Whack! Whack!*

[P68]
It was a moment of humiliation he would never forget—not until the day he died, and perhaps not even after death. If he could, he would have chewed that bastard from head to toe and swallowed him piece by piece, and it still wouldn’t have been enough.

[P69]
“I will never forgive that bastard!”

[P70]
“Don’t worry. I’ll help you however much I can, Young Hero Jeong!”

[P71]
Who were they? They were the heirs of the Five Gates of Shanxi. Apart from Jin Taekyung of the Jin Family of Taiyuan, they had enough power to deal with a young beggar.

[P72]
“Um, about that…”

[P73]
“Yes?”

[P74]
“Are you sure he really is a beggar? I’m not saying this because I’m afraid, but considering what happened with the Sleeping Dragon of Shanxi, I suddenly think there’s nothing to lose by preparing for the worst.”

[P75]
“…Should we look into him a little more?”

[P76]
“Y-yes. Let’s do that.”

[P77]
The pampered rich kids had taken a group beating and finally learned to be cautious.

[P78]
* * *

[P79]
Once the lesson was over, we decided to move to a private room.

[P80]
It was hard not to notice the eyes of the surrounding guests while we remained on the first floor.

[P81]
Enjoying attention was fun for a moment or two, but if I tried to eat under these circumstances, I’d probably get confused about whether the food was going into my mouth or my nose.

[P82]
“I’m Seok, the man responsible for Honghwa Inn. Please feel free to call me Chief Steward Seok.”

[P83]
The Sleeping Dragon of Shanxi’s reputation really was something. The man in charge, who hadn’t shown even a trace of himself until now, had come to bow his head to me.

[P84]
*This man must be part of the Lower District Sect, too, right?*

[P85]
Honghwaru was Wolhwa’s base as the Chief Branch Leader of the Lower District Sect’s Shanxi branch, and Honghwa Inn was practically one of its subordinate organizations, as anyone could tell from the name.

[P86]
He might even have known about my existence before I set foot inside Honghwa Inn.

[P87]
*I can’t say that makes me feel particularly good.*

[P88]
Was it overreacting to think that unseen gazes were monitoring my every move?

[P89]
Still, I wasn’t exactly offended.

[P90]
It was more like a little caution. We had certainly maintained a friendly relationship until now, but no one knew what might happen in the future.

[P91]
“I’ve prepared a quiet place for you separately.”

[P92]
“Oh, that sounds good.”

[P93]
They were offering it as a courtesy, so there was no reason to refuse. I was just about to follow the chief steward when—

[P94]
“Thank you for everything, Benefactor.”

[P95]
I turned toward the voice and saw Cheongpung, wearing an innocent smile.

[P96]
“What do you mean? Surely you aren’t planning to leave just like this?”

[P97]
“Yes. It’s already late, so I was thinking of heading out.”

[P98]
*Where does he think he’s going? We hadn’t even gotten to talk properly because those random bastards barged in.* I hurriedly waved him off. “Hey now, if it’s late, you should stay the night. You said you don’t have any travel money, right?”

[P99]
“It’s all right. I’m used to sleeping rough.”

[P100]
“You shouldn’t be used to that. Besides, this would be a new experience! Have you ever slept at an inn?”

[P101]
“I stayed at an inn a few times before I lost my travel money. And I’ve already imposed enough on the two of you.”

[P102]
Hyuk Mujin, who had been standing beside me, muttered,

[P103]
“That’s true. With my candied hawthorn skewers[^1]—”

[P104]
[^1]: Traditional fruit skewers coated in hardened sugar.

[P105]
“You be quiet. So, are you really leaving?”

[P106]
“Yes. Fortunately, I still have business left in Shanxi Province, so if we happen to get the chance, we’ll meet again.”

[P107]
At this point, I had nothing left to say. If a Peak master was determined to leave of his own accord, I couldn’t exactly hold him back by claiming the roads were dangerous at night.

[P108]
Even so, I was still intensely curious about the identity of this oddball who had suddenly appeared out of nowhere.

[P109]
“If you have nowhere to go, come to the Jin Family of Taiyuan. If you give them my name, they’ll let you through.”

[P110]
“Oh, now that you mention it, you’re a Young Master of the Jin Family of Taiyuan, aren’t you? The Sleeping Dragon of Shanxi, Jin Taekyung… I’ll remember the name of my Benefactor.”

[P111]
He had known who I was for a while, yet he hadn’t reacted at all. His response amounted to, *Oh, I see,* and nothing more.

[P112]
Hyuk Mujin subtly signaled me and cut in.

[P113]
“The Jin Family of Taiyuan. You don’t know it?”

[P114]
“Well, I think I’ve heard of it somewhere. It does sound familiar, but I don’t really know much about it.”

[P115]
After tilting his head for a moment, Cheongpung bowed to us.

[P116]
“If fate brings us together, we’ll meet again. Then I’ll be off.”

[P117]
I replied with deep regret.

[P118]
“Take care. And don’t forget the Jin Family of Taiyuan.”

[P119]
“Haha, of course I won’t.”

[P120]
He turned away with a hearty laugh. Thinking the conversation had come to an end, the chief steward spoke up.

[P121]
“Then I’ll escort you to the annex.”

[P122]
“Ah, yes. Mujin, let’s go.”

[P123]
“Oh! We’re going to sleep in the annex of the famous Honghwa Inn?”

[P124]
“We stayed in the annex at Phoenix Inn, too. Why are you acting like this is something new?”

[P125]
“What are you talking about? If Phoenix Inn is a young prodigy, then Honghwa Inn is already a famous Peak master. Its hot springs, in particular, are such a renowned attraction that even high officials and nobles visit them.”

[P126]
“Hot springs?”

[P127]
“I’ve only heard about them from rumors, but they say there’s no paradise like it.”

[P128]
The chief steward added in a calm voice,

[P129]
“My father is turning eighty this year. He came here once and nearly departed for paradise.”

[P130]
“…Isn’t that dangerous?”

[P131]
“It only means the hot springs are that good. He’s still hale and hearty.”

[P132]
“Ah, I see. I hope he lives a long life.”

[P133]
Hot springs…

[P134]
I had gone to saunas plenty of times, but I had never visited a hot spring. Just thinking about sinking into pleasantly hot water already had me excited.

[P135]
“Ahem. Shall we go?”

[P136]
“I’ll escort you.”

[P137]
I was just about to follow the chief steward when a firm hand suddenly seized my shoulder.

[P138]
“Um. Did you just say hot springs?”

[P139]
“…You haven’t left yet?”

[P140]
Looking at Cheongpung’s sheepish grin, I was certain of one thing.

[P141]
I’d stake both my balls on the fact that this bastard had never been to a hot spring before.

[P142]
* * *

[P143]
In the early dawn, while darkness still blanketed the training ground of the estate, a man was swinging a sword.

[P144]
He looked to be about thirty. His strong, rugged features were striking.

[P145]
*Swish, swish, swish!*

[P146]
He thrust, slashed, and swung without a moment’s hesitation. Each form flowed smoothly into the next, as softly as flower petals fluttering on the wind.

[P147]
The Seven Plum Sword, in which he had reached eight-tenths mastery, cut through the cold dawn air when a messenger opened the main gate and entered.

[P148]
“What is it? I forbade anyone from entering while I’m training.”

[P149]
“I beg your pardon. His Highness Prince Shangshan ordered me to deliver a message…”

[P150]
“His Highness?”

[P151]
“Yes. It is the Prince’s command that you attend the luncheon at noon today.”

[P152]
“The luncheon… You mean the gathering where the young prodigies of Murim are coming?”

[P153]
“Yes, sir.”

[P154]
The man let out a deep sigh. He was a Third-Rank Assistant Military Commissioner, an official who could easily be counted among the five highest-ranking figures in Shanxi Province.

[P155]
*I can’t refuse an order from His Highness. What a nuisance.*

[P156]
The position of Assistant Military Commissioner was by no means an idle one. It was a weighty office responsible for training the soldiers.

[P157]
But the order had come from Prince Shangshan, the City Lord and a man of royal blood. The man had no choice but to nod.

[P158]
“Tell him I accept the royal command.”

[P159]
“Yes, sir!”

[P160]
After the messenger left, the man picked up his sword again.

[P161]
As he began the Seven Plum Sword once more, it seemed as though the plum blossoms of Huashan, which he had left behind long ago, were blooming from his blade.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 초식     | **form**                                         | Numbered technique movement                           |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 지부장    | **Branch Leader**                            |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 136,
  "passed": true,
  "metrics": {
    "source_characters": 5616,
    "translation_characters": 12855,
    "length_ratio": 2.289,
    "source_paragraphs": 161,
    "translation_paragraphs": 163
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
        "korean": "인도",
        "preferred": "Human Butcher"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "순이",
        "preferred": "Sooni"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
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
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기해",
        "preferred": "qi sea"
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
