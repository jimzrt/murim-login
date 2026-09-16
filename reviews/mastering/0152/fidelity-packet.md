# Fidelity Gate — Chapter 152

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
  1|＃152화
  2|
  3|
  4|
  5|“흐아아아암.”
  6|
  7|늘어져라 하품을 한 중년 무인이 옆을 흘끗 바라봤다.
  8|
  9|몇 걸음 떨어지지 않은 곳에 오늘 새로 발령받은 신참이 뻣뻣한 자세로 정면을 주시하는 중이었다.
 10|
 11|‘그놈 참. 떡대 하나는 끝내주네.’
 12|
 13|절굿공이 같은 팔다리 하며, 딱 벌어진 어깨 하며.
 14|
 15|덩치만 보면 근골 좋기로 유명한 하북팽가(河北彭家) 출신은 아닌지 의심이 들 정도였다.
 16|
 17|‘그러고 보니 아직 이름도 모르는군.’
 18|
 19|날은 춥고, 근무 시간은 앞으로 세 시진도 더 남았다.
 20|
 21|이런 날에는 주둥이라도 털어야 시간도 금방 가고 몸도 따뜻해지는 법. 중년 무인이 슬그머니 입을 열었다.
 22|
 23|“여보게.”
 24|
 25|“예, 옛!”
 26|
 27|“어허, 벽력탄을 삶아 먹었나. 왜 이리 목청이 커?”
 28|
 29|“죄송합니다!”
 30|
 31|“그렇다고 사과할 것까진 없고. 신입이라 그런가? 패기 넘치는 모습이 보기 좋구먼.”
 32|
 33|“헛, 감사합니다.”
 34|
 35|“응. 그려, 그려.”
 36|
 37|중년 무인은 흐뭇하게 웃었다. 몇 마디 안 나눠 봤지만 괜찮은 놈 같다. 행동거지가 우직하고, 요즘 젊은것들답지 않게 예의도 바르다.
 38|
 39|슬슬 뒷방 늙은이 취급받는 처지인 그로서는 꽤 괜찮은 말동무가 생긴 셈이었다.
 40|
 41|“혹시 자네 성이 팽가인가?”
 42|
 43|“아닙니다. 장가입니다.”
 44|
 45|“혹시나 해서 물어봤네. 자네 근골이 좀 좋아야지. 난 또 하북팽가의 먼 방계라도 되나 싶었지 뭔가.”
 46|
 47|신참 무인이 뒤통수를 긁적였다.
 48|
 49|“제가 코흘리개 때부터 힘깨나 쓰긴 했지요.”
 50|
 51|“어쩐지. 팔다리에 아주 근육이 옹골차네그려. 내 젊을 때를 보는 것 같아.”
 52|
 53|물론 턱도 없는 소리다. 하지만 생긴 것답지 않게 제법 눈치가 있는 신참 무인은 넙죽 허리를 숙였다.
 54|
 55|“선배님께서 젊으셨을 적에 비하면 저는 아무것도 아닙니다.”
 56|
 57|“어허. 선배가 뭔가, 앞으로는 형님이라고 부르게. 아, 나는 홍가일세.”
 58|
 59|“예, 형님!”
 60|
 61|“허허. 좋은 아우가 생겼구먼. 그래, 우리 장 아우는 본가에 언제 입문(入門)했는가?”
 62|
 63|“벌써 수년 되었습니다.”
 64|
 65|“으잉? 그럴 리가, 아우 같은 장군감이 들어왔으면 내가 진작 알았을 터인데…….”
 66|
 67|어언 이십 년을 태원진가에 몸담은 그다. 나름 터줏대감이라 무인 중 누가 들어오는지, 누가 나가는지는 정확히 알았다.
 68|
 69|“아, 무인이 된 건 한 달도 안 됐습니다. 그전에는 하인으로 잡일이나 이것저것 했었죠. 눈에 잘 안 띄는 곳이라 모르셨을 수도 있습니다.”
 70|
 71|“아아, 그랬구먼.”
 72|
 73|중년 무인은 새삼스러운 눈빛으로 신참을 바라봤다.
 74|
 75|하인에서 무인이라. 아주 없는 일은 아니지만 그렇다고 흔한 일도 아니다.
 76|
 77|“뒷배가 좋나 보군.”
 78|
 79|“예?”
 80|
 81|“예끼, 알 만한 사람이 시치미 떼기는. 신참이 이 자리에 들어오는 게 쉬운 일인 줄 알아?”
 82|
 83|중년 무인이 씩 웃으며 신참의 옆구리를 쿡쿡 찔렀다.
 84|
 85|“누군가? 내총관이야 워낙 깐깐한 위인이니 아닐 테고, 수뇌부에 튼튼한 줄이라도 하나 잡았나?”
 86|
 87|“저, 그게…….”
 88|
 89|“나만 알고 있을 테니 살짝 말해 보게. 외당주인가? 아니면 철검대주?”
 90|
 91|아뇨, 소가주님께서 보내셨는데요.
 92|
 93|신참 무인, 장칠득은 튀어나오려던 말을 꿀꺽 삼켰다.
 94|
 95|사람의 입이 얼마나 가벼운가, 곧이곧대로 말했다가는 내일 해가 뜨기 전에 소문이 퍼질 것이 뻔했다.
 96|
 97|‘소가주님께 누를 끼칠 수는 없다!’
 98|
 99|태원진가에 대한 충성심 하나만큼은 여느 열사(烈士) 못지않은 칠득이다.
100|
101|그는 궁금함이 잔뜩 담겨 있는 중년 무인의 눈빛을 외면하며 입을 열었다.
102|
103|“그런데 여기가 그렇게 들어오기 힘든 곳이었습니까?”
104|
105|칠득의 화제 전환에 중년 무인이 실망한 표정으로 입맛을 다셨다. 굳이 말하기 싫다는데 더 찔러 보기도 뭐하다.
106|
107|“쩝. 자네, 본가에 몇 년 동안 있었다고 했지?”
108|
109|“그렇죠. 하인이었지만.”
110|
111|“그럼 그 몇 년간 수련동에 몇 번이나 와 봤나?”
112|
113|“딱 두 번 와 봤습니다.”
114|
115|“그렇지? 자, 그 자리에서 한 바퀴 쓱 둘러보게.”
116|
117|“지금요?”
118|
119|“그럼 내년에 할래?”
120|
121|장칠득은 시키는 대로 주위를 둘러봤다. 태원진가의 뒤를 빈틈없이 감싼 가파른 절벽 아래, 뻥 뚫려 있는 동공(洞空).
122|
123|그곳이 수련동의 입구였고, 그와 중년 무인 외에는 아무도 없었다.
124|
125|“어떤가?”
126|
127|“휑하네요.”
128|
129|“그렇지? 여기 하루에 몇 명이나 올 것 같나?”
130|
131|“몇 명이나 옵니까?”
132|
133|중년 무인이 심드렁하게 대답했다.
134|
135|“안 와.”
136|
137|“예?”
138|
139|“네 시진마다 교대하러 오는 인원 제외하면 아무도 안 온다고. 아, 식사 전해 주는 하인도 있었군.”
140|
141|“하지만…… 수련동이잖습니까?”
142|
143|“수련동이지. 그런데 여기서 수련하는 사람? 없어. 예전에 삼공자가 사고 치고 몇 번 들락거리긴 했지만.”
144|
145|이 무슨 황당무계한 말인가. 그러고 보니 말만 수련동이지, 막상 이곳에서 수련했다는 사람은 못 본 것 같다.
146|
147|반면 연무장은 사시사철 무인들로 득실거렸다.
148|
149|“그럼 여길 왜 지키는 겁니까?”
150|
151|“상징이지.”
152|
153|“상징이요?”
154|
155|“먼 옛날, 본가를 세우신 진무량 조사(祖師)께서 수련하시던 곳이거든. 전해지기로는 이 절벽에서 수련하시던 도중 문득 깨달음을 얻어 무공을 펼쳤는데, 일격에 절벽 밑이 뻥 뚫렸다는군.”
156|
157|장칠득은 입을 딱 벌렸다.
158|
159|진무량 조사에 대한 전설은 그도 들어 본 기억이 있다. 삼백 년 전에는 천하에서 손꼽히는 고수였다던가?
160|
161|하지만 어찌 인간의 몸으로 그것이 가능하단 말인가.
162|
163|“그, 그게 사실입니까?”
164|
165|“자그마치 수백 년 전의 일일세. 사실이면 어떻고, 거짓이면 어떤가? 정작 중요한 사실은 따로 있는 것을.”
166|
167|“……예?”
168|
169|“이 수련동 앞에서 하루 몇 시진만 죽치고 앉아 있으면 월봉이 따박따박 나온다는 것. 그게 중요한 걸세. 시간이 더럽게 안 가는 게 흠이긴 하지만.”
170|
171|씩 웃은 중년 무인이 장칠득의 어깨를 두드렸다.
172|
173|“축하하네. 자네는 본가의 무인들이 꿈꾸는 최고의 보직에 임명된 걸세. 일명 꿀보직이라고 하지.”
174|
175|“…….”
176|
177|장칠득의 얼굴이 일그러졌다. 곧 은퇴해도 이상하지 않을 나이라면 모를까, 지금처럼 한창때에 할 일 없이 수련동에서 시간이나 죽이고 있을 생각은 없다.
178|
179|그의 생각을 알 리 없는 중년 무인은 품에서 육포 하나를 꺼내어 씹었다.
180|
181|“자네도 하나 줘?”
182|
183|“전 괜찮습니다.”
184|
185|“왜? 짭조름하니 괜찮은데. 육포 씹으면서 하늘 보면 시간도 금방 가고 좋아.”
186|
187|수련동 입구에 비스듬히 기댄 중년 무인이 고개를 꺾어 하늘을 바라봤다.
188|
189|“아따, 하늘 한번 맑다. 보고만 있어도 가슴이 탁 트이네.”
190|
191|장칠득도 마지못해 위를 흘끗 바라봤다.
192|
193|중년 무인의 말처럼 날씨는 맑았다. 푸른 하늘 위, 천천히 흘러가는 조각구름과 검은 점 몇 개가 떠다녔다.
194|
195|“저건 뭡니까?”
196|
197|“새겠지, 뭐.”
198|
199|멍하니 하늘을 바라보던 장칠득의 시선이 까마득한 높이의 절벽을 향했다. 문득 그의 눈이 가늘어졌다.
200|
201|“절벽에 붙어 있는 저건요?”
202|
203|“절벽? 절벽에 뭐가 있나?”
204|
205|“예. 꽤 큰데요?”
206|
207|“몰러. 꽤 큰 새인가 보지. 가만있자, 술을 한 병 가져왔는데…….”
208|
209|중년 무인은 칠득이 가리키는 곳을 쳐다보지도 않고 품에서 조그마한 자기 병 하나를 꺼내 들었다.
210|
211|“새치고는 좀 너무 큰 것 같은데요.”
212|
213|“천응(天鷹)이라는 놈일 수도 있지. 그놈들은 덩치가 사람만 하거든. 보통 매가 아니여.”
214|
215|“허어, 진짜 사람만 하네요.”
216|
217|“영물 소리도 듣는 놈이니까. 날개 길이만 일장이 넘는다고 하던데, 나도 멀리서 딱 한 번 봤네.”
218|
219|“그런데 형님.”
220|
221|“아, 왜 자꾸 부르나?”
222|
223|“천응도 떨어집니까?”
224|
225|“그게 뭔 개소리여?”
226|
227|술병을 기울이던 중년 무인이 황급히 절벽을 쳐다봤다. 까마득한 높이, 거대한 점이 빠르게 추락하고 있었다.
228|
229|“으아아아아악!”
230|
231|장칠득이 감탄했다.
232|
233|“영물은 영물이네요. 비명이 꼭 사람 같습니다.”
234|
235|“저거 사람이야, 이 미친놈아!”
236|
237|“뜨아아!”
238|
239|“피해, 피해!”
240|
241|중년 무인이 비명을 내지른 다음 순간, 비처럼 쏟아지는 돌조각과 함께 한 사람이 지면에 추락했다.
242|
243|쾅! 후두두둑!
244|
245|돌과 먼지가 사방으로 비산했다. 두 사람이 동시에 침을 꼴깍 삼켰다.
246|
247|“주, 죽은 걸까요?”
248|
249|“저 높이에서 떨어져 봐. 옥황상제도 죽는다.”
250|
251|평온하던 일상에 이 무슨 참담한 사태란 말인가.
252|
253|중년 무인은 떨리는 가슴을 부여잡고 엎어진 시신을 바라봤다.
254|
255|“도대체 어떤 미친놈이 절벽에서…….”
256|
257|“젊은 놈 같은데요?”
258|
259|“지금 젊은 놈이건 늙은 놈이건 그게 중요한가? 죽었다는 게 중요하지.”
260|
261|“그건 그렇지만…….”
262|
263|“가서 한 번 뒤집어 보게.”
264|
265|“제, 제가 말입니까?”
266|
267|“여기 자네랑 나 말고 누가 있나? 어서!”
268|
269|중년 무인의 호통에 장칠득이 머뭇거리며 시신을 향해 다가가기 시작했다.
270|
271|무인이 된 지 고작 한 달. 눈앞에서 사람의 죽음을 목도한 것은 이번이 처음이다.
272|
273|“후욱, 후욱.”
274|
275|가까워질수록 시신의 모습이 명확하게 보이기 시작한다.
276|
277|축 늘어진 사지, 엎어진 뒤통수에서는 핏물이 줄줄 흘러내렸다. 저 높이에서 떨어진 것치고는 곱게 죽은 모습.
278|
279|“그, 극락왕생하시오.”
280|
281|눈을 질끈 감고 시신의 몸에 손을 댄 그 순간이었다.
282|
283|벌떡, 빡!
284|
285|눈앞이 번쩍하더니 격통이 밀려들었다.
286|
287|그대로 엉덩방아를 찧은 장칠득은 자신이 쌍코피를 흘리는 것도 모르고 입을 딱 벌렸다.
288|
289|“어어, 어어어.”
290|
291|“갑자기 뭔…… 으어어, 으어어어!”
292|
293|중년 무인도 다리에 힘이 풀려 털썩 쓰러졌다.
294|
295|“시체가, 시체가 살아 있다!
296|
297|“으어어, 강시다! 강시가 나타났다!”
298|
299|시체, 강시.
300|
301|졸지에 죽은 놈이 되어 버린 흙투성이의 괴인이 비틀거리며 일어났다.
302|
303|산발이 된 머리, 실핏줄이 터진 눈동자로 주위를 둘러보던 그가 빠드득, 이를 갈았다.
304|
305|“씨벌, 또 태초 마을이야?”
306|
307|
308|
309|* * *
310|
311|
312|
313|더럽게 아프네.
314|
315|머리, 어깨, 무릎, 발, 무릎, 발…… 안 쑤시는 곳이 없다. 그나마 절벽에 단검을 박아서 추락 속도를 늦춰 망정이지, 하마터면 골로 갈 뻔했다.
316|
317|물론 꾸준하게 올려놓은 근골, 맷집 스탯도 한몫했고.
318|
319|“어우, 뒷골 땡겨.”
320|
321|따끔한 뒤통수를 만져 보니 핏물이 축축하게 묻어 나온다.
322|
323|소매를 북 찢어 피를 닦아 내던 그때였다.
324|
325|“누, 누구냐!”
326|
327|“정체, 정체를 밝혀라, 이노옴!”
328|
329|아, 이 아저씨들도 있었지.
330|
331|대뜸 칼을 들이대는 두 사람 중 한 명의 얼굴이 낯이 익다. 그러니까 이름이…….
332|
333|“장칠득?”
334|
335|며칠 전까지만 해도 홍화객잔에서 여론 조작에 힘쓰시던 장칠득 씨가 기겁하며 물러났다.
336|
337|“허억! 어떻게 내 이름을?!”
338|
339|“강시가 말을 한다! 말로 사람을 홀린다!”
340|
341|“……누가 강시야. 숨 잘만 쉬고 있는 거 안 보여요?”
342|
343|수염이 듬성듬성한 중년 아재가 눈을 부릅뜨며 외쳤다.
344|
345|“이 사악한 것! 내 눈을 속일 수는 없다. 네가 사람이라면 저 높이에서 떨어지고도 멀쩡할 리 없을 터, 어디서 보냈느냐! 마교(魔敎)? 혈교(血敎)? 그것도 아니면…….”
346|
347|“태초 마을! 형님, 저 강시가 분명 태초 마을이라고 했습니다.”
348|
349|“그렇지! 태초 마을에서 보낸 강시구나!”
350|
351|감 잡았다는 듯이 버럭 소리친 중년인이 순간 멈칫하더니 장칠득에게 물었다.
352|
353|“그런데 태초 마을이 어디야?”
354|
355|“저도 모르죠.”
356|
357|“…….”
358|
359|알면 이상하지.
360|
361|나는 대화를 포기하고 흙투성이가 된 얼굴을 옷소매로 문질렀다.
362|
363|중년인은 몰라도 장칠득은 내 얼굴을 잘 아니까 이게 더 빠르겠지.
364|
365|“헉, 삼공자님!”
366|
367|“네, 오랜만이에요.”
368|
369|“아우, 삼공자님이라니. 그게 대체 무슨 소린가?”
370|
371|“삼공자님이 강시가 됐습니다!”
372|
373|“…….”
374|
375|결론이 왜 그따위냐.
```

## Assembled English

```markdown
[P1]
# Chapter 152

[P2]
“Yaaawn.”

[P3]
A middle-aged martial artist let out a long yawn and glanced to the side.

[P4]
Only a few paces away, the new recruit who had been assigned here today was standing stiffly and staring straight ahead.

[P5]
*What a guy. He’s got one hell of a build.*

[P6]
Limbs like pestles. Broad, squared shoulders.

[P7]
Judging by his size alone, anyone might have suspected he hailed from the Hebei Peng Family, renowned for its sturdy physiques.

[P8]
*Come to think of it, I don’t even know his name yet.*

[P9]
The weather was cold, and there were still more than three shichen left in his shift.

[P10]
On days like this, you had to flap your gums to make the time pass faster and keep warm. The middle-aged martial artist quietly opened his mouth.

[P11]
“Hey there.”

[P12]
“Yes, sir!”

[P13]
“Good heavens, did you swallow a thunderbolt? Why are you shouting so loud?”

[P14]
“I’m sorry!”

[P15]
“No need to apologize. Is it because you’re new? It’s good to see someone so full of spirit.”

[P16]
“Ah, thank you.”

[P17]
“Yeah, yeah. That’s right.”

[P18]
The middle-aged martial artist smiled, pleased. They had only exchanged a few words, but the kid seemed decent. His manner was straightforward, and unlike young people these days, he was polite too.

[P19]
For a man who was slowly being treated like an old-timer fit only for the back rooms, he had found himself a pretty good conversational partner.

[P20]
“Is your surname Peng, by any chance?”

[P21]
“No. It’s Jang.”

[P22]
“I was only curious. You’ve got quite the physique. I wondered if you might belong to some distant collateral branch of the Hebei Peng Family.”

[P23]
The new martial artist scratched the back of his head.

[P24]
“I’ve been pretty strong ever since I was a snot-nosed kid.”

[P25]
“I thought so. Your limbs are packed with muscle. Reminds me of myself when I was young.”

[P26]
Of course, that was utter nonsense. But despite his appearance, the new martial artist was perceptive enough to immediately bow deeply.

[P27]
“Compared to you in your youth, Senior, I’m nothing.”

[P28]
“Come now, none of this ‘Senior’ business. Call me hyung from now on. Ah, my surname is Hong.”

[P29]
“Yes, hyung!”

[P30]
“Heh heh. Looks like I’ve gained a good little brother. So, Little Brother Jang, when did you join our family?”

[P31]
“It’s already been several years.”

[P32]
What? That can’t be right. If a man like you, with a general’s bearing, had joined, I would’ve heard about it long ago…

[P33]
Hong had served the Jin Family of Taiyuan for nearly twenty years. As something of an old fixture, he knew exactly which martial artists came and went.

[P34]
“Ah, I haven’t been a martial artist for even a month. Before that, I was a servant doing odd jobs here and there. I mostly worked out of sight, so you may not have noticed me.”

[P35]
“Ahh, I see.”

[P36]
Hong looked at the new recruit with fresh interest.

[P37]
A servant who became a martial artist. It wasn’t unheard of, but it wasn’t common either.

[P38]
“You must have a powerful backer.”

[P39]
“Pardon?”

[P40]
“Oh, come now. Don’t play dumb when you know exactly what I mean. Do you think it’s easy for a new recruit to land this post?”

[P41]
Grinning, Hong poked him in the side.

[P42]
“Who is it? The Chief Steward is far too strict to be behind it, so did you manage to secure a solid connection somewhere in the leadership?”

[P43]
“Well, I…”

[P44]
“Just tell me quietly. I’ll keep it to myself. Is it the Outer Hall Master? Or the Iron Sword Squad Leader?”

[P45]
*The Lesser Family Head sent me here.*

[P46]
The new martial artist, Jang Childeuk, swallowed the words that had nearly slipped out.

[P47]
People had loose tongues. If he told the truth, the rumor would spread before sunrise tomorrow.

[P48]
*I can’t cause trouble for the Lesser Family Head!*

[P49]
When it came to loyalty toward the Jin Family of Taiyuan, Childeuk was no less devoted than any martyr.

[P50]
He avoided the middle-aged martial artist’s intensely curious gaze and opened his mouth.

[P51]
“By the way, was this really such a difficult place to get into?”

[P52]
The middle-aged martial artist looked disappointed at the change of subject and clicked his tongue. Since Childeuk clearly didn’t want to say, pressing him further would be a bit awkward.

[P53]
“Tsk. You said you’d been with the family for several years, right?”

[P54]
“That’s right. As a servant, though.”

[P55]
“Then how many times did you come to the training hall during those years?”

[P56]
“Exactly twice.”

[P57]
“Right? Now, take a good look around.”

[P58]
“Right now?”

[P59]
“Or would you rather do it next year?”

[P60]
Jang Childeuk looked around as instructed.

[P61]
The Jin Family’s rear was completely enclosed by steep cliffs. Beneath them yawned a vast cavern—the entrance to the training hall.

[P62]
Aside from Childeuk and Hong, not a soul was in sight.

[P63]
“What do you think?”

[P64]
“It’s deserted.”

[P65]
“Right? How many people do you think come here in a day?”

[P66]
“How many?”

[P67]
Hong answered indifferently.

[P68]
“No one.”

[P69]
“Pardon?”

[P70]
“Other than the people who come to change shifts every four shichen, nobody comes here. Ah, there is a servant who delivers meals.”

[P71]
“But… this is the training hall, isn’t it?”

[P72]
“It is. But does anyone train here? No. The Third Young Master came in and out a few times after causing trouble, but that’s about it.”

[P73]
What an absurd thing to say.

[P74]
Come to think of it, despite the name, Childeuk had never seen anyone actually training there.

[P75]
The training ground, on the other hand, was always crawling with martial artists, no matter the season.

[P76]
“Then why are we guarding this place?”

[P77]
“It’s a symbol.”

[P78]
“A symbol?”

[P79]
“Long ago, Founder Jin Muryang trained here. According to legend, he suddenly attained enlightenment while training on this cliff and unleashed his martial arts. With One Strike, he blasted open the base of the cliff.”

[P80]
Jang Childeuk’s jaw dropped.

[P81]
He remembered hearing legends about Founder Jin Muryang. Hadn’t he been one of the greatest masters under heaven some three hundred years ago?

[P82]
But how could such a thing be possible with a human body?

[P83]
“Is—is that really true?”

[P84]
“It happened hundreds of years ago. What does it matter whether it’s true or false? There’s a much more important fact.”

[P85]
“…Yes?”

[P86]
“If you sit around in front of this training hall for a few shichen every day, your monthly pay arrives like clockwork. That’s what matters. The only downside is that time passes damnably slowly.”

[P87]
Hong grinned and patted Childeuk on the shoulder.

[P88]
“Congratulations. You’ve been assigned to the finest post every martial artist in the family dreams of. What they call a cushy post.”

[P89]
“…”

[P90]
Childeuk’s face twisted.

[P91]
It would be one thing if he were old enough to retire at any moment, but he was still in his prime. He had no intention of wasting his time in the training hall with nothing to do.

[P92]
Oblivious to Childeuk’s thoughts, Hong pulled a strip of jerky from his robes and began chewing.

[P93]
“Want one?”

[P94]
“I’m fine.”

[P95]
“Why? It’s salty and pretty good. Looking at the sky while chewing jerky makes time pass quickly.”

[P96]
The middle-aged martial artist leaned against the entrance to the training hall and tilted his head back to look at the sky.

[P97]
“Well, would you look at that. The sky is so clear. Just looking at it makes my chest feel wide open.”

[P98]
Jang Childeuk reluctantly glanced upward.

[P99]
As Hong had said, the weather was clear. Wisps of cloud drifted slowly across the blue sky, accompanied by several black specks.

[P100]
“What are those?”

[P101]
“Birds, probably.”

[P102]
As Childeuk stared blankly at the sky, his gaze drifted toward the dizzyingly high cliff. Suddenly, his eyes narrowed.

[P103]
“What about that thing clinging to the cliff?”

[P104]
“The cliff? What’s on the cliff?”

[P105]
“Yes. It’s pretty big.”

[P106]
“Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…”

[P107]
Without even looking where Childeuk was pointing, Hong pulled a small porcelain bottle from his robes.

[P108]
“It looks a little too big to be a bird.”

[P109]
“It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.”

[P110]
“Wow. It really is as big as a person.”

[P111]
“They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.”

[P112]
“But, hyung.”

[P113]
“What? Why do you keep calling me?”

[P114]
“Do Heavenly Eagles fall, too?”

[P115]
“What the hell are you talking about?”

[P116]
Hong, who had been tipping the bottle toward his mouth, hurriedly looked at the cliff.

[P117]
At that dizzying height, a massive dot was plummeting rapidly.

[P118]
“Aaaaaaah!”

[P119]
Childeuk marveled.

[P120]
“It really is a spirit creature. Its scream sounds exactly like a person.”

[P121]
“That’s a person, you lunatic!”

[P122]
“Whaaa!”

[P123]
“Move! Move!”

[P124]
The instant Hong screamed, a person crashed into the ground amid a shower of stone fragments.

[P125]
*Boom! Rumble, rumble!*

[P126]
Rocks and dust burst in every direction. The two men swallowed at the same time.

[P127]
“D-do you think he’s dead?”

[P128]
“Try falling from that height. Even the Jade Emperor would die.”

[P129]
How had such a horrific calamity intruded upon their peaceful routine?

[P130]
The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown.

[P131]
“What kind of madman falls from a cliff…”

[P132]
“He looks young.”

[P133]
“Does it matter whether he’s young or old? The important thing is that he’s dead.”

[P134]
“That’s true, but…”

[P135]
“Go turn him over.”

[P136]
“M-me?”

[P137]
“Who else is here besides you and me? Hurry!”

[P138]
At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body.

[P139]
He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him.

[P140]
“Huff, huff.”

[P141]
The closer he got, the more clearly he could see the body.

[P142]
Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact.

[P143]
“M-may you be reborn in paradise.”

[P144]
He squeezed his eyes shut and reached out to touch the body.

[P145]
That was when it suddenly shot upright.

[P146]
*Crack!*

[P147]
The world flashed before Childeuk’s eyes, followed by a wave of excruciating pain.

[P148]
He landed hard on his backside, his mouth hanging open, unaware that blood was streaming from both nostrils.

[P149]
“Uh… uhhhh.”

[P150]
“What in the… Ugh, ughhh!”

[P151]
Hong’s legs gave out, and he collapsed.

[P152]
“The corpse—the corpse is alive!”

[P153]
“Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!”

[P154]
The dirt-covered stranger who had suddenly been written off as dead staggered to his feet.

[P155]
His hair was wild, and blood vessels had burst in his eyes. He looked around, then ground his teeth.

[P156]
“Fuck, Taecho Village[^2] again?”

[P157]
* * *

[P158]
Damn, that hurts.

[P159]
Head, shoulders, knees, feet, knees, feet… There wasn’t a single part of me that didn’t ache. Luckily, I’d driven a dagger into the cliff and slowed my fall. Otherwise, I might have kicked the bucket.

[P160]
Of course, the physique and toughness stats I had steadily raised had helped, too.

[P161]
“Ow, the back of my head is throbbing.”

[P162]
I touched the tender spot and found it wet with blood.

[P163]
I tore off a strip of my sleeve and was wiping away the blood when—

[P164]
“W-who are you?!”

[P165]
“Reveal your identity, you scoundrel!”

[P166]
Oh, right. These two guys were here too.

[P167]
One of the two men pointing swords at me looked familiar. What was his name again…

[P168]
“Jang Childeuk?”

[P169]
Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror.

[P170]
“Gasp! How do you know my name?!”

[P171]
“The jiangshi is talking! It’s bewitching people with its words!”

[P172]
“…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?”

[P173]
The middle-aged man with the patchy beard glared at me and shouted.

[P174]
“You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…”

[P175]
“Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’”

[P176]
“That’s right! You’re a jiangshi sent by Taecho Village!”

[P177]
The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk,

[P178]
“But where is Taecho Village?”

[P179]
“I don’t know either.”

[P180]
“…”

[P181]
It would have been strange if he did.

[P182]
I gave up on the conversation and wiped the dirt from my face with my sleeve.

[P183]
The middle-aged man might not know me, but Childeuk knew my face well. This would be faster.

[P184]
“Gasp! Third Young Master!”

[P185]
“Yes. Long time no see.”

[P186]
“Little brother, the Third Young Master? What in the world are you talking about?”

[P187]
“The Third Young Master has become a jiangshi!”

[P188]
“…”

[P189]
How the hell did he reach that conclusion?

[P190]
[^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire.

[P191]
[^2]: *Taecho* means “primordial” or “the beginning.”
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
# Chapter 152

[P2]
“Yaaawn.”

[P3]
A middle-aged martial artist glanced to the side after letting out a long yawn.

[P4]
Only a few paces away, the new recruit who had been assigned here today was standing stiffly and staring straight ahead.

[P5]
*What a guy. He’s got one hell of a build.*

[P6]
Limbs like pestles. Shoulders spread wide.

[P7]
Judging by his size alone, one might have suspected he came from the Hebei Peng Family, famous for producing martial artists with strong bones and muscles.

[P8]
*Come to think of it, I don’t even know his name yet.*

[P9]
The weather was cold, and there were still more than three shichen left in his shift.

[P10]
On days like this, chatting was the best way to make time pass faster and keep warm. The middle-aged martial artist slowly opened his mouth.

[P11]
“Hey there.”

[P12]
“Yes, sir!”

[P13]
“Good heavens, did you swallow a thunderbolt? Why are you shouting so loudly?”

[P14]
“I’m sorry!”

[P15]
“You don’t have to apologize for that. Is it because you’re new? It’s nice to see someone so full of spirit.”

[P16]
“Ah, thank you.”

[P17]
“Yeah, yeah. That’s right.”

[P18]
The middle-aged martial artist smiled, pleased. They had only exchanged a few words, but the kid seemed decent. His manner was straightforward, and unlike young people these days, he was polite too.

[P19]
For a man who was slowly being treated like an old-timer fit only for the back rooms, he had found himself a pretty good conversational partner.

[P20]
“Is your surname perhaps Peng?”

[P21]
“No. It’s Jang.”

[P22]
“I only asked because I was curious. Your physique is quite impressive. I wondered whether you might be from some distant collateral branch of the Hebei Peng Family.”

[P23]
The new martial artist scratched the back of his head.

[P24]
“I was pretty strong even when I was a little kid.”

[P25]
“I thought so. Your limbs are packed with muscle. You remind me of myself when I was young.”

[P26]
Of course, that was utter nonsense. But despite his appearance, the new martial artist was perceptive enough to immediately bow deeply.

[P27]
“Compared to what you were like in your youth, Senior, I’m nothing.”

[P28]
“Hey, none of this ‘Senior’ business. Call me hyung from now on. Ah, I’m Hong.”

[P29]
“Yes, hyung!”

[P30]
“Heh heh. Looks like I’ve got myself a good little brother. So, Jang, when did you join this family?”

[P31]
“It’s already been several years.”

[P32]
“Huh? That can’t be right. If a fine candidate for a general like you had joined, I would have heard about it long ago…”

[P33]
He had been with the Jin Family of Taiyuan for nearly twenty years. He considered himself something of an old hand and knew exactly which martial artists came and went.

[P34]
“Ah, I haven’t even been a martial artist for a month. Before that, I was a servant who handled odd jobs here and there. I worked in places where I didn’t stand out much, so you might not have noticed me.”

[P35]
“Ahh, I see.”

[P36]
The middle-aged martial artist looked at the new recruit with fresh interest.

[P37]
A servant who became a martial artist. It wasn’t unheard of, but it wasn’t common either.

[P38]
“You must have a powerful backer.”

[P39]
“Pardon?”

[P40]
“Oh, come on. Don’t play dumb. Do you think it’s easy for a new recruit to get assigned to this position?”

[P41]
The middle-aged martial artist grinned and poked the new recruit in the side.

[P42]
“Who is it? The Chief Steward is far too strict to be behind it, so did you manage to secure a solid connection somewhere in the leadership?”

[P43]
“Well, I…”

[P44]
“Just tell me quietly. I’ll keep it to myself. Is it the Outer Hall Master? Or the Iron Sword Squad Leader?”

[P45]
*The Lesser Family Head sent me here.*

[P46]
The new martial artist, Jang Childeuk, swallowed the words that had nearly slipped out.

[P47]
People’s tongues were terribly light. If he told the truth, the rumor would spread before the sun rose tomorrow.

[P48]
*I can’t cause trouble for the Lesser Family Head!*

[P49]
When it came to loyalty toward the Jin Family of Taiyuan, Childeuk was no less devoted than any martyr.

[P50]
He avoided the middle-aged martial artist’s intensely curious gaze and opened his mouth.

[P51]
“By the way, was this really such a difficult place to get into?”

[P52]
The middle-aged martial artist looked disappointed at the change of subject and clicked his tongue. Since Childeuk clearly didn’t want to talk about it, there was no point in pressing him further.

[P53]
“Tsk. You said you’d been with the family for several years, right?”

[P54]
“That’s right. Although I was a servant.”

[P55]
“Then how many times did you come to the training hall during those years?”

[P56]
“Exactly twice.”

[P57]
“Right? Now, take a good look around.”

[P58]
“Right now?”

[P59]
“Or would you rather do it next year?”

[P60]
Jang Childeuk looked around as instructed.

[P61]
Beneath the steep cliffs that enclosed the rear of the Jin Family without a single gap, there was a wide-open cavern.

[P62]
That was the entrance to the training hall, and other than Childeuk and the middle-aged martial artist, there was no one there.

[P63]
“What do you think?”

[P64]
“It’s deserted.”

[P65]
“Right? How many people do you think come here in a day?”

[P66]
“How many?”

[P67]
The middle-aged martial artist answered indifferently.

[P68]
“No one.”

[P69]
“Pardon?”

[P70]
“Other than the people who come to change shifts every four shichen, nobody comes here. Ah, there is a servant who delivers meals.”

[P71]
“But… this is the training hall, isn’t it?”

[P72]
“It is. But does anyone train here? No. The Third Young Master came in and out a few times after causing trouble, but that’s about it.”

[P73]
What an absurd thing to say.

[P74]
Come to think of it, it was called a training hall, but Childeuk had never seen anyone actually training there.

[P75]
The training ground, on the other hand, was always crawling with martial artists, no matter the season.

[P76]
“Then why are we guarding this place?”

[P77]
“It’s a symbol.”

[P78]
“A symbol?”

[P79]
“Long ago, Founder Jin Muryang trained here. According to the story, he suddenly attained enlightenment while training on this cliff and unleashed his martial arts, blasting open the base of the cliff with One Strike.”

[P80]
Jang Childeuk’s mouth fell open.

[P81]
He remembered hearing the legend of Founder Jin Muryang. Hadn’t he been one of the most renowned masters in the world three hundred years ago?

[P82]
But how could such a thing be possible with a human body?

[P83]
“Is, is that really true?”

[P84]
“It happened hundreds of years ago. What does it matter whether it’s true or false? There’s another fact that’s actually important.”

[P85]
“…Yes?”

[P86]
“If you sit around in front of this training hall for a few shichen a day, your monthly pay comes like clockwork. That’s what matters. The only downside is that time passes unbelievably slowly.”

[P87]
The middle-aged martial artist grinned and patted Childeuk on the shoulder.

[P88]
“Congratulations. You’ve been assigned to the finest post the martial artists of this family dream of. They call it a cushy post.”

[P89]
“…”

[P90]
Childeuk’s face twisted.

[P91]
It would be one thing if he were old enough to retire at any moment, but he was still in his prime. He had no intention of wasting his time in the training hall with nothing to do.

[P92]
The middle-aged martial artist, unaware of his thoughts, pulled out a strip of dried meat and began chewing.

[P93]
“Want one?”

[P94]
“I’m fine.”

[P95]
“Why? It’s salty and pretty good. Looking at the sky while chewing jerky makes time pass quickly.”

[P96]
The middle-aged martial artist leaned against the entrance to the training hall and tilted his head back to look at the sky.

[P97]
“Well, would you look at that. The sky is so clear. Just looking at it makes my chest feel wide open.”

[P98]
Jang Childeuk reluctantly glanced upward.

[P99]
Just as the middle-aged martial artist had said, the weather was clear. A few wispy clouds drifted slowly across the blue sky, along with several black specks.

[P100]
“What are those?”

[P101]
“Birds, probably.”

[P102]
Childeuk’s gaze, which had been fixed blankly on the sky, shifted toward the cliff towering into the heavens. His eyes narrowed.

[P103]
“What about that thing clinging to the cliff?”

[P104]
“The cliff? What’s on the cliff?”

[P105]
“Yes. It’s pretty big.”

[P106]
“Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…”

[P107]
Without even looking toward the place Childeuk was pointing, the middle-aged martial artist pulled a small porcelain bottle from his robes.

[P108]
“It seems too big for a bird.”

[P109]
“It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.”

[P110]
“Wow. It really is as big as a person.”

[P111]
“They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.”

[P112]
“But, hyung.”

[P113]
“What? Why do you keep calling me?”

[P114]
“Do Heavenly Eagles fall, too?”

[P115]
“What the hell are you talking about?”

[P116]
The middle-aged martial artist, who had been tilting the bottle toward his mouth, hurriedly looked at the cliff.

[P117]
At that dizzying height, a massive dot was plummeting rapidly.

[P118]
“Aaaaaaah!”

[P119]
Childeuk sounded impressed.

[P120]
“It really is a spirit creature. Its scream sounds exactly like a person.”

[P121]
“That’s a person, you lunatic!”

[P122]
“Whaaa!”

[P123]
“Move! Move!”

[P124]
The instant the middle-aged martial artist screamed, a person crashed into the ground amid a shower of stones.

[P125]
*Boom! Rumble, rumble!*

[P126]
Rocks and dust burst in every direction. The two men swallowed at the same time.

[P127]
“D-do you think he’s dead?”

[P128]
“Try falling from that height. Even the Jade Emperor would die.”

[P129]
What a calamity to interrupt their peaceful daily routine.

[P130]
The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown.

[P131]
“What kind of madman falls from a cliff…”

[P132]
“He looks young.”

[P133]
“Does it matter whether he’s young or old? The important thing is that he’s dead.”

[P134]
“That’s true, but…”

[P135]
“Go turn him over.”

[P136]
“M-me?”

[P137]
“Who else is here besides you and me? Hurry!”

[P138]
At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body.

[P139]
He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him.

[P140]
“Huff, huff.”

[P141]
The closer he got, the more clearly he could see the body.

[P142]
Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact.

[P143]
“May you be reborn in paradise.”

[P144]
He squeezed his eyes shut and reached out to touch the body.

[P145]
That was when—

[P146]
The body sprang upright.

[P147]
*Crack!*

[P148]
The world flashed before Childeuk’s eyes, followed by a wave of blinding pain.

[P149]
He landed hard on his backside, mouth hanging open, unaware that blood was pouring from both nostrils.

[P150]
“Uh… uhhhh.”

[P151]
“What the hell just… ugh, ughhh!”

[P152]
The middle-aged martial artist’s legs gave out, and he collapsed.

[P153]
“The corpse—the corpse is alive!”

[P154]
“Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!”

[P155]
The dirt-covered stranger who had suddenly been written off as dead staggered to his feet.

[P156]
He looked around with his hair in disarray and blood vessels burst in his eyes, then ground his teeth.

[P157]
“Fuck, Taecho Village[^2] again?”

[P158]
* * *

[P159]
Damn, that hurts.

[P160]
My head, shoulders, knees, feet, knees, feet… There wasn’t a single place that didn’t ache. Luckily, I had slowed my fall by driving a dagger into the cliff. Otherwise, I might have ended up dead.

[P161]
Of course, the physique and toughness stats I had steadily raised had helped, too.

[P162]
“Ow, the back of my head is throbbing.”

[P163]
When I touched the tender spot on the back of my head, blood came away damply on my fingers.

[P164]
I tore off a strip of my sleeve and was wiping away the blood when—

[P165]
“Who are you?!”

[P166]
“Reveal your identity, you scoundrel!”

[P167]
Oh, right. Those two older guys were here, too.

[P168]
One of the two men pointing swords at me looked familiar. What was his name again…

[P169]
“Jang Childeuk?”

[P170]
Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror.

[P171]
“Gasp! How do you know my name?!”

[P172]
“The jiangshi is talking! It’s bewitching people with its words!”

[P173]
“…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?”

[P174]
The middle-aged man with the patchy beard glared at me and shouted.

[P175]
“You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…”

[P176]
“Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’”

[P177]
“That’s right! You’re a jiangshi sent by Taecho Village!”

[P178]
The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk,

[P179]
“But where is Taecho Village?”

[P180]
“I don’t know either.”

[P181]
“…”

[P182]
It would have been strange if he did.

[P183]
I gave up on the conversation and wiped the dirt from my face with my sleeve.

[P184]
The middle-aged man might not know me, but Childeuk knew my face well. This would be faster.

[P185]
“Gasp! Third Young Master!”

[P186]
“Yes. Long time no see.”

[P187]
“Little brother, the Third Young Master? What in the world are you talking about?”

[P188]
“The Third Young Master has become a jiangshi!”

[P189]
“…”

[P190]
Why was that the conclusion?

[P191]
[^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire.

[P192]
[^2]: *Taecho* means “primordial” or “the beginning.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 태원진가   | **Jin Family of Taiyuan**        |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 152,
  "passed": true,
  "metrics": {
    "source_characters": 5583,
    "translation_characters": 12479,
    "length_ratio": 2.235,
    "source_paragraphs": 185,
    "translation_paragraphs": 191
  },
  "errors": [],
  "warnings": [
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
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "칠득",
        "romanization": "childeuk"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "태초",
        "romanization": "taecho"
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
