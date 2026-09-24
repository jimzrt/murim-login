<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1021.txt",
      "sha256": "c1e42102c7c4ac1066949110f4372fc9739e348f29720aa46311d90dba2ff106",
      "bytes": 12927
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5a85d11a215e4621ef2359cef56ecf1074bb1e49d8f517ad59a41c27c63d5e36",
      "bytes": 1174
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0dafd418aa393e495962bfa62c9107ec29bc8b93a7018fc838daf88d8b83fce0",
      "bytes": 238757
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "50c353e2d9cb40494112c072f86ef01c23f51df4559c85bc3a90f8da61f42e9f",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6d3bb2d1b6f023f1b9f4ee3aed49ab67023dfd7e742d37f34aebed0683b363bc",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "65a84abd256c3346630c20f5d63c054851af8726cf0a7067e7fdce820c0b149c",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d019732efd6cd1ed9783ed7c81fe56929e7b038196aecbe4e9b697e16fe0619b",
      "bytes": 623
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "1f54eac77e5d258bf53de1024eb0b8a58eb0e7c0d311a36e504dc073d6adc089",
      "bytes": 1005
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "719db6e69a9c330450808cb5be4b20074d43b3c1e4a68398fc7366d7e6080b54",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 11002
}
-->

# Durable State Update — Chapter 1021

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
1 and safe_through 1021. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1021. Profile updates may replace only one
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
  "chapter": 1021,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1021,
    "continuity_sources": [1021],
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
    "Dark Heaven has captured Dunhuang after breaching the Jade Gate Pass, and its army is advancing toward the Great Snow Mountain.",
    "The defense of Dunhuang suffered catastrophic losses; the Kongtong Sect Leader escaped, but his whereabouts and the fate of the other survivors are unknown.",
    "Jin Taekyung ordered all forces in the Qilian Mountains mobilized, overruling Sima Gong’s prior decision.",
    "A secret letter received by Sama Pyo was suspected to have come from Gansu or Qinghai; its sender, contents, and purpose remain unknown.",
    "Taekyung remains unsure whether he would kill Sama Pyo and Taishan if they were acting on Sima Gong’s orders connected to Dark Heaven."
  ],
  "continuity_sources": [
    1019,
    1020
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Are Sama Pyo and Taishan acting on Sima Gong’s orders, and are those orders connected to Dark Heaven?",
    "Where is the Kongtong Sect Leader, and what became of the surviving troops from Dunhuang?"
  ],
  "safe_through": 1020,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 감숙     | **Gansu**              |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 평화 | **Peace Guild** | Guild name. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1020
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1020
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1020
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1020
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1019
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, was Ju Hwaran's former fiancé in a political engagement, and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1020
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1021화



사실, 불과 얼마 전까지만 하더라도 이렇게까지 할 생각은 없었다.

관무불가침(官武不可侵)이라는 말이 괜히 생겨났겠나.

서로를 소 닭 보듯 하는 이 바닥에서 괜히 어느 한쪽의 권위를 내세워 봤자 반감을 사리라는 것은 자명한 사실.

하지만 동시에, 권위라는 것은 적재적소에 내세웠을 때 제법 큰 효력을 발휘하고는 한다.

바로 지금처럼.

“상산후(上山后)…….”

누군가의 입술 사이로 흘러나온 나지막한 침음성이 찰나의 침묵을 깨트린다.

무겁게 가라앉은 분위기 속, 내 손에 들린 호패를 크게 뜨인 눈으로 응시하던 사마공이 입을 연 것 또한 그때였다.

“권유가 아닌, 명령이라.”

모래알처럼 건조한 음성에 이어, 차갑게 식은 그의 시선이 내 얼굴을 향해 움직였다.

“재미있군. 참으로 재미있어.”

말과는 달리 입꼬리가 경직된 사마공의 모습에, 나는 뒤통수를 긁적이며 입을 열었다.

“재미있으셨다니 저도 기쁘긴 한데, 소감보다는 대답을 듣고 싶네요. 아시다시피 현재로서는 일각이 여삼추라.”

“지금 그 대답을, 조금 전 자네가 했던 말이 전부 진심이었다는 의미로 이해하면 되겠나?”

“어라, 혹시 아직도 이해 못 하셨습니까? 희한하네. 이 정도면 충분히 알아듣게 설명한 것 같은데.”

“……!”

“뭐, 정 그러시다면 다시 말씀드리겠습니다. 지금 당장 기련산에 짱박아 놓은 병력들, 밑바닥까지 싹싹 긁어모아서 대설산에 집결시키세요. 이건 상산후로서 내리는 명령입니다.”

수뇌부들 사이에서 헛숨을 삼키는 소리가 흘러나왔다.

흑야왕 사마공이 누구인가.

공동파와 함께 감숙성을 양분하는, 아니 이제는 그보다 더 독보적인 입지를 확보한 일대의 패자다.

아직 뜬구름 잡는 이야기이기는 하지만, 만약 이대로 모든 사태가 수습되고 평화가 찾아온다면 극심한 타격을 입은 공동파는 흑룡마문의 상대가 되지 못할 테니까.

하지만…….

‘그래서 뭐, 어쩌라고.’

나는 담담한 시선으로 사마공을 위시한 수뇌부들을 차례대로 훑었다.

지금 이 순간, 내 눈동자에 비친 그들의 모습은 막중한 책임과 목숨을 짊어진 일파의 영수(領袖)들이 아니라 단순한 도박 중독자와 같았다.

수만 명의 목숨을 건 거대한 도박판에서, 손에 든 골패나 만지작거리는 얼간이들.

권위는 이럴 때 써야 한다.

비록 그것이 극심한 반발과 분란을 초래하더라도.

그리고 바로 그 순간, 수뇌부 중 한 사람이 입을 열었다.

“듣자 하니, 갈수록 도를 지나치는 언행이구려.”

누군가 해서 봤더니 제법 눈에 익은 얼굴이다.

이백여 명 정도의 문도를 거느린, 감숙성에서 방귀깨나 뀐다는 중견 문파의 문주.

수뇌부가 한자리에 모일 때마다 사마공의 지척에 있었기에 다른 이들보다 더욱 낯익은 자이기도 했다.

이를테면, 측근이라고나 할까.

“한 말씀 드리자면, 본인은 석 문주의 말에 동의하는 바요.”

“진 소, 아니 대협께서 지금껏 보여 주신 의협심에 대해서는 경의를 표하지만, 그래도 지켜야 할 도리라는 것이 있지 않겠소이까?”

“비록 작금의 대국 황실이 암천이라는 대적에 맞서 함께하고 있다고는 하나, 그렇다 한들 무림의 일에 열후(列侯)라는 직위까지 앞세워 이리 강압적으로 나오는 것은 좀.”

초록은 동색이고 가재는 게 편이라고, 눈치를 보며 한 마디씩을 얹는 이웃사촌들의 응원 덕분일까.

아니면 이런 상황 속에서도 별다른 말 없이 팔짱을 낀 채 상황을 지켜보는 적천강의 모습 덕분일까.

석씨 성을 쓰는 문주는 한층 용기가 묻어 나오는 목소리로 재차 입을 열었다.

마치 주인의 기분을 살피는 충견처럼, 조용히 침묵을 지키고 있는 사마공을 힐끗 바라보며.

“보시오. 다들 같은 생각이지 않소. 또한 여기 계신 사마 문주께서도 충분히 심사숙고하신 끝에…….”

이쯤 되면 무슨 헛소리를 더 하려고 하는지 자못 궁금해질 지경이었지만, 나는 그리 인내심이 많은 편이 아니었다.

“그래서.”

이어지려는 말을 가로막은 내가 조용히 덧붙였다.

“무슨 문제라도 있습니까?”

말문이 막힌 듯, 가만히 나를 바라보던 예의 문주가 굳은 얼굴로 대답했다.

“있다면, 어쩌시겠소?”

“참으세요.”

“지금…… 뭐라고 했소?”

“더럽고 치사해도 참으시라고. 막말로 기분이 더럽다고 한들 뭐 어쩔 겁니까. 천자, 아니 지엄하신 황제 폐하께서 친히 임명하신 열후가 개좆으로 보여요?”

“그, 그런 뜻이 아니지 않소!”

벌겋게 달아오른 얼굴로 외치는 그의 모습에 나도 모르게 실소가 흘러나왔다.

“아니면 계급장 떼고 한 판 붙으시든지. 내가 폐하께는 비밀로 해 드릴게. 이제야 겨우 무림맹이랑 손잡고 으쌰으쌰 하고 있는데 이런 일 생기면 괜히 서로 안 좋잖아. 응, 안 그래요?”

지금 내 입술 사이로 흘러나오는 음성은 눈앞의 문주를 향하고 있지만, 시선은 아니다.

그리고 나와 눈이 마주친 사마공 역시, 그 사실을 모를 만큼 멍청한 위인이 아니었다.

“인상 깊은 말이로군.”

우두머리가 나서자 삽시간에 쥐죽은 듯이 고요해지는 좌중.

마침내 입을 연 사마공은 의미를 알 수 없는 눈빛으로 나를 바라보았다.

“자네 말이 맞네. 나 역시 대국에 속한 백성 중 한 사람. 황제께서 임명한 열후의 명을 따라야겠지.”

“……!”

“……!”

사람들의 눈동자가 흔들린다.

아마 그들은 사마공이 이토록 순순히 인정할 줄은 몰랐을 것이다.

물론, 나로서는 어느 정도 예상했던 반응이었지만.

“그 말씀은, 제 뜻을 따르겠다는 의미로 이해해도 되겠습니까?”

“그러겠네. 이번에 한해서만큼은 내 한 걸음 양보하지.”

“두 번은 없다는 뜻이군요.”

“어쩌겠나. 곧 죽어도 지켜야 할 체면과 나름대로의 판단이 있으니. 아마 이 정도는 자네나 저기 계신 노 선배께서도 양해해 주시리라 믿네.”

이제는 흐릿하게나마 웃어 보이기까지 하는 사마공의 모습에, 나도 모르게 눈빛이 침잠하게 가라앉았다.

‘이자, 도대체 뭐지?’

뭔가를 숨기고 있는 것이 분명한데, 그 실체가 명확하지 않다. 아니, 좀처럼 엿볼 틈새를 주지 않는다.

‘일부러 강하게 나갔는데도, 별다른 동요가 없다.’

내가 다짜고짜 열후의 권위를 내세워 찍어 누르려 한 것은, 단순히 지금의 상황이 시급하기 때문만은 아니다.

제아무리 무거운 만근거암(萬斤巨巖)이라 할지라도 충격을 받으면 흔들리는 법.

나는 사마공의 반응을 통해 그의 의중을 유추하고자 했다. 이 자리에 모인 수뇌부 중 몇이나 되는 사람들이 사마공과 뜻을 함께하고 있는지도.

하지만 약간의 소득을 얻을 수 있었던 후자와 달리, 전자는 보기 좋게 실패했다.

그리고 정확한 실체가 드러나지 않는 한, 사마공과 나는 한 울타리에 속한 아군이었다.

“앞서 자네가 말했듯이 현재로서는 일각이 여삼추인 듯한데, 뭔가 더 할 말이 남았나?”

나는 잠시 침묵했지만, 허공에서 맞닿은 시선을 통해 읽어 낼 수 있는 것은 아무것도 없었다.

“없습니다.”

“좋네. 하면 즉각 사람을 보내어 기련산의 모든 병력을 끌어오도록 하지. 종남 역시 이에 동의하시는지?”

혼란스러운 눈빛으로 나와 사마공을 번갈아 바라보던 풍운검군이 입을 열었다.

“당장 대설산마저 무너지면 감숙은 풍전등화나 다름 없는 상황. 빈도로서는 동의하지 않을 이유가 없소.”

“그럼 되었구려. 각 가주와 문주들께서는 휘하의 무인들에게 이 사실을 알리고 빈틈없이 준비시켜 주시오. 늦어도 한나절 안에는 놈들보다 앞서 대설산에 도착해야 하니.”

눈치를 살피던 감숙 무림의 영수들이 포권지례를 취하자, 서둘러 다시 말안장에 오르려던 사마공이 문득 걸음을 멈췄다.

그리고 뭔가를 잊고 있던 사람처럼, 나직한 탄성과 함께 나를 향해 고개를 돌렸다.

“아, 한 가지만 부탁해도 되겠나?”

“부탁이라면.”

“잠시 빌려 갔던 내 아들놈을 자네에게 다시 맡길까 하는데, 어떤가?”

그 예상치 못한 제안에 눈을 크게 뜬 그때, 사마공이 너털웃음과 함께 말을 이었다.

“오랜만에 본 혈육이 반가워 며칠이나마 곁에 두었을 뿐. 지금 같은 전시 상황에서 공과 사는 철저히 구분해야 하지 않겠나. 흑룡마문의 소문주이기 이전에, 화룡각의 일원이니. 그렇지 않으냐?”

잠시 망설이던 사마표가 이내 무뚝뚝한 음성으로 대답했다.

“……그렇습니다.”

과연 무슨 속셈일까.

사실 마음속으로는 이미 충분히 사마공의 의도를 짐작하고는 있었지만, 이런 상황에서 결코 내색해서는 안 된다.

나는 최대한 담담한 표정과 어투로 고개를 끄덕였다.

“그런 부탁이라면 당연히 들어드려야죠. 안 그래도 언제쯤 돌아오나 기다리고 있던 참입니다.”

“듣던 중 반가운 소리로군. 그럼 우선은 승낙한 것으로 알고 잠시 후에 후미로 돌려보내도록 하겠네. 당장 무슨 일이 벌어질지도 모르는 마당에, 부자간의 작별 인사는 해야 하지 않겠나.”

빙긋 웃어 보이는 사마공의 모습에서, 나는 믿고 싶지 않았던 짐작을 새삼 확신할 수 있었다.

사마표는 화룡각의 일원이기 이전에, 사마공의 피를 이은 혈육이자 흑룡마문의 소문주라는 것을.

지금부터는 동료가 아닌, 첩자로서 함께하리라는 것을.

‘빌어먹을.’

일그러지는 얼굴을 감추기 위해, 나는 깊게 포권을 취하고 돌아섰다.



* * *



두두두두두!

오천에 달하는 인마(人馬)는 출발과 함께 혼신의 힘을 다해 달려 나갔다.

지진이라도 일어난 듯 대지가 뒤흔들렸고, 굉음과 함께 피어오른 먼지구름은 혹시 모를 이목을 가려 주기에 차고 넘쳤다.

“너를 진태경의 곁에 머무르게 하려는 이유를 알고 있느냐?”

사마공은 물음과 함께 날카로운 눈빛으로 아들의 표정을 살폈지만, 되돌아온 음성은 한 치의 흔들림도 없었다.

“제가 어찌하길 바라십니까?”

“짐작하는 그대로다. 저들의 일거수일투족을 지켜보는 것.”

“어려운 임무로군요.”

“어찌하여 그리 생각하느냐?”

“괜한 의심을 받아서는 안 되니까요.”

이미 명령을 받아들인 사마표의 대답에, 사마공은 내심 만족스럽게 웃었다.

이유를 묻지 않고, 의문을 품지 않는 것.

이러한 태도야말로 그가 아들에게 바랐던, 동시에 되찾기를 바랐던 모습이었다.

“왜 이런 명령을 내리는지 궁금하지는 않으냐?”

“그저 명을 따를 뿐입니다. 필시 본문을 위한 일일 테니까요.”

망설임 없는 대답을 들은 사마공의 입가에 흐릿한 미소가 맺혔다.

“그래, 맞다. 전부 우리 일가(一家)와 흑룡마문의 부흥을 위한 것이다. 그리고 머지않아 모두 네 것이 될 테지. 그때는 명실상부한 감숙성의 패자요, 중원까지 진출할 수도 있을 것이다.”

“그 말씀은…….”

작게 말꼬리를 흐리는 아들의 모습에, 아버지는 작게 고개를 끄덕였다.

“한 산에 두 마리의 호랑이가 존재할 수는 없는 법.”

“……!”

“당초에 예상했던 것과는 달리 일이 틀어졌으나, 달라지는 것은 없다. 어떤 훼방이 있더라도, 우리는 원하는 것을 얻게 될 것이다.”

언제나 그렇듯이.

나직하게 덧붙인 뒷말이 바람에 파묻혀 사라진다. 야망으로 번뜩이는 아버지의 모습을 말없이 지켜보던 아들은 공손한 포권지례와 함께 말고삐를 돌렸다.

조금 전, 사마공이 진태경에게 말했던 애틋한 부자간의 인사는 없었다.

언제나 그렇듯이.
```

## Final English reading copy

```markdown
# Chapter 1021

The truth was, until just a little while ago, I hadn’t planned to go this far.

The rule that officials and martial artists must not interfere with each other hadn’t come from nowhere.

In a world where the two sides barely spared each other a glance, it was obvious that flaunting either side’s authority would only breed resentment.

But at the same time, authority could be remarkably effective when used in the right place.

Like right now.

“Marquis of Shangshan…”

A low groan slipped from someone’s lips, breaking the brief silence.

In the heavy, sunken atmosphere, Sima Gong stared wide-eyed at the identity tablet in my hand. It was then that he spoke.

“So this isn’t a request. It’s an order.”

His voice was dry as sand. Then his gaze, gone cold, shifted to my face.

“How interesting. Truly interesting.”

Despite his words, the corners of his mouth were stiff. I scratched the back of my head and spoke.

“I’m glad you find it interesting, but I’d rather hear your answer than your opinion. As you know, every fifteen minutes feels like three autumns right now.”

“Am I to understand that you mean every word you said a moment ago?”

“Oh? You still don’t understand? That’s strange. I thought I’d explained it clearly enough.”

“……!”

“Well, if you insist, I’ll say it again. Gather every last soldier you’ve got holed up in the Qilian Mountains and bring them to the Great Snow Mountain right now. That’s an order from the Marquis of Shangshan.”

A stifled gasp went around the leadership.

Who was Sima Gong, the Black Night King?

He was a ruler who shared Gansu Province with the Kongtong Sect—or rather, one who now held an even more dominant position than they did.

It was still only speculation, but if things were settled and peace returned, the Kongtong Sect, having suffered such severe losses, wouldn’t be able to stand against the Black Dragon Demon Gate.

But…

*So what?*

I calmly surveyed Sima Gong and the other leaders, one by one.

At that moment, the people before me didn’t look like the heads of factions shouldering immense responsibility and tens of thousands of lives. They looked like gambling addicts.

Fools, fiddling with their tiles at a vast gambling table where tens of thousands of lives were at stake.

This was when you used authority.

Even if it brought fierce opposition and discord.

And right then, one of the leaders spoke.

“I hear your words and conduct have been getting more and more out of line.”

I looked to see who it was. His face was fairly familiar.

The Sect Leader of a mid-sized sect with around two hundred disciples, someone who carried a fair amount of weight in Gansu.

He’d been at Sima Gong’s side whenever the leadership gathered, which made him more familiar to me than the others.

A close ally, you might say.

“I’ll say this much: I agree with Sect Leader Seok.”

“Young Hero Jin—no, Great Hero Jin—I respect the sense of justice you’ve shown us until now, but surely there are certain principles we must uphold.”

“Although the Great Nation’s imperial court is now standing with us against the great enemy Dark Heaven, that doesn’t mean you should invoke your title as a marquis to strong-arm us like this over Murim’s affairs.”

Birds of a feather flock together; crabs side with crabs. Maybe it was the support of the neighbors, each adding their own word while watching the room. Or maybe it was because Jeok Cheongang stood there with his arms crossed, quietly watching without saying a thing.

Whatever the reason, Sect Leader Seok sounded bolder when he spoke again. Like a loyal dog checking his master’s mood, he stole a glance at the silent Sima Gong.

“Look. Everyone feels the same way. And Sect Leader Sima here has given this plenty of thought…”

At this point, I was almost curious what nonsense he’d say next. But I wasn’t very patient.

“So?”

I cut him off, then added quietly,

“Is there a problem?”

The Sect Leader stared at me in silence, as though he’d been struck dumb. Then, his face stiff, he replied,

“And if there is?”

“Put up with it.”

“What… did you just say?”

“Put up with it, even if it feels dirty and unfair. What are you going to do about it, even if it pisses you off? Does a marquis appointed by the Son of Heaven—no, by His August Majesty the Emperor himself—look like jack shit to you?”

“T-that’s not what I meant!”

His face flushed as he shouted. A laugh slipped out of me before I could stop it.

“Then take off your rank badge and fight me. I’ll keep it a secret from His Majesty. We’ve only just managed to join hands with the Murim Alliance and work together. It’d be bad for both sides if something like this happened now, wouldn’t it? Right?”

The words coming from my lips were directed at the Sect Leader before me. But my gaze wasn’t.

And Sima Gong, whose eyes met mine, wasn’t stupid enough to miss that.

“Those are memorable words.”

As soon as the leader spoke, the room fell silent as a grave.

At last, Sima Gong spoke, looking at me with an expression I couldn’t read.

“You’re right. I, too, am a subject of the Great Nation. I should obey the order of a marquis appointed by His Majesty.”

“……!”

“……!”

Eyes shifted uneasily around the room.

They probably hadn’t expected Sima Gong to agree so readily.

As for me, I’d more or less expected this response.

“May I take that to mean you’ll follow my orders?”

“I will. This time, I’ll be the one to yield.”

“So there won’t be a second time.”

“What can I do? I have my pride, which I must uphold even if it kills me, and my own judgment. I trust you and the Senior over there will understand that much.”

Sima Gong was even managing a faint smile now. Without meaning to, my gaze sank.

*What the hell is this guy?*

He was definitely hiding something, but I couldn’t tell what it was. No—he wasn’t giving me the slightest opening to catch a glimpse.

*I came on strong on purpose, but he barely reacted.*

I hadn’t invoked the authority of a marquis and tried to force him into line simply because the situation was urgent.

Even a massive boulder weighing ten thousand *geun* would shake when struck.

I wanted to infer Sima Gong’s intentions from his reaction. I also wanted to see how many of the leaders gathered here were on his side.

The latter had yielded a little. The former had failed spectacularly.

And until his true intentions came to light, Sima Gong and I were allies under the same banner.

“As you said, every fifteen minutes feels like three autumns right now. Is there anything else you need to say?”

I stayed silent for a moment, but I couldn’t read anything in the gaze we held across the open space between us.

“No.”

“Good. Then I’ll immediately send someone to bring in every force in the Qilian Mountains. Does Zhongnan agree?”

The Wind-and-Cloud Sword Lord had been glancing back and forth between Sima Gong and me, his eyes still unsettled. He opened his mouth.

“If the Great Snow Mountain falls, Gansu will be on the brink. I see no reason to disagree.”

“Then it’s settled. Family Heads and Sect Leaders, inform your martial artists and make sure they’re ready. We must reach the Great Snow Mountain ahead of them within half a day at the latest.”

The leaders of Gansu’s Murim exchanged wary glances, then performed the clasped-fist salute. Sima Gong was hurrying back to his saddle when he suddenly stopped.

As if he’d forgotten something, he gave a quiet exclamation and turned toward me.

“Ah, could I ask one favor?”

“What favor?”

“I’m thinking of entrusting my son to you again. The one I borrowed for a while. What do you think?”

I stared at him in surprise. Sima Gong continued with a hearty laugh.

“I was glad to see a blood relative I hadn’t seen in a long time, so I kept him by my side for a few days. But in wartime, we must strictly separate public duty from private affairs. He’s a member of the Fire Dragon Pavilion before he’s the Young Sect Leader of the Black Dragon Demon Gate. Isn’t that right?”

Sama Pyo hesitated for a moment, then answered in his usual blunt voice.

“……That’s right.”

What was he up to?

Truthfully, I already had a good idea of Sima Gong’s intentions. But I couldn’t let that show—not in a situation like this.

I nodded, keeping my expression and tone as calm as possible.

“If that’s all you’re asking, of course I’ll do it. I’ve been wondering when he’d come back.”

“That’s good to hear. Then I’ll take that as a yes and send him back to the rear shortly. With no one knowing what could happen at any moment, shouldn’t a father and son have a chance to say goodbye?”

At Sima Gong’s faint smile, I found myself newly certain of the suspicion I didn’t want to believe.

Before he was a member of the Fire Dragon Pavilion, Sama Pyo was Sima Gong’s blood relative—and the Young Sect Leader of the Black Dragon Demon Gate.

From now on, he’d be with us not as a comrade, but as a spy.

*Damn it.*

To hide my twisting expression, I gave a deep clasped-fist salute and turned away.

* * *

Thud, thud, thud, thud!

The five thousand men and horses surged forward at full speed the moment they set out.

The earth shook as if there had been an earthquake, and the cloud of dust rising amid the thunderous noise was more than enough to obscure them from any prying eyes.

“Do you know why I want you to stay by Jin Taekyung’s side?”

Sima Gong asked, watching his son’s expression with a sharp gaze. The answer that came back didn’t waver in the slightest.

“What do you want me to do?”

“Exactly what you suspect. Watch their every move.”

“That’s a difficult task.”

“Why do you think so?”

“Because I mustn’t draw needless suspicion.”

Sama Pyo had already accepted the order. Sima Gong smiled inwardly with satisfaction.

To ask no questions. To harbor no doubts.

That was exactly the way he wanted his son to be—and the way he’d wanted him to be again.

“Aren’t you curious why I’m giving you this order?”

“I’ll simply follow your command. It must be for the good of our sect.”

His answer came without hesitation. A faint smile appeared at the corners of Sima Gong’s mouth.

“That’s right. It’s all for the resurgence of our family and the Black Dragon Demon Gate. And before long, it will all be yours. Then you’ll be the undisputed ruler of Gansu Province, and you might even be able to expand into the Central Plains.”

“You mean…”

His son let the words trail off. The father gave a small nod.

“There can’t be two tigers on one mountain.”

“……!”

“Things went awry, unlike what we initially expected, but nothing has changed. No matter what gets in our way, we will get what we want.”

As always.

The words he added quietly were swallowed by the wind. His son watched his father’s eyes gleam with ambition, then turned his horse with a respectful clasped-fist salute.

There was no tender father-son farewell like the one Sima Gong had just spoken of to Jin Taekyung.

As always.
```
