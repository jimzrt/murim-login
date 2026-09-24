<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0948.txt",
      "sha256": "635f9966799a0afe6b3443428fc98dbd3ceb7f08f9c56daeb79526cff3583871",
      "bytes": 12927
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3dfcf28d6b241a7725476f335bdd680e3989ac4e0d71a0dbeab790f3b62d6a4d",
      "bytes": 2928
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e5bfffbb63a397599ec22f2dd35770b64b205f7588e8cf6e8a91960b87d5f769",
      "bytes": 233488
    },
    {
      "path": "characters/Cheolyeong.md",
      "sha256": "1c4893eb31d0baf4d1c789282cf05eea0437bd847452dfc9347e4860a7791bff",
      "bytes": 342
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "f154083ce947509f33fb34b8171b608645c78ac27e7f24172523bdd1dbe126ef",
      "bytes": 577
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0896344edf677e092099d44eab77d3693030b2c77e85c4fad83d3e68d49e166c",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "480b458c2173818284df6f938e1fb7e9eed4e7e63cec1b7839bff6870ad9a16e",
      "bytes": 1204
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "bd15629a8f549f0ac1635d29ffafee56df9a5a619ff1390cce9c06507b8c295e",
      "bytes": 778
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "ac37d13c1754186ddb08eaaa02e285b825352c3cfdf6addffeeddae91ccecef9",
      "bytes": 680
    },
    {
      "path": "characters/Peng Cheolyeong.md",
      "sha256": "cee058a61a396edc031c103c6f1f4e71332104021cd57d20cd4ed527fbfaa16c",
      "bytes": 550
    },
    {
      "path": "characters/Temur.md",
      "sha256": "9d2b95e084884aca92ed985cae9b09a32f4ac4b09e673a48f2b98a5ad333e0dd",
      "bytes": 616
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f66daa4bae985fcbafa7ec30ad9fc462f9834c125f917088f6bc22c9afe669f8",
      "bytes": 267309
    }
  ],
  "estimated_tokens": 11035
}
-->

# Durable State Update — Chapter 948

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
1 and safe_through 948. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 948. Profile updates may replace only one
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
  "chapter": 948,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 948,
    "continuity_sources": [948],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "War against Dark Heaven is imminent; its main force is targeting Shanxi as a foothold for invading the Central Plains, with the Double Ninth Festival the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The improved Temporary Strength Pill has circulated for months and may create a dangerous, addictive drive for strength across Murim; its full effects and distribution network remain unknown.",
    "An unconscious bandit chief is being taken to the Nangong Family for possible interrogation; he may hold important information about the pill.",
    "Taekyung ordered Anhui’s City Lord to tighten security and investigate the pill’s distribution; the Murim Alliance’s Fire Dragon Pavilion and a thousand Embroidered Uniform Guards are expected within a day or two.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious and being taken to the Nangong Family.",
    "Jang Sam’s silk pouch, received from an unknown traveler in Hubei, likely contained a modified Temporary Strength Pill; its effects and side effects remain unconfirmed.",
    "The Bow Saint once wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance."
  ],
  "continuity_sources": [
    947,
    946
  ],
  "open_questions": [
    "Who was the traveler who gave Jang Sam the silk pouch, and what are the modified pill’s exact effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 947,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 팽철후    | **Peng Cheolhu**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 철영 | **Cheolyeong** | Peng Cheolhu’s eldest son and the current Family Head of the Peng Family. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 칠로군 | **Seven-Route Army** | Seven-pronged force led by Wipeng and the Jin Dragon Squad. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |

## Listed compact profiles

### Cheolyeong.md

# Cheolyeong (철영)

- **Safe through:** Chapter 947
- **Aliases:** None
- **Role:** Cheolyeong is the current Family Head of the Peng Family in Hebei.
- **Personality:** Not established.
- **Voice:** Not established
- **Relationships:** He is Peng Cheolhu’s eldest son.

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 939
- **Aliases:** None
- **Role:** Chinggen is a Khan of the northern grasslands, ruling alongside Temur over tens of thousands of horses and warriors.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 947
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 947
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 938
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 947
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

### Peng Cheolyeong.md

# Peng Cheolyeong (팽철영)

- **Safe through:** Chapter 194
- **Aliases:** Iron Blood Saber
- **Role:** Family Head of the Hebei Peng Family; son and successor of the Thunderbolt Saber King.
- **Personality:** Not established in Chapter 194.
- **Voice:** Not heard in Chapter 194.
- **Relationships:** Son of the Thunderbolt Saber King; Jeok Cheongang says his past fight was followed by no further contact and that the Peng Family fabricated a later story about their encounter.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 939
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and inclined to dismiss distant threats while indulging in celebration.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

## Korean source

```text
＃948화



이리저리 깨지고 부서진 가구를 다급하게 치우는 시비와 하인들.

그리고 한바탕 태풍이라도 휩쓸고 지나간 듯한 그 풍경 속에서, 거친 숨을 몰아쉬며 서로를 노려보는 거한들.

그것이 벽력도왕(霹靂刀王) 팽철후가 내당의 대회의실에 들어서자마자 본 광경이었고, 대강의 상황을 파악한 그는 모두를 바라보며 한 마디를 툭 내뱉었다.

“셋. 더도 말고 덜도 말고 딱 셋을 세겠다. 만약 그때까지 제자리로 돌아가지 않으면…….”

쉬쉭!

말이 끝나기도 전에 수십여 명의 거한들이 바람처럼 본래의 자리를 찾아 돌아갔다.

단 한 사람만 빼고.

“오셨습니까, 아버지.”

어느덧 칠순을 바라보는 장자(長子)의 인사에, 벽력도왕이 눈살을 찌푸렸다.

“아침 문안 인사치고는 한참 늦었구나.”

“곤히 주무신다기에…….”

“집어치워라. 이제 슬슬 사람 구실 하겠다 싶어서 가주 직을 물려줬더니, 피를 나눈 식솔들끼리 싸움박질을 해? 그것도 가문의 중대사를 논하는 신성한 대회의실에서!”

쩌렁쩌렁한 고함을 묵묵히 받아 내던 하북팽가의 현 가주, 철혈도(鐵血刀) 팽철영이 입을 열었다.

“아버지께서 셋째 숙부의 왼팔을 부러트렸던 기억이 새록새록 나는군요. 그것도 가문의 중대사를 논하는 이 신성한 대회의실에서.”

순간 멈칫한 벽력도왕이 이내 준엄한 목소리로 대답했다.

“한창 혈기왕성할 때의 일이다.”

“작년입니다.”

“……그럴 리가 없는데.”

“그뿐입니까? 재작년에는 둘째 숙부께서 회의 중에 잠시 졸았다고 아구창을…….”

“어허, 가주!”

감히 아버지이자 태상가주인 벽력도왕을 향해 대드는 팽철영에게 엄한 목소리로 일갈한 둘째 숙부가 덧붙였다.

“난 정강이였네. 아구창은 누구였는지 모르겠지만.”

“죄송합니다. 제가 착각했군요. 그건 아마 다섯째 숙부셨던 것 같습니다.”

벽력도왕의 등장과 동시에 한쪽 구석에 찌그러져 있던 다섯째 숙부가 우수에 젖은 눈빛으로 중얼거렸다.

“그래, 삼 년 전이었지. 깨어나 보니 이틀이 지났…….”

“그만, 그만하지. 충분히 알겠으니까 넘어가자고.”

본전도 못 찾은 벽력도왕은 고개를 절레절레 내저으며 상석에 앉았다.

그나마 다행히도, 조금이라도 수틀렸다 하면 주먹부터 휘두르고 보는 하북팽가의 유서 깊은 전통을 위해 마련된 튼튼한 철제 의자는 멀쩡하게 형태를 유지하고 있었다.

“다들 흰소리는 집어치우고 자리에 앉게. 무슨 문제로 두 시진씩이나 치고받고 떠들었는지부터 들어보지.”

벽력도왕을 따라 옆자리에 앉은 팽철영이 즉각 입을 열었다.

“북부의 낌새가 이상합니다.”

“북부? 모용세가(慕容世家)가 갑자기 왜?”

벽력도왕이 갑자기 모용세가를 입에 올린 것은 당연했다.

예로부터 하북팽가에게 있어 북부라 함은, 곧 모용세가를 뜻하는 것이었으니까.

이 광활한 천하의 끄트머리.

진정한 변방이라 할 수 있는 요녕성(遼寧省)의 패자이자 수백 여년 전 일국의 왕을 자처하던 선비족의 후예들은 오대 세가의 일원으로 당당히 자리매김한 지 오래였다.

“모용세가의 낌새가 이상하다니, 그럴 리가 없다. 어디선가 잘못된 정보를 들은 거겠지.”

벽력도왕은 들을 필요도 없다는 듯이 손사래를 쳤지만, 다음 순간 들려온 팽철영의 대답에 얼굴을 굳혔다.

“모용세가를 말씀드린 것이 아닙니다.”

“뭐라?”

모용세가가 아니다.

그렇다면 남은 건 한 곳밖에 없다.

진정한 의미의 북부. 온갖 암수와 창칼이 도사린 무림보다 더한 무법자들의 땅.

“설마…… 초원의 그 오랑캐 놈들을 말하는 것이냐?”

“예.”

그나마 하북팽가의 핏줄 중 가장 온순하다는 평가를 받는 가주 팽철영이 침착한 어조로 말을 이었다.

“아무래도 들려오는 소문들이 심상치 않습니다.”

“본래 뼛속까지 흉흉한 족속들이긴 하지만, 근 몇 년 동안은 잠잠했을 텐데?”

벽력도왕의 말은 틀림없는 사실이었다.

정확히는 약 이 년 전부터, 한시도 분란이 끊이질 않던 초원에 평화와 번영이 깃들기 시작했으니까.

그리고 그 모든 일의 중심에는 북방의 신흥 강자로 급부상한 태원진가가 있었다.

“태원진가가 칠로군(七路軍)인지 뭔지를 결성해서 싹 쓸어버린 후로는 아무런 문제도 없다고 들었다. 노부가 잘못 알고 있는 것이냐?”

“정확히 알고 계십니다. 단 한 번의 출병으로 앓던 이를 단번에 빼 버렸지요.”

산서 무림을 손에 넣은 직후 태원진가가 보인 움직임은 오대세가와 구파일방마저 혀를 내두를 정도로 과감하면서도 신속했다.

과거 태원진가를 향해 이빨을 드러냈던 여러 문파는 물론 표국과 상단마저 합병한 뒤, 그 힘을 바탕으로 일곱 개의 무력대를 편성하여 초원을 휩쓸었다.

일정 주기로 국경을 넘어 노략질과 살인을 일삼던 마적 떼도, 기마 민족도 칠로군의 앞에서는 상대가 되지 못했다.

아니, 그들 중 일부는 오히려 태원진가의 깃발 아래에 섰고 승리의 대가를 두둑하게 챙겼다.

“테무르. 칭겐.”

아들의 입술 사이로 흘러나온 이국적인 이름에 벽력도왕은 미간을 좁혔다.

일선에서 물러난 후에는 무공에만 전념한 그였지만, 명실상부한 하북팽가의 태상가주다.

간혹 가다 참석하는 회의의 내용도 어지간하면 빠짐없이 기억하고 있었고, 얼굴조차 모르는 오랑캐의 이름이라고 한들 예외는 아니었다.

“태원진가에 붙어 대족장이 됐다는 그 두 놈이로군. 맞느냐?”

“예. 초원에서는 ‘칸’이라고 불린다 들었습니다.”

“칸이건 간이건 내 알 바 아니다. 중요한 건 그놈들이 뭔 짓거리를 벌이고 있느냐지.”

벽력도왕은 쇠막대기 같은 손가락으로 탁자를 두드리며 생각에 잠겼다.

테무르와 칭겐.

태원진가와 협력한 덕분에 초원의 강자로 급부상한 그놈들이 수상한 낌새를 보인다면 그 이유는 둘 중 하나다.

지금 가진 것에 만족하지 못하고 더 큰 야욕을 드러냈거나.

혹은…….

“암천. 그 찢어 죽여도 시원치 않을 놈들과 손을 잡았을 가능성은 얼마나 되느냐?”

“아직은 확실치 않습니다만.”

팽철영이 나직하게 덧붙였다.

“정황상 암천과 결탁했으리라 예상됩니다.”

벽력도왕은 내심 침음성을 흘렸다.

‘하긴, 그놈들이 미치지 않고서야 갑자기 이렇게 나올 리가 없지. 더군다나 화왕(火王), 그 미친 늙은이가 태원진가의 뒤에 떡하니 버티고 있는 것을 뻔히 알면서도.’

화왕 적천강과 태원진가의 관계는 더 이상 모르는 이가 없다.

테무르와 칭겐이 일부 동족들을 배신하면서까지 태원진가와 손을 잡고, 현재의 세력을 갖출 수 있었던 것 역시 화왕에 대한 두려움 때문이었다는 소문이 파다했다.

‘한데 이런 식으로 뒤통수를? 말도 안 되는 소리지.’

화왕 적천강은 그 자체로 겁화(劫火)다.

모든 것을 잿더미로 만든 후에야 비로소 사그라지는 겁화.

자존심 하나만큼은 누구보다 강한 벽력도왕이었지만, 화왕과 진심으로 척을 지게 되는 상황은 생각하기도 싫을 정도였다.

‘뒷배가 있다. 분명히.’

마음속으로 뇌까린 벽력도왕은 자신의 맏아들을 물끄러미 응시했다.

“그렇게 생각한 이유가 있을 터. 근거가 무엇이냐?”

“지금으로부터 약 이 년 전, 초원에 믿을만한 이들을 심어 두었습니다.”

“간자(間者)라……. 제법 머리를 굴렸구나.”

“초원의 정세가 아직 불안정한 시기였습니다. 새롭게 교역로가 열렸을 때를 노렸지요.”

개방은 곧 유입을 뜻하는 법.

태원진가를 필두로 한 칠로군의 정벌 직후, 초원의 교역로를 통해 흘러 들어간 것은 고아한 도자기나 장신구뿐만이 아니었다.

사람.

오랜 시간 동안 무법지대였던 초원에서 찾아볼 수 없었던, 새로운 인간군상들.

그리고 초원의 공백을 일부 차지한 그들 중에는 하북팽가의 간자도 포함되어 있었다.

“그들 중 몇몇이 최근 들어 초원의 오랑캐들이 집결하고 있다는 정보를 전해 왔습니다.”

“숫자는?”

“최소 일만 이상.”

“……뭐라? 일만?”

“아버지.”

눈을 크게 뜬 채 자신을 바라보는 벽력도왕의 모습에, 팽철영은 어렵사리 입을 열었다.

“현재까지 확인된 병력만 말씀드린 겁니다.”

“……!”

순간, 벽력도왕은 자신의 귀를 의심했다.

일만. 무려 일만이다.

그것도 한낱 오합지졸이 아니라, 한때 대륙을 질타했던 기마 민족의 군세다.

들판에서 태어나, 말안장 위에서 죽는 이들.

‘심지어 그마저도 전부가 아니라면…….’

벽력도왕은 어느새 힘이 들어가 하얗게 물든 주먹을 내려다보았다.

한 손에는 말고삐를, 다른 한 손에는 활과 돌격창을 들고 한 몸이 되어 달려드는 무수한 인마(人馬)의 모습이 벌써부터 눈앞을 스치는 듯했다.

그리고 다음 순간, 가슴 깊숙한 곳에서 차오른 극심한 분노가 그 광경을 뒤덮었다.

“갈(喝)!”

후우웅, 쾅!

막강한 기파(氣波)와 굉음이 뒤섞인다.

거대한 철제 탁자를 일권으로 박살 내며 자리에서 일어난 벽력도왕이 팽철영을, 아니 대회의실 안의 모두를 노려보았다.

“이런 중대한 사안을 노부가 없는 자리에서 결정하려 하다니, 네놈들이 정녕 제정신인 것이냐!”

드드득.

사방을 짓누르는 거인의 힘.

늙은 태상가주의 분노에 대회의실 전체가 태풍이라도 만난 듯이 뒤흔들리던 그때, 팽철영이 불쑥 입을 열었다.

“아버지께 말씀드리기 전에, 각자의 의견을 알아야 했습니다.”

“놈! 가문의 존망이 걸린 일이다!”

가주직을 물려줄 만큼 믿고 있었던 장자의 차분한 모습에도, 벽력도왕의 분노는 좀처럼 수그러들지 않았다.

지금까지 확인된 것만으로도 무려 일만이라니.

앞으로 보름, 아니 당장 며칠 안에 수만의 대군세로 불어난 오랑캐들이 하북 땅에 접어든다면 그때는 걷잡을 수 없다.

“네놈이 어떻게 감히……!”

지독한 배신감. 그리고 실망.

팽철영의 가라앉은 목소리가 귓가를 파고든 것은, 바로 그 순간이었다.

“부디 용서하십시오. 섣부른 판단으로 팽가(彭家)의 피를 흘릴 수는 없었습니다. 단지 그뿐입니다.”

“그게 무슨.”

분노를 이기지 못해 파르르 떨리던 전신이 덜컥 굳는다.

그제야 무언가 이상함을 느낀 벽력도왕은 천천히 모두의 얼굴을 훑었다.

그리고 조금 전 들었던 말에 숨어 있던 기시감의 정체를 깨달았다.

‘놈들이 노리는 건…… 본가가 아니다!’

한 줄기 벼락과도 같이 뇌리를 스친 깨달음.

맞다.

이미 초원의 군세가 하북으로 남하(南下) 중이라면, 이 대회의실에 앉아 있는 사람은 누구도 없을 것이다.

한시라도 빨리 전투에 대비하기 위해 가문은 물론 하북 무림의 전력을 동원하고 있었을 것이다.

‘그렇다면. 설마?’

순간 머릿속을 스친 어떤 생각에, 벽력도왕의 얼굴이 딱딱하게 굳었다.

“산서(山西). 산서성이로군.”

마치 혼잣말처럼 흘러나온 뇌까림에, 팽철영이 조용히 고개를 끄덕였다.

“언제냐. 그 빌어먹을 놈들이 산서성에 발을 디디는 시점이.”

누군가가 무거운 목소리로 대답했다.

“늦어도 칠 주야 후로 예상됩니다.”

“그들은, 태원진가는 이 사실을 알고 있느냐?”

“예.”

팽철영이 나직하게 덧붙였다.

“이미 전투를 준비 중입니다.”

벽력도왕은 신음하며 고개를 들었다. 창밖에 펼쳐진 푸른 하늘은, 어느덧 먹구름으로 가득했다.

중양절까지 열흘도 남지 않은, 어느 날의 일이었다.
```

## Final English reading copy

```markdown
# Chapter 948

Servants and maids hurriedly cleared away the furniture, broken and smashed in every which way.

And amid a scene that looked as if a typhoon had swept through, a group of hulking men glared at one another, breathing hard.

That was what the Thunderbolt Saber King, Peng Cheolhu, saw the moment he entered the Inner Hall’s grand conference room. After grasping the general situation, he looked around and casually said one thing.

“I’ll count to three. No more, no less. If you’re not back in your places by then…”

Whoosh!

Before he’d even finished speaking, dozens of hulking men scattered like the wind, returning to their original places.

All but one.

“You’re here, Father.”

At the greeting from his eldest son, who was already nearing seventy, the Thunderbolt Saber King furrowed his brow.

“You’re awfully late for your morning greeting.”

“I heard you were sleeping soundly…”

“Cut the nonsense. I thought you were finally ready to act like a proper person, so I handed over the Family Head position—and now you’re fighting with your own blood relatives? In this sacred conference room, no less, where we’re discussing matters of vital importance to the family!”

Peng Cheolyeong, the Iron Blood Saber and current Family Head of the Hebei Peng Family, silently endured the booming shout before speaking up.

“It brings back fond memories of when you broke Third Uncle’s left arm. In this sacred conference room, no less, where we were discussing matters of vital importance to the family.”

The Thunderbolt Saber King paused for a moment, then replied in a stern voice.

“That was when I was in my prime.”

“That was last year.”

“…That can’t be right.”

“And that’s not all. The year before, Second Uncle dozed off for a moment during a meeting, so you punched him in the jaw—”

“Now, Family Head!”

Second Uncle cut in sharply, rebuking Peng Cheolyeong for daring to talk back to the Thunderbolt Saber King, his father and Grand Family Head. Then he added,

“It was my shin. I don’t know who got punched in the face, though.”

“I’m sorry. I must have mixed them up. That was probably Fifth Uncle.”

The moment the Thunderbolt Saber King appeared, Fifth Uncle had crumpled into a corner. Now he muttered with sorrowful eyes,

“Right. That was three years ago. I woke up and two days had passed…”

“That’s enough. I get it. Let’s move on.”

Having failed to come out of the exchange with any dignity, the Thunderbolt Saber King shook his head and took the seat of honor.

Fortunately, the sturdy iron chair—provided in keeping with the Hebei Peng Family’s time-honored tradition of throwing punches at the slightest provocation—had survived intact.

“Enough nonsense. Everyone, sit down. First, tell me what was so important you spent two shichen beating each other up and arguing.”

Peng Cheolyeong took the seat beside him and immediately spoke.

“Something’s wrong in the north.”

“The north? Why would the Murong Family suddenly be acting strange?”

It was only natural that the Thunderbolt Saber King brought up the Murong Family.

For the Hebei Peng Family, the north had always meant the Murong Family.

The descendants of the Xianbei, whose ancestors had proclaimed themselves kings of a nation centuries ago, ruled Liaoning Province—the true frontier—and had long since secured their place among the Five Great Families.

“There’s no way anything’s wrong with the Murong Family. You must have heard bad information somewhere.”

The Thunderbolt Saber King waved the idea away as if it weren’t even worth hearing out. But at Peng Cheolyeong’s next words, his expression hardened.

“I wasn’t talking about the Murong Family.”

“What?”

If it wasn’t the Murong Family, there was only one place left.

The real north. A land of outlaws even more lawless than the Murim, where hidden schemes and blades lurked at every turn.

“Don’t tell me… you mean those barbarian bastards from the grasslands?”

“Yes.”

Peng Cheolyeong, considered the mildest of the Hebei Peng Family by blood, continued in a calm voice.

“The rumors we’ve been hearing are troubling.”

“They’re a vicious lot to the bone, but things have been quiet for the past few years, haven’t they?”

What the Thunderbolt Saber King said was true.

More precisely, peace and prosperity had begun to settle over the grasslands about two years ago, after ages of unceasing conflict.

And at the center of it all was the Jin Family of Taiyuan, a rising power in the north.

“I heard there haven’t been any problems since the Jin Family of Taiyuan formed the Seven-Route Army—or whatever they call it—and swept through the place. Am I mistaken?”

“You’re exactly right. They went on a single campaign and pulled out the tooth that had been aching for ages.”

Right after taking control of the Shanxi Murim, the Jin Family of Taiyuan had acted with a speed and boldness that left even the Five Great Families and the Nine Sects and One Gang speechless.

They’d absorbed not only the various sects that had bared their teeth at the Jin Family in the past, but also Escort Bureaus and merchant houses. Then, using that strength, they formed seven military forces and swept across the grasslands.

Neither the mounted bandits who periodically crossed the border to pillage and kill, nor the horse-riding tribes could stand against the Seven-Route Army.

In fact, some of them had even rallied beneath the Jin Family of Taiyuan’s banner and reaped a handsome reward for their victories.

“Temur. Chinggen.”

At the foreign names that slipped from his son’s lips, the Thunderbolt Saber King narrowed his eyes.

Since stepping back from the front lines, he’d devoted himself to martial arts. But he was still, in name and in truth, the Grand Family Head of the Hebei Peng Family.

He remembered the substance of nearly every meeting he occasionally attended, and the names of barbarians whose faces he’d never seen were no exception.

“Those two who joined the Jin Family of Taiyuan and became Great Chieftains. Is that right?”

“Yes. I hear they’re called ‘khans’ on the grasslands.”

“Khan or con, I don’t care. What matters is what those bastards are up to.”

The Thunderbolt Saber King tapped the table with fingers like iron rods, lost in thought.

Temur and Chinggen.

Thanks to their alliance with the Jin Family of Taiyuan, those two had risen to power on the grasslands. If they were acting suspiciously, there were two possible reasons.

They weren’t satisfied with what they had and were showing greater ambition.

Or…

“What are the chances they’ve joined hands with Dark Heaven—those bastards I could tear to pieces and still not feel satisfied?”

“It isn’t certain yet.”

Peng Cheolyeong added quietly,

“But the circumstances suggest they’ve conspired with Dark Heaven.”

The Thunderbolt Saber King let out a low groan to himself.

*Well, those bastards wouldn’t suddenly pull something like this unless they’d lost their minds. Especially when they know full well that Fire King, that crazy old man, is planted right behind the Jin Family of Taiyuan.*

Everyone knew about the relationship between Fire King Jeok Cheongang and the Jin Family of Taiyuan.

There were plenty of rumors that Temur and Chinggen had even betrayed some of their own people to join hands with the Jin Family of Taiyuan and build their current strength, all because they feared the Fire King.

*And now they’re going to stab him in the back like this? It makes no sense.*

Fire King Jeok Cheongang was hellfire itself.

Hellfire that only died down after turning everything to ash.

The Thunderbolt Saber King was prouder than anyone, but the thought of truly becoming Jeok Cheongang’s enemy was enough to make him uneasy.

*They’ve got someone backing them. No doubt about it.*

The Thunderbolt Saber King kept that thought to himself as he stared intently at his eldest son.

“You must have a reason for thinking that. What’s your evidence?”

“About two years ago, we placed trustworthy people on the grasslands.”

“Informants… You put some thought into it.”

“The situation on the grasslands was still unstable then. We took advantage of the new trade routes opening up.”

Opening the trade routes meant opening the way for people, too.

And after the Seven-Route Army’s campaign, led by the Jin Family of Taiyuan, the new trade routes across the grasslands had carried more than refined ceramics and jewelry.

People.

New kinds of people, never before seen on the grasslands, which had long been a lawless region.

Some of those who filled the vacuum there included informants from the Hebei Peng Family.

“Recently, a few of them sent word that the barbarians on the grasslands are gathering.”

“How many?”

“At least ten thousand.”

“…What? Ten thousand?”

“Father.”

Peng Cheolyeong struggled to speak at the sight of the Thunderbolt Saber King staring at him, eyes wide.

“That’s only the number of troops confirmed so far.”

“…”

For a moment, the Thunderbolt Saber King thought he’d misheard.

Ten thousand. A full ten thousand.

And not some rabble, but the forces of a horse-riding people who’d once thundered across the continent.

Men born in the open fields and destined to die in the saddle.

*And if even that isn’t all of them…*

The Thunderbolt Saber King looked down at his fist, clenched so tightly it had turned white.

He could almost see countless riders charging as one, reins in one hand and bows and lances in the other.

And then, the sight was swallowed by the fury that welled up from deep in his chest.

“Enough!”

Whoom! Crash!

A powerful burst of energy and a thunderous boom rang out together.

The Thunderbolt Saber King smashed the huge iron table with a single punch and rose to his feet, glaring at Peng Cheolyeong—or rather, everyone in the conference room.

“Are you all out of your minds? You were going to decide something this important without me present!”

Rumble.

The force of a giant pressed down from all sides.

The Grand Family Head’s anger shook the entire conference room as if a typhoon had swept through. That was when Peng Cheolyeong abruptly spoke.

“I needed to hear everyone’s opinions before telling you.”

“You fool! The fate of the family is at stake!”

Even with his eldest son standing calm and composed—the very son he’d trusted enough to hand over the position of Family Head—the Thunderbolt Saber King’s anger showed no sign of easing.

Ten thousand already confirmed.

If tens of thousands of barbarians swelled into a massive army and entered Hebei within fifteen days—or even just a few days—there’d be no stopping them.

“How dare you…”

Bitter betrayal. Disappointment.

Peng Cheolyeong’s subdued voice cut into the Thunderbolt Saber King’s ears at that very moment.

“Please forgive me. I couldn’t risk Hebei Peng Family blood being spilled over a hasty decision. That’s all.”

“What are you…”

His whole body had been trembling with rage. Now it abruptly went still.

Only then did the Thunderbolt Saber King sense that something was off. He slowly looked around at everyone’s faces.

And he realized why the words he’d just heard had seemed so familiar.

*What they’re after… isn’t our family!*

The realization struck his mind like a bolt of lightning.

That was right.

If the grassland forces were already heading south toward Hebei, no one would be sitting in this conference room.

The family would have mobilized not only its own forces, but the strength of the Hebei Murim as well, and everyone would be preparing for battle as quickly as possible.

*Then… could it be?*

At a thought that flashed through his mind, the Thunderbolt Saber King’s face went rigid.

“Shanxi. It’s Shanxi Province.”

Peng Cheolyeong quietly nodded at the words, spoken almost as if to himself.

“When will those goddamn bastards set foot in Shanxi Province?”

Someone answered in a heavy voice.

“We expect them no later than seven days from now.”

“Do they—the Jin Family of Taiyuan—know about this?”

“Yes.”

Peng Cheolyeong added quietly,

“They’re already preparing for battle.”

The Thunderbolt Saber King groaned and lifted his head. The blue sky outside the window was now filled with dark clouds.

It was a day with fewer than ten days left until the Double Ninth Festival.
```
