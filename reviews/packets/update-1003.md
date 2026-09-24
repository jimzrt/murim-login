<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1003.txt",
      "sha256": "d099677db016a61a5dc347e97945820b3d24ff9ab5a1da7dc5323938409a98ad",
      "bytes": 13455
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "055481a9e3092cdd862466310f703ad2e595446c1465aefcf9156a76cb6f1957",
      "bytes": 1449
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fdab488e2abd2ce853a2aa9136a548ae8e5b0f6db159f89f31548bb52eaca518",
      "bytes": 236792
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b5bf2e9884b2ab58eaa93ca7e9583b5b9e8e4778317145ad1575a99e27d73e7e",
      "bytes": 1375
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "af9a3717082b2a5c1d245f5348f9a66fb10ac9d1b42d0493ad290414797fd42b",
      "bytes": 974
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "9de065de49c5702b5af92e3a0de3a50307b619e8008f627744071ab679ddbe20",
      "bytes": 937
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "38edcdc3be2106bb0af14eea6ab3a0d186a98cbec7d93e59bc230d2c2c2559fc",
      "bytes": 686
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "e446d3336afb1cf6ac6667daee52f0ddc7070be651db12e8585fc2a200dc471c",
      "bytes": 2458
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "afeffb3ea305c8845f5db1934d4fead68351bfc1c1b8648c3085723dff7f2d83",
      "bytes": 274761
    }
  ],
  "estimated_tokens": 10844
}
-->

# Durable State Update — Chapter 1003

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
1 and safe_through 1003. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1003. Profile updates may replace only one
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
  "chapter": 1003,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1003,
    "continuity_sources": [1003],
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
    "Taekyung’s group and the Zhongnan party have reached Gansu after four days of travel from Taiyuan; Zhongnan disciples remained behind to escort the villagers toward Shaanxi.",
    "The reported mounted bandits near the Shaanxi–Gansu border were a deliberate exaggeration; Ningxia’s mounted-bandit groups had recently shown strange activity but have disappeared.",
    "One unidentified individual pacified Ningxia nearly ten years ago; Jeok Cheongang judged that person to have reached at least Supreme Peak.",
    "Dark Heaven’s advancing army remains a threat, but its destination and objective are unknown.",
    "The Demon-Sealing Formation may neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang."
  ],
  "continuity_sources": [
    1001,
    1002
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?",
    "Who pacified Ningxia nearly ten years ago?",
    "What caused the mounted-bandit groups in Ningxia to show renewed activity, and where have they gone?"
  ],
  "safe_through": 1002,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 주화란    | **Ju Hwaran**      |
| 월화     | **Wolhwa**         |
| 하오문    | **Lower District Sect**          |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마적     | **mounted bandits**                              |                                                       |
| 지부장    | **Branch Leader**                            |
| 표국     | **Escort Bureau**                            |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1002
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1000
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1001
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1000
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 1002
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃1003화



마침내 감숙성에 접어들었다는 사실을 깨닫자, 묘한 긴장감이 좌중 사이로 감돌기 시작했다.

새삼 다시 한번 깨달은 것이다.

자신들이 이곳에 온 목적을.

그리고 바로 이 땅 어딘가에 도사리고 있는 위험을.

‘이중 몇이나 살아남을 수 있을까.’

순간 문득 떠오른 생각을, 나는 조용히 입안으로 삼켰다.

곧 코앞에 들이닥칠 대전투는 피할 수 없다.

그것이 정확히 언제, 어디서냐의 차이일 뿐 반드시 무수한 죽음과 핏물이 온 사방으로 흘러넘칠 것이다.

감숙이 아니라면 청해. 청해도 아니라면 서장과 사천.

‘혹은 여러 방면에서 동시다발적으로 벌어질 수도 있겠지.’

은영각이 입수한 정보가 사실이라면, 사막 너머에서 가까워지고 있을 암천의 병력은 과거의 십만마도(十萬魔徒)와 비견되거나 그 이상.

그 정도의 머릿수라면 비단 한 곳만을 집중적으로 노리지 않아도 될만한, 실로 어마어마한 대군세다.

‘십만마도만큼이나 많고, 그보다 더욱 위험하며, 거기에 더해 이동진(以東陳)까지 가지고 있으니…… 결코 좋은 흐름이 아냐.’

물론 대국까지 합류했으니 아군의 전력 역시 엄청난 수준이지만, 적들이 우리보다 더 많은 선택지를 지니고 있다는 사실은 부정할 수 없었다.

더군다나 내가 어렴풋이나마 품고 있는 짐작이 맞다면, 암천은 고작 사술(邪術)과 광신(狂信)으로 이루어진 집단이 아닐 테니까.

‘어쩔 수 없지. 무림맹 수뇌부도 암천의 저력을 모르지 않을 테니 믿음을 가져 보는 수밖에.’

매 순간 최선을 다하지 않았던 적이 없다.

항상 죽을 고비를 넘겼고, 한 수위의 강적들을 쓰러트렸으며, 더 큰 위기를 막기 위해 고군분투했다.

하지만 그럼에도 불구하고 나 혼자만의 힘으로 모든 것을 해결할 수는 없었다.

이번에도 역시 마찬가지다.

그들이 나를 믿어 주었듯이, 나 역시 그들을 믿어야 한다.

화약의 불씨를 당기는 것은 한 사람의 손으로도 충분하지만, 그 폭발의 여파를 잠재우는 데에는 수많은 이들의 도움이 필요한 법이니까.

그리고 잠시 뇌리를 감돌던 상념은 산길과 함께 끝을 맺었다.

섬서와 감숙 사이를 잇는 험준한 산맥을 완전히 넘어서자, 마치 위장막을 한 겹 벗겨 내듯 전혀 다른 풍경이 드러났기 때문이었다.

높은 고지대와 그로 인하여 비롯된 차가운 공기.

그리고 그 너머로 모습을 드러낸 허허벌판의 중심지에 우뚝 선 황토색 성벽까지.

모래바람과 함께 나타난 저 도시가, 감숙성의 동쪽 끄트머리이자 섬서와 경계를 맞대고 있는 천수(天水)임을 모르는 이는 없었다.

“……거, 분위기 한 번 끝내주네요.”

어쩌면 혁무진의 저 떨떠름한 한 마디는 모두의 마음을 대변하는 것일 터였다.

쓸쓸하고 황량한 분위기.

그것이 나뿐만 아니라 대부분의 사람들이 느꼈을 감숙성의 첫인상이었다.

“어우, 날씨는 또 왜 이래.”

흙먼지를 동반한 서늘한 바람에 몸을 부르르 떤 혁무진이 옷깃을 여몄다.

아닌 게 아니라, 지금 이 순간에도 적지 않은 사람들이 새하얀 입김을 뿜어내는 중이었다.

물론 예외도 있었다.

고강한 초절정의 무위를 바탕으로 한서불침(寒暑不侵)의 경지에 이르렀거나, 그보다는 못 하지만 공력으로 추위를 밀어낼 수 있는 절정 고수들이라든지.

혹은…….

“태산이. 시원해서 좋다!”

그래, 애초에 이곳이 고향인 놈도 있다.

정확히는 ‘놈들’이라고 해야 맞겠지만.

“오랜만이겠네. 안 그래?”

내가 불쑥 던진 한마디에, 말없이 주위를 둘러보던 사마표가 입을 열었다.

“글쎄. 좀 이상한 기분이긴 하군. 고작 일 년 남짓 떠나 있었을 뿐인데…… 마치 십 년은 흐른 것 같아.”

일 년 남짓이라.

누군가에게는 짧고, 누군가에게는 긴 시간이다.

그리고 나는 그런 사마표의 심정을 충분히 이해할 수 있었다.

무림맹이 새롭게 재탄생되던 그 무렵부터 오늘날에 이르기까지.

화룡각의 일원으로서 함께 겪어 왔던 그 위기의 순간들을 그러모아 꾹꾹 눌러 담기에는, 일 년 남짓에 불과한 시간은 너무나도 짧았으니까.

‘그래, 벌써 시간이 그렇게 흘렀나…….’

자신이 나고 자란 고향으로 돌아온 사마표와 태산이 그렇듯, 그런 그들을 바라보는 나 역시 묘한 감흥에 젖었다.

돌이켜보면 참 많은 일들이 있었다.

며칠 동안 쉼 없이 떠들어 대도 부족할 만큼 길고도 복잡한 사건들이.

그리고 그 치열했던 순간마다, 저 두 녀석은 늘 우리의 곁에 있었다.

아니, 그 자체로 ‘우리’였다.

화룡각이라는 이름으로 묶인 동료이자 등 뒤를 맡길 수 있는 전우.

아마도 그 때문일 것이다.

지난날의 감회에 젖어 그윽해진 내 시선에, 사마표 역시 격동을 느낀 듯 파르르 떨리는 눈빛으로 나를 바라보았다.

“각주. 한마디만 해도 되겠나?”

“그럼. 뭐든지.”

“나는 남색(男色)에 아무런 관심도 없다.”

“……?”

“물론 이 부분은 각주도 아닐 거라 믿고 있지만, 혹시 모를 상황을 대비해 말하는 것이니 오해 없길 바란다. 그럼 이만.”

“……!”

격동은 개뿔이.

서둘러 대답한 뒤 말을 몰아 앞질러 나가는 사마표의 뒷모습을 멍하니 지켜보던 나는, 옆에서 느껴지는 은근한 시선에 한숨을 푹 내쉬었다.

“왜요, 뭐 할 말 있어요?”

불쑥 던진 날 선 음성에, 줄곧 옆에서 야무지게 따라오던 하오문도가 황급히 고개를 저었다.

“없습, 아니 사실 있긴 합니다만 나중에 하겠습니다요.”

“…….”

“…….”

“제발 지금 해요. 미루니까 더 수상해 보이잖아.”

“그, 그래도 될는지.”

“아니, 미치겠네.”

뒤통수를 벅벅 긁는 내 모습에 움찔한 하오문도가 눈치를 살피며 입을 열었다.

“다름이 아니라, 제게 하달된 임무는 여기까지라는 말씀을 드리려고 했습지요.”

“여기까지라는 건…….”

“인근의 주민들과 행인들을 피신시킨 뒤, 진 대협께 최근에 있었던 상황을 전달해 드리는 것이었지요. 다행히도 별다른 일 없이 감숙성에 접어들었으니 이제 돌아가야 할 시점인 것 같습니다.”

“돌아간다면, 어디로?”

“혹시 모를 사태를 대비하여 본문과 개방의 문도들이 서방 일대를 주시하고 있으니, 소인은 지부장님께 최대한 빨리 이 소식을 전할 생각입니다.”

눈앞의 하오문도는 섬서지부 소속이고, 하오문 섬서지부장은 내가 익히 아는 사람이다.

산서성 홍화루(紅花樓)의 주인이자, 내가 이 세상에서 처음으로 만난 무림인.

“월화, 아니 지부장님께 안부 전해 주세요. 신경 써 줘서 고맙다고.”

“그렇지 않아도 지부장님 역시 다시 만날 날을 고대하고 계십니다. 본래 섬서 땅을 지나실 때 직접 오시려 했으나, 사정이 여의치 않게 되어…….”

말꼬리를 흐린 하오문도가 품 안에서 뭔가를 꺼내어 내밀었다.

“이건?”

“지부장님께서 진 대협께 직접 전하라 하시더군요. 꼭! 반드시! 절대 잊어선 안 된다고 얼마나 신신당부하시던지.”

단단히 밀봉된 죽통(竹筒)을 내민 하오문도가 은근한 미소와 함께 엄지를 척 치켜세웠다.

“개인적으로 매우 존경합니다.”

“……갑자기?”

“갑자기는 아닌 것 같은뎁쇼.”

뒤룩뒤룩 굴러가는 하오문도의 시선을 따라 고개를 돌리자, 어째서인지 이쪽을 뚫어져라 바라보고 있는 주화란이 있었다.

아니, 정확히는 내 손에 들린 죽통을 침잠한 눈빛으로 응시하는 그녀가.

그러나 그것도 아주 잠시뿐. 이내 나와 시선을 마주친 주화란은 자연스럽게 고개를 돌려 곁에 있던 사람들에게 말을 건넸다.

워낙 순식간에 벌어진 일이라 지금 내가 봤던 게 사실이었나 싶을 정도.

‘도대체 뭐였지?’

눈을 깜빡거리던 내가 그제야 죽통을 받아 들자, 그것으로 자신에게 주어진 마지막 임무를 끝마친 하오문도가 말고삐를 조금씩 늦추기 시작했다.

“그럼 전 이만. 부디 무운(武運)을 빌겠습니다.”

포권지례를 취한 그가 말머리를 돌려 떠나려던 그때, 문득 해결하지 못한 일이 뇌리를 번개처럼 스쳤다.

“아, 잠깐. 마지막으로 한 가지만 부탁해도 되겠습니까?”

“부탁이시라면 어떤……?”

“청해와 감숙 일대에서 벌어지는 모든 상황을 알고 싶습니다. 아주 작은 조짐이라도 상관없으니 최대한 빠르게 전달해 주신다면 좋겠는데요.”

“그 부분에 대해서는 걱정하지 않으셔도 됩니다. 이미 무림맹의 정보망이 가동된 지 오래이니, 비상령이 떨어진 인근의 모든 문파에 속속들이 정보가 전달되고 있을 겁니다.”

나 역시 노파심에 덧붙였을 뿐, 그 부분은 크게 걱정하지 않는다.

애당초 은영각이 멸지(滅地)라고까지 불리는 사막 너머의 정황을 파악한 것부터, 아군의 정보망이 넓고 촘촘하다는 증거였으니까.

그러나 아직 한 가지 마음에 걸리는 부분이 있었다.

“그 정보망에, 녕하성 역시 포함됩니까?”

“예의 마적단이 우려되시는 모양이군요.”

“지금까지의 이야기를 들어 보니, 우려할 수밖에 없는 일인 것 같은데요.”

당연한 일이다.

십여 년 전의 어느 날 미국 서부 시대 뺨치는 무법천지에 갑작스러운 평화가 찾아왔고, 그 모든 사건의 중심에는 정체 모를 초절정 고수가 있다고 했으니.

만약 그가 암천이 천하 곳곳에 심어둔 또 하나의 복검(覆劍)일 가능성이 조금이라도 있다면, 지금 당장 말머리를 돌리는 것부터 고민해 볼 일이었다.

‘정면에서 들이닥치는 놈들을 막는 것도 쉽지 않은 마당에, 양면 전선이 형성된다면 그야말로 최악이야.’

하지만 그런 내 우려와는 반대로, 하오문도는 빙긋 웃어 보였다.

“이거, 소인의 설명이 부족한 탓에 괜히 진 대협의 우려만 키운 모양입니다.”

“그 말씀은.”

“비록 변방이라고는 해도 천하의 일부. 이미 저희 하오문을 비롯한 여러 정보 단체들은 오래전부터 녕하성을 주시해 왔습니다. 정체불명의 고수에 의해 분란이 종결되자 더욱 촉각을 곤두세웠지요.”

“아.”

잠시 간과했다.

정보는 곧 돈이고, 이는 비단 현대에만 국한된 법칙이 아니라는 것을.

아니, 오히려 이런 세상이기에 쓸모있는 정보가 더더욱 귀할 수밖에 없었다.

그리고 하오문은 비슷한 결로 평가받는 개방보다도 훨씬 무림 방파로서의 색채가 옅은, 말 그대로 철저한 정보 상인들.

그런 자들이 녕하성에 벌어진 대사건을 나 몰라라 하고 있었을 리가 있나.

아니나 다를까, 곧 이어진 하오문도의 음성은 내 우려가 무색할 정도로 담담했다.

“녕하성의 마적단들은 이미 해산된 지 오래입니다. 가장 악명을 떨쳤던 두목들은 모두 죽임을 당했고, 나머지는 저항할 엄두조차 못 냈죠. 그 당시의 과정을 주도면밀히 재분석한 결과, 별다른 의문점은 찾지 못했습니다.”

“그럼 인근에서 나타났다는 그 마적들은……?”

“마방(馬房)입니다. 정확히는 ‘한때 마적이었던’ 마방들이라고 해야겠군요.”

마방.

말과 별을 벗 삼아 천하 곳곳을 떠돈다는 자들이다.

상인인 동시에 길잡이 역할을 하는 마방들은 각 지역의 터줏대감이기도 했다.

“해산된 마적들이 마방이 된 거군요.”

하오문도가 고개를 끄덕였다.

“마적으로 계속 남아 있을 수는 없었으니까요. 더러는 마방이 되었고, 더러는 상단이나 표국을 꾸렸다고 합니다. 새로운 시대에 걸맞게 체질을 바꾼 셈이죠.”

“그럼 마적단들을 평정했다는 그 초절정 고수는……?”

“그게 유일한 의문점입니다. 그 후로 줄곧 녕하성에 머무르고 있다고는 하는데, 마두가 아니라는 것 빼고는 누구도 정체를 모릅니다. 본문에서 내로라하는 정보원들도 두 손 두 발 다 들었지요.”

마두가 아니라면 심산유곡의 기인이라는 셈인데.

확실하지는 않아도 우선은 한시름 놓을 수 있는 대답이었다.

그 직후 내가 만족할만한 대답을 내놓은 하오문도는 곧장 길을 떠났고, 천수에 도착한 우리는 생각지도 못한 누군가를 맞닥트렸다.
```

## Final English reading copy

```markdown
# Chapter 1003

At last, we realized we’d entered Gansu Province, and a strange tension began to settle over the group.

It was a reminder of why we’d come here.

And of the danger lurking somewhere in this land.

*How many of us will make it out alive?*

I quietly swallowed the thought that had suddenly crossed my mind.

The great battle about to break over us was unavoidable.

It was only a question of exactly when and where. One way or another, countless lives would be lost, and blood would flood the land.

If not Gansu, then Qinghai. If not Qinghai, then Tibet and Sichuan.

*Or it could break out on several fronts at once.*

If the information the Hidden Shadow Pavilion had obtained was true, Dark Heaven’s forces were drawing closer from beyond the desert. Their numbers were comparable to those of the Hundred Thousand Demonic Disciples—or greater.

That was an absolutely staggering army, so large it wouldn’t need to concentrate its forces on just one place.

*As numerous as the Hundred Thousand Demonic Disciples, even more dangerous, and on top of that, they have Moving Formations… This is going in the worst possible direction.*

Of course, with the Great Nation joining us, our own forces were formidable too. But there was no denying that our enemies had more options than we did.

And if even part of my vague suspicion was right, Dark Heaven wasn’t just a group held together by dark arts and fanaticism.

*It can’t be helped. The Murim Alliance leadership knows Dark Heaven’s strength as well as anyone. All I can do is trust them.*

I’d never once failed to give everything I had.

I’d survived one brush with death after another, defeated stronger opponents, and fought tooth and nail to prevent even greater disasters.

But even so, I couldn’t solve everything by myself.

This time was no different.

Just as they’d trusted me, I had to trust them, too.

One person was enough to light the fuse, but it took many people to deal with the aftermath of the explosion.

And so the thoughts that had circled through my mind came to an end, along with the mountain road.

Once we’d crossed the rugged range separating Shaanxi from Gansu, a completely different landscape appeared, as if someone had pulled away a layer of camouflage.

The high elevation and the cold air that came with it.

And beyond that, ocher-colored walls rising in the middle of a vast, open plain.

There was no mistaking the city that emerged through the sand-laden wind. It was Tianshui, on the eastern edge of Gansu Province, bordering Shaanxi.

“...Now that’s one hell of an atmosphere.”

Hyuk Mujin’s dubious remark might have spoken for all of us.

A bleak, desolate mood.

That was the first impression Gansu made on me—and, I suspected, on most of the others.

“Ugh, and what’s with this weather?”

Hyuk Mujin shivered in the chilly, dust-laden wind and pulled his collar closed.

And sure enough, even now, plenty of people were breathing out clouds of white.

There were exceptions, of course.

Those who’d reached the realm of being Unaffected by Cold and Heat through their formidable Supreme Peak martial arts, or Peak masters who couldn’t quite manage that but could use their internal energy to push back the cold.

And then there was…

“Taishan. Nice and cool!”

Right. One of them was from here to begin with.

Actually, make that two.

“It’s been a while, hasn’t it?”

At my sudden question, Sama Pyo, who’d been silently looking around, answered.

“Hard to say. It feels a little strange. I’ve only been gone for a little over a year, but… it feels like ten years have passed.”

A little over a year.

For some, that was a short time. For others, a long one.

And I could understand how Sama Pyo felt.

From the time the Murim Alliance had been reborn to where we were now, the year we’d spent together as members of the Fire Dragon Pavilion was far too short to hold all the moments of crisis we’d been through.

*Yeah. Has it really been that long already…?*

Like Sama Pyo and Taishan, returning to the place where they’d been born and raised, I was overcome with a strange feeling as I watched them.

When I looked back, so much had happened.

So many long, complicated events that we could talk for days without running out of things to say.

And through every one of those fierce moments, those two had always been at our side.

No—they were part of us.

Comrades bound together by the name of the Fire Dragon Pavilion, warriors who could trust each other with their backs.

Maybe that was why. My gaze had grown distant with memories of the past, and Sama Pyo seemed to feel something too. His eyes quivered as he looked at me.

“Pavilion Master. May I say something?”

“Sure. Anything.”

“I have no interest whatsoever in men.”

“...What?”

“I trust you don’t either, Pavilion Master, but one can never be too careful. I hope there’s no misunderstanding. I’ll be going now.”

“...!”

A moving moment, my ass.

I stared blankly after Sama Pyo as he hurriedly rode ahead, then sighed at the knowing look I felt from beside me.

“What? Got something to say?”

At my sharp, sudden question, the Lower District Sect member who’d been keeping pace beside me quickly shook his head.

“No, sir—well, actually, I do, but I’ll say it later.”

“...”

“...”

“Please say it now. Putting it off makes you look even more suspicious.”

“W-Would that be all right?”

“Oh, for the love of—”

The Lower District Sect member flinched at the sight of me scratching the back of my head, then glanced at me nervously and spoke.

“The mission I was assigned ends here.”

“Ends here…?”

“I was to evacuate the nearby residents and travelers, then inform Great Hero Jin of the recent events. Fortunately, we entered Gansu without incident, so I believe it’s time for me to turn back.”

“Turn back where?”

“Our sect and the Beggars’ Sect have disciples watching the western region in case something happens. I plan to deliver this news to our Branch Leader as quickly as possible.”

The Lower District Sect member before me belonged to the Shaanxi branch. Its Branch Leader was someone I knew well.

The proprietor of Honghwaru in Shanxi Province, and the first martial artist I’d met in this world.

“Give Wolhwa my regards—or, I mean, tell the Branch Leader I appreciate her looking out for us.”

“The Branch Leader is looking forward to seeing you again, too. She originally planned to come in person while you were passing through Shaanxi, but circumstances…”

The Lower District Sect member let his voice trail off, then reached into his robe and held something out to me.

“What’s this?”

“The Branch Leader told me to deliver it directly to Great Hero Jin. She kept emphasizing it—‘Make sure you do! You absolutely have to! Don’t forget!’”

The Lower District Sect member offered me a tightly sealed bamboo tube, then gave me a suggestive smile and flashed a thumbs-up.

“I have a great deal of respect for you, personally.”

“...All of a sudden?”

“Doesn’t seem all that sudden to me.”

I followed the Lower District Sect member’s roving gaze and turned my head. For some reason, Ju Hwaran was staring intently this way.

No, more precisely, she was gazing at the bamboo tube in my hand with a somber look in her eyes.

But only for a moment. As soon as our eyes met, Ju Hwaran naturally turned away and started talking to the people beside her.

It had happened so quickly that I almost wondered if I’d really seen it.

*What was that about?*

I blinked, then finally took the bamboo tube. Having completed the last task assigned to him, the Lower District Sect member began to ease his horse’s pace.

“I’ll be going, then. I wish you good fortune in battle.”

He clasped his hands in farewell and turned his horse to leave, when something I hadn’t dealt with yet flashed through my mind.

“Oh, wait. May I ask you one last favor?”

“What favor would that be?”

“I want to know everything happening in Qinghai and Gansu. Even the smallest sign would be useful. The sooner you can get it to us, the better.”

“You don’t need to worry about that. The Murim Alliance’s intelligence network has been active for quite some time. Information should already be reaching every nearby sect under emergency orders.”

I’d only added that out of caution. I wasn’t too worried about it.

The fact that the Hidden Shadow Pavilion had learned what was happening beyond the desert—a place even called the Land of Ruin—was proof enough that our intelligence network was wide-reaching and thorough.

Still, one thing was bothering me.

“Does that network include Ningxia Province?”

“You’re worried about those mounted bandits?”

“From what I’ve heard so far, it seems like I have reason to be.”

Of course I was.

One day, more than ten years ago, peace had suddenly descended upon a lawless land straight out of the American Wild West. And at the center of it all was an unidentified Supreme Peak master.

If there was even the slightest chance he was another hidden weapon Dark Heaven had planted across the world, then I’d have to consider turning my horse around right now.

*It’s bad enough trying to stop the enemy coming at us head-on. A two-front war would be the worst possible outcome.*

But contrary to my concerns, the Lower District Sect member smiled.

“It seems my explanation was lacking. I’ve only made you worry for nothing, Great Hero Jin.”

“What do you mean?”

“Though it’s a frontier region, it’s still part of the world. Our sect and several other intelligence groups have been keeping an eye on Ningxia Province for a long time. We watched even more closely after the trouble there ended at the hands of that unidentified master.”

“Ah.”

I’d let something slip my mind.

Information was money, and that wasn’t a rule limited to the modern world.

If anything, valuable information had to be even more precious in a world like this.

And the Lower District Sect was far less like a martial sect than the Beggars’ Sect, despite the two being regarded as similar. They were, in the truest sense, merchants who dealt exclusively in information.

There was no way they’d ignored the major incident in Ningxia Province.

Sure enough, the Lower District Sect member’s next words were so matter-of-fact that they made my worries seem misplaced.

“The mounted-bandit gangs in Ningxia Province disbanded long ago. Their most notorious leaders were all killed, and the rest didn’t dare resist. We’ve carefully gone over what happened back then and found nothing particularly suspicious.”

“Then what about the mounted bandits said to have appeared nearby?”

“Horse caravans. More precisely, caravans made up of people who used to be mounted bandits.”

Horse caravans.

People who wandered all over the land with their horses and the stars as their companions.

As both merchants and guides, horse caravans were also fixtures of their respective regions.

“So the disbanded mounted bandits became horse caravans.”

The Lower District Sect member nodded.

“They couldn’t remain mounted bandits forever. Some became horse caravans, while others formed merchant companies or Escort Bureaus. They adapted to suit the new age.”

“Then what about the Supreme Peak master who pacified the mounted bandits?”

“That’s the one thing we still can’t explain. We’re told he’s stayed in Ningxia Province ever since, but no one knows who he is, beyond the fact that he isn’t a fiend. Even our best informants have given up.”

If he wasn’t a fiend, then that left a recluse living deep in the mountains.

It wasn’t certain, but for now, his answer was enough to ease my mind.

The Lower District Sect member had just given me the answer I wanted, and he soon set off on his way.

When we reached Tianshui, we came face-to-face with someone we never expected to see.
```
