<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1176.txt",
      "sha256": "b48b586fe6e6b8478d5418aea649e8369e84e7c0356b38c1cedf8004da91396e",
      "bytes": 11689
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c09d1916db06ae9631b1148d1f8a284eb31368ae7eeb51540bb1ed8cffa2d64f",
      "bytes": 1635
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6bd67da46d2a4fea774ad7ef64f30f16a650b1c6d85bd1a995fc818ad294b01a",
      "bytes": 248538
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "55bd329a4e71c9d580d5d1b751494d7dd80316505f0d66ad67165b20254bf6b8",
      "bytes": 844
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "42ef732a7c142094b2394a7e410d9da6db7ab37b2e653c1c0faf2b4addf2c670",
      "bytes": 1701
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "b2660f31656a95e54eb2cf5fd1e7c222fb826542bc78052eb3fdd52debee68a5",
      "bytes": 853
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1df348f7bbe89043d28753da52bd027dbceabfa4104532e5568759a2c330762c",
      "bytes": 295029
    }
  ],
  "estimated_tokens": 9079
}
-->

# Durable State Update — Chapter 1176

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1176. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1176. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1176,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1176,
    "continuity_sources": [1176],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung has logged in to return to the other world after promising his modern-world allies he will come back.",
    "Jin identifies the Lord of Heaven as the living Demon King Asmodeus, who caused the Great Cataclysm.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none is given before the scene ends.",
    "Three days passed while Jin Taekyung was unconscious; Choi Minwoo and the others survived.",
    "The Dragon Heart opened, causing magical power and rift progress to surge.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1175,
    1174
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "What choices will Jin make in the new Main Quest, and what consequences will follow?",
    "Why is Cheon Taemin still alive despite the capsule’s stated permanent binding to its Player until death?"
  ],
  "safe_through": 1175,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 중화 | **Zhonghua** | Patriotic term used in Xiao Shen’s rallying speech. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 타커라마간 | **Taklamakan Desert** | Desert the coalition army is crossing in Xinjiang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 적천강 | 혈주 | hostile_opponents | you | blunt and threatening | Jeok Cheongang blocks the Blood Lord’s final attack on Taekyung and rebukes him. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1153
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1174
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1174
- **Aliases:** None
- **Role:** Morgoth was a Dragon Lord and sovereign of a vast palace, slain by Jin Taekyung when Jin pierced his Dragon Heart.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and regards powerful beings as sources of amusement, willing to aid a worthy rival when it promises greater future entertainment.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth returned the Skeleton King to Jin to help him grow stronger and commands seven soul-stolen S-rank Hunters as Guardians.

## Korean source

```text
＃1176화



로그인, 혹은 로그아웃.

어린 시절 했던 게임이 그랬듯, 보이지 않는 경계를 뛰어넘어 두 세상을 오고 가는 것은 어느덧 나에게 있어 익숙한 과정이 되었다.

단 한 순간에 주위의 모든 것이 사라지고 시야가 암전(暗轉)되면, 나는 어느샌가 홀로 남겨져 있다.

한 치 앞도 볼 수 없는 캄캄한 어둠 속에.

물론 그 어둠은 그리 오래가지 않는다.

곧이어 찾아온 알 수 없는 힘은 내 의식을 어딘가로 이끌고, 그 끝에는 새로운 세상의 빛이 기다리고 있으니까.

하지만 어째서일까.

‘평소와 다르다.’

나는 본능적으로 직감했고, 그 생각이 머릿속을 스친 이후에도 사라지지 않는 어둠에 놀랐다.

‘어째서?’

숨을 쉬듯 익숙해졌던 과정도, 감각도 지금만큼은 낯설다.

평소대로라면 이미 내 의식은 현대를 넘어 무림으로 넘어가 있어야 한다.

그리고 잠시 헤어져 있던 또 다른 육신에서 본래의 감각과 의식을 회복하는 것이 일종의 루틴.

그러나 이번만큼은 모든 것이 달랐다.

영원처럼 길게 이어지는 어둠과 정적도.

그 숨 막히는 인내 끝에 찾아온 이끌림도.

솨아아악.

마치 거대한 토네이도에 맞닿은 것처럼, 감히 짐작할 수도 없을 만큼 깊은 어딘가를 향해 빨려 들어가는 의식.

지금껏 느껴 본 적 없는 강력한 흡인력(吸引力)에 흔들리는 의식의 끈을, 나는 온 힘을 다해 부여잡았다.

‘빌어먹을. 도대체 뭐지?’

이전의 이동 방식이 리무진이라면 지금은 기관차나 다름없었다.

온통 녹슬고 어긋난 선로를 미친 듯이 내달리는, 심지어는 이 속도를 조절해 줄 기관사도 존재하지 않는 고장 난 폭주 기관차.

‘멈춰!’

나도 모르게 마음속에서 울려 퍼진 비명 같은 외침.

하지만 이미 싹수가 샛노란 학교 폭력 가해자가 그 짧은 외침에 괴롭힘을 멈추지 않듯이, 내 의식을 실은 채 어딘가로 향하는 강력한 힘의 파도 역시 멈추지 않았다.

그리고 그 정신 나간 질주의 끝에.

화아아악!

찢겨 나가듯 갈라지는 어둠 너머로, 어느 때보다 강렬한 빛줄기가 들이닥쳐 시야를 집어삼켰다.

어느새 선명하게 자리 잡은 오감(五感)을 통해 전해지는 한 줄기의 목소리도 함께.

“돌아왔구나.”

깨어났느냐, 가 아니다.

돌아왔느냐 물었다.

조금 전의 급박한 상황을 뒤로한 채, 천천히 눈꺼풀을 들어 올린 나는 목소리의 주인을 바라보았다.

로그인이 성공했음을 알리는 시스템 메시지를 시작으로 여러 번의 종소리가 요란하게 울려 퍼지고 있었지만, 그의 음성은 봄비처럼 귓가를 적셨다.

“예, 스승님.”

스승님.

그 자연스러운 호칭에 화왕(火王) 적천강의 눈이 크게 뜨였다.

그리고 이내 보름달처럼 부드럽게 휘었다.

“그래, 잘 왔다.”

마침내, 무림(武林)이었다.



* * *



재회의 기쁨은 짧았다.

정확히는, 굳이 길게 나눌 필요가 없었다.

서로를 누구보다 잘 아는 이들은 그리 긴 말이 필요 없고, 적천강과 나는 그런 관계가 된 지 오래였으니까.

그리고 바로 그런 이유로, 적천강은 내 상태가 심상치 않다는 사실을 즉각 알아차린 것이 분명했다.

“그래, 또 무슨 거지발싸개 같은 일이 벌어진 것이냐?”

“귀신이시네. 어떻게 아셨어요?”

“네놈 몸뚱어리를 봐라. 모를 수가 있는지.”

“제가 뭘…… 아.”

나는 그제야 온몸이 식은땀에 푹 젖어 있다는 사실을 깨달았다.

아니, 몸을 넘어 침상까지 축축하게 적실 정도였으니 이미 오래전 한서불침(寒暑不侵)의 경지에 도달했다는 사실이 무색해질 정도다.

“언제부터 이랬던 겁니까?”

“조금 전부터. 하도 끙끙대길래 똥이라도 지리나 싶었다.”

“…….”

조금 전 느꼈던 훈훈한 공기는 어디 가고, 공중화장실 냄새가 감도는 건 기분 탓인가.

떨떠름하게 입맛을 다신 내가 대답했다.

“글쎄요, 짚이는 일이 한두 가지가 아니라서. 그보다 다른 사람들은요?”

사실, 가장 먼저 묻고 싶었던 질문이다.

아무리 주위를 둘러보아도 보이는 얼굴은 적천강 한 사람뿐이요, 지금 이 순간에도 열심히 내달리는 말들의 투레질 소리를 제외하면 느껴지는 인기척도 없었으니까.

그리고 다음 순간 되돌아온 적천강의 대답은, 이미 곤두서있던 내 촉각을 더욱 서늘하게 만들었다.

“없다.”

“……!”

표현 그대로, 심장이 쿵 하고 내려앉는 기분.

나는 떨리는 음성으로 재차 물었다.

“없어요?”

“없다니까.”

“그러니까 있었는데?”

“아, 없다고! 지금은!”

버럭 화를 낸 적천강이 말을 이었다.

“정확히는 한 시진 전쯤에 다 떠났지. 정찰 겸 오늘 밤 머무를 야영지를 찾아야 해서. 아마 곧 돌아올 게다.”

아니, 이게 뭔 소리야.

잠시 침묵하던 나는 짜게 식은 눈빛으로 적천강을 응시했다.

덜컥 내려앉았던 심장은 원 위치된 지 오래다.

“아니, 처음부터 그걸 말씀해 주셨어야죠.”

“이 버르장머리 없는 놈 보게. 사람 말을 끝까지 안 들은 네놈 잘못이지, 노부 잘못이냐?”

눈을 부라리는 적천강의 모습에 나는 슬쩍 옆으로 고개를 돌렸다.

대국, 아니 대명 제국의 황제가 오직 나를 위해 내려준 크고 아름다운 팔두마차(八頭馬車)의 창밖으로는 어둠에 물든 세상이 펼쳐져 있었다.

“그나저나 이곳은…….”

“그래, 신강(新疆)이다.”

신강.

천하에서 가장 드넓은 땅이자, 아득한 세월 동안 감히 그 누구도 침범하지 못했던 멸지(滅地).

내가 잠시 무림을 떠나 있는 동안, 청해 땅에서 시작된 발걸음이 마침내 이곳까지 닿은 것이다.

그리고 지금 이 순간에도 마차의 틈새로 조금씩 흘러 들어오는 모래 알갱이는, 이곳이 신강의 중심부라는 사실을 증명하고 있었다.

“타커라마간(塔克拉玛干).”

나직하게 뇌까린 적천강이 입안에 들어온 모래를 뱉어 냈다.

“염병할 사막 같으니라고. 노부가 지난 한 달 가까이 했던 그 개고생을 생각하면 정말…….”

적천강의 뒷말은 들리지 않았다.

그리고 그것은 그가 말을 흐려서도, 마차의 창을 때리는 매서운 모래바람 때문도 아니었다.

‘한 달, 벌써 한 달이나 지났다고?’

내가 현대에 머물렀던 기간은 불과 일주일도 되지 않는다.

그런데 그 며칠 동안 무림에서는 한 달의 시간이 흘렀다니.

‘시간의 축이 뒤틀렸다. 돌이킬 수 없을 정도로.’

물론 나로서도 이미 예상은 하고 있었다.

청해성에서 혈주와의 일전을 치른 직후, 현대로 돌아왔을 때부터 시간 비율이 단단히 어긋났다는 사실을 깨달았으니까.

하지만 마음속에만 머물러있는 불길함과 현실로 드러난 불길함은 다른 법.

째깍, 째깍.

로그인 직전, 인벤토리 깊숙이 넣어둔 [고장난 회중시계]의 그 서늘한 초침 소리가 환청처럼 귓가를 울리는 듯했다.

‘하지만…… 한편으로는 벌써 이 정도의 시간이 흘렀다는 게 다행일 수도 있지. 그만큼 목적지에 가까워졌다는 뜻이니까.’

한 달은 결코 짧다고 할 수 없는 시간이다.

현재 천하가 직면한 상황을 생각한다면 더더욱.

그러나 모르고스라는 재앙의 등장으로 불과 열흘 만에 극심한 피해를 입은 현대의 세상과 달리, 이곳에서는 아직 별다른 피해가 없었다.

아니, 적어도 지금 당장은 그리 느껴졌다.

이 질문이 끝났을 때는 모르겠지만.

“혹시 제가 잠들어 있는 동안…….”

“별다른 일이 있었냐고? 아니, 없었다.”

내가 무엇을 물을지 짐작했다는 듯, 망설임 없이 대답한 적천강이 한층 낮아진 음성으로 덧붙였다.

“너무나도 평온해서 기이하게 느껴질 정도로.”

“무슨 뜻입니까?”

“말 그대로다. 하늘은 혼탁하고 도무지 종잡을 수가 없어 시시때때로 눈과 비, 혹은 녹아내릴 듯한 폭염과 우박까지 쏟아지는데…… 그 외에는 아무것도 없어.”

그리 놀라운 이야기는 아니다.

갑작스러운 기후 변화는 현대와 무림, 두 세계에서 동시에 벌어지고 있었고 이제는 어제오늘 일이 아니니까.

게다가 이곳은 신강, 바로 그 천주(天主)가 웅크리고 있는 곳이니 그 강도가 더했으면 더했지 결코 덜하진 않을 것이다.

다만, 나는 그의 마지막 말에 주목했다.

“아무것도 없었다고요?”

“그래. 첫 날에는 그리 큰 이질감을 느끼지 못했지만, 곧 노부를 포함한 모두가 알게 되었지.”

그리고 곧이어 이어진 적천강의 이야기에, 나는 그가 앞서 했던 말에 조금의 과장이나 거짓도 섞지 않았음을 깨달았다.

“처음에는 누구도 신경 쓰지 않았다. 반 시진마다 돌아가며 인근을 정찰하고, 밤에도 경계를 서느라 바빴거든.”

당연한 일이다.

이곳은 신강.

한때 천하를 휩쓸었던 십만마도(十萬魔徒)의 천년 성지이자 암천의 본거지. 

중원에서도 피바람을 불러일으킨 암천이었으니, 제 앞마당이나 다름없는 신강이라면 피바람을 넘어 피바다를 만들어도 이상하지 않다.

“하지만 이상하게도 잠잠하더군. 청해성에서 개떼처럼 몰려들던 그 미친 광신도 놈들은 물론, 상리를 벗어난 괴물들이나 그 흔한 마적 떼 하나 보이지 않았어. 하여 처음에는 그저 저놈들도 겁을 먹었나 싶었다.”

적천강이 그리 생각하던 것도 결코 오만이나 방심은 아니었다.

청해성에서 출발하기 직전, 황제와 천하 무림의 영수들로 구성된 연합군 수뇌부는 물경 십만이 훌쩍 넘는 대군을 세 갈래로 나누었고 그중 하나가 바로 우리였으니.

비록 스무 명도 되지 않는 한 줌의 병력에 불과했지만, 그 면면을 보면 달라진다.

두 개의 별(星)과 열 명의 왕 중에서도 가장 강한 왕(王).

궁성과 살성, 그리고 그런 그들과 어깨를 나란히 하는 화왕까지.

내가 의식을 잃은 상태라고는 해도, 이 세 명의 면면만으로도 능히 일군(一軍)을 칭하기에 부족함이 없었다.

“한데, 바로 그 다음 날이 되자마자 알게 되었지. 노부가 처음부터 잘못 짚었다는 사실을.”

나직한 목소리로 뇌까린 적천강이 불현듯 창가를 향해 턱짓했다.

“알겠느냐?”

“그게 무슨…….”

그 이해할 수 없는 행동에 미간을 좁힌 나는, 문득 말꼬리를 흐렸다.

그리고 일순간 깨달았다.

짙은 어둠 속, 끝없이 펼쳐져 있는 저 광대한 사막에는 모래알만이 가득하다는 것을.

동시에, 아무 소리도 들려오지 않는다는 사실을.

“혹시?”

“그래.”

적천강이 무겁게 가라앉은 음성으로 말을 이었다.

“이 땅에, 살아있는 것이라고는 아무것도 없다.”
```

## Final English reading copy

```markdown
# Chapter 1176

Login—or Logout.

Just like the games I played as a kid, crossing an invisible boundary between two worlds had become a familiar process.

The moment everything around me vanished and my vision went dark, I found myself alone.

In darkness so deep I couldn’t see an inch ahead.

Of course, it never lasted long.

An unknown force would soon take hold of my consciousness and lead it somewhere, and at the end of that journey, the light of a new world would be waiting.

But why?

*Something’s different.*

I sensed it instinctively. Even after the thought crossed my mind, the darkness didn’t fade. That was what startled me.

*Why?*

The process and sensations that had grown as familiar as breathing felt strange now.

By all rights, my consciousness should have already crossed out of the modern world and into Murim.

Then I would recover my usual senses and consciousness in the other body I’d been apart from. It was practically a routine.

But this time, everything was different.

The darkness and silence that went on for what felt like an eternity.

The pull that came at the end of that suffocating wait.

*Whoooosh.*

My consciousness was sucked toward some unfathomably deep place, as if it had collided with a massive tornado.

I clung with all my strength to the thread of my consciousness, shaken by a force of attraction more powerful than anything I’d ever felt.

*Damn it. What the hell is this?*

If the previous trips had been limousines, this one was a locomotive.

A runaway, broken-down locomotive hurtling down tracks that were rusted and out of alignment, with no engineer to control its speed.

*Stop!*

A scream rang out in my mind before I could stop it.

But just as a school bully who was rotten to the core wouldn’t stop tormenting someone because of one short shout, the powerful wave carrying my consciousness somewhere didn’t stop either.

And at the end of that insane ride—

*Whooosh!*

A shaft of light more intense than ever burst through the darkness as if tearing it apart, swallowing my vision.

Along with it came a voice, conveyed through my senses, which had all snapped sharply into focus.

“You’ve come back.”

He didn’t ask if I’d woken up.

He asked if I’d come back.

Leaving the frantic ordeal behind me, I slowly lifted my eyelids and looked at the owner of the voice.

Several bells were ringing loudly, starting with a System message announcing that Login had succeeded. But his voice washed over my ears like spring rain.

“Yes, Master.”

*Master.*

At the natural sound of that title, the Fire King, Jeok Cheongang, widened his eyes.

Then they curved gently, like a full moon.

“Yes. Good to have you back.”

At long last, I was in Murim.

* * *

The joy of our reunion was brief.

More precisely, there was no need to draw it out.

People who knew each other better than anyone else didn’t need many words. Jeok Cheongang and I had been like that for a long time.

And for that very reason, Jeok Cheongang must have noticed right away that something was wrong with me.

“So, what kind of dogshit situation has happened this time?”

“You really can read minds. How’d you know?”

“Look at yourself. How could I not?”

“What about me? I—oh.”

Only then did I realize I was drenched in cold sweat.

It had soaked through my clothes and even the bedding beneath me. So much for having reached the realm of Unaffected by Cold and Heat a long time ago.

“When did this start?”

“Just a little while ago. You were groaning so much I thought you might shit yourself.”

“…”

Where had that warm, gentle feeling from a moment ago gone? Had I imagined the public-restroom stink in the air, too?

I grimaced and answered, “Hard to say. There are too many things that come to mind. Anyway, where’s everyone else?”

That was what I’d wanted to ask first.

No matter how I looked around, Jeok Cheongang was the only face I could see. And aside from the horses snorting as they galloped along, I couldn’t sense anyone nearby.

The answer Jeok Cheongang gave me next made my already-prickling nerves go cold.

“Gone.”

“…”

My heart dropped with a thud. That was exactly how it felt.

I asked again, my voice trembling. “Gone?”

“I said they’re gone.”

“So they were here, but—”

“Ah, they’re gone! Right now!”

Jeok Cheongang snapped, then continued.

“To be precise, they all left about two hours ago. They had to scout around and find a place to camp tonight. They’ll probably be back soon.”

What the hell was that supposed to mean?

I went quiet for a moment, then looked at Jeok Cheongang with a flat stare.

My heart had returned to its proper place long ago.

“You should’ve said that first.”

“Look at this disrespectful brat. You’re the one who didn’t listen to the end. How’s that my fault?”

As Jeok Cheongang glared at me, I turned my head slightly to the side.

Outside the window of the magnificent eight-horse carriage the emperor of the Great Nation—no, the Great Ming Empire—had sent just for me, the world lay shrouded in darkness.

“By the way, where are we…?”

“Xinjiang.”

Xinjiang.

The largest land in the world, a Land of Ruin that no one had dared invade throughout the ages.

While I’d been away from Murim, the journey that began in Qinghai had finally reached here.

Even now, grains of sand trickled through the gaps in the carriage, proving that we were in the heart of Xinjiang.

“Taklamakan Desert.”

Jeok Cheongang muttered the name under his breath, then spat out the sand in his mouth.

“Damn desert. After all the hell I’ve been through for nearly a month, I really…”

I didn’t hear the rest of what he said.

Not because he’d trailed off, or because of the fierce sandstorm beating against the carriage window.

*A month. A whole month has already passed?*

I’d spent less than a week in the modern world.

And yet a month had passed in Murim during those few days.

*The flow of time has gone badly out of sync. Beyond the point of no return.*

I’d already suspected as much.

Right after my battle with the Blood Lord in Qinghai, I’d realized the time ratio was seriously out of whack when I returned to the modern world.

But there was a difference between a sense of foreboding that existed only in your heart and one that had become reality.

Tick. Tick.

The cold ticking of the [Broken Pocket Watch] I’d tucked deep in my Inventory just before logging in seemed to ring in my ears like a phantom sound.

*But… on the other hand, maybe it’s a good thing that this much time has passed already. It means we’re that much closer to our destination.*

A month was no short stretch of time.

Especially given the situation the world faced now.

But unlike the modern world, which had suffered terrible damage in just ten days since Morgoth’s arrival, there hadn’t been any significant damage here yet.

Or at least, it felt that way for now.

Who knew what things would be like once I’d finished asking this question?

“While I was asleep, did anything happen…?”

“You mean, was there any trouble? No.”

Jeok Cheongang answered without hesitation, as if he’d guessed what I was about to ask. His voice dropped lower as he added, “It’s so peaceful it feels strange.”

“What do you mean?”

“Just what I said. The sky is murky and impossible to predict. Snow and rain fall without warning, along with heat that could melt you and even hailstones. But aside from that, there’s nothing.”

That wasn’t all that surprising.

The sudden climate changes were happening in both the modern world and Murim, and they were nothing new by now.

Besides, this was Xinjiang—the place where the Lord of Heaven had holed up—so if anything, the changes here would be worse, not better.

What caught my attention was the last thing he’d said.

“Nothing at all?”

“That’s right. On the first day, none of us noticed anything too strange. But it didn’t take long for everyone, including this old man, to realize.”

And when Jeok Cheongang went on to explain, I realized there wasn’t the slightest exaggeration or lie in what he’d said.

“At first, nobody paid it any mind. We were busy scouting the area in shifts every half shichen and standing watch through the night.”

That was only natural.

This was Xinjiang.

The thousand-year sacred land of the Hundred Thousand Demonic Disciples, who’d once swept across the land, and the base of Dark Heaven.

Dark Heaven had unleashed bloodshed across the Central Plains. It wouldn’t have been surprising if they’d turned Xinjiang, practically their own front yard, into a sea of blood.

“But strangely, it was quiet. Not a single one of those crazy fanatics who’d swarmed at us like a pack of dogs in Qinghai, not a single one of those monsters who defied all reason, not even the usual mounted bandits. At first, I thought maybe those bastards were scared.”

It wasn’t arrogance or carelessness that had led Jeok Cheongang to think that way.

Just before we set out from Qinghai, the emperor and the leaders of the alliance army—made up of the foremost figures in Murim—had divided a force of well over a hundred thousand into three groups. We were one of them.

Our group was a mere handful, fewer than twenty. But look at who was in it.

Two Saints and the strongest of the Ten Kings.

The Bow Saint, the Slaughter Saint, and the Fire King, who stood shoulder to shoulder with them.

Even with me unconscious, those three alone were more than enough to be called an army.

“But the very next day, I realized I’d been wrong from the start.”

Jeok Cheongang muttered in a low voice, then suddenly jerked his chin toward the window.

“Do you see?”

“What are you—”

I frowned at the incomprehensible gesture, then let my words trail off.

And in that instant, I understood.

In the deep darkness, that vast, endless desert was filled with nothing but sand.

At the same time, not a sound could be heard.

“Could it be…?”

“That’s right.”

Jeok Cheongang continued, his voice heavy and subdued.

“There isn’t a single living thing in this land.”
```
