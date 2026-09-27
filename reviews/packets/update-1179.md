<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1179.txt",
      "sha256": "2a1bb11221330ae21f3b4ccb93faea5bca36227e67bef53d87b66d7782171047",
      "bytes": 14256
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8dedf5d3fbe7fe7b6b6bab2a56a64bd310e543ddf88d53cb1cff38ebf0af6558",
      "bytes": 1685
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6bd67da46d2a4fea774ad7ef64f30f16a650b1c6d85bd1a995fc818ad294b01a",
      "bytes": 248538
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6deaa3a0b85bdb17da95366fb1fd79405e817b2c3d3075e3007c1de51afa0901",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "9d79986b66cfd0bca36d090668c9d70c2c5a1153ea5d12cab938e1aa400a761e",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4a407dba67f0e41f1c1946f6880001082c4e58ea5306057dcfb9ea02af9b1166",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0c9d445f2e22410d0120cd0c1f24b6119c7e023122b0ed282720ce38a10300c9",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6bde0ee8d08e760f8c64d4d868416fa97056e7f6c3a1580c5a122956a5f58e78",
      "bytes": 295234
    }
  ],
  "estimated_tokens": 10696
}
-->

# Durable State Update — Chapter 1179

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
1 and safe_through 1179. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1179. Profile updates may replace only one
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
  "chapter": 1179,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1179,
    "continuity_sources": [1179],
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
    "Taekyung and his group are crossing the Taklamakan Desert, where the land appears to contain no living things.",
    "Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung comes from the realm of immortals; he has explained that he is human and around twenty-eight.",
    "Great Sir has not been told Taekyung’s secret; Jeok leaves that decision to Taekyung.",
    "Bow Saint has learned Taekyung’s secret and questions whether the Martial God’s letter is truly right; a faint sound comes from behind her.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1178,
    1177
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why does the land around Taekyung’s group in Xinjiang contain no living things?",
    "Who or what is behind Bow Saint?"
  ],
  "safe_through": 1178,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1178
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1178
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1178
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1178
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1179화



반응은 즉각적이었다.

궁성은 마치 모든 것을 예상했던 것처럼 지면을 박차며 뒤로 물러났다.

그리고 그와 동시에, 어느덧 새하얀 강기(罡氣)에 휩싸인 손바닥을 소리의 진원지를 향해 내뻗었다.

퍼어엉!

일순간, 눈부신 섬광이 그녀가 홀로 서 있던 모래 언덕을 뒤덮었다.

아니, 이제는 둘이다.

초대한 적도 없는 불청객이 찾아왔으니까.

‘이런 실수를……!’

평소였다면 굳이 공력의 힘을 빌리지 않아도 반경 이십여 장 안의 모든 것을 빈틈없이 파악하고 있었을 그녀다.

한데 적이 십여 장 안까지 다가왔음에도 알아차리지 못했다니, 궁성은 자신도 모르게 입술을 깨물었다.

상념에 너무 깊게 빠져 있었다.

그 어느 때보다 흔들리고 있던 마음도 분명 한몫했을 것이다.

하지만 그 무슨 이유를 들어도 변명의 여지가 없는 방심이다. 이곳이 신강(新疆)이라는 사실을 생각한다면 더더욱 그랬다.

그나마 다행인 점이 두 가지 있다면, 첫째는 의외로 적의 잠행술(潛行術)이 생각보다 형편없었다는 것이고 둘째는…….

“으허어억!”

숨넘어갈 듯한 비명과 함께 저 멀리 철퍽, 처박힌 적의 뒷모습이 제법 낯익다는 점이었다.

정확히는, 그보다 먼저 도적처럼 들이닥친 무시무시한 악취가.

‘……이 냄새는.’

활을 다루는 만큼 타의 추종을 불허하는 안력(眼力)을 지닌 그녀였지만, 이번만큼은 시야 따위는 필요 없을 정도로 후각이 먼저 반응했다.

꿈에서라도 맡을까 염려될 만큼 끔찍한 악취.

어떻게 이제야 저 냄새를 맡게 된 건지 의문이 들 정도다.

궁성은 울렁거리는 속을 억누르며, 앓는 소리와 함께 일어나는 불청객을 바라보았다.

“당신이 왜 여기에 있죠?”

희미한 의심이 묻어나는 질문.

그리고 다음 순간, 불청객은 언제나 그랬듯이 그녀를 당혹스럽게 만들었다.

“헉, 적! 적이다! 암천이구나!”

“…….”

“복면을 밝히고 정체를 벗어라! 감히 본녀(本女)를 기습하다니, 천주 신명이 두렵지 않느냐!”

처음부터 끝까지 충격적인 그 말에 더는 참지 못한 궁성이 입을 열었다.

“반대예요.”

“뭐?”

“정체가 아니라 복면을 벗어야죠.”

물론 그전에 복면을 쓰고 있지도 않았지만, 그녀는 굳이 더 이상 말해 줄 필요성을 느끼지 못했다.

하나하나 짚어 줘 봤자 내일, 아니 한 시진 후면 잊어버릴 테니까.

아무렇지 않게 스스로를 본녀라 칭하는 저 사내, 대인(大人)은 그런 사람이었다.

‘그래도 암천이 적이라는 사실은 인지하고 있으니 다행인가.’

궁성이 내심 한숨을 내쉬던 그때, 마침내 눈앞의 상대가 누구인지 알아본 대인이 눈을 동그랗게 떴다.

“아니, 소저가 왜 여기에?”

“우선 저는 소저라 불릴 만한 나이가 아니고, 조금 전 그 질문은 제가 할 말인 것 같네요. 심지어 이미 하기까지 했었고.”

궁성은 나직한 목소리로 덧붙였다.

“그 물음에 대한 답은 아직 듣지 못했지만.”

손을 휘감고 있던 강기는 이미 흔적도 없이 사그라졌으나, 보이는 것이 전부는 아니다.

궁성의 몸 안에 쌓인 수 갑자의 공력은 흐름을 늦추기는커녕, 더욱 쾌속하고 은밀하게 회전하고 있었다.

언제든, 주인이 원하는 때에 가장 강맹한 힘을 뿜어내기 위해.

실수는 한 번으로 족하다.

만약 같은 실수를 두 번 저질렀다면 그녀는 궁성이라는 별호로 불리지도, 정마대전에서 살아남지도 못했을 것이다.

“당신이 정찰해야 할 곳은 이 근방이 아닌 것으로 아는데…… 제가 착각한 건가요?”

궁성은 쉬이 의심을 거두지 않았다.

편의상 대인이라 부르고 있지만, 실상은 괴인(怪人)이나 다름없는 그의 정체는 아무도 몰랐으니까.

대인 자신조차 정신이 오락가락하는 마당이니 다른 사람들이야 알 턱이 없다.

그는 자신의 이름도, 과거도 기억하지 못했다.

심지어 화왕 적천강이 ‘이거 하나면 태어나기 전 기억까지 되살아난다.’라고 호언장담하며 뜨끈한 주먹 찜질을 감행했음에도 달라지는 건 없었다.

궁성이 대인에 대해 확신하는 것은 오직 단 하나, 그가 명문정파(名門正派)의 명맥을 이었다는 것뿐이었다.

‘분명 그의 공력은 지극히 정순하다. 하지만 단지 그것만으로 안심할 수는 없어.’

앞서 암천에게 포섭당한 배신자들은 대부분 정파였다.

심지어 천하 오대세가의 일익을 맡고 있던 모용세가는 그 뿌리부터 썩어 있었으니, 중요한 것은 무공이 아닌 그것을 익힌 자의 마음이다.

‘게다가 대인은 초절정의 경지에 오른 고수. 황궁(皇宮)에 머무르고 있을 때 그에 관한 정보를 접한 적은 있지만…… 결국 과거의 행적은 제대로 밝혀지지 않았었지.’

그럼에도 대인을 일행에 포함했을 때 그녀가 반대하지 않은 이유는 두 가지였다.

첫째, 비록 합류가 늦긴 했으나 대인 역시 감숙과 청해에서 죽을 고비를 넘겨 가며 지금껏 제법 돈독한 신뢰를 쌓았으니까.

둘째, 만에 하나 그가 암천이 심어 둔 복검(覆劍)이라 할지라도 지금의 그들에게는 조금도 위협이 되지 않을 테니까.

궁성이 파악한 바에 따르면 대인의 무위는 초절정의 초입.

그것만으로도 대단한 경지인 것은 맞지만, 일행의 면면을 본다면 ‘고작’이라고 표현해도 좋을 정도다.

복검이라고 하기에는 무디고, 간자치고는 허술한.

그렇기에 오히려 가까이 두었다.

너무나도 알 수 없기에, 마지막까지 야트막한 의심의 끈을 놓지 않은 채.

그리고 다음 순간, 그런 궁성을 멀뚱멀뚱 바라보던 대인이 돌연 손뼉을 쳤다.

“아, 맞다. 내가 여기에 온 이유가 소저 때문이었지 참.”

“그게 무슨.”

“한 식경 전쯤인가, 시킨 대로 근방을 싹 돌아보고 마차로 돌아갔다가 엉덩이도 못 붙여 보고 다시 내쫓겼소.”

반쯤 울먹거리던 대인이 목소리를 낮추며 덧붙였다.

“왜, 그 있잖소. 시뻘건 수염만큼이나 성질 더러운 인간. 그 작자 이름이 뭐더라?”

“……적천강 대협?”

“대협은 무슨. 그 인간이 대협이면 본녀는 선녀지. 여하튼 그 인간이 노발대발하면서 얼른 소저를 찾아오라지 뭐요. 뭐 중요한 일이라도 생긴 모양이던데.”

궁성은 맥이 탁 풀리는 것을 느끼며 물었다.

“중요한 일이라는 게 뭐죠?”

“본녀야 모르지. 엉덩이도 못 붙이고 쫓겨났다니까? 그런데 겨우 여기까지 왔더니 소저가 인정사정없이 일장을……!”

“적으로 오해했어요. 미안해요.”

말하다가 열이라도 받았는지, 발을 동동 구르는 대인을 다독인 궁성은 천천히 공력을 가라앉혔다.

사실 여부는 돌아가서 확인해 봐야겠지만, 지금의 대인이 거짓말을 하는 것처럼 느껴지지는 않았다.

그러니까, 적어도 오늘 이 자리에서만큼은.

“한데 무슨 생각을 그리 깊게 하고 있었소? 뒷모습이 너무 활기차 보여서 부르려다가 꾹 참았는데. 뭐 그거 때문에 오해를 사긴 했지만.”

또 한 번 기습적으로 발휘된 기상천외한 언행에, 궁성은 자신도 모르게 피식 실소를 흘렸다.

“제가 그렇게 활기차 보였나요?”

“그랬소. 희미한 달빛을 받으며 홀로 서 있는데 그 모습이 어찌나 밝고 활기찬지…… 어, 이게 아닌가?”

“아니에요. 맞아요. 그리고요?”

“뭐라 혼잣말로 중얼거리는 것 같긴 했는데, 잘은 못 들었소. 소리가 워낙 작아서.”

궁성으로서는 다행이었다. 그리 큰 문제가 될 내용은 아니었지만, 그렇다고 해서 남에게 들려 주고 싶은 이야기도 아니었으니까.

이건 그녀만의 비밀이다.

그 누구도 알아서는 안 되는, 그러나 언젠가는 선택해야만 하는.

하지만 대인의 말은 거기서 끝이 아니었다.

“누구를 생각하고 있던 거요?”

막 앞을 향해 나아가려던 발걸음이 허공에서 우뚝 멈췄다. 이내 천천히 내려간 궁성의 발끝이 사박, 모래를 밟았다.

“무슨 뜻이죠?”

애써 담담하게 되묻는 궁성을, 대인은 물끄러미 바라보았다.

먹구름이 낀 것처럼 혼란한 정신을 지닌 그였지만, 눈동자는 한여름날의 그것처럼 맑고 깨끗했다.

“글쎄, 본녀도 잘은 모르겠소. 다만…… 당신은 분명 누군가를 그리워하고 있었소. 동시에 괴로워했지.”

“……!”

일순간, 궁성의 눈빛이 파르르 떨렸다.

귓가를 타고 흘러들어온 대인의 목소리가, 마치 칼날처럼 뇌리를 헤집는 듯했다.

그러나 어째서일까.

그것은 단순한 고통처럼 느껴지지 않았다.

너무나도 오래 방치되어, 이미 썩을 대로 썩은 환부(患部)를 씻어내는 차가운 물과 같았다.

아마도 그 때문이었을지 모른다.

영원히 굳게 닫혀 있을 것만 같던 입술이 불현듯 열린 것은.

흐린 달빛만 남은 이 쓸쓸한 사막에서 마주하고 있는 유일한 인물이, 스스로의 이름을 잊었듯 내일이면 아무것도 기억하지 못할 괴인이라는 사실 때문일지도 몰랐다.

어쩌면 이 모든 것이 그저 핑계일지라도.

“맞아요.”

“역시, 내 그럴 줄 알았지! 어떻소, 본녀의 안목이?”

어린아이처럼 좋아하는 대인의 모습에, 궁성은 작게 소리내어 웃었다.

그것은 이 자리에 없는 일행이 보았다면 깜짝 놀랐을 만큼, 진실된 웃음이었다.

“정확하네요. 지금껏 알던 그 사람이 맞나 싶을 정도로.”

“이게 다 경험에서 우러나온 거요. 잘 기억은 안 나지만 본녀가 소싯적에는 남녀노소를 불문하고 인기가 참 많았던 것 같거든. 여하튼 좌우지간 누구요? 소저가 그리워하는 그 사람이.”

“비밀이에요.”

“비밀이라, 그거 좋지.”

몸이 단 사람처럼 손바닥을 비빈 대인이 재차 물었다.

“그를 연모했소?”

잠시 침묵하던 궁성이 고개를 저었다.

“경애(敬愛)했죠. 다른 모두가 그랬듯이.”

“저런, 끝끝내 마음을 전하지 못한 모양이구려. 안타까운지고.”

“아니라고 말했을 텐데요.”

“말은 어디까지나 말일 뿐이오. 말과 행동이 다르면 행동만이 진실이지. 소저가 잠시나마 망설인 것처럼 말이오.”

“……!”

“망설임은 언제나 후회를 낳지. 후회는 때때로 잘못된 선택을 부르기도 하고. 하지만 누구에게나 선택의 기회는 있소. 한번 쏟아진 물을 온전히 주워 담지 못하더라도, 닦아 낼 수는 있는 것처럼.”

얼음장처럼 차가운 물을 뒤집어쓴다면 이런 기분일까.

짧았던 꿈에서 깬 사람처럼, 그녀는 크게 뜨인 눈으로 대인을 바라보았다.

“당신…….”

묻고 싶었다.

대관절 당신은 누구인지, 어떻게 그와 같은 괴인에게서 현기(玄機)가 느껴지는 것인지.

하지만 궁성의 말이 채 끝맺어지기도 전에, 대인이 은근한 목소리로 속삭였다.

“그러니까 더 늦기 전에 고백하시오. 조만간, 아니지. 당장 오늘이 좋겠군.”

“네?”

“어허, 사람을 물로 보지 마시오. 본녀는 진즉 알고 있었소. 소저가 그 성질 더러운 인간의 제자에게 깊은 관심을 갖고 있었다는 사실을.”

아주 잠깐, 그 말의 의미를 이해하지 못하던 궁성이 가까스로 입을 열었다.

“……설마 진태경, 그 아이를 말하는 건가요?”

“그거야 당연, 흠. 비밀이라고 했지. 그 부분은 내 지켜드리리다.”

“…….”

“부끄러워할 필요 없소. 그냥 확 저질러 버리면 편하다니까? 물론 그 친구가 무공 세고 가문이 좋기야 한데, 소저도 전혀 꿀리지 않소. 내 듣자 하니 가업으로 하는 표국도 잘 나간다면서?”

그 한 마디로 모든 의문이 풀렸다. 왜 아들뻘인 대인이 그녀를 소저라 불렀는지도.

궁성은 자신도 모르게 눈을 질끈 감았다.

그리고 많은, 아주 많은 생각과 감정을 온 힘을 다해 억누르며 대답했다.

“그건 제가 아니에요.”

“아니긴 무슨, 본녀도 다 들은 이야기가 있는…… 어라?”

문득 말을 멈춘 대인이 소매로 눈가를 쓱쓱 비비더니, 이내 정색하며 말했다.

“여협(女俠)께서 왜 여기 계십니까?”

“……!”

“아, 맞다. 어느 성질 더러운 인간. 아니 적 대협께서 여협을 모셔 오라고 했습니다.”

궁성은 반쯤 해탈한 보살의 마음으로 대답했다.

“당장 가죠, 제발. 무슨 중요한 일인지도 안 물어볼 테니까.”

“그러게요. 저도 궁금합니다.”

그러나 궁성이 진정한 해탈의 경지에 도달하는 일은 벌어지지 않았다.

다음 순간 이어진 대인의 말에, 그녀는 이성의 끈이 끊어지는 것을 느꼈다.

“뭔 일이 있긴 한 건지, 진태경 그 친구도 여협을 찾더라고요. 한 달이나 푹 자고 일어나서 그런지 쌩쌩해 보이던데.”

제자리에 석상처럼 굳어 버린 궁성을 뒤로한 채, 대인은 휘적휘적 걸음을 옮겼다.

그리고 여전히 흐린 하늘의 저 너머를 바라보다 툭, 내뱉었다.

이미 백팔번뇌(百八煩惱)에 휩싸인 궁성의 귀에는 들리지 않을, 아주 작은 목소리로.

“한바탕 폭우가 쏟아지겠군.”
```

## Final English reading copy

```markdown
# Chapter 1179

Her reaction was immediate.

As if she’d expected this all along, Bow Saint kicked off the ground and darted backward.

At the same time, she thrust out a palm toward the source of the sound, now wreathed in brilliant white Force.

*Boom!*

In an instant, a blinding flash engulfed the sand dune where she’d stood alone.

No—not alone anymore.

An uninvited guest had arrived.

*What a mistake…!*

Normally, she could have sensed everything within a radius of twenty-odd zhang without even drawing on her internal energy.

And yet she hadn’t noticed the enemy until they were within a dozen zhang. Bow Saint bit her lip before she knew it.

She’d been lost in thought.

The fact that her heart had been more unsettled than ever had surely played a part.

But whatever the reason, there was no excuse for such carelessness. Especially when they were in Xinjiang.

If there were two silver linings, the first was that her enemy’s stealth technique was surprisingly poor. The second was…

“Gwaaaah!”

With a strangled scream, the enemy went flying and landed with a wet smack in the distance. Their silhouette was strangely familiar.

More precisely, the horrendous stench that had arrived before him, barging in like a thief.

*…That smell.*

Bow Saint was an archer, and her eyesight was second to none. But this time, her sense of smell reacted before her eyes were even needed.

A horrendous stench—the kind she feared she might catch even in a dream.

She almost wondered how she’d only just noticed it.

Suppressing the queasy churn in her stomach, Bow Saint watched the uninvited guest groan and struggle to his feet.

“Why are you here?”

Her question carried a trace of suspicion.

And then, as always, the uninvited guest managed to leave her dumbfounded.

“Gah! An enemy! It’s Dark Heaven!”

“…”

“Reveal your mask and take off your identity! How dare you ambush me! Do you not fear the Lord of Heaven?”

Bow Saint couldn’t hold back any longer. She spoke up, stunned from beginning to end.

“It’s the other way around.”

“What?”

“You take off the mask, not your identity.”

Of course, he hadn’t been wearing a mask in the first place. She didn’t think there was any need to explain that much.

Even if she spelled it all out for him, he’d forget by tomorrow—no, in an hour.

That man, who casually referred to himself as “this lady,” was Great Sir.

*At least he knows Dark Heaven is the enemy.*

Bow Saint was sighing inwardly when Great Sir finally recognized the person before him. His eyes widened.

“Wait, why are you here, Young Lady?”

“First, I’m not young enough to be called that. And I think I’m the one who should be asking you that. I even asked you already.”

Bow Saint added in a quiet voice, “And I still haven’t heard your answer.”

The Force that had wrapped around her hand had already vanished without a trace, but appearances could be deceiving.

The internal energy accumulated within Bow Saint—several jiazi’s worth—wasn’t slowing its flow. It was circulating faster and more quietly than ever.

Ready to unleash its full strength whenever its master wished.

One mistake was enough.

If she’d made the same mistake twice, she wouldn’t be called Bow Saint, and she wouldn’t have survived the Great Faction War.

“I thought you were supposed to scout somewhere else. Am I mistaken?”

Bow Saint didn’t let her suspicion go easily.

For convenience, she called him Great Sir. In truth, he was little different from a strange eccentric, and no one knew who he really was.

Even Great Sir himself could barely keep his mind straight. How could anyone else know?

He remembered neither his name nor his past.

Not even when the Fire King, Jeok Cheongang, had confidently promised, “This’ll bring back memories from before you were born,” then given him a thorough beating with his fists.

The one thing Bow Saint knew for certain about Great Sir was that he carried on the legacy of an orthodox sect.

*His internal energy is undoubtedly pure. But that alone isn’t enough to put me at ease.*

Most of the traitors who’d joined Dark Heaven had come from orthodox factions.

Even the Murong Family, one of the Five Great Families, had rotted from its roots. What mattered wasn’t the martial arts themselves, but the heart of the person who practiced them.

*Besides, Great Sir is a Supreme Peak master. When I was staying in the Imperial Palace, I came across information about him, but… in the end, no one ever properly uncovered his past.*

Even so, there were two reasons she hadn’t objected to including him in their group.

First, though he’d joined them late, Great Sir had faced death alongside them in Gansu and Qinghai. By now, they’d built a fairly solid trust.

Second, even if he was a hidden blade planted by Dark Heaven, he posed no threat to them now.

As far as Bow Saint could tell, Great Sir was at the very beginning of the Supreme Peak realm.

That was a remarkable level in its own right. But compared with the people in their group, it was fair to call him “merely” a Supreme Peak master.

Too blunt to be a hidden blade. Too careless to be a spy.

That was precisely why she’d kept him close.

Because he was so impossible to understand, she’d kept a faint thread of suspicion alive to the very end.

Then, as Bow Saint watched him stare blankly at her, Great Sir suddenly clapped his hands.

“Oh, right! I came here because of you, Young Lady.”

“What are you talking about?”

“About half an hour ago, I finished scouting the whole area like I was told and went back to the carriage. But before I could even sit down, I got kicked right back out.”

His voice had been half tearful. Now he lowered it.

“You know that red-bearded man with the temper to match? What was his name?”

“…Great Hero Jeok Cheongang?”

“Great Hero, my foot. If that man’s a Great Hero, then this lady’s a fairy. Anyway, he was furious and told me to hurry up and find you. Sounded like something important had happened.”

Bow Saint felt her energy drain away.

“What’s this important thing?”

“How should I know? I told you, I didn’t even get to sit down. And then, after I’d come all the way here, you hit me with no mercy!”

“Sorry. I mistook you for an enemy.”

Great Sir was stamping his feet, apparently getting worked up as he spoke. Bow Saint soothed him and slowly calmed her internal energy.

She’d have to check whether what he’d said was true once they got back, but Great Sir didn’t seem to be lying.

At least, not here and now.

“But what were you thinking so hard about? You looked so cheerful from behind. I was going to call out to you, but I held back. Then you mistook me for an enemy anyway.”

Once again, he’d caught her off guard with his bizarre words and behavior. Bow Saint couldn’t help letting out a quiet laugh.

“Did I really look that cheerful?”

“You did. Standing there alone in the faint moonlight, you looked so bright and cheerful that… Oh, was that not right?”

“No, it was. And then?”

“You looked like you were muttering something to yourself, but I couldn’t make out what. Your voice was so quiet.”

That was a relief. It hadn’t been anything too serious, but it wasn’t something she wanted anyone else to hear.

This was her secret.

One no one could know about—but one she would have to decide on someday.

But Great Sir wasn’t finished.

“Who were you thinking about?”

The step she’d been about to take forward stopped in midair. Then Bow Saint’s foot slowly came down, pressing softly into the sand.

“What do you mean?”

Great Sir looked at her steadily as she made an effort to keep her voice calm.

His mind was clouded, as if covered by dark clouds, but his eyes were as clear and bright as a midsummer day.

“I don’t know, either. But… you were definitely missing someone. And you were suffering at the same time.”

“…”

For an instant, Bow Saint’s eyes trembled.

Great Sir’s voice swept into her ears and seemed to rake through her mind like a blade.

But why?

It didn’t feel like mere pain.

It was like cold water washing over a wound that had been neglected for so long it had already rotted through.

Maybe that was why her lips, which had seemed sealed forever, suddenly parted.

Perhaps it was because the only person with her in this lonely desert beneath a dim moon was an eccentric who’d forgotten his own name and wouldn’t remember anything tomorrow.

Or perhaps that was all just an excuse.

“That’s right.”

“I knew it! What do you think of this lady’s eye for people?”

Watching Great Sir delight in himself like a little child, Bow Saint let out a soft laugh.

It was so genuine that anyone from their group who’d been there would have been stunned.

“You were right. I almost wondered if you were the same person I’d known all this time.”

“It all comes from experience. I don’t remember much, but I think I used to be pretty popular in my younger days, with men and women, young and old. Anyway, who is it? The person you miss?”

“It’s a secret.”

“A secret? I like that.”

Great Sir rubbed his palms together, as impatient as a child, then asked again.

“Were you in love with him?”

After a moment’s silence, Bow Saint shook her head.

“I respected and admired him. Just as everyone else did.”

“Ah, so you never managed to tell him how you felt. What a shame.”

“I told you that’s not what I meant.”

“Words are only words. When words and actions don’t match, actions are the truth. Like how you hesitated just now.”

“…”

“Hesitation always leads to regret. And regret sometimes leads to the wrong choice. But everyone gets a chance to choose. Even if you can’t put spilled water back in the cup, you can still wipe it up.”

Was this what it felt like to have a bucket of ice-cold water thrown over her?

As if waking from a brief dream, she stared at Great Sir, her eyes wide.

“You…”

She wanted to ask.

Who was he, really? How could an eccentric like him give off such an air of profound wisdom?

But before she could finish, Great Sir whispered conspiratorially.

“So confess before it’s too late. Soon—no, today would be best. Right now.”

“What?”

“Oh, don’t take me for a fool. I knew it all along. You’ve got a deep interest in that ill-tempered man’s Disciple.”

For a brief moment, Bow Saint couldn’t understand what he meant. Then she finally managed to speak.

“…You mean Jin Taekyung?”

“Obviously, hm. You said it was a secret. I’ll keep that part to myself.”

“…”

“There’s no need to be embarrassed. Just go for it. It’ll be a relief! Sure, that fellow’s good at martial arts and comes from a good family, but you’ve got nothing to envy there. I hear your family’s Escort Bureau is doing well, too.”

Those words explained everything. Why Great Sir, a man old enough to be her son, had called her Young Lady.

Bow Saint squeezed her eyes shut.

Then, with all her strength, she reined in a great many thoughts and feelings before answering.

“That’s not me.”

“Don’t be ridiculous. I heard it from someone and everything… Hm?”

Great Sir abruptly stopped talking. He rubbed his eyes with his sleeve, then turned serious.

“Why is a heroine here?”

“…”

“Oh, right. That ill-tempered man—no, Great Hero Jeok told me to bring you over.”

Bow Saint answered with the heart of a Bodhisattva who’d almost reached enlightenment.

“Let’s go. Now, please. I won’t even ask what the important thing is.”

“I’m curious, too.”

But Bow Saint never reached true enlightenment.

At Great Sir’s next words, she felt the thread of her reason snap.

“I wonder if something’s happened—Jin Taekyung was looking for you, too. He looked full of energy after sleeping for a whole month.”

Bow Saint froze like a statue as Great Sir ambled away.

He gazed out toward the far side of the still-clouded sky, then murmured casually.

So quietly that Bow Saint, already caught in the grip of a hundred and eight earthly desires, couldn’t hear him.

“A downpour’s coming.”
```
