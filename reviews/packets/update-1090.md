<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1090.txt",
      "sha256": "8a596de98f050d4c1c0d7b62438b0dc9bc32bd70961f1a90c869564e2862d9bb",
      "bytes": 13521
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9ae2354cb9e018238532b39505fd2157d34b72ed3beb42ca3d7ef4fd13b85c11",
      "bytes": 1845
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bee69e076364377f31e7856d6f9b353d3362d24e22138f2ec1d79723928adc10",
      "bytes": 243843
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "c65f4443c6f2f8bbbd3313e9af5c5073743b627dcb6bbed09bd2faddebe443e0",
      "bytes": 916
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "29ef01f897d10d542b4036cd53ff9799714ba57939183c3ea0df00272e23f550",
      "bytes": 544
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1e3bd31233f669ff652855259c03fe676e029830504dc376b348de53b72fcf65",
      "bytes": 563
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "e3e1d7c4be375f653298d939e09fae7e4732743faf557df7aa261df60d1a9ef5",
      "bytes": 554
    },
    {
      "path": "characters/Hak Su.md",
      "sha256": "996cbaf6733f6555585b45def7af044b6e3babb4a2b4024274f767a6905dcffe",
      "bytes": 615
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "2d27c5e6a17fd5c93db9413d4f9afb31ecc3970220db6c984d538250311b00c5",
      "bytes": 1001
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8d6abf28b785baebb6c5b9d8b2348543da8a64df69acc0459ebca766c49b05d8",
      "bytes": 1502
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "07fadd17a2bbb833beb1b4601b7f657bf9991b91ec7f7971cea4b29cb6f83c22",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 11036
}
-->

# Durable State Update — Chapter 1090

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
1 and safe_through 1090. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1090. Profile updates may replace only one
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
  "chapter": 1090,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1090,
    "continuity_sources": [1090],
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
    "The Yangtze River Channel League and Green Forest Alliance are advancing west with Dark Heaven forces; their combined force is estimated at roughly 30,000, including 10,000 Dark Heaven faithful.",
    "The Blood Lord’s forces are marching on Xining to take Qinghai; securing Jin Taekyung is a further objective if possible.",
    "The Blood Lord and Grand Mage have attacked the Beggars’ Sect gathering at Qinghai Lake; the Grand Mage froze the lake, and the Blood Lord intends for a survivor to carry his threat.",
    "Potala Palace has allied with Dark Heaven, and Sichuan support can no longer be counted on.",
    "The Great Nation’s vessels guarding the Yangtze tributaries have been destroyed; the enemy controls the river routes for now.",
    "Jin Taekyung has chosen to remain in Xining and defend its civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to put his remaining strength to use.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has its intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang."
  ],
  "continuity_sources": [
    1088,
    1089
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who survives the Blood Lord’s attack at Qinghai Lake?"
  ],
  "safe_through": 1089,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 소림     | **Shaolin**                      |
| 곤륜파    | **Kunlun Sect**                  |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 방장      | **Abbot**                                                       |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 학수 | **Hak Su** | Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 블리자드 | **Blizzard** | Johnson's large-scale ice spell. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 황하 | **Yellow River** | River along which civilization began. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 리자드 | **Charmeleon** | Game-monster comparison. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 태산 | 청허자 | younger martial artist to senior sect leader | you | clipped and childlike | Asks whether Cheongheoja brought meat. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1089
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1089
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1087
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hak Su.md

# Hak Su (학수)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Hak Su is Cheongheoja’s Senior Disciple and a senior brother to Hak Woo in the Kunlun Sect.
- **Personality:** Gracious and hopeful, he responds to Taekyung’s mistakes with patience and warmth.
- **Voice:** He speaks in courteous, formal phrases and tempers earnest reassurance with hearty, lightly humorous remarks.
- **Relationships:** Cheongheoja is his Master, and Hak Woo is his youngest Junior Brother; he treats Jin Taekyung warmly as a Fellow Daoist.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1087
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1088
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1085
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1090화




청해성은 엄연히 변방(邊防)에 속하는 지역이다.

천하에서 손에 꼽힐 정도의 광활한 면적과 아름다운 경관을 지녔지만, 물자의 풍부함과 가호(家戶)의 숫자는 중원에 비해 턱없이 부족한 것이 현실.

그렇기에 누천년에 걸쳐 천하의 중심으로 자리매김하며 다방면의 문물(文物)을 발전시킨 중원과 비교될 때마다, 청해성의 사람들은 농담 삼아 이렇게 자평하고는 했다.

― 청해와 중원의 공통점은 오직 세 가지뿐이다. 같은 해를 보고, 같은 물(황하黃河)로 이어져 있고, 마지막으로 거지가 있다.

거지는 그만큼 어느 곳에서나 흔해 빠진 존재들이었다.

시끌벅적한 대로변이나 어둡고 지저분한 뒷골목, 혹은 개울가 근처의 움막촌 따위에서 살아가는 그들은 중원이든 변방이든 가리지 않았다.

그 머릿수가 얼마나 많은지, 천하의 모든 거지를 개방이 흡수한다면 능히 일국(一國)을 세울 수도 있다는 우스갯소리가 나올 정도니까.

하지만 서서히 동이 틀 무렵, 어스름한 새벽안개를 뚫고 주위를 탐색하던 정찰대에 의해 발견된 어느 백발의 거지는 지금껏 누구도 본 적 없는 행색을 하고 있었다.

아니, 솜털이 곤두설 만큼 낯설었다.

터벅, 터벅.

당장이라도 쓰러질 듯이 비틀거리는 발걸음. 혼백이 빠져나간 것처럼 공허한 눈동자.

그리고…….

“전해라. 반드시. 누가 살아남든.”

파랗게 질린 입술 사이로 흘러나오는 공포 어린 목소리.

아마도 그래서였을 것이다.

찰나의 순간, 석상처럼 굳어 있던 정찰대가 뒤늦게 거지의 허리춤에 묶인 두 개의 매듭을 발견한 것은.

“……개방(丐幇).”

틀림없다. 눈앞의 저 거지는 개방에 몸담은 무림인이었다.

그것도 분타주 바로 아랫급의 이결제자.

그리고 정찰대가 출발한 서녕으로부터 서쪽에서 백 리나 떨어진 이곳에서 개방도가 모습을 드러낼 이유는, 그들이 알기로 단 한 가지 경우밖에 없었다.

“노인장, 도대체 청해호에서 무슨 일이 있었……!”

그 순간. 다급히 말에서 내려 다가가던 정찰대원이 헛숨을 삼키며 눈을 부릅떴다.

그제야 보았기 때문이다.

희끄무레한 안개 속에서는 그저 노화로 인한 백발로 보였던 개방도의 머리카락이, 사실은 빙하에 갇혀 있던 사람처럼 얼어 붙어 있었음을.

새하얗게 물든 그의 얼굴은 노인이 아닌 청년에 불과했음을.

“이, 이게 무슨.”

한 줄기의 벼락이 정수리를 관통한다면 이런 기분일까.

스무 명의 정찰대는 찌르르 울리는 등골을 느끼며 침묵할 수밖에 없었다.

바로 다음 순간 들려온 개방도의 한 마디가, 그가 혼신을 다한 마지막 불꽃이라는 사실조차 알지 못한 채.

“전해라. 내가 갈 것이다. 가서, 서녕의 모든 것을 죽이고 불태울 것이다.”

“……!”

“……!”

일순간, 정찰대는 경악에 찬 눈빛으로 몸을 떨었다.

그 말에 담긴 무시무시한 살의(殺意) 때문에?

아니다. 틀렸다.

개방도.

그는 웃고 있었다. 동시에 울고 있었다.

마치 이 말을 전하라고 명령한 누군가를 따라 하듯이.

그와 더불어 이미 불귀의 객이 되어 버린 동료들의 죽음을 슬퍼하듯이.

그리고 온 사방을 짓누르는 그 숨 막히는 침묵 속, 힘겨운 여정을 끝마친 개방도의 몸뚱어리가 흐릿한 목소리와 함께 기울어졌다.

“기다려라. 내가, 혈주(血主)가 돌아 왔…….”

쿵.

썩은 통나무처럼 허물어지는 육신.

아니, 마침내 숨이 끊어진 개방도의 시신을 멍하니 바라보던 정찰대원들은 불현듯 고개를 들어 서쪽을 바라보았다.

어째서일까.

이미 마음속에서 싹 튼 두려움 때문일까, 아니면 곧 마주하게 될 현실을 깨달은 본능적인 직감일까.

저 자욱한 안개 너머에서 끔찍한 괴물들이 내지르는 괴성과 악취가 풍겨오는 듯했다.

“……시신을 수습해라.”

간신히 쥐어 짜낸 상관의 목소리에서조차 숨길 수 없는 공포가 묻어나왔다.

“서녕으로 돌아간다. 지금 당장.”



* * *



이제는 목 없는 시체가 되어 버린 청해성주의 집무실은 언제 보아도 이루 말할 데 없이 넓고 호화로웠다.

그가 죽을 수밖에 없었던 이유를 증명하기라도 하는 것처럼.

값비싼 흑단(黑檀)을 깎아 만든 탁자는 수십여 명이 동시에 자리할 만큼 컸고, 사천에서도 특등품 취급받는 촉금(蜀錦) 비단을 햇빛을 가리기 위한 용도로 썼을 정도였다.

하지만 청해성주는 까맣게 몰랐을 것이다.

그가 죽기 직전까지도 아까워했을 그 요란한 사치품들이, 지금 이 순간 어느 초라한 거지를 위해 쓰이고 있다는 것을.

“이결제자 주제에 이런 호사라니. 거지의 본분을 잊었군.”

궁기방은 애써 담담한 목소리로 뇌까렸다.

촉금 비단에 감싸 인 채, 흑단 탁자 위에 올려진 시신을 바라보는 녀석의 눈빛은 축축하게 젖어 있었다.

“그리 오래 알았던 건 아니지만 썩 괜찮은 녀석이었어. 아직 어린 나이인데도 이결을 허락받을 만큼의 재능도 있었고.”

나는 대답하지 않았다.

아니, 나뿐만 아니라 집무실 안에 모여있던 수뇌부 중 그 누구도.

“상황이 괜찮아지면 나중에라도 중원에 꼭 한번 가 보고 싶다고 부탁하길래, 철없는 소리 하지 말라고 역정을 냈었는데……. 제기랄.”

먹먹한 목소리로 욕설을 내뱉은 궁기방이 쓴웃음을 지었다.

“어쩌겠어. 단지 운이 없었던 거지. 이 녀석도, 그들도.”

삼십여 명에 가까운 개방도가 청해호 건너편에 남았지만, 서녕으로 돌아올 수 있었던 것은 저 이름 모를 젊은 개방도 하나뿐이다.

그리고 그마저도 도중에 숨이 끊어졌다.

가장 먼저 그를 발견한 정찰대들이 제대로 말을 잇지 못할 만큼 처참한 모습으로.

하지만 유언(遺言)이나 다름없게 된 그의 마지막 한 마디에는, 이 빌어먹게 호화로운 집무실 전체보다 값진 정보가 담겨 있었다.

“혈주. 혈주라면…….”

불현듯 입을 연 곤륜파의 장문인, 청허자(淸虛子)의 뇌까림에 내가 고개를 끄덕였다.

“장문인께서 알고 계시는 그 이름이 맞습니다. 소림혈사(小林血史)를 일으켰던.”

“……!”

“……!”

보이지 않는 파동이 주위로 번진다.

이미 전부터 혈주의 존재를 알고 있던 이들은 말없이 침음성만 흘렸고, 자세한 정황을 몰랐던 이들은 놀라서 눈을 부릅떴다.

그리고 화왕 적천강은, 그 어디에도 속하지 않은 극소수의 인물 중 하나였다.

“그리웠던 이름이군.”

나직한 음성과 별다른 변화가 보이지 않는 표정.

그러나 나는 누구보다 잘 알고 있다.

지금 이 순간 적천강이 얼마나 분노하고 있는지.

동시에 그 분노를 억누르기 위해 얼마나 안간힘을 쓰고 있는지.

“이제야 그 땡중에게 면이 설 수 있겠어.”

무림의 태산북두라 불리는 소림사의 방장이자, 법왕(法王)이라는 별호를 얻을 만큼 신망이 두텁던 굉도였지만 적천강은 그를 늘 땡중이라고 불렀다.

일생을 통틀어 몇 안 되는. 아니, 어쩌면 하나밖에 없었을지도 모르는 친우였으니까.

그렇기에 지금껏 단 한 순간도 잊지 않았을 것이다.

그런 굉도를 죽인 장본인, 혈주에 대한 원한을.

하지만 지금은 그의 원한보다 중요한 문제가 남아 있었다.

“결국 놈들로서도 총력전을 벌일 심산이군요.”

냉정하게 느껴질 만큼 침착한 목소리로 입을 연 젊은 도사, 청허자의 둘째 제자인 학의(鶴義)가 말을 이었다.

“이미 사로잡은 개방도를 구태여 풀어 주었다는 건, 그만큼 승리를 확신한다는 뜻일 테고요.”

“두, 둘째야.”

그와는 달리 옆자리에서 눈치를 보던 사형, 학수(學洙)가 만류하려 했지만 학의는 개의치 않았다.

청해성주에 관련된 지난번 회의 이후 어느 정도의 발언권을 얻게 된 그였다.

“하지만 가장 중요한 정보를 전달받지 못한 것이 아쉽습니다. 적들의 숫자만이라도 알 수 있었다면 훨씬 더 나은 대책을…….”

바로 그 순간이었다.

“뭐?”

그때까지도 말없이 시신만을 바라보던 궁기방의 미간이 와락 일그러진 것은.

“지금, 뭐라고 했소?”

분노를 내비치는 궁기방을 향해, 학의가 담담한 어투로 대꾸했다.

“단지 아쉬움에 제 생각을 말씀드린 것뿐입니다.”

“그래서? 모두를 위해 위험을 무릅쓰다 죽은 사람에게 책임을 묻겠다는 건가? 왜 더 노력하지 않았느냐고?”

“그건…….”

감정이 격해진 궁기방의 모습에 학의가 뭐라 답하려던 그때, 조용히 사태를 지켜보던 한 사람이 불쑥 입을 열었다.

“둘째야.”

다름 아닌 스승, 청허자다.

그의 나직한 부름에 멈칫한 학의가 이내 궁기방을 향해 고개를 숙였다.

“제가 미숙한 탓에 그만 실언을 했습니다. 더 이상의 오해는 없었으면 합니다.”

별다른 감정이 느껴지지 않는 그 딱딱한 사죄에 궁기방의 표정이 더욱 험악해진 그때, 청허자가 재차 입을 열었다.

“빈도가 제자를 잘못 키웠네. 진심을 다해 사과하지.”

다른 사람도 아니고 한참 대선배, 그것도 곤륜파의 장문인이 직접 건네는 사과다.

뿐인가.

지금 이 자리에는 그보다 높은 이들도 있다.

궁기방이 아무리 개방의 후개라도 해도 더 이상의 분란은 엄청난 무례로 여겨질 수 있는 상황.

입술을 질끈 깨무는 녀석과 학의를 물끄러미 응시하던 나는 때맞춰 전음(傳音)을 흘려보냈다.

― 넘어가자, 우선은.

“……!”

― 아니면 내가 지금 당장 저 사회 부적응자 새끼를 반쯤 죽여 줄 수도 있고. 뭐가 더 나은지 말만 해.

그제야 쓴웃음을 흘린 궁기방이 고개를 절레절레 저었다.

“알겠습니다. 저도 괜히 분위기를 흐려서 죄송합니다.”

그렇게 잠깐의 소란이 일단락되었지만, 학의는 조금도 움츠러든 기색 없이 입을 열었다.

“다행히 적들이 서녕에 도달하기까지는 아직 시간이 남아 있습니다. 그 안에 충분한 대비책을 마련해야겠지요.”

어째서인지 묘한 어투다.

깊게 가라앉은 눈빛으로 줄곧 그를 주시하던 나도 이제는 묻지 않을 수 없었다.

“뭡니까. 그 대비책이?”

“진 대협께서도 이미 알고 계시지 않습니까.”

물론 안다. 너무 잘 알아서 문제다.

그래서 더욱 놀라웠다.

눈앞의 학의가, 곤륜파의 도맥(道脈)을 이은 그가 그런 생각을 했다는 것이.

“지금이라도 늦지 않았습니다. 후방이 완전히 가로막히기 전에 당장 이곳을 떠나야 합니다.”

“사제, 지금 이게 무슨!”

그러나 참다못한 학수가 자리에서 벌떡 일어났음에도, 스승인 청허자가 침음성을 흘렸음에도 그는 멈추지 않았다.

“이건 전투가 아니라 전쟁입니다. 비록 이렇게 말하는 것이 옳지 않다는 것은 알지만……. 소탐대실(小貪大失)의 우를 범할 수는 없지 않겠습니까?”

“……!”

“……!”

내부의 공기가 삽시간에 얼어붙은 그 순간, 내가 입을 열었다.

“그, 우선 개소리가 너무 많아서 일일이 반박하기도 어렵긴 한데. 우선은 이것부터 짚고 넘어갑시다.”

얼굴이 딱딱하게 굳은 학의를 향해 나직이 덧붙였다.

“혈주, 그 새끼가 그렇게 만만한 놈으로 보입니까?”

나는 곧장 손으로 탁자를 가리켰다.

아니, 정확히는 군데군데 서리 낀 몸으로 누워 있는 개방도의 시신을.

처음 본 순간부터 알았다.

죽은 육신 군데군데에 남아 있는 저 끔찍한 냉기. 오직 이들 중 나만이 발견할 수 있는 익숙한 흔적을 느꼈다.

‘블리자드(Blizzard).’

가공할 위력을 지닌 최고위 빙결(氷結) 마법.

이는 두 가지를 의미했다.

첫째, 이미 예상했던 대로 대술사가 저들과 함께하고 있다는 것.

그리고 둘째.

“놈들은 이미 청해호를 넘었어.”

선박 따위는 필요도 없었을 것이다. 빙결 마법으로 단단히 얼어붙은 호수를 건너면 그만이었으니까.

애당초 개방도를 풀어 준 건, 어디까지나 혈주의 유희에 지나지 않았다.

“그러니까.”

뜻 모를 표정을 짓고 있는 학의를 향해, 나는 나직이 덧붙였다.

“도망치려면 지금이라도 떠나. 이 겁쟁이 새끼야.”

그리고 그 순간.

드득. 드드드득.

어디선가 들이닥친 진동에, 집무실이 떨리기 시작했다.

아니, 서녕 전체가.
```

## Final English reading copy

```markdown
# Chapter 1090

Qinghai was unquestionably a border region.

It had one of the largest areas in the world and some of the most beautiful scenery, but in truth, its supplies were scarce and its population was nowhere near that of the Central Plains.

So whenever people compared Qinghai to the Central Plains—which had stood at the center of the world for thousands of years and developed a wide range of culture and civilization—Qinghai’s people liked to joke:

“Qinghai and the Central Plains have only three things in common: they see the same sun, they’re connected by the same river—the Yellow River—and, last of all, they have beggars.”

Beggars were common everywhere, after all.

They lived along busy main roads, in dark, filthy alleys, or in shantytowns near streams. They could be found in the Central Plains or the border regions without distinction.

There were so many of them, in fact, that people joked the Beggars’ Sect could found a nation of its own if it took in every beggar in the world.

But around daybreak, as a scouting party searched the area through the faint morning mist, they came across a white-haired beggar whose appearance was unlike anything anyone had ever seen.

No—he was so strange that their hair stood on end.

Step. Step.

His staggered footsteps made him look ready to collapse at any moment. His eyes were empty, as if his soul had left his body.

And then…

“Deliver this message. No matter who survives.”

A voice filled with terror slipped between his blue lips.

Perhaps that was why the scouts, frozen like statues for an instant, noticed the two knots tied at the beggar’s waist only too late.

“……The Beggars’ Sect.”

There was no mistaking it. The beggar before them was a martial artist of the Beggars’ Sect.

And a two-knot disciple, just one rank below a Branch Master.

As far as they knew, there was only one reason a Beggars’ Sect disciple would appear here, a hundred li west of Xining, where the scouts had set out from.

“Old man, what on earth happened at Qinghai Lake—”

At that moment, one scout hurriedly dismounted and rushed toward him. Then he sucked in a breath and stared.

Only then did he see.

In the faint mist, the Beggars’ Sect disciple’s hair had looked white from age. In truth, it was frozen stiff, like someone trapped in a glacier.

And his face, pale as snow, belonged not to an old man but to a young one.

“W-what is this…”

Was this what it felt like to have a bolt of lightning strike through the crown of your head?

The twenty scouts could only fall silent, a tingling sensation running down their spines.

They didn’t even realize that the Beggars’ Sect disciple’s next words were the last spark of his life, delivered with every ounce of strength he had left.

“Deliver this message. I’m coming. I’ll go there and kill and burn everything in Xining.”

“……!”

“……!”

For an instant, the scouts trembled, their eyes wide with shock.

Was it the terrifying killing intent behind those words?

No. They had it wrong.

The Beggars’ Sect disciple was smiling. And crying at the same time.

As if imitating whoever had ordered him to deliver that message.

As if grieving the deaths of the comrades who had already become the dead.

Then, in the suffocating silence pressing down around them, the Beggars’ Sect disciple’s body tilted with a faint murmur, his difficult journey finally at an end.

“Just wait. I, the Blood Lord, have returned—”

Thud.

His body crumpled like a rotten log.

The scouts stared blankly at the body of the Beggars’ Sect disciple, his breath finally gone. Then, all at once, they lifted their heads and looked west.

Why?

Was it the fear that had already taken root in their hearts, or the instinctive sense of those who had realized what they were about to face?

Beyond the thick mist, they could almost hear the shrieks and smell the stench of hideous monsters.

“……Take care of the body.”

Even the commander’s voice, strained out with difficulty, couldn’t hide his fear.

“We’re going back to Xining. Right now.”

* * *

The office of the Qinghai City Lord, now a headless corpse, was as impossibly spacious and luxurious as ever.

As if to prove why he had been doomed to die.

The table, carved from expensive ebony, was large enough for dozens of people to sit around at once. He had even used Shu brocade—considered the finest quality in Sichuan—to keep the sunlight out.

But the Qinghai Governor could never have known that those gaudy luxuries he’d been reluctant to part with until the moment of his death were now being used for a shabby beggar.

“Living in this kind of luxury when you’re only a two-knot disciple. He forgot what it means to be a beggar.”

Gung Gibang muttered, doing his best to sound calm.

The corpse lay atop the ebony table, wrapped in Shu brocade. Gung Gibang stared at it with eyes glistening with tears.

“I didn’t know him for that long, but he was a decent kid. He was still young, and already talented enough to be granted the second knot.”

I didn’t answer.

Neither did anyone else among the leaders gathered in the office.

“He asked me if he could visit the Central Plains someday, once things got better. I snapped at him and told him not to say such childish things.……Damn it.”

Gung Gibang swore in a hollow voice, then managed a bitter smile.

“What can you do? He and the others were just unlucky.”

Nearly thirty Beggars’ Sect disciples had been left on the other side of Qinghai Lake. Only one young, nameless disciple had made it back to Xining.

And even he had died along the way.

He’d been in such a wretched state that the scouts who found him first could barely get their words out.

But his final words, which might as well have been a will, contained information more valuable than this entire goddamn lavish office.

“Blood Lord. If it’s the Blood Lord…”

The Sect Leader of the Kunlun Sect, Cheongheoja, suddenly spoke. I nodded.

“It’s the same name you know, Sect Leader. The one who caused the Shaolin Bloodshed.”

“……!”

“……!”

An invisible ripple spread through the room.

Those who had already known the Blood Lord’s name only murmured in silence. Those who knew nothing of the details stared in shock.

And the Fire King, Jeok Cheongang, was among a rare few who belonged to neither group.

“It’s been a long time since I heard that name.”

His voice was quiet, and his expression barely changed.

But I knew better than anyone.

How furious Jeok Cheongang was right now.

And how hard he was fighting to hold that fury back.

“Now I can hold my head up in front of that damned monk.”

Hong Dao was the Abbot of Shaolin Temple, hailed as a pillar of the Murim and respected enough to earn the title of Dharma King. Jeok Cheongang had always called him “that damned monk.”

He was one of the very few friends Jeok Cheongang had ever had. Maybe the only one.

That was why he could never have forgotten, not for a single moment.

His grudge against the man who had killed Hong Dao: the Blood Lord.

But there was a more pressing matter than his grudge.

“So they’re planning to throw everything they have into this after all.”

A young Daoist spoke in a voice so calm it almost sounded cold. Hak Eui, Cheongheoja’s second Disciple, continued,

“They went to the trouble of releasing a Beggars’ Sect disciple they’d already captured. That must mean they’re certain of their victory.”

“S-second Junior Brother.”

Hak Su, his Senior Brother, had been watching the room uneasily and tried to stop him. Hak Eui paid him no mind.

He’d gained a measure of influence after the last meeting about the Qinghai Governor.

“But it’s unfortunate that we weren’t given the most important information. If we’d known even the enemy’s numbers, we could have come up with a much better plan—”

That was when Gung Gibang’s brow furrowed.

He’d been staring at the corpse in silence until then.

“What?”

He turned on Hak Eui, his anger plain.

“What did you just say?”

Hak Eui replied evenly to Gung Gibang’s glare.

“I was only expressing my thoughts. I regret that we didn’t receive more information.”

“So what? Are you blaming the man who risked his life for everyone and died? Asking why he didn’t try harder?”

“That’s…”

Hak Eui was about to respond to Gung Gibang, whose emotions were running high, when someone who had been watching quietly suddenly spoke up.

“Second Disciple.”

It was none other than his Master, Cheongheoja.

Hak Eui paused at the quiet call, then bowed his head to Gung Gibang.

“I spoke carelessly because I was inexperienced. I hope there won’t be any further misunderstanding.”

His stiff apology showed little feeling. Gung Gibang’s expression grew even more hostile, but Cheongheoja spoke again.

“I failed to raise my Disciple properly. I offer my sincere apology.”

It was no small thing for someone else to apologize on his behalf—especially a much more senior figure, and the Sect Leader of the Kunlun Sect.

And there were others present who outranked him, too.

No matter that Gung Gibang was the Beggars’ Sect Successor Beggar; taking the argument any further here could be considered a grave act of disrespect.

I watched Gung Gibang bite his lip, then glanced at Hak Eui. At just the right moment, I sent Gung Gibang a Sound Transmission.

*—Let it go. For now.*

“……!”

*—Or I can beat that socially maladjusted bastard half to death right now. Just say which you’d prefer.*

At last, Gung Gibang gave a bitter smile and shook his head.

“Understood. I’m sorry for disrupting the mood, too.”

That brought the brief commotion to an end. Hak Eui spoke again, without the slightest sign of having been cowed.

“Fortunately, we still have time before the enemy reaches Xining. We should come up with adequate defenses before then.”

There was something odd about his tone.

I’d been watching him all along with a somber gaze. Now I couldn’t help asking,

“What defenses?”

“You already know, Great Hero Jin.”

Of course I did. I knew all too well.

That was why it surprised me even more.

That Hak Eui, heir to the Kunlun Sect’s Daoist lineage, had come up with that idea.

“It’s not too late to leave, even now. We should abandon this place before our rear is completely cut off.”

“Junior Brother, what are you saying?”

But even when Hak Su finally sprang to his feet, unable to hold back any longer, and his Master, Cheongheoja, murmured in dismay, Hak Eui didn’t stop.

“This isn’t a battle. It’s a war. I know it’s wrong to say this, but… we can’t make the mistake of grasping at something small and losing everything.”

“……!”

“……!”

The air inside the room froze in an instant. Then I spoke.

“First off, there’s so much bullshit here that it’s hard to know where to start. But let’s get one thing straight.”

I added quietly, looking at Hak Eui, whose face had gone rigid.

“Does the Blood Lord look like a pushover to you?”

I pointed straight at the table.

More precisely, at the corpse of the Beggars’ Sect disciple, lying there with frost on patches of his body.

I’d known from the moment I first saw him.

That terrible cold lingering in places on his dead body. I recognized the familiar traces, the kind only I could notice.

*Blizzard.*

A top-tier ice spell with devastating power.

It meant two things.

First, just as I’d expected, the Grand Mage was with them.

And second—

“They’ve already crossed Qinghai Lake.”

They wouldn’t have needed any boats. They could just cross the lake, frozen solid by magic.

In the first place, the Blood Lord had released the Beggars’ Sect disciple only for his own amusement.

“So.”

I added quietly, looking at Hak Eui, who was wearing an inscrutable expression.

“If you want to run, go now. You cowardly bastard.”

And at that moment—

Grnk. Grnnnk.

A rumble came from somewhere, and the office began to shake.

No—the whole of Xining.
```
