<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1053.txt",
      "sha256": "afb62c53d21643ccbe8b2415629db93e50b640a42603d307a7ba058dad5fdb8e",
      "bytes": 12139
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b2ee31a91db97f136c83786382cdab3d0c244d68f06e720af26e4c095d2be559",
      "bytes": 1462
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5b43d3c9735c32cc11a9f8eff9ee9cd6f7b55a03b9543c836bea43c19c07aa53",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "90097562166115b4a20d35d30f3e4e50ba087310cd246eae5041d311fa9b664e",
      "bytes": 753
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "955cec5b7c743a267f89aa5d6f7ccccc3e13e3e0eecdaed2ac76bd5b0bd82577",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "40b91e5d4c586152c7725d6424ffd4b28b0f9f4f6a33e728b5baf74509bb7e1a",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "38038635239e462c44b3a165b5651376868224661263f2bf065563e01feb4e2e",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 9911
}
-->

# Durable State Update — Chapter 1053

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
1 and safe_through 1053. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1053. Profile updates may replace only one
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
  "chapter": 1053,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1053,
    "continuity_sources": [1053],
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
    "The Bow Saint’s Force arrow struck the Grand Mage; signs of Teleport near her remains leave her fate uncertain.",
    "Jin killed the Blood-Sword Demon Lord after refusing his offer of information; the System chime afterward renewed Jin’s strength.",
    "Jin named Sima Gong, Song Il, and Hwangbo Eom as suspected traitors, but witnessed them fight against the Blood-Sword Demon Lord and help turn the battle. He does not forgive them, but will remember their final acts of honor.",
    "The battle below the hill continues.",
    "The Lord of Heaven wants Jin to survive and grow stronger; the reason is unknown."
  ],
  "continuity_sources": [
    1051,
    1052
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why does the Lord of Heaven want Jin to survive and grow stronger?",
    "What is the Grand Mage’s fate after the signs of Teleport were found near her remains?",
    "What is the Grand Mage’s master’s identity and connection to the Chosen One?"
  ],
  "safe_through": 1052,
  "temporary_decisions": [
    "Render 대마도사 and 대술사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation.",
    "Render the achievement 배 째 as “Go Ahead, Gut Me!”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 마법사     | **mage**              |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1052
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1052
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** Fanatically devoted to the Lord of Heaven, she stays composed while coercing her enemies and treats their resistance with contempt.
- **Voice:** Calm and formally polite while taunting, but drops the courtesy for blunt, scornful challenges when addressing an enemy.
- **Relationships:** She commands the white-robed mages, serves a master who has long awaited Jin Taekyung, and acts to keep Jin alive despite being unable to kill him without her master’s permission.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1052
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1052
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1052
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1053화



세상이 정지한 듯한 거대한 충격 속, 진태경은 일순간 숨을 삼켰다.

섬광처럼 뇌리를 스친 이 믿기 싫은 짐작 앞에서, 마치 칼에 찔린 것처럼 가슴 한구석이 욱신거리는 듯했다.

“무슨 일…….”

“잠시, 잠시만.”

불현듯 석상처럼 굳어 버린 진태경의 모습에, 무언가를 알아차린 적천강이 손을 들어 궁성의 뒷말을 막아 세웠다.

물론 그도 알고 있었다.

촌각이 여삼추라는 것을.

언덕 아래에서는 아직도 치열한 혈투가 이어지고 있는 상황.

하지만 이제는 눈빛만 보아도, 아니 굳이 서로의 눈빛을 보지 않아도 뜻이 통하는 사이다.

어린 제자가 이러한 행동을 보이는 데에는 틀림없이 그만한 이유가 있으리라 늙은 사부는 확신했고, 그 짐작은 빗나가지 않았다.

저벅, 저벅.

극심한 피로로 인해 비틀거리면서도, 홀린 듯이 어딘가로 나아가는 발걸음.

그에 따라 조금씩 가까워지는 눈앞의 광경이, 진태경의 망막 위로 선명하게 틀어박혔다.

갈기갈기 찢어진 채, 어디선가 불어오는 바람을 받아 흔들리는 새하얀 옷자락. 작게 고여 있는 피 웅덩이.

그것은 누군가가 그 자리에 존재했음을 증명하는 마지막 흔적이었고, 진태경은 파르르 떨리는 손을 뻗어 그중 가장 큰 흔적을 매만졌다.

혈관이 비칠 만큼 하얗고, 가느다란 여인의 팔과 다리.

지금 이 순간에도 검붉은 핏물을 울컥울컥 쏟아내고 있는 그것의 단면(斷面)은, 믿을 수 없을 만큼 반듯하고 예리했다.

마치, 잘려 나간 것이 아니라 ‘분리’된 것처럼.

‘이건…… 결코 강기(罡氣)로 인한 상흔이 아니야.’

마침내 마주한 진실 앞에서, 진태경은 참았던 숨을 토해 냈다.

틀림없다. 모를 수가 없었다.

그는 두 세계에 속한 사람이었으니까.

무림인인 동시에, 헌터였으니까.

그렇기에 각각 하나씩 몸뚱어리에서 떨어져 나온 이 팔과 다리에 새겨진 흔적을, 누구보다 확실히 알아볼 수 있었다.

“텔레포트(Teleport)…….”

진태경 자신조차 모르게 입술을 비집고 흘러나온 탄식에, 어느덧 옆으로 다가온 적천강이 딱딱하게 굳은 얼굴로 물었다.

“설마, 노부가 생각하는 그런 상황은 아니겠지.”

진태경은 대답하지 않았다.

그러나 무언(無言)은 곧 긍정을 의미한다는 것을, 적천강은 이미 알고 있었다.

“또 그 해괴한 술법. 아니, 마법(魔法)이냐?”

그래, 맞다.

마법이다. 빌어먹을 그 마법.

뭐라 표현할 수도 없는 탈력감에 휩싸인 진태경이 조용히 고개를 끄덕이자, 적천강의 안광이 번뜩였다.

이미 크고 작은 부상과 피로로 지친 그였으나, 불길이 쏟아지는 눈동자에는 조금의 체념도 깃들어 있지 않았다.

“이럴 때가 아니다. 더 늦기 전에 지금이라도 당장…….”

“이미 늦었습니다.”

“뭐라?”

진태경은 대답 대신 이를 악물었다.

텔레포트.

무수한 종류의 마법 중에서도 유달리 고난이도로 악명 높은 공간 이동 마법.

단거리라는 한계성을 지닌 블링크 마법과는 달리, 텔레포트는 마법사의 등급과 보유한 마나에 따라 단번에 수십. 혹은 수백 킬로미터를 뛰어넘을 수도 있다.

수백 장이 아니라, 수백 킬로미터를.

그렇다면 마법이라는 진리의 끝자락에 도달한 대마도사들은 어느 정도일까.

‘어쩌면…… 모든 조건이 완벽하게 갖춰졌다는 가정하에서라면 대륙의 절반을 가로지를 수도 있겠지.’

확실한 수치는 진태경도 몰랐다.

다만 대마도사라는 대어(大漁)가 이미 그물을 찢고 저 멀리 도망쳤다는 것이 중요할 뿐.

진태경은 더욱 무겁게 전신을 짓누르는 피로를 느끼며 입술을 뗐다.

“저희가 추격할 수 있는 범위를 벗어났어요. 지금쯤이라면 아무리 못해도 최소 수십 리 밖에 있을 겁니다.”

“그게 무슨……!”

적천강은 눈을 부릅떴지만, 이내 뒷말을 삼킬 수밖에 없었다.

눈 깜짝할 사이에 수십 리 밖으로 이동하다니, 이는 상리(常理)를 아득히 벗어난 믿을 수 없는 일이다.

하지만 그 또한 이미 잘 알고 있었다. 심지어 직접 두 눈으로 똑똑히 보기까지 했다.

암천과 연관된 불가사의한 현상들을.

말로도, 상식으로도 설명할 수 없는 마법이라는 귀신의 힘을.

“이런 개 같은!”

콰아앙!

분노를 실어 내리찍은 발끝을 따라 거미줄처럼 갈라지는 지면.

거센 굉음 너머로 궁성의 낮게 가라앉은 음성이 울려 퍼진 것은, 바로 그때였다.

“설령 네 말이 사실이라 해도 사지가 찢어졌으니 목숨이 위태로울 터. 숨이 끊어졌을 가능성은 없느냐?”

진태경은 힘없이 고개를 저었다.

“모릅니다. 하지만 그럴 가능성은 희박할 겁니다.”

“어째서?”

“마법사, 아니 술사(術士)라 불리는 존재들이 분명 그곳에도 있을 테니까요.”

“그렇다는 건…….”

“예. 아군에게 돌아간 겁니다. 저희로서는 그곳이 어디인지 짐작할 수 없지만, 대술사는 정확하게 알고 있었겠죠.”

진태경은 피 웅덩이에 잠긴 팔과 다리를 응시하며 덧붙였다.

“살아남을 수 있다는 믿음이 있었으니, 이런 도박수를 던질 수 있었을 거고요.”

텔레포트는 고난이도의 장거리 이동 마법이다.

출발지와 목적지의 좌표가 한 치의 오차도 없이 정확해야 하며, 다른 어떤 마법보다 철저한 준비 끝에 발동시켜야 한다.

현대 사회에서 텔레포트 마법을 주특기이자 밥벌이로 삼는 고위 마법사들조차 예외는 아니었다.

아니, 오히려 그 위험성을 누구보다 잘 알고 있기에 더욱 신경을 곤두세우기 마련이었다.

주문이 발현되는 과정에서 미세하게라도 수치가 어긋난다면, 바위나 나무와 한 몸이 되어 즉사할 수도 있으니까.

혹은…….

‘사지가 분리되거나.’

마음속으로 조용히 흘러나오는 뇌까림.

진태경은 무거운 눈빛으로 주인의 몸뚱어리에서 떨어져나온 피륙을 바라보았다.

그것은 이제 더 이상 누군가의 죽음을 의미하는 흔적이 아니었다.

대마도사가 목숨을 건 도박을 감행했고, 성공했음을 알리는 증거였다.

‘실수였다. 더 확실하게, 내 손으로 직접 끝장냈어야 했어.’

미처 예상치 못했다.

출발지의 좌표가 매 순간 바뀌어 가는 그 급박한 상황 속에서 대마도사가 텔레포트를 시도하리라고는.

심지어 그토록 지극히 불안정한 상황 속에서 발동한 텔레포트가 성공하리라고는.

하지만 후회는 항상 한 걸음 늦게 찾아오는 법이었고, 진태경은 자신의 앞에 펼쳐진 길을 계속해서 걸어가야 했다.

이제는 조금 더 선명하고 가까워진, 그럼에도 불구하고 어째서인지 더욱 멀고도 아득하게 느껴지는 그 좁고 험한 길을.

더불어 그 끝에서 기다리고 있을, 한 존재를 향해.

‘천주(天主).’

차마 소리가 되어 흘러나오지 못한 채 혀끝에서만 맴도는 그 두 글자를, 진태경은 곰의 쓸개처럼 조용히 곱씹었다.

도대체 그는 누구일까.

무엇을 위해 온 세상을 피로 물들이고, 그 검붉은 장막 속에서 자신을 향해 손짓하는 걸까.

그리고.

바로 지금, 아니 오래전부터 줄곧 머릿속에 맴돌던 또 다른 존재와는 어떤 연관이 있는 것일까.

‘마왕(魔王). 마왕 아스모데우스.’

마계의 지배자. 악마들의 군주.

강대한 힘으로 차원의 경계를 찢고, 모든 상식과 문명을 무너트리며 수십억 인류를 공포와 죽음으로 몰아넣은 침략자.

하지만 끝끝내 어느 한 인간의 손에 쓰러짐으로써, 이제는 역사의 일부로 영원히 기억될 존재.

‘그래, 놈은 죽었어. 분명히.’

그런데 어째서.

도대체 어째서.

그 저주받은 존재가, 머릿속에서 떠나지 않는 것일까.

으득.

진태경은 피가 터지도록 입술을 깨물었다.

현대와 무림을 넘나드는 수년간의 시간 속에서 보았던 수많은 빛과 그림자들.

그러나 암천(暗天)이라는 두 글자가 드리운 어둠은 그 무엇보다 깊고 짙었고, 그 모든 것의 중심에 있는 천주의 존재는 이제는 애써 부정하기조차 어려울 지경까지 이르러 있었다.

상식을 송두리째 허물어트리는 온갖 기현상에 이어, 이제는 마법까지.

‘이 끝에, 도대체 뭐가 기다리고 있는 거지?’

진태경은 문득 고개를 돌려 저 머나먼 서쪽 어딘가를 바라보았다.

마왕과 천주.

천주와 마왕.

본래부터 하나였는지, 혹은 전혀 다른 개인인지 모를 일생일대의 대적(大敵)이 저 서쪽 너머 어딘가에 있다.

‘선택받은 자’를 향해 손짓하며.

아직은 그 누구도 정확히 알 수 없는, 오직 그만이 알고 있을 모종의 이유로.

그리고 이러한 사실을 알고 있음에도, 진태경은 계속해서 이 길을 걸어가야만 했다.

묵묵하고, 처절하게. 온 힘을 다해서 자신이 택한 이 길을.

철벅.

피 웅덩이를 밟으며 일어난 진태경은 떨어지지 않은 발걸음을 뗐다.

아직 끝나지 않은 이 전투를 마무리 짓기 위해서.

지금 이 순간에도 영혼 없는 인형처럼 죽고 죽이는 혈투를 이어가고 있는 수많은 적들을 향해.

“버틸 수 있겠느냐?”

“아뇨.”

당장이라도 쓰러질 것 같은 제자의 모습에 우려를 표하는 사부에게, 진태경은 흐릿하게 웃어 보였다.

“하지만 버텨 내야죠. 어떻게든.”

과거에도, 현재에도.

항상 그래 왔듯이.

쉬이익!

진태경은 망설임 없이 적들을 향해 쇄도했다.

자신의 늙은 스승과 어깨를 나란히 한 채.

이미 머리 위 허공을 가로질러 쏘아지는 강기의 화살과 함께.

그리고 이 거대하고도 끔찍했던 전투를 종결짓기 위해 전장으로 달려가는 것은, 비단 그들 세 사람뿐만이 아니었다.

부우우우!

불현듯 울려 퍼진 뿔피리 소리를 따라 고개를 돌린 이들은 볼 수 있었다.

광활한 대설산의 산맥을 휩쓸며 전장을 향해 짓쳐 드는 희뿌연 먼지구름을.

물경 수천을 아우르는 무수한 인마의 선두에서, 찢어진 깃발을 맹렬하게 휘날리며 피를 토하듯 부르짖는 일단의 무리를.

“복마(伏魔), 멸천(滅天)!”

정순한 공력이 실린 수백의 외침이 공기를 터트린다. 바람을 타고 나부끼는 깃발이 그들과 함께 나아간다.

새하얀 천 위에 점점이 흩뿌려진 핏물도, 찢겨 나간 조각도 그 의미를 사라지게 할 수는 없었다.

그것은 자긍심이었다.

먼 옛날, 시성(詩聖)이라 불린 어느 노인이 심산유곡의 도사들을 칭송하기 위해 지은 시구이기도 했다.

“호신일장검(防身一長劍), 장욕기공동(将欲倚崆峒).”

바람을 타고 흩어지는 적천강의 목소리에 이어, 궁성이 굳게 닫혀있던 입술을 뗐다.

“장검 하나로 몸을 지키고자 하면, 공동(崆峒)에 의지하라.”

그리고 바로 그 순간.

콰드드드드득!

불과 두 시진도 되지 않는 짧은 시간 속.

장장 일만이 넘는 목숨을 집어삼킨, 이 잔혹한 전투의 승패를 결정지을 저울추가 완전히 기울었다.

아니, 부서졌다.

수천 리 밖 어디에선가 오늘의 무대를 준비한, 알 수 없는 누군가가 의도했던 대로.
```

## Final English reading copy

```markdown
# Chapter 1053

Amid the tremendous shock, as if the world had stopped, Jin Taekyung caught his breath for an instant.

At the sight of this guess flashing through his mind—a guess he didn’t want to believe—a corner of his chest throbbed as if he’d been stabbed.

“What happened…?”

“Wait. Just a moment.”

At the sight of Jin Taekyung suddenly frozen like a statue, Jeok Cheongang realized something and raised a hand to stop the rest of the Bow Saint’s question.

Of course, he knew.

That every moment was precious.

A fierce battle was still raging below the hill.

But by now, they understood each other from a glance—or even without looking into each other’s eyes.

The old Master was certain that his young Disciple had a good reason for acting this way. He wasn’t wrong.

Step. Step.

Though staggering from extreme exhaustion, Jin Taekyung walked somewhere as if entranced.

The scene before him drew nearer little by little, imprinting itself sharply on his retinas.

Torn to shreds, the tails of a pure white robe fluttered in a breeze from somewhere. A small pool of blood lay nearby.

They were the last traces proving someone had been there. Jin Taekyung reached out with a trembling hand and touched the largest of them.

A woman’s arm and leg, slender and white enough to show the veins beneath her skin.

Even now, dark red blood was gushing from their cross sections. They were cut with unbelievable precision, smooth and sharp.

As if they hadn’t been cut off, but “separated.”

*This… definitely wasn’t a wound caused by Force.*

At last, faced with the truth, Jin Taekyung let out the breath he’d been holding.

There was no doubt. He couldn’t mistake it.

Because he belonged to two worlds.

He was a Murim martial artist and a Hunter.

That was why he could recognize better than anyone the marks left on these arm and leg, each severed from its owner’s body.

“Teleport…”

At Jin Taekyung’s sigh, which slipped past his lips without his even realizing it, Jeok Cheongang came up beside him and asked, his face rigid,

“Tell me the situation isn’t what this old man thinks it is.”

Jin Taekyung didn’t answer.

But Jeok Cheongang already knew that silence meant yes.

“That bizarre sorcery again. No, Magic?”

That was right.

Magic. That damnable Magic.

Overcome by an indescribable sense of helplessness, Jin Taekyung quietly nodded. A gleam flashed in Jeok Cheongang’s eyes.

He was already worn down by injuries, both large and small, and by exhaustion. Yet there wasn’t a trace of resignation in those eyes, where flames seemed to pour forth.

“This isn’t the time. Before it’s too late, we need to—”

“It’s already too late.”

“What?”

Jin Taekyung clenched his teeth instead of answering.

Teleport.

Among countless kinds of Magic, it was infamous for being exceptionally difficult: a spell that moved someone through space.

Unlike Blink, which was limited to short distances, Teleport could cover dozens or even hundreds of kilometers at once, depending on the mage’s Grade and how much mana they possessed.

Not hundreds of *jang*, but hundreds of kilometers.

Then how far could Grand Mages, who had reached the edge of the truth of Magic, go?

*If… all the conditions were perfectly aligned, maybe they could cross half the continent.*

Jin Taekyung didn’t know the exact distance.

What mattered was that the Grand Mage—a big catch—had already torn through the net and fled far away.

Jin Taekyung felt exhaustion weigh even more heavily on his whole body as he parted his lips.

“She’s beyond our range. By now, she must be at least dozens of *ri* away.”

“What do you mean…!”

Jeok Cheongang’s eyes widened, but he had no choice but to swallow the rest of his words.

To move dozens of *ri* in the blink of an eye—it was unbelievable, far beyond common sense.

But he already knew. He’d even seen it with his own two eyes.

The inexplicable phenomena connected to Dark Heaven.

The ghostly power called Magic, which couldn’t be explained by words or common sense.

“Goddamn it!”

*Boom!*

The ground split like a spiderweb beneath Jeok Cheongang’s foot as he slammed it down in rage.

Beyond the deafening crash, the Bow Saint’s low voice rang out.

“Even if you’re right, her limbs were torn apart. Her life must be in danger. Couldn’t she have lost her life?”

Jin Taekyung weakly shook his head.

“I don’t know. But I doubt that’s likely.”

“Why?”

“There must be people there, too, who are called mages—or sorcerers.”

“Then…”

“Yes. She returned to her allies. We can’t guess where that is, but the Grand Mage would have known exactly.”

Jin Taekyung added, staring at the arm and leg submerged in the pool of blood,

“She must have believed she could survive. That’s why she took a gamble like this.”

Teleport was a high-difficulty spell for long-distance movement.

The coordinates of the starting point and destination had to be accurate to the smallest margin, and the spell required more thorough preparation than any other.

Even high-ranking mages in modern society, who made a living specializing in Teleport, were no exception.

If anything, they were more on edge because they knew its dangers better than anyone.

If even the slightest figure went wrong as the spell took effect, they could die instantly, fused with a rock or a tree.

Or…

*Their limbs could be separated.*

The thought quietly surfaced in Jin Taekyung’s mind.

With a heavy gaze, he looked at the flesh severed from its owner’s body.

It no longer signified someone’s death.

It was proof that the Grand Mage had risked her life on a gamble—and succeeded.

*I made a mistake. I should’ve finished her off myself, made absolutely sure.*

He hadn’t expected it.

Not that the Grand Mage would attempt Teleport in the midst of that frantic situation, with the starting coordinates changing every moment.

And not that Teleport would succeed under such terribly unstable conditions.

But regret always came a step too late, and Jin Taekyung had to keep walking the path ahead of him.

The narrow, treacherous path that now seemed clearer and closer—and yet, for some reason, more distant and beyond reach.

Toward the being waiting at its end.

*Lord of Heaven.*

The name hovered on the tip of his tongue, never spoken. Jin Taekyung silently chewed it over, bitter as bear gall.

Who on earth was he?

What was he trying to do, staining the whole world with blood and beckoning to Jin from behind that dark red curtain?

And…

What connection did he have to the other being who’d been lingering in Jin Taekyung’s mind—not just now, but for a long time?

*The Demon King. Asmodeus.*

The ruler of the Demon Realm. The lord of demons.

An invader who’d torn through the boundaries between dimensions with his overwhelming power, shattered every convention and civilization, and driven billions of people to terror and death.

But in the end, he’d fallen to the hand of a single human—and would now be remembered forever as a part of history.

*Right. He’s dead. He definitely is.*

Then why?

Why on earth couldn’t that accursed being leave his mind?

*Crack.*

Jin Taekyung bit his lip until it bled.

In the years he’d spent moving between the modern world and Murim, he’d seen countless lights and shadows.

But the darkness cast by the name *Dark Heaven* was deeper and denser than any of them. And the existence of the Lord of Heaven, at the center of it all, had become too difficult to deny any longer.

After all the bizarre phenomena that tore common sense apart, now there was Magic, too.

*What on earth is waiting at the end of this?*

Jin Taekyung suddenly turned his head and looked somewhere far to the west.

The Demon King and the Lord of Heaven.

The Lord of Heaven and the Demon King.

He didn’t know whether they’d originally been one being or two entirely different people. The greatest enemy of his life was somewhere beyond the western horizon.

Beckoning to the Chosen One.

For some reason known only to him—one that no one else could yet understand.

And even knowing all this, Jin Taekyung had no choice but to keep walking this path.

Silently and desperately, giving his chosen path everything he had.

*Splash.*

Jin Taekyung rose, stepping in the pool of blood, and forced himself to take a step.

To finish the battle that still wasn’t over.

Toward the countless enemies still killing and dying, even now, like soulless puppets.

“Can you hold on?”

“No.”

Jin Taekyung gave a faint smile to his Master, who’d voiced concern at the sight of his Disciple looking ready to collapse at any moment.

“But I have to. Somehow.”

In the past and in the present.

Just as he always had.

*Whoosh!*

Jin Taekyung charged toward the enemy without hesitation.

At his side, shoulder to shoulder with his old Master.

And with Force arrows already streaking through the air above their heads.

They weren’t the only ones rushing to the battlefield to bring this vast, horrific battle to an end.

*Bwooo!*

At the sound of a horn that rang out without warning, those who turned their heads saw it.

A pale cloud of dust sweeping across the vast mountain range of the Great Snow Mountain as it charged toward the battlefield.

At the head of thousands of people and horses, a group fiercely waved a torn banner and roared as if coughing up blood.

“Subdue the Demons! Destroy Heaven!”

Hundreds of shouts, imbued with pure internal energy, burst through the air. The banner billowed in the wind as it advanced with them.

Not the blood spattered across the pure white cloth, nor the pieces torn away, could erase its meaning.

It was their pride.

Long ago, it had also been a line of verse written by an old man called the Poet Sage, praising the Daoists who lived in the remote mountain valleys.

“*With one long sword to guard the body, one would seek support from Kongtong.*”

After Jeok Cheongang’s voice scattered on the wind, the Bow Saint finally parted her tightly closed lips.

“To protect yourself with a single long sword, rely on Kongtong.”

And at that very moment—

*Rrrrrumble!*

In the brief span of less than two shichen, this cruel battle had swallowed more than ten thousand lives.

The scales that would decide its victor tilted completely.

No—they broke.

Just as some unknown person, somewhere thousands of *ri* away, had intended when they prepared today’s stage.
```
