# Fidelity Gate — Chapter 155

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
  1|＃155화
  2|
  3|
  4|
  5|적막한 공간. 예닐곱 명의 유생들이 정신없이 업무에 몰두하고 있었다.
  6|
  7|그들은 초췌한 얼굴로 산처럼 쌓인 죽간을 하나씩 처리해 나가는 한편, 여러 사안을 집무실의 주인에게 보고했다.
  8|
  9|“황하방과 소공문 사이에 분쟁이 일어났습니다. 본가에 중재를 청해 왔는데…….”
 10|
 11|“원단에 자리를 마련할 테니 그때 이야기하자 전하게. 내당주에게 미리 일러 놓고.”
 12|
 13|“산서오문에 관한 사안은 어떻게 하는 게 좋겠습니까?”
 14|
 15|“아, 셋째와 관련된 일인가?”
 16|
 17|“예. 산서오문의 당주들이 사죄의 말씀을 전하기 위해 기다리고 있습니다.”
 18|
 19|“돌려보내게. 정말 아쉬웠다면 손발을 보낼 게 아니라 머리가 직접 왔어야지. 그것도 내당주에게 일러 놓고.”
 20|
 21|“다음은 남부상회(商會)에서…….”
 22|
 23|사안을 보고받는 와중에도 집무실의 주인, 진위경은 죽간에서 눈을 떼지 않았다.
 24|
 25|그러나 이어지는 보고에는 그도 고개를 들 수밖에 없었다.
 26|
 27|“소가주님. 대동(大同) 부근에서 북부 고원의 마적단들이 수상한 움직임을 보이고 있습니다.”
 28|
 29|“마적? 하오문에서 보낸 소식인가?”
 30|
 31|“예. 이대로 내버려 둔다면 양민들을 대상으로 대대적인 노략질이 있을 겁니다.”
 32|
 33|“규모는?”
 34|
 35|“다섯 개의 마적단이 연합, 약 오백에 달하는 인원이 속속 집결 중입니다.”
 36|
 37|“마적들이라. 두고두고 말썽이로군.”
 38|
 39|진위경은 피곤한 얼굴로 미간을 문질렀다.
 40|
 41|태원진가의 세력이 막강한 것은 사실이지만 아직 산서 전역을 아우르기에는 역부족이다.
 42|
 43|적풍단의 궤멸을 알고 있음에도 마적들이 호시탐탐 기회를 엿보는 이유이기도 했다.
 44|
 45|“무인들을 차출할까요?”
 46|
 47|유생의 말에 진위경이 곧장 고개를 가로저었다.
 48|
 49|“불가.”
 50|
 51|“근래 본가에 입문한 무인들은 헤아릴 수도 없습니다. 충분한 여력이 있습니다.”
 52|
 53|“그러기에는 이미 너무 많은 피를 흘렸네. 게다가 이번에 받아들인 이들은 아직 경험이 부족해. 수백을 충원해도 수백이 죽어 나가겠지.”
 54|
 55|항산검문.
 56|
 57|산서성이라는 세발솥을 지탱하던 다리 하나가 부러지니 담겨 있던 물이 흘러넘치기 시작했다.
 58|
 59|펄펄 끓는 물에 화상을 입기 전에 대책을 강구해야 했다.
 60|
 61|잠시 고민하던 진위경이 입을 열었다.
 62|
 63|“당분간은 각 군현에 지부를 설립하고 안정화하는 것에 집중하게. 그게 최우선일세.”
 64|
 65|“소가주님!”
 66|
 67|유생이 깜짝 놀라 외쳤다. 각자 맡은 일에 집중하고 있던 다른 이들도 고개를 들었다.
 68|
 69|수백의 마적단이 쳐들어온다는데 지부 설립이 최우선이라니. 양민들이 죽건 말건 신경 쓰지 않겠다는 것인가?
 70|
 71|유생들의 얼굴에 실망이 번질 때, 진위경의 말이 이어졌다.
 72|
 73|“대신 산서오문에 지원을 요청하게. 이백 정도면 적당할 것 같은데…… 어떻게 생각하나?”
 74|
 75|“그 정도로는 턱도 없습니다.”
 76|
 77|태원진가의 소가주에게 이렇게 직설적으로 말할 수 있는 사람은 적어도 이 집무실 안에 없다.
 78|
 79|진위경이 막 문을 열고 들어오는 위팽을 보며 씩 웃었다.
 80|
 81|“그런가? 난 충분할 것 같은데.”
 82|
 83|“지금의 산서오문이 어떤 자들입니까? 이전투구에 혈안이 된 자들입니다. 공들여 기른 정예는 담장 안에 꽁꽁 숨겨 두고 어리바리한 이류, 삼류들로 꽉꽉 채워서 보내겠죠.”
 84|
 85|“그럴듯하군.”
 86|
 87|“그럴듯한 정도가 아니라 십중팔구입니다. 솜털 보송보송한 어린놈들을 보고 마적 놈들만 좋아서 입이 찢어지겠군요.”
 88|
 89|“하하, 그래서 우리가 나서야 한다?”
 90|
 91|“별수 있겠습니까? 쓸 만한 놈들로 붙여 주시면 제가 직접 다녀오겠습니다. 그럼 산서오문 쪽에서도 얌생이 짓은 못 할 테니까요.”
 92|
 93|“그렇지. 귀신보다 무서운 게 귀검(鬼劍) 아닌가?”
 94|
 95|놀리듯이 말하는 진위경의 목소리에 위팽이 고개를 절레절레 흔들었다.
 96|
 97|“이제 그만하시고 알려 주십시오.”
 98|
 99|“뭘?”
100|
101|“이미 생각해 둔 방도가 있으시지 않습니까?”
102|
103|“방도는 무슨. 자네 의견 좋던데?”
104|
105|“거참. 언제부터 제 말을 그렇게 귀 기울여 들으셨다고.”
106|
107|“자네 입에서 나오는 말은 내게 금과옥조지.”
108|
109|한숨을 푹 내쉰 위팽이 멀거니 서 있는 유생을 향해 고개를 돌렸다.
110|
111|“자네는 어떻게 생각하나?”
112|
113|“예, 예?”
114|
115|마른 체구에 희멀건 얼굴. 방구석에서 서책이나 들여다보던 백면서생의 표본이다.
116|
117|위팽의 갑작스러운 질문에 그가 더듬더듬 대답했다.
118|
119|“여, 역부족이라고 생각합니다.”
120|
121|“그게 끝인가?”
122|
123|“인원을 더 차출해야…….”
124|
125|그 모습을 지켜보던 진위경이 웃으며 끼어들었다.
126|
127|“거기까지 하게. 그리고 자네.”
128|
129|위팽의 날카로운 기세에 위축되어 있던 유생이 몸을 움찔 떨었다.
130|
131|“예.”
132|
133|“산서오문. 그리고 산서성부에 연통을 넣게. 대동 근방에 마적들이 들끓으니 도움을 바란다고 말이야.”
134|
135|“산서성부 말입니까?”
136|
137|“백성이 위험에 처했는데 나라가 발 벗고 나서야지. 아, 산서오문 쪽에도 슬쩍 그에 대해 언질 하고.”
138|
139|“근 몇 년간 보여 준 관의 소극적인 태도를 보아 성사될 가능성은 희박합니다.”
140|
141|“성사시켜야지.”
142|
143|진위경이 웃음기가 사라진 얼굴로 한마디를 덧붙였다.
144|
145|“그게 자네 할 일 아닌가?”
146|
147|“아.”
148|
149|유생은 정신이 번쩍 들었다. 며칠 밤을 새는 바람에 지쳐 있었다고는 하나 너무 쉽게 생각하고 있었다.
150|
151|산서성에 도움을 요청하라니. 차라리 뼛속까지 무인인 위팽이 내놓은 의견이 훨씬 그럴듯한 대책이다.
152|
153|“송구합니다.”
154|
155|“아직 서투를 테니 이해하네. 하지만 본가에 필요한 건 유생이 아니라 본가를 위해 최선의 대책을 내놓을 지자(智者)야. 내 말을 잘 기억하길 바라네.”
156|
157|유구무언이다. 눈앞의 유생뿐만 아니라 모두의 얼굴이 붉어진 걸 확인한 진위경이 재차 입을 열었다.
158|
159|“다들 피곤할 테니 오늘은 이만 들어가 쉬게.”
160|
161|쉬라는데 거부할 사람은 없다. 사흘째 죽간을 베개 삼아 쪽잠으로 버티던 이들이라면 더더욱.
162|
163|유생들이 지친 몸을 이끌고 빠져나가자 위팽이 빈 의자를 끌어당겼다.
164|
165|“새로 뽑은 자들입니까?”
166|
167|“역시 혼자서는 역부족이더군. 그래도 없는 것보다는 나아.”
168|
169|“글쎄요. 어째 다들 밍밍합니다만.”
170|
171|“저들 중 본가에 들어오려고 학문을 익힌 이들이 몇이나 되겠나? 어쩌면 당연한 거지.”
172|
173|진위경이 기지개를 쭉 켰다. 우두둑, 뼈 어긋나는 소리가 요란하게 울려 퍼졌다.
174|
175|“아직 며칠밖에 안 됐어. 옥석을 가려내고 떠날 자는 떠나보내야지.”
176|
177|“굳이 산서성부와의 밀약을 알리지 않으신 이유도 그 때문입니까?”
178|
179|“밀약(密約)이 왜 밀약인가? 아는 사람은 적을수록 좋아.”
180|
181|사실 산서성부의 도움을 이끌어 내는 것은 그리 어려운 일이 아니다. 이미 닷새 전 방문한 도지휘동지 홍진과의 대화를 통해 많은 것을 주고받지 않았던가?
182|
183|“본가는 아직 완전히 자리를 잡지 못했네. 이런 상황에서 관과 밀약을 맺었다는 식의 소문이 떠돌면 곤란하지.”
184|
185|“그건 그렇지요. 소문이 아니라 사실일 경우에는 더더욱.”
186|
187|홍진과 주고받은 대화에는 산서성의 중소 문파들, 그중에서도 산서오문이 달가워하지 않을 만한 주제들이 여럿 끼어 있다.
188|
189|특히 성운표국 측에서 진위경과 홍진의 대화를 듣게 된다면 입에 거품을 물고 쓰러질지도 모르는 일이다.
190|
191|“그래, 다른 준비는 잘되어 가고?”
192|
193|“예. 분부하신 대로 인사 조치를 끝냈습니다. 내외당의 당주들은 그대로 두었고, 세 개의 대(隊)를 신설했으며…….”
194|
195|위팽의 입에서 흘러나오는 보고는 진위경이 종전 직후 가장 먼저 처리한 부분이다.
196|
197|현재의 태원진가는 떠오르는 태양과 같다. 한창 피 끓는 산서성의 젊은이들에게는 최고의 선택지.
198|
199|끊임없이 몰려드는 이들을 모두 포용하기 위해서는 품이 더욱 넓어져야 했다.
200|
201|“……이렇게 처리했습니다만, 계속해서 규모가 늘어날 예정이니만큼 추후 재정비가 필요해 보입니다.”
202|
203|“그러길 바라야지.”
204|
205|위팽의 보고를 들은 진위경은 담담한 척하려 애썼다.
206|
207|정마대전 이후 조금씩, 그리고 꾸준히 쇠락해 가던 태원진가다. 그러나 지금의 태원진가는 빠르게 과거의 성세를 회복해 가고 있었다.
208|
209|‘아니, 어쩌면 정마대전이 일어나기 이전보다 더욱 강성해질지도 모른다.’
210|
211|만약 그렇게 된다면…….
212|
213|그때야말로 세가(世家)의 자격을 갖추게 된다.
214|
215|변방의 무가를 벗어나, 천하의 거목들과 어깨를 나란히 하게 되는 것이다.
216|
217|‘세가, 세가라는 말이지.’
218|
219|생각만 해도 가슴이 뛰는 단어다.
220|
221|모든 무인이 무신을 꿈꾸는 것처럼, 진위경은 가문을 세가의 반석에 올리기를 오랫동안 소원해 왔으니까.
222|
223|‘이제 곧 원단이다.’
224|
225|그 날, 산서 무림의 모든 문파가 보는 앞에서 태원진가는 명실상부한 산서성의 패자로 인정받는다.
226|
227|곧 다가올 새해 첫날이 태원진가가 세가로 나아가는 첫 발판이자 효시가 될 것이라 진위경은 믿어 의심치 않았다.
228|
229|그리고 그가 남몰래 주먹을 꽉 움켜쥔 그 순간이었다.
230|
231|“저어, 들어가도 되겠습니까?”
232|
233|“응? 물론일세.”
234|
235|곧이어 등장한 목소리의 주인공은 방금 떠났던 유생이었다.
236|
237|“무슨 일인가? 놓고 간 물건이라도 있나?”
238|
239|“그것이 아니라…….”
240|
241|진위경과 위팽의 의아한 시선을 받은 그가 조심스럽게 말을 이었다.
242|
243|“미처 보고드리지 못한 소식이 있습니다.”
244|
245|“사람도 참 고지식하기는. 며칠 동안 잠도 제대로 못 자고 고생했는데 괘념치 말고 들어가서 푹 쉬시게.”
246|
247|“아닙니다. 제가 진작 말씀드렸어야 했는데 깜빡하는 바람에…….”
248|
249|“어허, 괜찮네. 그만 쉬라니까.”
250|
251|위팽도 한마디 거들었다.
252|
253|“소가주님 말씀이 맞네. 사람이 강시도 아니고, 충분한 휴식을 취해야 다음 날도 힘내서…….”
254|
255|“화산파에서 매화삼절(梅花三晣)을 보냈답니다.”
256|
257|진위경과 위팽이 동시에 자리에서 벌떡 일어났다.
258|
259|“뭣이!”
260|
261|“뭐라!”
262|
263|매화삼절이 누군가.
264|
265|화산파의 최정예로 불리는 매화검수. 그중에서도 두각을 드러낸 걸출한 기재들이다.
266|
267|특히 화산일학 백무성은 화산파의 미래를 짊어질 차기 장문인으로 꼽히는 거물.
268|
269|그런 얘길 들었으니 두 사람의 눈이 튀어나올 수밖에 없었다.
270|
271|“그게 정말인가?”
272|
273|“예, 마지막에 말씀드리려다가 그만. 그리고 하나 더 있습니다.”
274|
275|“하나 더?”
276|
277|“또? 어서 말해 보게!”
278|
279|매화삼절의 방문만 해도 놀라운데, 하나가 더 있단다.
280|
281|유생이 눈살을 찌푸리며 말을 이었다.
282|
283|“태사부께서 사라지셨다고. 본가로 가신 것 같으니 뵙게 되면 꼭 좀 연통을 넣어 달라 하는데…… 태사부가 누굽니까?”
284|
285|아직 무림 실정에 어두운 유생은 이게 뭔가 싶었지만, 진위경과 위팽은 입을 딱 벌렸다.
286|
287|“화산파의 태사부면…….”
288|
289|“거, 거, 거…….”
290|
291|검성 매종학. 차마 입 밖에 내지 못하고 입만 벙긋거린 두 사람이 침을 꿀꺽 삼켰다.
292|
293|화산파는 아직까지 검성의 행방을 불문에 부쳐 두고 싶어 한다. 이럴 때일수록 말은 아끼는 게 좋다.
294|
295|“거, 뭐라고 하셨습니까?”
296|
297|“거, 거시기, 그런 게 있네.”
298|
299|“예?”
300|
301|“자네는 이만 나가 보게. 지금 있었던 일은 머릿속에서 지우고. 알겠나?”
302|
303|유생이 어리둥절한 얼굴로 고개를 숙이고 나가자 비로소 참았던 말이 튀어나왔다.
304|
305|“검성이 온다!”
306|
307|“쉿, 목소리 낮추십시오. 아직 확실하지도 않잖습니까.”
308|
309|말과는 달리 위팽의 얼굴도 홍조로 붉게 달아올라 있었다. 그와 같은 검수(劍手)에게 있어 검성 매종학은 옥황상제 그 이상이었으니까.
310|
311|그런 분을 직접 만날 수 있다니! 아니, 어쩌면 한 수 가르침까지 받을 수 있을지 모른다.
312|
313|“그, 그런데 검성이 왜 본가에.”
314|
315|“뭣 때문이겠나?”
316|
317|“아.”
318|
319|너무 흥분한 나머지 깜빡하고 있었다. 지금 태원진가에 누가 와 있는지를.
320|
321|“그 검성이 애제자를 찾으러 은거를 깼군요.”
322|
323|“아직은 짐작이지만 그럴 가능성이 농후하지. 친손자처럼 길렀다는데 그 정이야 오죽할까.”
324|
325|진위경은 싱글벙글 웃었다.
326|
327|이유야 어찌 되었건 검성의 방문은 한 사람의 무인으로서도, 태원진가의 소가주로서도 쌍수를 들고 환영할만한 일이다.
328|
329|“청풍이라고 했지, 그 친구는 지금 어디 있나? 막내에게 벽호공 수련시킨다는 이야기를 한참 전에 들은 것 같네만.”
330|
331|“벽호공 수련은 이틀 전에 끝났고 지금은…….”
332|
333|“지금은?”
334|
335|“삼 공자를 줘 패고 있습니다.”
336|
337|“뭣이이이!”
```

## Assembled English

```markdown
[P1]
# Chapter 155

[P2]
A silent room. Six or seven scholars were frantically immersed in their work.

[P3]
With haggard faces, they processed the bamboo slips piled up like mountains one by one while reporting various matters to the master of the office.

[P4]
“There’s been a dispute between the Yellow River Gang and the Sogong Sect. They’ve asked our family to mediate…”

[P5]
“Tell them we’ll set aside time on New Year’s Day to discuss it. Inform the Inner Hall Master in advance.”

[P6]
“What should we do about the matter concerning the Five Gates of Shanxi?”

[P7]
“Ah, is this related to the third one?”

[P8]
“Yes. The hall masters of the Five Gates of Shanxi are waiting to offer their apologies.”

[P9]
“Send them back. If they were truly sorry, the heads themselves should have come in person instead of sending their hands and feet. Inform the Inner Hall Master of that, too.”

[P10]
“Next, there’s a matter from the Southern Merchant Guild…”

[P11]
Even as he received their reports, Jin Wikyung, the master of the office, never looked up from the bamboo slips.

[P12]
But the next report made even him raise his head.

[P13]
“Lesser Family Head, mounted-bandit groups from the northern plateau are showing suspicious movements near Datong.”

[P14]
“Mounted bandits? Is this information from the Lower District Sect?”

[P15]
“Yes. If left unchecked, they’ll launch a large-scale raid against the common people.”

[P16]
“How large is their force?”

[P17]
“Five mounted-bandit groups have formed an alliance. Around five hundred men are gradually gathering.”

[P18]
“Mounted bandits, huh? They’ve been a constant nuisance.”

[P19]
Jin Wikyung rubbed between his brows, his face weary.

[P20]
The Jin Family of Taiyuan was undeniably powerful, but it still lacked the strength to cover all of Shanxi Province.

[P21]
That was also why the mounted bandits kept watching for an opportunity despite knowing that the Red Wind Band had been annihilated.

[P22]
“Should we draft some martial artists?”

[P23]
At the scholar’s question, Jin Wikyung immediately shook his head.

[P24]
“No.”

[P25]
“We’ve had more martial artists join our family recently than we can count. We have men to spare.”

[P26]
“We’ve already shed too much blood for that. Besides, those we accepted this time still lack experience. Even if we recruit several hundred, several hundred will die.”

[P27]
The Mount Heng Sword Sect.

[P28]
One of the legs supporting the tripod of Shanxi Province had broken, and the water inside was beginning to spill over.

[P29]
They had to devise a countermeasure before the boiling water scalded them.

[P30]
After a moment’s thought, Jin Wikyung spoke.

[P31]
“For the time being, focus on establishing and stabilizing branches in each prefecture and county. That is our top priority.”

[P32]
“Lesser Family Head!”

[P33]
The scholar cried out in surprise. The others, who had been focused on their own tasks, also raised their heads.

[P34]
Hundreds of mounted bandits were supposedly invading, and yet establishing branches was the top priority. Did that mean they did not care whether the common people died?

[P35]
As disappointment spread across the scholars’ faces, Jin Wikyung continued.

[P36]
“Instead, ask the Five Gates of Shanxi for support. Two hundred men should be about right… What do you think?”

[P37]
“That won’t be nearly enough.”

[P38]
There was no one in this office, at least, who could speak so bluntly to the Lesser Family Head of the Jin Family of Taiyuan.

[P39]
Jin Wikyung grinned at Wipeng as he came through the door.

[P40]
“Is that so? I thought it would be enough.”

[P41]
“What sort of people are the Five Gates of Shanxi now? They’re obsessed with clawing at one another for scraps. They’ll hide their carefully trained elites inside their walls and send us a force packed with clueless Second Rate and Third Rate martial artists.”

[P42]
“That sounds plausible.”

[P43]
“It’s not just plausible. That’s what will happen nine times out of ten. The mounted bandits will see all those peach-fuzzed little punks and be so delighted their mouths will split open.”

[P44]
“Haha. So we have to step in?”

[P45]
“What choice do we have? If you attach some useful men to the force, I’ll go there myself. Then the Five Gates of Shanxi won’t be able to pull any sneaky tricks.”

[P46]
“Exactly. Isn’t the Ghost Sword more frightening than a ghost?”

[P47]
At Jin Wikyung’s teasing tone, Wipeng shook his head from side to side.

[P48]
“That’s enough. Tell me.”

[P49]
“Tell you what?”

[P50]
“You already have a plan, don’t you?”

[P51]
“What plan? Your idea sounded good to me.”

[P52]
“Good grief. Since when have you listened so closely to anything I say?”

[P53]
“Every word from your mouth is a golden rule to me.”

[P54]
Wipeng let out a deep sigh and turned toward the scholar standing blankly nearby.

[P55]
“What do you think?”

[P56]
“P-pardon?”

[P57]
A thin frame and a pale, washed-out face. He was the very picture of a pale-faced scholar who did nothing but pore over books in his room.

[P58]
At Wipeng’s sudden question, he stammered out an answer.

[P59]
“I-I don’t think it will be enough.”

[P60]
“Is that all?”

[P61]
“We should draft more men…”

[P62]
Watching him, Jin Wikyung cut in with a laugh.

[P63]
“That’s enough. And you.”

[P64]
Already cowed by Wipeng’s sharp aura, the scholar flinched.

[P65]
“Yes.”

[P66]
“Send word to the Five Gates of Shanxi and the Shanxi Provincial Office. Tell them mounted bandits are swarming near Datong and that we request their assistance.”

[P67]
“The Shanxi Provincial Office?”

[P68]
“The people are in danger. The government ought to roll up its sleeves and help. Ah, casually give the Five Gates of Shanxi a hint about it, too.”

[P69]
“Judging by the government’s passive attitude over the past several years, the chances of that succeeding are slim.”

[P70]
“Then make it succeed.”

[P71]
Jin Wikyung’s face lost its smile as he added one more thing.

[P72]
“Isn’t that your job?”

[P73]
“Ah.”

[P74]
The scholar’s mind snapped awake. He was exhausted from staying up several nights, but he had been thinking far too simply.

[P75]
Request help from Shanxi Province? The countermeasure proposed by Wipeng, a man who was a martial artist down to his bones, was much more plausible.

[P76]
“I apologize.”

[P77]
“You’re still inexperienced, so I understand. But what our family needs isn’t scholars. We need wise men who can offer the best possible measures for the sake of our family. I hope you’ll remember that.”

[P78]
There was nothing the scholar could say. Seeing that not only the man before him but everyone else had reddened faces, Jin Wikyung spoke again.

[P79]
“You’re all tired, so go in and rest for today.”

[P80]
No one would refuse an order to rest, least of all men who had spent the last three days surviving on brief naps with bamboo slips for pillows.

[P81]
Once the scholars dragged their exhausted bodies out, Wipeng pulled over an empty chair.

[P82]
“Are those the new recruits?”

[P83]
“Being on my own was too much. Still, they’re better than nothing.”

[P84]
“I’m not sure. They all seem rather bland.”

[P85]
“How many of them studied in order to join our family? It’s only natural.”

[P86]
Jin Wikyung stretched his arms high. The loud cracking of bones echoed through the room.

[P87]
“It’s only been a few days. We need to separate the jade from the stones and send away those who need to go.”

[P88]
“Is that also why you didn’t tell them about the secret agreement with the Shanxi Provincial Office?”

[P89]
“Why is a secret agreement called a secret agreement? The fewer people who know about it, the better.”

[P90]
In truth, securing the assistance of the Shanxi Provincial Office was not particularly difficult. Hadn’t he and Deputy Military Commissioner Hong Jin already exchanged plenty through their conversation five days earlier?

[P91]
“Our family hasn’t fully established itself yet. It would be troublesome if rumors spread that we had entered into a secret agreement with the government under these circumstances.”

[P92]
“True. Especially when the rumors happen to be facts.”

[P93]
The conversation Jin Wikyung had exchanged with Hong Jin had included several topics that the small and medium-sized sects of Shanxi Province—and especially the Five Gates of Shanxi—would not welcome.

[P94]
If the Seongun Escort Bureau heard what Jin Wikyung and Hong Jin had discussed, they might collapse frothing at the mouth.

[P95]
“So, are the other preparations going well?”

[P96]
“Yes. I’ve completed the personnel changes as you ordered. The heads of the Inner and Outer Halls have been left in place, and we’ve established three new squads…”

[P97]
The report flowing from Wipeng’s mouth concerned the first matter Jin Wikyung had handled immediately after the war ended.

[P98]
The Jin Family of Taiyuan was like a rising sun. To the hot-blooded young people of Shanxi Province, it was the finest choice available.

[P99]
To embrace the endless stream of people coming to them, the family had to widen its arms even further.

[P100]
“…That’s how I handled it, but with our numbers expected to keep growing, we’ll likely need to reorganize again later.”

[P101]
“That’s what we should hope for.”

[P102]
Jin Wikyung tried to appear calm as he listened to Wipeng’s report.

[P103]
The Jin Family of Taiyuan had declined slowly but steadily since the Great Faction War. Now, however, it was rapidly regaining its former glory.

[P104]
*No. Perhaps it will become even stronger than it was before the Great Faction War.*

[P105]
If that happened…

[P106]
Only then would they truly earn the right to be called a great family.

[P107]
They would break free of their status as a frontier martial family and stand shoulder to shoulder with the towering powers of the realm.

[P108]
*A great family. A great family, huh.*

[P109]
It was a word that made his heart race just to think about it.

[P110]
Just as every martial artist dreamed of becoming the Martial God, Jin Wikyung had long dreamed of raising his family onto the foundation of a great family.

[P111]
*New Year’s Day is almost here.*

[P112]
On that day, before all the sects of Shanxi Murim, the Jin Family of Taiyuan would be recognized as the undisputed hegemon of Shanxi Province.

[P113]
Jin Wikyung had no doubt that the first day of the coming year would become the Jin Family of Taiyuan’s first stepping-stone—and the harbinger of its rise—as a great family.

[P114]
And it was at the very moment he secretly clenched his fists that—

[P115]
“Um… May I come in?”

[P116]
“Hm? Of course.”

[P117]
The voice belonged to the scholar who had just left.

[P118]
“What is it? Did you leave something behind?”

[P119]
“It’s not that…”

[P120]
Under Jin Wikyung and Wipeng’s puzzled gazes, the scholar continued cautiously.

[P121]
“There’s some news I failed to report.”

[P122]
“You’re too conscientious for your own good. You’ve been working hard for days without even getting proper sleep. Don’t worry about it. Go in and get some rest.”

[P123]
“No. I should have told you earlier, but it slipped my mind…”

[P124]
“Now, now. It’s fine. I told you to rest.”

[P125]
Wipeng chimed in.

[P126]
“My lord is right. You aren’t a jiangshi. You need to get enough rest so you can have the strength to work again tomorrow…”

[P127]
“Huashan has sent the Three Plum Blossom Elites.”

[P128]
Jin Wikyung and Wipeng shot to their feet at the same time.

[P129]
“What!”

[P130]
“What did you say?”

[P131]
Who were the Three Plum Blossom Elites?

[P132]
They were the most exceptional talents among the Plum Blossom Swordsmen, Huashan’s finest.

[P133]
In particular, Huashan’s Lone Crane, Baek Museong, was a major figure expected to become the next Sect Leader and carry Huashan’s future upon his shoulders.

[P134]
After hearing such news, how could the two men’s eyes not nearly pop from their sockets?

[P135]
“Is that really true?”

[P136]
“Yes. I meant to tell you at the end, but I forgot. And there’s one more thing.”

[P137]
“One more?”

[P138]
“Another? Tell us quickly!”

[P139]
The visit of the Three Plum Blossom Elites was shocking enough, and now he was saying there was something else.

[P140]
Frowning, the scholar continued.

[P141]
“They say the Grandmaster has disappeared. He seems to have gone to our family, so they asked us to send word if we happen to meet him… But who is the Grandmaster?”

[P142]
The scholar was still unfamiliar with the realities of Murim and wondered what this was all about. Jin Wikyung and Wipeng, however, stood with their mouths hanging open.

[P143]
“If Huashan’s Grandmaster is…”

[P144]
“Th-th-that…”

[P145]
Sword Saint Mae Jonghak.

[P146]
Unable to bring themselves to say the name aloud, the two men merely mouthed the words and swallowed hard.

[P147]
Huashan still wanted to keep the Sword Saint’s whereabouts secret. At times like this, it was best to keep one’s mouth shut.

[P148]
“Th-that… What did you say?”

[P149]
“Th-that thing. You know, that sort of thing.”

[P150]
“Pardon?”

[P151]
“You can leave now. Erase everything that just happened from your mind. Understood?”

[P152]
The scholar bowed with a bewildered expression and left. Only then did the words they had been holding back burst out.

[P153]
“The Sword Saint is coming!”

[P154]
“Shh! Lower your voice. We don’t even know for certain yet.”

[P155]
Despite his words, Wipeng’s face had also flushed bright red. To a swordsman like him, Sword Saint Mae Jonghak was greater than even the Jade Emperor.

[P156]
To think they might be able to meet such a person in the flesh! No, perhaps he might even receive instruction from him.

[P157]
“B-but why would the Sword Saint come to our family?”

[P158]
“What else could it be?”

[P159]
“Ah.”

[P160]
He had been so excited that he had momentarily forgotten who was currently staying at the Jin Family of Taiyuan.

[P161]
“That Sword Saint broke his seclusion to look for his beloved disciple.”

[P162]
“It’s only a guess for now, but that’s highly likely. I hear he raised him like his own grandson. How deep must his affection be?”

[P163]
Jin Wikyung grinned broadly.

[P164]
Whatever the reason, the Sword Saint’s visit was something to welcome with open arms—not only as a martial artist, but also as the Lesser Family Head of the Jin Family of Taiyuan.

[P165]
“You said his name was Cheongpung, right? Where is he now? I seem to remember hearing a while ago that he was training my youngest brother in the Wall Lizard Technique.”

[P166]
“The Wall Lizard Technique training ended two days ago, and now he’s…”

[P167]
“And now?”

[P168]
“He’s beating the crap out of the Third Young Master.”

[P169]
“Whaaat!”
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
# Chapter 155

[P2]
A silent room. Six or seven scholars were frantically immersed in their work.

[P3]
With haggard faces, they processed the bamboo slips piled up like mountains one by one while reporting various matters to the master of the office.

[P4]
“There’s been a dispute between the Yellow River Gang and the Sogong Sect. They’ve asked our family to mediate, but…”

[P5]
“Tell them we’ll arrange a place on New Year’s Day and discuss it then. Inform the Inner Hall Master in advance.”

[P6]
“What should we do about the matter concerning the Five Gates of Shanxi?”

[P7]
“Ah, is this related to the third one?”

[P8]
“Yes. The heads of the Five Gates of Shanxi are waiting to convey their apologies.”

[P9]
“Send them back. If they were truly sorry, the heads themselves should have come in person instead of sending their hands and feet. Inform the Inner Hall Master of that, too.”

[P10]
“Next, there’s a matter from the Southern Merchant Guild…”

[P11]
Even while receiving reports, the master of the office, Jin Wikyung, never looked up from the bamboo slips.

[P12]
But at the next report, even he had no choice but to raise his head.

[P13]
“Lesser Family Head, the mounted bandits from the northern plateau are showing suspicious movements near Datong.”

[P14]
“Mounted bandits? Is this information from the Lower District Sect?”

[P15]
“Yes. If we leave them alone, they’ll launch a large-scale raid against the common people.”

[P16]
“How large is their force?”

[P17]
“Five mounted-bandit groups have formed an alliance. Around five hundred men are gradually gathering.”

[P18]
“Mounted bandits, huh? They’ve been a constant nuisance.”

[P19]
Jin Wikyung rubbed the space between his brows with a tired expression.

[P20]
It was true that the Jin Family of Taiyuan possessed formidable power, but it still lacked the strength to cover all of Shanxi Province.

[P21]
That was also why the mounted bandits kept watching for an opportunity despite knowing that the Red Wind Band had been annihilated.

[P22]
“Should we draft some martial artists?”

[P23]
At the scholar’s question, Jin Wikyung immediately shook his head.

[P24]
“No.”

[P25]
“We have more martial artists joining our family than we can count. We have enough manpower.”

[P26]
“We’ve already shed too much blood for that. Besides, those we accepted this time still lack experience. Even if we recruit several hundred, several hundred will die.”

[P27]
The Mount Heng Sword Sect.

[P28]
One of the legs supporting the tripod of Shanxi Province had broken, and the water inside was beginning to spill over.

[P29]
They had to devise a countermeasure before they were scalded by the boiling water.

[P30]
After thinking for a moment, Jin Wikyung spoke.

[P31]
“For the time being, focus on establishing and stabilizing branches in each prefecture and county. That is our top priority.”

[P32]
“Lesser Family Head!”

[P33]
The scholar cried out in surprise. The others, who had been focused on their own tasks, also raised their heads.

[P34]
Hundreds of mounted bandits were supposedly invading, and yet establishing branches was the top priority. Did that mean they did not care whether the common people died?

[P35]
As disappointment spread across the scholars’ faces, Jin Wikyung continued.

[P36]
“Instead, request assistance from the Five Gates of Shanxi. Two hundred should be about right… What do you think?”

[P37]
“That won’t come close to being enough.”

[P38]
There was no one in this office, at least, who could speak so bluntly to the Lesser Family Head of the Jin Family of Taiyuan.

[P39]
Jin Wikyung grinned as he looked at Wipeng, who had just entered through the door.

[P40]
“Is that so? I thought it would be enough.”

[P41]
“What sort of people are the Five Gates of Shanxi now? They’re obsessed with clawing at one another for scraps. They’ll hide their carefully trained elites inside their walls and send us a force packed with clueless Second Rate and Third Rate martial artists.”

[P42]
“That sounds plausible.”

[P43]
“It’s not just plausible. That’s what will happen nine times out of ten. The mounted bandits will see all those peach-fuzzed little punks and be so delighted their mouths will split open.”

[P44]
“Haha. So we have to step in?”

[P45]
“What else can we do? If you attach some useful men to the force, I’ll go there myself. Then the Five Gates of Shanxi won’t be able to pull any sneaky tricks.”

[P46]
“Exactly. Isn’t the Ghost Sword more frightening than a ghost?”

[P47]
At Jin Wikyung’s teasing tone, Wipeng shook his head from side to side.

[P48]
“Enough of that. Tell me what you have in mind.”

[P49]
“What do you mean?”

[P50]
“You already have a plan, don’t you?”

[P51]
“What plan? I thought your idea was pretty good.”

[P52]
“Good grief. Since when have you listened to my words so attentively?”

[P53]
“Every word that comes out of your mouth is a golden rule to me.”

[P54]
Wipeng let out a deep sigh and turned toward the scholar standing blankly nearby.

[P55]
“What do you think?”

[P56]
“Y-yes?”

[P57]
A thin frame and a pale, washed-out face. He was the very picture of a pale-faced scholar who did nothing but pore over books in his room.

[P58]
Startled by Wipeng’s sudden question, he stammered out an answer.

[P59]
“I-I think it’s insufficient.”

[P60]
“Is that all?”

[P61]
“We should draft more men…”

[P62]
Watching him, Jin Wikyung cut in with a laugh.

[P63]
“That’s enough. And you.”

[P64]
The scholar, already cowed by Wipeng’s sharp aura, flinched.

[P65]
“Yes.”

[P66]
“Send word to the Five Gates of Shanxi and the Shanxi Provincial Office. Tell them mounted bandits are swarming around Datong and that we request their assistance.”

[P67]
“The Shanxi Provincial Office?”

[P68]
“The people are in danger. The government ought to step forward. Ah, casually give the Five Gates of Shanxi a hint about it, too.”

[P69]
“Judging by the government’s passive attitude over the past several years, the chances of that succeeding are slim.”

[P70]
“Then make it succeed.”

[P71]
Jin Wikyung’s face lost its smile as he added one more thing.

[P72]
“Isn’t that your job?”

[P73]
“Ah.”

[P74]
The scholar’s mind snapped awake. He was exhausted from staying up several nights, but he had been thinking far too simply.

[P75]
Request help from Shanxi Province? The countermeasure proposed by Wipeng, a man who was a martial artist down to his bones, was much more plausible.

[P76]
“I apologize.”

[P77]
“You’re still inexperienced, so I understand. But what our family needs isn’t scholars. We need wise men who can offer the best possible measures for the sake of our family. I hope you’ll remember that.”

[P78]
There was nothing the scholar could say. Seeing that not only the man before him but everyone else had reddened faces, Jin Wikyung spoke again.

[P79]
“You’re all tired, so go in and rest for today.”

[P80]
No one would refuse an order to rest. Especially not those who had been surviving on brief naps with bamboo slips for pillows for three straight days.

[P81]
Once the scholars dragged their exhausted bodies out, Wipeng pulled over an empty chair.

[P82]
“Are they newly recruited?”

[P83]
“Being on my own was too much. Still, they’re better than nothing.”

[P84]
“I’m not sure. They all seem rather bland.”

[P85]
“How many of them studied in order to join our family? It’s only natural.”

[P86]
Jin Wikyung stretched his arms high. The loud cracking of bones echoed through the room.

[P87]
“It’s only been a few days. We need to separate the jade from the stones and send away those who need to go.”

[P88]
“Is that why you didn’t inform them of the secret agreement with the Shanxi Provincial Office?”

[P89]
“Why is a secret agreement called a secret agreement? The fewer people who know about it, the better.”

[P90]
In truth, securing the assistance of the Shanxi Provincial Office was not particularly difficult. Hadn’t he and Deputy Military Commissioner Hong Jin already exchanged plenty through their conversation five days earlier?

[P91]
“Our family hasn’t fully established itself yet. It would be troublesome if rumors spread that we had entered into a secret agreement with the government under these circumstances.”

[P92]
“That’s true. Even more so if they weren’t rumors but facts.”

[P93]
The conversation Jin Wikyung had exchanged with Hong Jin had included several topics that the small and medium-sized sects of Shanxi Province—and especially the Five Gates of Shanxi—would not welcome.

[P94]
If the Seongun Escort Bureau heard what Jin Wikyung and Hong Jin had discussed, they might collapse frothing at the mouth.

[P95]
“So, are the other preparations going well?”

[P96]
“Yes. I’ve completed the personnel changes as you ordered. The heads of the Inner and Outer Halls have been left in place, and we’ve established three new squads…”

[P97]
The report flowing from Wipeng’s mouth concerned the first matter Jin Wikyung had handled immediately after the war ended.

[P98]
The Jin Family of Taiyuan was like a rising sun. To the hot-blooded young people of Shanxi Province, it was the finest choice available.

[P99]
To embrace the endless stream of people coming to them, the family had to widen its arms even further.

[P100]
“…That’s how I handled it, but since our numbers are expected to continue growing, we’ll likely need to reorganize again later.”

[P101]
“That’s what we should hope for.”

[P102]
Jin Wikyung tried to appear calm as he listened to Wipeng’s report.

[P103]
The Jin Family of Taiyuan had been slowly but steadily declining since the Great Faction War. Yet the Jin Family of Taiyuan now was rapidly recovering its former glory.

[P104]
*No. Perhaps it will become even stronger than it was before the Great Faction War.*

[P105]
If that happened…

[P106]
That would be when they truly earned the right to be called a great family.

[P107]
They would break free of their status as a frontier martial family and stand shoulder to shoulder with the great powers of the realm.

[P108]
*A great family. A great family, huh.*

[P109]
Just thinking about it made his heart race.

[P110]
Just as every martial artist dreamed of becoming the Martial God, Jin Wikyung had long dreamed of raising his family onto the foundation of a great family.

[P111]
*New Year’s Day is almost here.*

[P112]
On that day, before all the sects of Shanxi Murim, the Jin Family of Taiyuan would be recognized as the undisputed hegemon of Shanxi Province.

[P113]
Jin Wikyung had no doubt that the first day of the coming year would become the Jin Family of Taiyuan’s first stepping-stone—and the harbinger of its rise—as a great family.

[P114]
And it was at the very moment he secretly clenched his fists that—

[P115]
“Um, may I come in?”

[P116]
“Hm? Of course.”

[P117]
The owner of the voice that appeared next was the scholar who had just left.

[P118]
“What is it? Did you leave something behind?”

[P119]
“It’s not that…”

[P120]
Under the puzzled gazes of Jin Wikyung and Wipeng, the scholar carefully continued.

[P121]
“There’s some news I failed to report.”

[P122]
“You’re a stubborn one. You’ve been working hard for days without even getting proper sleep. Don’t worry about it. Go in and get some rest.”

[P123]
“No. I should have told you earlier, but I forgot…”

[P124]
“Now, now, it’s all right. I said go rest.”

[P125]
Wipeng added his voice.

[P126]
“My lord is right. You aren’t a jiangshi. You need to get enough rest so you can have the strength to work again tomorrow…”

[P127]
“Huashan has sent the Three Plum Blossom Elites.”

[P128]
Jin Wikyung and Wipeng shot to their feet at the same time.

[P129]
“What!”

[P130]
“What did you say?”

[P131]
Who were the Three Plum Blossom Elites?

[P132]
They were Plum Blossom Swordsmen, known as Huashan’s finest. Among them were three outstanding prodigies who stood above the rest.

[P133]
In particular, Baek Museong, Huashan’s Lone Crane, was a major figure regarded as the future Sect Leader who would carry Huashan’s future on his shoulders.

[P134]
Having heard that, there was no way the two men’s eyes would not bulge.

[P135]
“Is that really true?”

[P136]
“Yes. I meant to tell you at the end, but I forgot. And there’s one more thing.”

[P137]
“One more?”

[P138]
“Another? Tell us quickly!”

[P139]
The visit of the Three Plum Blossom Elites was shocking enough, and now he was saying there was something else.

[P140]
The scholar continued with a frown.

[P141]
“They say the Grandmaster has disappeared. He seems to have gone to our family, so they asked us to send word if we happen to meet him… But who is the Grandmaster?”

[P142]
The scholar was still unfamiliar with the realities of Murim and wondered what this was all about. Jin Wikyung and Wipeng, however, stood with their mouths hanging open.

[P143]
“If Huashan’s Grandmaster is…”

[P144]
“Th-the, th-the…”

[P145]
Sword Saint Mae Jonghak.

[P146]
The two men could not bring themselves to say the name aloud. They merely moved their lips and swallowed hard.

[P147]
Huashan still wanted to keep the Sword Saint’s whereabouts secret. At times like this, it was best to keep one’s mouth shut.

[P148]
“Th-the… What did you say?”

[P149]
“Th-that thing. You know, that sort of thing.”

[P150]
“Yes?”

[P151]
“You can leave now. Erase everything that just happened from your mind. Understood?”

[P152]
The scholar bowed with a bewildered expression and left. Only then did the words they had been holding back burst out.

[P153]
“The Sword Saint is coming!”

[P154]
“Shh! Lower your voice. We don’t even know for certain yet.”

[P155]
Despite his words, Wipeng’s face had also flushed bright red. To a swordsman like him, Sword Saint Mae Jonghak was greater than even the Jade Emperor.

[P156]
To think they might be able to meet such a person in the flesh! No, perhaps he might even receive instruction from him.

[P157]
“B-but why would the Sword Saint come to our family?”

[P158]
“What else could it be?”

[P159]
“Ah.”

[P160]
He had been so excited that he had momentarily forgotten who was currently staying at the Jin Family of Taiyuan.

[P161]
“That Sword Saint broke his seclusion to look for his beloved disciple.”

[P162]
“It’s only a guess for now, but that’s highly likely. I hear he raised him like his own grandson. How deep must his affection be?”

[P163]
Jin Wikyung grinned broadly.

[P164]
Whatever the reason, the Sword Saint’s visit was something to welcome with open arms—not only as a martial artist, but also as the Lesser Family Head of the Jin Family of Taiyuan.

[P165]
“You said his name was Cheongpung, right? Where is he now? I seem to remember hearing a while ago that he was training the youngest in the Wall Lizard Technique.”

[P166]
“The Wall Lizard Technique training ended two days ago, and now he’s…”

[P167]
“And now?”

[P168]
“He’s beating the crap out of the Third Young Master.”

[P169]
“What!”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 백무성    | **Baek Museong**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 155,
  "passed": true,
  "metrics": {
    "source_characters": 5809,
    "translation_characters": 13627,
    "length_ratio": 2.346,
    "source_paragraphs": 168,
    "translation_paragraphs": 169
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "청해",
        "preferred": "Qinghai"
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
        "korean": "고원",
        "preferred": "Gaoyuan"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전하",
        "preferred": "His Highness"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "소원",
        "preferred": "Sowon"
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
