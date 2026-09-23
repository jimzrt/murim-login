<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0862.txt",
      "sha256": "9102dc57f1f613018b162a38993f65e691bae66c45457ff6542272cb48d49fad",
      "bytes": 14518
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5822067acd17094d78cd36b58190c3973294ed8362fbf420a1aadd9f725536ae",
      "bytes": 1126
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3552b1247d3798af00bad212f7d26401033d6b11d5c919211e41228f01decd15",
      "bytes": 229142
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "cb771920ff9836f9789512b5b326f2829fbcfa39b68f4f912459e342981f808a",
      "bytes": 797
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ad01fd92b306f205a2e1411df7d754d5f5976c2c9649d226a568b077e4bf5bca",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "2dadb959b00fd5b9fdfcadf8548cbd5cc14ee3601f277735a445ca13fa5473b8",
      "bytes": 634
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bd5eb491c8c81ee252aa6807e96a9a20b61dc64cadc6a294272c4fcc795a886c",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f13fccba74b9572d199c5f5911bf6f475c9fb9ebc6fb765cc8c5eddd725215ff",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3c11f4e9834d4856c5a8b625b448ba4efc294983217498c856958c2a85252970",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "981dbbc3212facab1f9230121860ea4ad1875b3b3e106fe94d2084eb92c30f73",
      "bytes": 883
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b840487442daf61bf05a414cdd77c57af7a509e056f4f451ca28ac839eb396b6",
      "bytes": 254590
    }
  ],
  "estimated_tokens": 11915
}
-->

# Durable State Update — Chapter 862

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
1 and safe_through 862. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 862. Profile updates may replace only one
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
  "chapter": 862,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 862,
    "continuity_sources": [862],
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
    "Prince Shangshan and his party have reached the imperial palace; the Emperor’s intentions toward the prince remain uncertain.",
    "Hong Jin became a eunuch to escape poverty and save his family; the late Emperor recognized his abilities and told him they could be put to use.",
    "Hong Jin has asked Taekyung whether he knows of the East Depot; his connection to it is unexplained.",
    "Taekyung’s other helpers have not yet appeared, and Hong Jin wants to know where they are.",
    "The Emperor is regarded as capable but ruthless and rose to the throne after the Crown Prince was killed in a purge."
  ],
  "continuity_sources": [
    861
  ],
  "open_questions": [
    "What does the Emperor intend for Prince Shangshan?",
    "What is Hong Jin’s connection to the East Depot?",
    "Where are Taekyung’s other helpers, and when will they reveal themselves?"
  ],
  "safe_through": 861,
  "temporary_decisions": [
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 저승사자 | **Grim Reaper** | Mungyeong's threatening self-description during the banter. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 십상남자 | **Tenfold Man** | A joking title Zhu Bao grants Hyuk Mujin, who inscribes it on a bronze token. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |

## Listed compact profiles

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 861
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide charged with protecting Prince Shangshan, whose abilities drew the late Emperor’s attention.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung as the person best able to keep the prince safe.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 861
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 861
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 859
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 859
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 861
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 861
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, compassionate, and eager to emulate Jin Taekyung; he takes responsibility for his loyal subjects’ hardship, though his trust in his elder brother shows his youth.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃862화



동창(東廠).

무협 소설 좀 봤다 하는 사람이면 모를 수 없는 이름이다.

구파일방과 오대세가가 클리셰처럼 등장한다면, 황실에는 금의위와 더불어 쌍두마차를 이루는 동창이 있었으니까.

그런데 홍진이 바로 그 동창의 일원이었다니.

나도 모르게 멍하니 입이 벌어졌다.

“동창이요? 제가 아는 그 동창?”

“천하에 동창은 하나뿐이에요, 진 공자.”

“아니, 그게 진짜로 있었습니까?”

“……그럼 가짜 동창도 있나요?”

“아. 제 말은 그 뜻이 아니라.”

동창이 진짜 존재하는 줄은 몰랐지.

애초에 금의위가 실존한다는 사실을 안 것도 그리 오래되지 않았다.

무림에서 쉴 새 없이 벌어지는 사건 사고만으로도 정신이 없었는데, 갑자기 이런 식으로 황실과 엮이리라고 누가 생각이나 했을까.

‘그나저나, 홍진이 바로 그 동창 출신이라면 지금까지 보여 준 모습들이 어느 정도 설명이 되긴 하지.’

나는 새삼 놀라움을 느끼며 홍진을 바라보았다.

자세한 사정은 몰라도 동창의 위세 역시 금의위에 비해 부족함이 없을 터.

처음에는 그저 소싯적에 침 좀 뱉었던 고자인 줄 알았는데, 이야기를 듣고 나니 황궁 복도에서 가래침을 뱉었을 홍진의 과거 모습이 눈앞을 스치는 듯했다.

혁무진 역시 나와 비슷한 생각을 했는지, 곁눈질로 홍진을 힐끗거리던 녀석이 잔뜩 숨죽인 목소리로 속삭였다.

“조장님. 이거 보통 고자가 아닌데요.”

“……입 좀 다물어, 제발.”

“괜찮습니다. 안 들려요.”

“미안한데, 잘 들려요.”

불쑥 들려온 홍진의 목소리에, 내가 잽싸게 대답했다.

“저는 아무 말도 안 했습니다. 저 새끼가 그랬어요.”

“헉. 조장님.”

이럴 때일수록 마음이 약해져서는 안 된다. 나는 소매를 붙잡은 혁무진의 손길을 뿌리치며 호통쳤다.

“당장 사과드려라. 이 나쁜 새끼야. 가진 거라곤 불알 두 쪽밖에 없는 주제에 감히 그런 말을 해?”

“죄송합니다. 정말 죄송합니다.”

“하남자 특. 생각 없이 지껄이다가 동창한테 끌려감.”

“죄송합니다! 정말 죽을죄를 지었습니다!”

“하남자 특. 죽을죄를 지어서 진짜 죽음.”

“안 돼! 제발 살려 주십시오, 홍 동지! 제겐 호랑이 같은 부모님과 토끼 같은 동생이 있습니다!”

어, 깜짝이야. 순간 북한인 줄 알았네.

혁무진은 마치 사상 검증에 걸려 아오지 탄광에 끌려가는 공산당원처럼 엎드려 울부짖었고, 그 모습을 짜게 식은 눈빛으로 바라보던 홍 동지, 아니 산서성 도지휘동지 홍진은 땅이 꺼져라 한숨을 내쉬었다.

“누가 보면 내가 저승사자라도 되는 줄 알겠네. 상산왕 전하 앞에서 추태 그만 보이고 일어나요. 안 그래도 보는 눈도 많은데, 이러다가 부끄러워서 죽을 것 같아.”

매우 슬프게도, 홍진의 말은 사실이었다.

금의위들은 뭐 이런 병신들이 있나 하는 눈빛으로 우리를 바라보는 중이었고, 막 잠에서 깨어나 비몽사몽하던 상산왕도 눈을 동그랗게 뜬 채 내게 물었다.

“저자의 별호가 진정 십상남자(十上男子)가 맞는가?”

잠시 머뭇거린 내가 대답했다.

“그, 비슷합니다.”

틀린 말은 아니다.

십상남자나 십하남자나 어차피 겨우 한 글자 차이니까.

‘물론 의미는 정반대지만.’

어린 왕의 동심을 지켜 주기 위해 말을 삼킨 그때, 저 정도면 신하들을 고문하기 위해 만들어진 게 아닐까 싶을 만큼 끝없이 이어진 계단을 내려온 일단의 무리가 우리의 앞에 섰다.

아니, 정확히 말하자면 상산왕 주표의 앞에서 무릎을 꿇었다.

“상산왕 전하를 뵈옵나이다.”

“천세! 천세! 천천세!”

검은 비단으로 만들어진 관복(官服)을 걸친 그들의 연령대는 제법 다양했다.

많이 쳐줘야 약관 어림으로 보이는 젊은이부터, 주름이 자글자글한 노인까지.

그러나 그들의 공통점은 관복뿐만이 아니었고, 나는 즉각 그 사실을 깨달았다.

‘환관.’

틀림없었다.

하나같이 하얗게 분칠한 얼굴에 붉은 입술. 그 사이로 흘러나온 목소리는 여인의 것도, 사내의 것도 아니었으며 왜소한 체격은 넉넉한 품을 지닌 관복으로도 가리지 못할 정도였으니.

하지만.

‘강하다.’

무위는 덩치로 정해지는 것이 아닌 법.

보이는 것이 전부가 아니다.

나는 그들의 왜소한 체구 안에 웅크린 거대한 기운을 느낄 수 있었고, 동시에 조금 전 들었던 어느 단체의 이름을 떠올렸다.

아니, 자연스럽게 중얼거렸다.

“동창?”

사락.

길게 늘어진 옷자락이 지면을 스친다.

환관들의 선두에서 상산왕을 향해 깊숙이 절을 올리던 늙은 환관이 고개를 들어 나를 바라보았다.

도무지 속내를 읽을 수 없는 묘한 눈빛.

짧은 순간, 마치 마음을 꿰뚫어 보듯 나를 응시하던 늙은 환관이 옆에 선 홍진을 향해 입을 열었다.

“오랜만이오, 홍 첩형(貼刑). 아니, 이제는 도지휘동지라고 불러 드리면 될까.”

홍진이 담담하게 대답했다

“원하는 대로. 그나저나 넌 못 본 새에 더 늙었구나?”

상당한 나이 차가 있음에도 자연스러운 하대.

이는 곧 과거 홍진의 지위가 그만큼 높았다는 뜻이었고, 늙은 환관의 주름은 더욱더 깊어졌다.

“말을 조심하는 것이 좋을 거요. 지난 십 년 동안 바뀐 것은 강산뿐만이 아니니까.”

“변해 봤자지 뭐. 그리고 늙어서 머리가 굳은 모양인데, 정확히는 십일 년 하고도 아흐레야.”

“그걸 그리 정확히 기억하고 있었소?”

“잊으려 해도, 잊을 수 없는 기억이 있으니까.”

“그러기에는 너무 많은 것을 잊은 듯하오만.”

늙은 환관이 서늘한 목소리로 말을 이었다.

“감히 허락받지 않은 외인(外人)을, 그것도 강호의 무뢰배를 황궁에 들이다니. 제아무리 황실을 떠났다 하여 그 법도마저 잊은 거요?”

“세월이 흐르긴 했네. 상산왕 전하께서 허락하신 일에 감히 네놈 따위가 왈가왈부하다니. 그리고…….”

홍진이 또렷한 음성으로 말을 이었다.

“모든 것이 법도대로 흘러갔다면, 지금 이런 상황까지 오지도 않았겠지.”

“……!”

“……!”

단단한 뼈가 숨어 있는 홍진의 한 마디에, 주위의 공기가 차갑게 얼어붙었다.

그의 말마따나 모든 일이 정해진 법도에 따라 흘러갔다면, 작금의 천자는 옥좌에 오르지 못했을 테고 상산왕 주표의 처지 역시 지금과는 크게 달라졌을 테니까.

홍진은 그 사실을 에둘러 꼬집었고, 천자의 수족이나 다름없는 금의위와 동창의 환관들이 보일 반응은 처음부터 정해져 있었다.

스릉.

서늘한 날붙이의 마찰음이 귓가에 닿은 그 순간.

나는 일말의 망설임도 없이 움직였다.

훅.

단 한 걸음.

공간이 지워진다. 바람이 사라진다.

나는 느리게 흘러가는 시간 속에서 손을 뻗어, 힘있게 검파(劍把)를 쥔 누군가의 손아귀를 짓눌렀다.

채 절반도 뽑히지 않은 검신이, 원래의 자리로 돌아갈 수 있도록.

철컥.

나직한 소음과 함께, 잠시 느려졌던 시간이 돌아온다. 이름 모를 금의위 무사의 부릅뜬 눈이 이렇게 속삭이는 듯했다.

어떻게?

그러나 나는 구태여 대답하지도, 이미 석상처럼 굳어 버린 상대를 쓰러트리지도 않았다.

아니, 어쩌면 내가 대답했을지라도 그는 듣지 못했을 것이다.

섬광처럼 움직인 신형을 뒤늦게 따라잡은 바람이 온 사방에 휘몰아쳤으니까.

화아아악!

터져나가는 공기와 함께 부풀어 오르는 옷자락들.

하나의 예술 작품처럼 지면에 가지런히 깔린 청석(靑石)들 사이로, 켜켜이 쌓여 있던 먼지가 일어나며 바람을 타고 흩날렸다.

마치 진눈깨비처럼.

그리고 기침 소리 하나 없는 그 숨 막히는 침묵 속에서, 나는 담담하게 입을 열었다.

“어디서 함부로 병장기를 뽑고 지랄이냐. 그것도 어린애, 아니 상산왕 전하께서도 지켜보고 계시는 마당에.”

“……!”

“……!”

“더 이상 일 크게 키우지 말자고. 그게 서로를 위한 길이니까. 안 그래?”

지금 한 말은 순도 백 퍼센트의 진심이다.

당장 눈앞에 보이는 놈들을 처리하는 건 어렵지 않지만, 황궁 입구에서 그런 짓을 벌였다가는 최악의 상황으로 치달을 수도 있으니까.

그리고 이런 내 진심은, 생각지도 못한 누군가에게까지 닿았다.

“태도는 불경하지만, 틀린 말은 아니군.”

“……!”

도대체 언제?

나는 찬물을 뒤집어쓴 듯한 기분을 느끼며 돌아섰다.

삼십여 장 밖, 황궁으로 끝없이 이어져 있는 계단의 중간 어림에 우뚝 서 있는 중년인이 보였다.

‘기척을…… 느끼지 못했다.’

시스템에 최대한 의존하지 않기 위해 끊임없이 기감(氣感)을 벼려 온 나다.

그와 나 사이에 상당한 거리가 있는 것은 부정할 수 없는 사실이지만, 이는 갑작스럽게 등장한 저 중년인의 무위가 나와 비교해도 결코 부족함이 없다는 증거이기도 했다.

‘아니, 어쩌면 그 이상.’

나는 머리가 차갑게 식는 것을 느끼며 중년인을 응시했다.

경신술을 발휘하는 대신, 마치 한량과 같은 발걸음으로 천천히 계단에서 내려온 그는 나를 향해 빙긋 웃으며 입을 열었다.

“강호의 여느 무뢰배들처럼 무모하기 그지없으나, 그들만큼 무지하지는 않구나. 태원진가의 진태경.”

눈앞의 중년인이 이미 내 정체를 알고 있다는 사실은 그리 놀랍지 않았다.

금의위의 앞길을 가로막은 그 순간부터 충분히 예상했던 일이었으니까.

더군다나 그가 나를 알고 있듯이, 나 역시 그의 정체를 어렴풋이 짐작하고 있기도 했다.

설령 중년인이 화려한 황금빛 갑옷을 걸치고 있지 않았더라도, 다음 순간 터져 나온 외침을 들었다면 저절로 알게 되었을 것이다.

“충(忠)!”

“지휘사(指揮使)를 뵈옵니다!”

정호군을 선두로, 휘하의 금의위들이 일제히 한쪽 가슴을 두드리며 군례(軍禮)를 외치는 모습은 나름대로 장관이었다.

사방에서 번뜩이는 황금빛 물결을 가로질러 다가오는 중년인의 모습 역시도.

저벅. 저벅.

나직한 발걸음 소리가 함성 직후의 침묵을 깨트린다.

체구가 크지도, 작지도 않으나 거인처럼 느껴지는 중년인은 어린 왕의 앞에 이르러서야 걸음을 멈추었다.

“신, 금의위 지휘사 백연이 상산왕 전하를 뵈옵니다. 오직 황상께 충정을 다하는 몸이기에 무릎을 꿇지 못하는 점, 하해와 같은 마음으로 용서해 주시길.”

정중한 말과는 달리 목소리는 가볍고, 직계 황족이자 왕을 향한 마땅한 예의조차 보이지 않는다.

거기에 더하여 입가에 맺힌 흐릿한 미소까지.

하지만 금의위 지휘사라는 직책에는 그만한 힘이 있었다. 그는 천자가 가장 신임하는 무관이자, 고관대작(高官大爵)들조차 두려워 마지않는 금의위의 수장이니까.

“더불어 바라옵건대, 감히 전하 앞에서 불경을 저지른 수하들의 죄 역시 소신께 물으소서.”

이건 사죄나 부탁이 아니다. 통보다.

일련의 사태를 이쯤에서 마무리 짓고 끝내자는 통보.

우선은 그저 지켜만 보고 있던 나로서도 눈살이 찌푸려질 정도였지만, 상산왕의 충복인 홍진의 반응은 조금 전과 달랐다.

까득.

살갗이 하얗게 물들 만큼 힘껏 움켜쥔 주먹.

열 손가락에 끼워진 반지들이 거슬리는 마찰음을 토해 낸다.

그러나 깊게 가라앉은 눈빛으로 중년인, 아니 금의위 지휘사 백연을 응시하던 홍진은 상산왕을 향해 작게 속삭였다.

“전하.”

나직한 부름이었으나 그 억눌린 목소리에 담긴 뜻은 명백했다.

지금의 홍진은 백연과 맞서는 것을 우려하고 있었다.

그가 막강한 권력을 틀어쥔 금의위 지휘사이기 때문인지, 아니면 또 다른 이유 때문인지는 모르겠지만.

그리고 냉정하게 판단했을 때, 이 결정에 내가 끼어들 여지는 없었다.

먼저 검을 뽑은 금의위 무사를 가로막은 것은 명목상의 호위로서 합당한 행동이었으나, 이 이상은 홍진의 뜻을 따르는 것이 상책이다.

이곳은 무림이 아닌 황실이니까.

하지만 다음 순간 들려온 상산왕의 음성은, 이 자리의 누구도 예상치 못한 것이었다.

“만약 그대라면, 어떻게 하겠는가.”

사방에서 쏟아지는 무수한 시선들.

이 뜻밖의 상황에 내가 잠시 할 말을 잃어버린 사이, 상산왕 주표가 재차 입을 열었다.

다른 누구도 아닌, 바로 나 한 사람을 향해.

“열화신룡 진태경. 그대라면 어찌하겠느냐 물었다.”

또렷하게 빛나는 눈동자.

새로운 서명을 받고 기뻐하던 어린아이는 더 이상 어디에서도 찾아볼 수 없었고, 나는 기억 속의 한 아이가 소년으로 성장했음을 깨달았다.

지금 그가 원하는 답이 무엇인지도.

“어, 솔직히 말씀드려도 됩니까?”

“그것이야말로 짐이 원하는 바. 이는 왕으로서 내리는 명령이다.”

당찬 왕명(王命)에, 나는 소리 내어 웃었다.

그리고 모두를 바라보며 입을 열었다.

“말씀하신 대로, 만약 제가 전하였다면…….”

잊지 말자.

이곳은 황궁. 수위 조절이 필수다.

“이미 싹 다 조져놨을 겁니다.”

“……!”

“……!”

오케이. 조절 실패.
```

## Final English reading copy

```markdown
# Chapter 862

The East Depot.

Anyone who’d read a few martial arts novels knew that name.

If the Nine Sects and One Gang and the Five Great Families showed up like clockwork in those stories, then the imperial court had the East Depot, which stood alongside the Embroidered Uniform Guard as its other great power.

And Hong Jin was a member of that very East Depot.

My mouth fell open before I even realized it.

“The East Depot? The one I’m thinking of?”

“There’s only one East Depot in the world, Young Master Jin.”

“No, I mean, it actually exists?”

“……Is there a fake East Depot, then?”

“Ah. That’s not what I meant.”

I hadn’t known the East Depot really existed.

It hadn’t been that long since I’d learned the Embroidered Uniform Guard was real, either.

The endless incidents and disasters in Murim kept me busy enough. Who would’ve expected to suddenly get tangled up with the imperial court like this?

*Still, if Hong Jin really did come from the East Depot, then some of the things he’s shown me make a lot more sense.*

Newly astonished, I looked at Hong Jin.

I didn’t know the details, but the East Depot’s influence couldn’t be far behind the Embroidered Uniform Guard’s.

At first, I’d thought he was just a eunuch who’d been a bit of a tough guy in his youth. Now that I’d heard his story, I could almost picture him hawking up phlegm in the palace corridors.

Hyuk Mujin must have had a similar thought. He’d been glancing sideways at Hong Jin, and now he whispered in a voice barely above a breath.

“Captain. This is no ordinary eunuch.”

“……Please, just shut your mouth.”

“It’s fine. He can’t hear me.”

“Sorry, but I can hear you just fine.”

At Hong Jin’s sudden reply, I answered quickly.

“I didn’t say anything. That bastard did.”

“Gasp. Captain!”

This was no time to go soft. I shook off Hyuk Mujin’s hand as he grabbed my sleeve and snapped at him.

“Apologize this instant, you bastard. You’ve got nothing but a pair of balls to your name, and you dare say that?”

“I’m sorry. I’m truly sorry.”

“Beta-male behavior: runs his mouth without thinking, then gets dragged off by the East Depot.”

“I’m sorry! I’ve committed a crime worthy of death!”

“Beta-male behavior: commits a crime worthy of death, then actually dies.”

“No! Please spare me, Comrade Hong! I have tiger-like parents and a rabbit-like younger sibling!”

Whoa, that startled me. For a second, I thought we were in North Korea.

Hyuk Mujin was facedown, wailing like a Communist Party member caught in an ideological purge and dragged off to the Aoji coal mines. Hong Comrade—or rather, Hong Jin, Deputy Military Commissioner of Shanxi Province—watched him with a thoroughly unimpressed look and heaved a sigh that seemed to come from the depths of the earth.

“Anyone would think I was the Grim Reaper. Stop making a spectacle of yourself in front of His Highness Prince Shangshan and get up. There are already plenty of eyes on us. At this rate, I’ll die of embarrassment.”

Very sadly, Hong Jin was right.

The Embroidered Uniform Guards were staring at us like they couldn’t believe what a bunch of idiots we were. Prince Shangshan, who’d just woken up and was still groggy, had his eyes wide as he asked me,

“Is that man truly known by the sobriquet Tenfold Man?”

I hesitated for a moment, then answered,

“Something like that.”

It wasn’t wrong.

Tenfold Man and Tenfold Beta Man were only one character apart, after all.

*Though their meanings are complete opposites.*

I held my tongue to protect the young prince’s innocence. Just then, a group of people came down the endless staircase—long enough to make me wonder if it had been built to torture subjects—and stopped in front of us.

Or, more precisely, they knelt before Prince Shangshan Zhu Bao.

“We pay our respects to His Highness Prince Shangshan.”

“A thousand years! A thousand years! A thousand thousand years!”

They wore official robes made of black silk, and their ages varied widely.

Some looked barely twenty, at most; others were old men with deeply wrinkled faces.

But their robes weren’t the only thing they had in common. I realized at once.

*Eunuchs.*

No doubt about it.

Every one of them had a face powdered white and lips painted red. Their voices were neither a woman’s nor a man’s, and their small frames showed even through the loose fit of their robes.

And yet—

*They’re strong.*

Martial power wasn’t decided by the size of your body.

There was more to people than what you could see.

I could feel the immense energy coiled inside their small frames. At the same time, I recalled the name of the organization I’d just heard.

No—I found myself muttering it aloud.

“The East Depot?”

Rustle.

A long hem brushed the ground.

At the head of the eunuchs, an old man who’d bowed deeply to Prince Shangshan raised his head and looked at me.

His strange gaze gave nothing away.

The old eunuch stared at me for a brief moment, as if he could see right through me, then spoke to Hong Jin beside him.

“It’s been a long time, Hong Cheophyeong. Or should I call you Deputy Military Commissioner now?”

Hong Jin answered calmly.

“Call me whatever you like. But you’ve gotten even older since I last saw you.”

Though there was a considerable age difference between them, Hong Jin spoke to him casually and without deference.

That meant Hong Jin’s position back then must have been quite high. The old eunuch’s wrinkles deepened further.

“You’d be wise to watch your words. The landscape isn’t the only thing that’s changed in the last ten years.”

“Things can only change so much. And your brain must have gone stiff with age. It’s been eleven years and nine days, to be precise.”

“You remember that exactly?”

“There are some things you can’t forget, even if you try.”

“And yet you seem to have forgotten rather a lot.”

The old eunuch continued in a chilly voice.

“How dare you bring an outsider into the imperial palace without permission—one of those ruffians from the martial world, no less. Just because you left the imperial court, have you forgotten its rules as well?”

“Times really have changed. Someone like you dares to question something His Highness Prince Shangshan permitted? And…”

Hong Jin continued in a clear voice.

“If everything had gone according to the rules, things wouldn’t have come to this.”

“……!”

“……!”

Hong Jin’s words had a hard edge beneath them, and the air around us froze.

Just as he said, if everything had followed the rules, the current Son of Heaven wouldn’t be sitting on the throne, and Prince Shangshan Zhu Bao’s situation would be very different.

Hong Jin had alluded to that fact, and the reaction of the Embroidered Uniform Guards and the East Depot eunuchs—the Son of Heaven’s own hands and feet—was settled from the start.

Shing.

The cold scrape of a blade reached my ears.

I moved without the slightest hesitation.

Whoosh.

One step.

Space disappeared. The wind fell silent.

In time that seemed to pass slowly, I reached out and pressed down on the hand of someone gripping a sword hilt tightly.

To send the blade, not even halfway drawn, back where it belonged.

Click.

At the soft sound, time—which had slowed for a moment—returned to normal. The wide eyes of an Embroidered Uniform Guard I didn’t know seemed to whisper:

*How?*

But I didn’t bother answering, nor did I knock down my opponent, who’d already gone rigid as a statue.

Then again, even if I had answered, he might not have heard me.

The wind, catching up with my figure after it had moved like a flash of light, whipped in every direction.

Fwoosh!

Clothes billowed in the burst of air.

Dust that had lain in layers between the bluestones, fitted neatly into the ground like a work of art, rose and scattered on the wind.

Like sleet.

In that breathless silence, without a single cough, I spoke calmly.

“Who the hell told you to draw your weapon? With a child—no, with His Highness Prince Shangshan watching, no less.”

“……!”

“……!”

“Let’s not make this any bigger than it has to be. That’s best for everyone, isn’t it?”

I meant every word.

Taking care of the men in front of me wouldn’t be difficult, but doing that at the entrance to the imperial palace could send things spiraling into the worst possible situation.

And my sincere words reached someone I hadn’t expected.

“Your manner is disrespectful, but you’re not wrong.”

“……!”

When had he—

I turned around, feeling as if someone had dumped a bucket of cold water over my head.

About thirty *jang* away, halfway down the endless staircase leading up to the imperial palace, stood a middle-aged man.

*I didn’t sense him at all.*

I’d been constantly honing my Qi Sense so I wouldn’t have to rely on the System as much as possible.

There was no denying the distance between us was considerable, but the fact that I hadn’t sensed him was proof that the middle-aged man’s martial prowess was no less than mine.

*No. It might even be greater.*

I fixed my gaze on the man, feeling my mind grow cold.

Instead of using lightness skill, he came slowly down the stairs with the leisurely gait of a carefree man. He smiled at me and spoke.

“You’re reckless, like the other ruffians of the martial world, but not as ignorant. Jin Taekyung of the Jin Family of Taiyuan.”

It wasn’t especially surprising that the middle-aged man already knew who I was.

I’d expected as much the moment I stepped in front of the Embroidered Uniform Guard.

And just as he knew who I was, I had a vague idea of who he was, too.

Even if he hadn’t been wearing a gleaming golden suit of armor, the shout that rang out the next moment would’ve told me.

“Loyalty!”

“We pay our respects to the Commander!”

Led by Jeong Hogun, the Embroidered Uniform Guards under his command struck their chests and shouted their military salute as one. It was quite a sight.

So was the middle-aged man approaching through a sea of flashing gold.

Step. Step.

His soft footsteps broke the silence that followed the shouts.

He was neither large nor small, but somehow seemed like a giant. He stopped only when he reached the young prince.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, pay my respects to His Highness Prince Shangshan. I serve only the Emperor with my utmost loyalty, so please forgive me for being unable to kneel, with a heart as vast as the sea.”

His words were respectful, but his voice was light. He didn’t even show the proper deference due to a direct member of the imperial family—a prince.

And then there was that faint smile on his lips.

Still, he held the post of Commander of the Embroidered Uniform Guard for a reason. He was the Son of Heaven’s most trusted military officer, and the head of a force even the highest-ranking officials feared.

“Furthermore, I humbly ask that Your Highness hold me responsible for the crimes of my subordinates, who dared to show disrespect in your presence.”

That wasn’t an apology or a request. It was a notification.

He was telling us to put an end to this here and now.

Even I, who was only watching for the moment, couldn’t help frowning. But Hong Jin, Prince Shangshan’s loyal servant, reacted differently from before.

Crack.

He clenched his fist so tightly that his skin turned white.

The rings on his ten fingers scraped against one another with an unpleasant sound.

But Hong Jin stared at the middle-aged man—or rather, Baek Yeon, the Commander of the Embroidered Uniform Guard—with a deeply restrained gaze, then leaned toward Prince Shangshan and whispered,

“Your Highness.”

It was a quiet call, but the meaning in his suppressed voice was clear.

Hong Jin was worried about confronting Baek Yeon right now.

Whether that was because Baek Yeon held the immense power of the Embroidered Uniform Guard’s command, or for some other reason, I couldn’t say.

And looking at it coldly, I had no place in this decision.

Intervening when an Embroidered Uniform Guard drew his sword was the proper thing to do as a guard in name, but from here on, it was best to follow Hong Jin’s lead.

This was the imperial court, not Murim.

But the next words out of Prince Shangshan’s mouth were something no one there could have anticipated.

“If you were in my place, what would you do?”

Countless eyes turned toward me from every direction.

As I stood there, briefly at a loss for words, Prince Shangshan Zhu Bao spoke again.

To me, and no one else.

“Blazing Flame Divine Dragon Jin Taekyung. I asked what you would do in my place.”

His eyes shone brightly.

The little boy who’d been delighted to get a new autograph was nowhere to be seen. I realized that the child in my memory had grown into a young man.

I knew what answer he wanted now, too.

“Uh, may I speak honestly?”

“That is precisely what I want. This is an order from your prince.”

At the prince’s bold command, I laughed aloud.

Then I looked at everyone and spoke.

“As you said, if I were in your place…”

Let’s not forget.

This was the imperial palace. I had to keep things under control.

“I’d have already beaten the shit out of every last one of them.”

“……!”

“……!”

Okay. So much for keeping it under control.
```
