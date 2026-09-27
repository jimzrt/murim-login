<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1077.txt",
      "sha256": "37e630716859e813fca3957eb22379a05237523cf6774ab205787be10d69014e",
      "bytes": 12314
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d9cc4c60e3349258998f4ae3309feedb13b7304dd84509ae68c8fb67f9187c57",
      "bytes": 1232
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "216361ec2af0a487c1fafa03364fc57b01a7ff585b2d9e383074e84057128d5d",
      "bytes": 242679
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "75460b29f7185f4e0142a6894b89a7274726c75603f2c4f4f782f11fe05432a5",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "c1d6ae51f6a8ab267f6d39df9bcdb743051f7717ca2b353b1d91b6becd76c605",
      "bytes": 839
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7fef100386c3179224469916ab0a6e3db6bf6b8cb4faa301e86cabdae0cd1dd7",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b9265b6ae1a0bb425c2b54ee1a7e53d08604afda66db8f3d438ffc7d1b8a5604",
      "bytes": 623
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "70899d065712a2b7efd5773440175c9b057147bf95cda433b1c6a67c60a02572",
      "bytes": 832
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "904406ca0e1b0c39da57c11e5923df421e74498481ccb1bc16da72ee06542272",
      "bytes": 285760
    }
  ],
  "estimated_tokens": 9566
}
-->

# Durable State Update — Chapter 1077

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
1 and safe_through 1077. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1077. Profile updates may replace only one
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
  "chapter": 1077,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1077,
    "continuity_sources": [1077],
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
    "Taekyung’s group reunited with Cheongpung and the Slaughter Saint after several months.",
    "The Slaughter Saint and Cheongpung defeated the monsters and stopped Dark Heaven’s pursuit.",
    "The group reached Qinghai Lake with Gung Gibang’s group and a bound black-robed captive.",
    "Cheongheoja, the Kunlun Sect Leader and Hak Woo’s master, arrived at Qinghai Lake; Hak Woo is safe and will meet Taekyung after they leave.",
    "Dozens of ships are arriving to carry the group’s roughly three thousand allies away from Qinghai Lake.",
    "Kunlun surrendered its headquarters to protect lives.",
    "Cheongheoja warned of a hidden ember that may bring disaster; campfires on the shore represent hope of resisting it."
  ],
  "continuity_sources": [
    1075,
    1076
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "What is the connection between Soonja and the Slaughter Saint?",
    "What does the Bow Saint mean by setting everything right?",
    "What happened to the Great Sir’s boy companion?",
    "What is the hidden ember Cheongheoja warned about?"
  ],
  "safe_through": 1076,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 살성     | **Slaughter Saint**           | —              |
| 일신     | **One God**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 청해     | **Qinghai**            |
| 소생      | **I**; occasionally “this humble one” in highly formal dialogue |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 살문 | **Killing Gate** | Command given while the Hundred and Eight Arhats Formation is deployed. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 살천문 | **Salcheonmun** | Vanished assassin sect once associated with Mungyeong. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 무영 | **No Shadow** | The concealed Supreme Peak assassin serving the Emperor. |
| 계야부 | **Gye Yabu** | Level 140 Salcheonmun assassin killed by Jin Taekyung. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1072
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1070
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1075
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1075
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1068
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s former Brush-Holding Eunuch, a sorcerer and former Disciple of another Demon Lord who now serves the Blood Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan; he now serves the Blood Lord.

## Korean source

```text
1077화




한 무리의 흑의인들이 어느 야트막한 언덕 위에 모습을 드러낸 것은, 정오 무렵의 일이었다.

슥.

파파팟!

선두의 사내가 가볍게 내저은 손짓에, 수십여 명의 흑의인이 곳곳으로 흩어졌다.

이곳에서 벌어진 일들을 조사하고, 동시에 수습하기 위해서.

“벌써 선객(先客)이 와 있었군.”

작게 뇌까린 사내는 언덕 아래에 펼쳐진 광경을 내려다보았다.

정확히는, 반경 십여 리에 걸쳐 펼쳐진 광활한 갈대숲과 그 사이사이를 새카맣게 메운 무수한 날짐승들을.

“그간 굶주렸겠지. 퍽 힘든 여정이었을 테니.”

이곳에서 며칠 거리에 있는 청해호(靑海湖)는 철새들의 안식처이기도 하다.

천 리에 달하는 거리를 쉼 없이 날갯짓해야 하는 고난이 뒤따르지만, 그럼에도 매년 엄청난 숫자의 철새들이 청해호에 오는 이유는 깨끗한 물과 풍부한 식량이 있기 때문이었다.

물론, 이제는 모두 옛말이 되어 버렸지만.

솨아아아.

시린 냉기를 머금은 바람이 불현듯 갈대숲을 휩쓸자, 열심히 주린 배를 채우던 철새들이 부르르 몸을 떨었다.

단순히 고지대(高地帶)라는 이유로는 도저히 설명할 수 없는 추위.

태양이 가장 높게 떠 있어야 할 정오의 하늘은 어느덧 새카만 먹구름으로 뒤덮였고, 때아닌 서리에 갈대숲은 꽁꽁 얼어붙었다.

그리고 이처럼 계절을 잊은 듯한 불가사의한 현상은, 불과 어제오늘의 일이 아니었다.

기온이 내려가고, 혹독한 맹추위가 밤낮을 가리지 않고 기승을 부렸으며, 그에 따라 햇빛을 충분히 받지 못한 초목(椒目)은 과거의 싱그러움을 보여 주지 못했다.

반면 어느 땅에서는 극심한 가뭄이 들기도 했으니, 실로 하늘의 장난이요 귀신의 조화라 볼 수밖에 없었다.

이 모든 것이 불과 일 년 남짓한 짧은 시간 동안 이루어진 변화라는 것을 생각한다면 더더욱.

하지만 사내, 마삼보의 생각은 달랐다.

사박, 사박.

천천히 언덕을 내려오는 그의 발끝을 따라 땅을 뒤덮은 서리가 부서진다. 그에 따라 새겨지는 발자국처럼 그의 상념도 깊어졌다.

‘고작 귀신의 조화 따위가 아니다. 그분의 권능은 천신(天神)과 맞닿아 있어.’

하늘 그 자체이자, 전지전능한 신.

자신의 주인인 천주(天主)를 떠올린 마삼보는 마음 깊은 곳에서 절로 두려움과 존경이 피어오르는 것을 느꼈다.

천하를 위협에 빠트리는 것으로도 모자라 기후를 바꾸고, 죽은 자마저 소생시키는 절대자.

마삼보는 문득 생각했다.

과연 그런 이를 자신과 같은 인간이라 칭할 수 있을지.

그리고 어찌하여 그 믿을 수 없는 권능의 일부를, 당신의 수족이었던 스승조차 버리고 도망쳐 온 자신에게 나누어 주었는지.

‘아니, 나는 스승님과는 다르다. 모든 면에서 그분께 더욱 큰 도움이 될 수 있어.’

마삼보는 마음속으로 되뇌었다.

비록 일평생을 스승으로 모셨던 동천마군은 나약한 최후를 맞이했으나, 자신은 다를 것이라고.

천주가 품은 대계(大計)에 큰 보탬이 되어, 그분의 새로운 수족으로서 이 천하의 일부를 다스리겠노라고.

까악.

문득 상념에서 깨어난 마삼보는 어느덧 자신을 향해 빛나고 있는 수많은 안광(眼光)을 보며 피식 웃었다.

“아무래도 내가 식사를 방해한 모양이로군. 신경 쓰지 말고 마저 들거라.”

하지만 마삼보의 친절한 이야기와는 상관없이, 갈대숲을 뒤덮은 수많은 철새는 이 뜻밖의 불청객을 향해 날 선 울음소리를 토해 냈다.

한껏 핏발 선 눈동자를 번뜩이며.

그리고 그 안에 담겨 있는 것은, 평범한 날짐승에게서 결코 찾아볼 수 없을 정도로 짙은 살기(殺氣)였다.

“이런, 이미 변화가 시작됐군.”

작게 혀를 찬 마삼보는 흥미로운 눈빛으로 철새들을 바라보았다.

피가 흥건하게 묻어 있는 부리와 맹수의 그것처럼 두껍고 예리해진 깃털과 발톱.

그리고 그런 철새들의 아래에는, 이 호화로운 만찬을 장식한 요리들이 외관만큼이나 끔찍한 사취(死臭)를 풍기며 쓰러져 있었다.

“하여간, 그놈의 본능이 문제란 말이지.”

어찌 된 일인지 충분히 알 만했다.

이미 앞선 기후의 변화에 따라 초목이 얼어 죽고 짐승과 벌레들은 자취를 감춘 지 오래.

이처럼 예상치 못한 식량난에 먹이를 찾지 못한 수많은 철새는 청해호를 벗어나 일대를 떠돌았을 것이고, 그중 일부는 그리 멀지 않은 갈대숲에서 마침내 굶주린 배를 채울 수 있었을 것이다.

다름 아닌, 실 끊어진 인형이나 다름없이 쓰러져 있던 괴물들의 피와 살로.

“그렇지 않아도 전력 보충이 필요했는데, 때마침 잘 되었군.”

마삼보는 서서히 변이(變異)되기 시작한 철새들을 바라보며 빙긋 웃었다.

근래 들어 대인이라 불리는 웬 정신 나간 놈 하나가 닥치는 대로 휘하의 날짐승들을 때려잡기 시작해서 감시가 쉽지 않았는데, 이 정도의 머릿수라면 예상치 못했던 큰 성과가 아닐 수 없었다.

까아아악!

물론 그 전에, 저주받은 피와 살을 섭취하여 난폭해진 저 날짐승들을 위한 각인(刻印)이 필요하겠지만.

“자, 지금부터는 내가 너희의 주인이다.”

쩔그럭.

마삼보가 손에 쥐고 있던 요령을 흔든 그 순간.

솨아아악!

거친 날갯짓과 함께 그를 향해 쇄도하던 무수한 숫자의 철새들이 일순간 방향을 틀어 하늘 높이 솟구쳤다.

요령의 움직임을 따라 울려 퍼진, 둔탁하면서도 음산한 방울 소리가 명령하는 대로.

그리고 그에 반응한 것은 비단 날짐승들뿐만이 아니었다.

스륵, 쿠우웅.

굽혀졌던 무릎이, 뻣뻣하게 굳어 있던 허리가, 마지막으로 굳게 감겨 있던 눈이 반개(半開)한다.

“생각보다 많이 살아남았군.”

너른 갈대숲 곳곳에서 거대한 체구를 일으키는 괴물들의 모습을 바라보던 마삼보가 작게 중얼거린 그때. 앞서 사라졌던 흑의인들이 되돌아와 보고했다.

“모두 확인했습니다.”

“어떻더냐?”

마삼보의 물음에, 흑의인 중 하나가 손에 쥔 무언가를 공손히 내밀었다.

얼굴의 일부가 새들에게 쪼아 먹힌 것을 제외한다면 생전의 모습 그대로, 조금의 위화감도 없는 자연스러운 표정으로 굳어 버린 그것은 바로 누군가의 목이었다.

불과 며칠 전까지만 하더라도 마삼보의 수하이자, 그들의 동료였던.

“대부분 이와 같은 상태였습니다.”

“이건.”

수급을 살펴보던 마삼보의 눈이 문득 크게 뜨였다.

그는 술사인 동시에 일신의 무위가 초절정에 다다른 고수.

그러나 수급에 남아 있는 검흔(劍痕)은, 마삼보로서도 등골이 서늘해질 만큼 희미했다.

“……살검(殺劍)이다. 그것도 극의에 달한.”

“그 말씀은.”

“무영(無影)이라 불리는 자가 있다. 한때 내가 몸담았던 동창조차 정확한 정체를 알 수 없을 만큼 천자를 암중에서 호위하던, 대국 황실이 키워 낸 최고의 살수였지.”

하지만 그런 무영조차 이 정도의 검흔을 만들어 내진 못한다.

끈질긴 조사와 추격으로 무영의 손에 고혼이 된 시체 한 구를 손에 넣은 바 있었던 마삼보는 그 사실을 익히 알고 있었다.

그리고 불현듯 기억 속에 남아 있는 한 사람을 떠올렸다.

지금으로부터 몇 달 전, 대연회장을 중심으로 벌어진 혈전 속에서 진태경에게 죽음을 맞이했던 어느 절름발이 노인을.

‘계야부.’

이미 사라졌다 알려진 천하제일의 살문, 살천문(殺天門)의 마지막 후예.

어찌하여 지금 이 순간 그가 떠오른 것일까.

마삼보는 오래지 않아 그 물음에 대한 답을 찾아냈다.

“살성(殺星)…….”

그래, 그의 존재라면 모든 것이 설명된다.

분명 치열한 격전이 벌어졌을 이 광활한 갈대숲에 인간의 시체가 단 한 구조차 보이지 않는 것도.

술사들마저 제거된 마당에 어떻게 이토록 많은 괴물이 두 번째 죽음을 맞이하지 않았는지도.

“속전속결로 끝냈군. 우리의 약점을 정확하게 파고들었어.”

혼잣말처럼 중얼거린 마삼보는 수하의 수급을 저 멀리 내던졌다.

그에게는 천주에게 선물 받은 권능이 있었지만, 어떠한 제한도 없이 모두를 죽음에서 일으킬 수 있는 것은 아니었다.

“돌아간다. 지금쯤 놈들은 청해호를 떠났을 터, 서둘러 돌아가 다음 명령을 이행할 것이다.”

이미 엎질러진 물.

그나마 상당한 숫자의 전력을 수습하고 새로운 수하들까지 얻었으니, 마삼보는 아쉬움을 뒤로한 채 돌아섰다.

아니, 돌아서려고 했다.

“하온데.”

흑의인 중 하나가 머뭇거리며 입을 열기 전까지는.

“한 명. 단 한 명이 빕니다.”

“뭐라?”

“훼손당한 손목 하나를 발견하긴 했으나, 이를 제외하면 어디에서도 시체를 찾을 수 없었습니다.”

“그렇다는 건…….”

“아무래도 놈들에게 생포 당한 듯싶습니다.”

“……!”

마삼보는 자신도 모르게 얼굴을 일그러트렸다.

그토록 조심하라 일렀거늘, 죽은 것도 아니고 생포라니.

하지만 그가 느낀 분노와 동요도 잠깐뿐이었다.

제법 귀중한 수하들을 잃고 생포 당하기까지 했지만, 전체로 보자면 그들은 어디까지나 곁가지에 불과하다.

곁가지 하나에 신경을 기울이는 이가 없듯이, 마삼보가 그들에게 알려 준 정보 또한 많지 않았다.

다만 조금 신경에 거슬리는 것은, 곧바로 이어진 수하의 뒷말이었다.

“그들이 지니고 있던 요령들도 사라졌습니다. 하나도 빠짐없이.”

“……무슨 도둑놈도 아니고, 알뜰하게도 챙겨 갔군.”

눈살을 찌푸린 채, 잠시 생각에 잠겨 있던 마삼보가 고개를 내저었다.

“신경 쓸 필요 없다. 요령을 손에 넣었다 한들 저들이 할 수 있는 것은 아무것도 없으니까.”

어느 촌부가 신병이기(神兵利器)를 얻었다고 하루아침에 초절정 고수로 둔갑할 수 없는 것처럼, 요령이 제 쓰임새를 발휘하기 위해서는 그에 걸맞는 수련을 거듭해야 했다.

“게다가 생포 당한 그놈이 우리를 배반해 보았자, 놈이 부릴 수 있는 숫자는 고작 수백에 불과하다.”

“그럴 리 있겠습니까. 저희는 그를 잘 압니다. 본천에 대한 충성심도 충성심이지만 결코 누군가를 배반한 인물이 못 되는…….”

잡혀간 동료를 비호하는 수하들의 모습에, 마삼보는 자신도 모르게 헛웃음을 터트렸다.

“할 것이다.”

“예?”

“놈은 배반할 것이다. 아니, 반드시 그렇게 만들겠지.”

마삼보는 나직이 덧붙였다.

“내가 아는 그 빌어먹을 개자식이라면, 반드시.”

불현듯 눈앞을 스치는 ‘빌어먹을 개자식’의 얼굴과 함께, 그는 반사적으로 품 안을 더듬었다.

그와 동시에 불과 몇 달 전, 진태경이 자신을 속이기 위해 중요한 밀서랍시고 건넸던 그 쪽지에 적힌 글자를 떠올렸다.

아니, 정확히는 학문에 조예가 깊은 마삼보조차 알아볼 수 없었던 정체불명의 기호를.

- 븅신새끼ㅋ

여전히 뜻을 알아내지 못한 그 이상한 기호를 떠올린 마삼보는 이를 뿌득 갈았다.

‘기다려라. 곧 갚아 주마.’

동쪽을 노려보는 그의 시선은, 청해호를 가로지르고 있을 누군가를 향하는 듯 했다.
```

## Final English reading copy

```markdown
# Chapter 1077

Around noon, a group of men dressed in black appeared atop a low hill.

*Swish.*

*Pat, pat, pat!*

At a casual wave from the man in front, several dozen black-clad men scattered in every direction.

They were here to investigate what had happened—and clean up afterward.

“So we have company already.”

The man murmured to himself as he looked down at the scene spread out below the hill.

More precisely, he looked at the vast reed beds extending for a little over ten li in every direction, and the countless birds packed into every open patch between them.

“They must have been hungry. It can’t have been an easy journey.”

Qinghai Lake, only a few days’ travel from here, was also a haven for migratory birds.

The trip was arduous. They had to beat their wings without rest across a thousand li. Even so, enormous numbers of them came to Qinghai Lake each year for its clean water and abundant food.

Of course, that was all in the past now.

*Whoooosh.*

A wind carrying a biting chill suddenly swept through the reeds. The migratory birds, busy filling their empty stomachs, shivered.

The cold was far too severe to be explained by high elevation alone.

At noon, when the sun should have been at its highest, the sky was already covered in black clouds. Untimely frost had frozen the reed beds solid.

And this sort of inexplicable phenomenon, as though the seasons had forgotten their place, had been going on for more than a day or two.

The temperature had fallen. A fierce, bitter cold held sway day and night, and the plants, deprived of sufficient sunlight, could no longer show the lushness they once had.

Elsewhere, a severe drought had struck. It was nothing short of a prank by the heavens, or some supernatural mischief.

All the more so when one considered that these changes had taken place in little more than a year.

But Ma Sanbao saw things differently.

*Crunch, crunch.*

As he slowly descended the hill, frost broke beneath his feet. His thoughts grew deeper, like the footprints forming behind him.

*This is no mere supernatural mischief. His power borders on that of a heavenly god.*

Heaven itself. An all-knowing, all-powerful god.

As he thought of his master, the Lord of Heaven, Ma Sanbao felt fear and reverence rise from the depths of his heart.

An absolute being who not only threatened the whole world, but could change the climate and even bring the dead back to life.

Ma Sanbao wondered, for a moment, whether someone like that could truly be called human.

And why had he shared a portion of that unbelievable power with Ma Sanbao, who had abandoned and fled from his own master—a man who had served the Lord of Heaven himself?

*No. I’m different from my Master. I can be of far greater use to him in every way.*

Ma Sanbao repeated the words to himself.

Though the Eastern Heaven Demon Lord, whom he had served as Master all his life, had met a weak end, Ma Sanbao would be different.

He would contribute greatly to the Lord of Heaven’s grand design, and rule over a part of this world as his new servant.

*Caw.*

Snapping out of his thoughts, Ma Sanbao gave a quiet laugh when he noticed countless pairs of eyes glinting at him.

“Looks like I’ve interrupted your meal. Don’t mind me. Go on and finish.”

His kind words made no difference. The countless migratory birds covering the reed beds let out sharp cries at the unexpected intruder, their bloodshot eyes flashing.

The killing intent in them was far too intense to belong to ordinary birds.

“Well, the changes have already begun.”

Clicking his tongue, Ma Sanbao looked at the birds with interest.

Their beaks were smeared with blood, and their feathers and claws had grown thick and sharp, like those of predators.

Below them lay the dishes that had decorated this sumptuous feast, just as horrifying in stench as they were to look at.

“Really, that instinct of yours is the problem.”

It wasn’t hard to work out what had happened.

The earlier changes in the climate had frozen the plants to death, and the beasts and insects had vanished long ago.

Unable to find food amid this unexpected famine, countless migratory birds must have left Qinghai Lake and wandered the surrounding area. Some of them had finally found a meal in this nearby reed bed.

The blood and flesh of the monsters lying there like puppets with their strings cut.

“I needed to replenish my forces anyway. This worked out nicely.”

Ma Sanbao smiled as he watched the birds begin to mutate.

Recently, some lunatic called the Great Sir had started beating down his subordinate birds indiscriminately, making them difficult to keep watch with. A flock this large was an unexpected windfall.

*Cawww!*

Of course, before that, he needed to imprint his will on the birds, now savage from eating cursed flesh and blood.

“All right. From now on, I’m your master.”

*Jingle.*

The moment Ma Sanbao shook the ritual bell in his hand—

*Whoooosh!*

The countless migratory birds that had been hurtling toward him with a rush of wings abruptly changed course and shot high into the sky.

They obeyed the command carried by the bell’s dull, eerie chime.

And the birds weren’t the only ones to respond.

*Shrrk. Rumble.*

Bent knees straightened, rigid backs unbent, and, finally, tightly shut eyes opened halfway.

“More of them survived than I expected.”

As Ma Sanbao murmured, watching the monsters rise to their full height throughout the broad reed beds, the black-clad men who had gone off earlier returned to report.

“We’ve checked everything.”

“What did you find?”

At Ma Sanbao’s question, one of the men respectfully held out something in his hand.

Except for part of its face, which had been pecked away by birds, it looked just as it had in life. Its expression was natural, without the slightest trace of disturbance—frozen in place.

It was someone’s head.

Until a few days ago, he had been Ma Sanbao’s subordinate and their comrade.

“Most of them were in this condition.”

“This…”

Ma Sanbao’s eyes widened as he examined the head.

He was a sorcerer, but also a master whose personal martial skill had reached Supreme Peak.

Even so, the sword mark on the head was so faint that it sent a chill down his spine.

“…A killing sword. And one that’s reached the highest level.”

“What does that mean?”

“There was someone called No Shadow. The Great Nation’s imperial household raised him as its finest assassin, a man who guarded the Son of Heaven from the shadows. Even the East Depot I once served couldn’t determine his true identity.”

But even No Shadow couldn’t leave a sword mark this faint.

Ma Sanbao knew that well. After a relentless investigation and pursuit, he had once obtained the corpse of one of No Shadow’s victims.

Then a face from his memory suddenly came to mind.

An old, lame man who had been killed by Jin Taekyung in the bloodbath that had taken place at the Grand Banquet a few months earlier.

*Gye Yabu.*

The last heir of Salcheonmun, the greatest assassin sect in the world, long believed to have vanished.

Why had he come to mind at this moment?

Ma Sanbao soon found the answer.

“The Slaughter Saint…”

Yes. His existence explained everything.

Why there wasn’t a single human corpse in these vast reed beds, where a fierce battle must have taken place.

And how so many monsters had avoided a second death, even after the sorcerers had been eliminated.

“He finished it quickly. He went straight for our weakness.”

Ma Sanbao spoke under his breath, then flung his subordinate’s head far away.

The power bestowed on him by the Lord of Heaven allowed him to raise the dead, but not without limit.

“We’re leaving. By now, they must have left Qinghai Lake. We’ll hurry back and carry out the next order.”

The damage was done.

They had at least recovered a considerable number of their forces and gained new subordinates. Setting aside his regret, Ma Sanbao turned to leave.

Or rather, he was about to turn away.

“However…”

Until one of the black-clad men hesitantly spoke up.

“One man is missing. Just one.”

“What?”

“We found a severed wrist, but no body anywhere else.”

“Then…”

“It seems he was captured by them.”

“……!”

Ma Sanbao’s face twisted before he could stop himself.

After all his warnings to be careful, the man hadn’t even died—he’d been captured.

But his anger and agitation lasted only a moment.

They had lost some valuable subordinates and one had been captured, but as a whole, those men were no more than minor branches.

Just as no one bothered with a minor branch, Ma Sanbao hadn’t told them much.

What bothered him a little was what his subordinate said next.

“The ritual bells they were carrying are gone, too. Every last one.”

“…What are they, thieves? They even made sure to take everything.”

Frowning, Ma Sanbao thought for a moment, then shook his head.

“No need to worry. Even if they get their hands on the bells, they won’t be able to do anything with them.”

Just as some country bumpkin couldn’t become a Supreme Peak master overnight by getting hold of a divine weapon, the bells required extensive training before they could be put to proper use.

“Besides, even if that man we lost betrays us, the most he can command is a few hundred.”

“That’s impossible. We know him. He’s loyal to the Heavenly Court, yes, but he’s also not the sort of person who would ever betray anyone…”

At the sight of his subordinates defending their captured comrade, Ma Sanbao let out a quiet laugh.

“He will.”

“Pardon?”

“He will betray us. No—Jin Taekyung will make sure he does.”

Ma Sanbao added in a low voice:

“If that son of a bitch I know is involved, he will.”

As the face of that *son of a bitch* flashed before his eyes, he reflexively reached inside his robe.

At the same time, he remembered the characters written on the note Jin Taekyung had handed him a few months earlier, claiming it was an important secret letter, all to deceive him.

Or, more accurately, the mysterious symbols that even Ma Sanbao, a man well versed in scholarship, couldn’t decipher.

—You fucking dumbass lol

Remembering the strange symbols whose meaning he still hadn’t figured out, Ma Sanbao ground his teeth.

*Just wait. I’ll pay you back soon.*

His gaze, fixed on the east, seemed to be directed at someone crossing Qinghai Lake.
```
