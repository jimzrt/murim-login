<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1000.txt",
      "sha256": "a609b46d7ec394cf4f10a8f796b46f1a1ca910ae1628a52dbdf670d787f3d764",
      "bytes": 13073
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e22160428d9d2a3347073b08e78fd0751a9291d0c949ef359fcf6871bda0f39b",
      "bytes": 1818
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "75accbef85394997549f8a1b2304f7e817ba65c0fe506e445e2c62939e8883e8",
      "bytes": 759
    },
    {
      "path": "characters/Gong Iljung.md",
      "sha256": "2c83e711bac4c22e310292542084abb263a1470d4a9ab30dcdcef8f36be20d30",
      "bytes": 466
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "18bf71735988d2ebcbd12cfa2a7ccd1739afceba2237ecafe08c4518cb49defd",
      "bytes": 629
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8a1e491ad3b6252152692a5eb6df76f9be53e86c2eeb175cbd6f36b8c25ffb38",
      "bytes": 1391
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "ff9d59cc04d80cbb9a348f587e82e221575da96c51f14abb9ef545e2ce18ebf8",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "7613c974ee97c90f939882bee9c23140b6969e1db2b49d04e254bb8beeb8ba25",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "6123d96e8aa8da2795e7d9ed3a98cb2de4659b68c1be850ce24210ff75e543a5",
      "bytes": 964
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "790239a451658191cc4e990511561693c467c61bfbe7d1d60a72e0e22b5c9b40",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f79dcde740735d23b6b5db059d53d356f4090c7c7930971fc6d7da9b59a7c8f",
      "bytes": 274208
    }
  ],
  "estimated_tokens": 11410
}
-->

# Durable State Update — Chapter 1000

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
1 and safe_through 1000. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1000. Profile updates may replace only one
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
  "chapter": 1000,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1000,
    "continuity_sources": [1000],
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
    "Taekyung’s group has reached the Shaanxi–Gansu border after three days overland and plans to check Gansu before continuing to Qinghai.",
    "Dark Heaven’s army is reportedly advancing beyond the desert, but its destination is unknown; Qinghai, Gansu, and Tibet are possible routes into the Central Plains.",
    "Dark Heaven’s Moving Formations could transport forces into the Central Plains; their number and locations are unknown, and neutralizing them would require time and manpower.",
    "The Demon-Sealing Formation may be able to neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.",
    "The Nanman Beast Palace accepted the Murim Alliance’s request and is defending Sichuan alongside the still-intact Qingcheng and Emei.",
    "Zhongnan’s party, led by Sect Leader Gong Iljung and including Song Il and Hwangbo Eom, is traveling near the Shaanxi–Gansu border; Taekyung and Jeok suspect the two elders have delayed the group.",
    "Jeok Cheongang has regained a middle-aged appearance and youth.",
    "Zhongnan sent only three hundred of its reported thousand reinforcements to Shanxi, and they arrived a day after the fighting ended."
  ],
  "continuity_sources": [
    998,
    999
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?",
    "Why have Song Il and Hwangbo Eom been holding Zhongnan’s party back?"
  ],
  "safe_through": 999,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 공일중    | **Gong Iljung**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장문인    | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 보상               | **Reward**                     |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 오왕전 | **Five Kings Hall** | Organization containing five of the Ten Kings. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 적천강 | 공일중 | senior_martial_master_to_sect_leader | you; man with the sycophant's beard | blunt and insulting | Jeok mocks Gong's beard and dismisses the title Wind-and-Cloud Sword Lord. |
| 주화란 | 황보엄 | visitor_to_Zhongnan_senior_martial_uncle | Great Hero Hwangbo | formal-deferential | Ju Hwaran formally introduces herself to Hwangbo Eom as the Taeeul Merciless Sword. |
| 황보엄 | 주화란 | Zhongnan senior to Yongbong Young Bureau Head | you | cold, commanding, and manipulative | Uses 자네 while ordering Hwaran to open the casket and demanding compensation. |
| 황보엄 | 적천강 | rival_martial_masters | Fire King Jeok Cheongang | cold and taunting | Reveals that he knows Jeok's illness and threatens to settle his bad blood with the Fire Gate Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 공일중 | 적천강 | Zhongnan Sect Leader to renowned senior martial master | Great Hero Jeok | formal and deferential | Gong respectfully greets Jeok as 적 대협. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 996
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Gong Iljung.md

# Gong Iljung (공일중)

- **Safe through:** Chapter 999
- **Aliases:** Wind-and-Cloud Sword Lord
- **Role:** Current Sect Leader of the Zhongnan Sect and bearer of the Wind-and-Cloud Sword Lord title
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Gong Ilhyuk's father's cousin; Senior Brother of the Roaring Fury Swordsman.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 999
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il is his only Senior Brother, the current Sect Leader is his martial brother, and Hyuk Sopyung is his junior.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 999
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 999
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 998
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 999
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 996
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1000화



아마도 노호검객과 태을무정검이 그 시점에서 띠꺼운 티를 냈다면, 혹은 근질거리는 손을 참지 못하고 검파(劍把)를 만지작거리기 시작했다면 심각한 불상사가 일어났을지도 모른다.

나야 둘째 치더라도, 당장 적천강은 그런 꼴을 가만히 두고 볼 위인이 아니니까.

그리고 종남파의 장문인인 풍운검군 공필. 아니, 공일중 역시 이와 같은 우려를 품고 있었다.

― 이보게, 진 도우. 이대로 보고만 있을 셈인가?

귓가를 파고드는 나직한 전음(傳音).

동시에 소리의 파동을 감지한 적천강의 눈썹이 꿈틀거린 바로 그 순간이었다.

“저희가 어찌해야…… 용서하시겠습니까.”

나는 물론이고 모두가 눈을 크게 떴다.

이유?

간단했다.

생각지도 못한 인물에게서, 생각지도 못한 한 마디가 흘러나왔기 때문이었다.

노호검객 송일. 그다.

자존심이 강한 것을 넘어 오만하기까지 한 저 노도사가, 굳게 닫혀 있던 입술을 열어 용서라는 단어를 입에 담았다.

게다가 노호검객이 앞서 언급한 ‘저희’라는 대명사에는, 또 다른 한 사람 역시 포함된 것이었다.

“지난 몇 달간 수없이 생각했다. 지금껏 빈도가 저질렀던 과오(過誤)에 대해서, 그리고 그 결과에 대해서.”

태을무정검 황보엄.

노호검객과 함께 풍운검군의 둘밖에 없는 사형이자, 현 종남파의 최고 배분인 그가 나를 응시하며 말을 이었다.

“빈도의 잘못이었다. 결코 부정할 수 없는.”

침잠하게 가라앉는 눈빛. 파르르 떨리는 목소리.

그런 그의 모습을 말없이 지켜보던 나는 불쑥 입을 열었다.

“지금 하신 그 말씀, 진심입니까?”

“빈도의 진심을, 의심하는 것이냐?”

“그럴 리가요.”

크게 숨을 삼킨 내가 덧붙였다.

“믿습니다. 동시에 저 역시 지난날의 좋지 않은 기억을 잊겠습니다. 그날 벌어졌던 분란에 제 잘못 역시 없다고는 할 수 없으니.”

침착한 대답에 모두가 눈을 크게 떴다. 특히 나라는 사람에 대해 잘 아는 이들은 그 놀라움이 특히 더했을 것이다.

당장 나만 해도 입술 사이로 흘러나오는 목소리가 남의 것처럼 낯설게 느껴질 지경이었으니.

그러나 동시에 새어 나간 또 다른 목소리는 달랐다.

그것이야말로 내가 모두의 앞에서 소리 내어 말하지 못한 진심이었으니까.

― 못 믿겠습니다. 아니, 안 믿습니다.

― ……!

― 만약 황보 대협께서 진심으로 반성하셨다면, 조금 전까지 보였던 모습들이 설명이 안 됩니다. 이게 무슨 뜻인지는 두 분께서도 잘 아시리라 생각됩니다만.

전음을 흘려보낸 나는 담담한 시선으로 노호검객과 태을무정검을 바라보았다.

말 몇 마디에 이를 악물고, 주먹을 부르르 떨었던 그들의 모습을 잊기에는 촌각이라는 시간이 너무나도 짧았다.

또한 그와는 반대로 저들이 지금의 이 자리에 두 발로 서 있기까지 걸린 시간은, 실로 길고도 고통스러웠을 것이다.

‘앙금이 남아 있겠지. 분명히.’

마음속의 그 앙금을 완전히 지우고 없애라는 것이 아니다.

사람은 쉽게 변하지 않는다.

나도, 저들도 마찬가지다.

다만 지금은 서로 간의 악연을 덮고 나아가야 하는 시점이었고, 이는 모두가 아는 사실이었다.

― 무슨 대답을 원하는 것이냐.

― 진심을 원합니다. 다른 누군가에게 보여 주고 들려주기 위한 것이 아닌, 온전하고도 진실 된 생각을.

― ……!

― 이해까지는 필요 없습니다. 다만 자신의 마음을 인정하고 상대와의 간극을 받아들여야 비로소 손을 잡을 수 있습니다. 두 분께서도 이미 잘 알고 계실 텐데요.

침묵이 길어지면 주위의 의심을 사는 법.

찰나의 고요 속에서 서로를 바라보던 두 노도사는 우리를 향해 포권을 취했다.

“나 송일, 과거 태원진가에 저지른 무례를 고개 숙여 사죄하겠소.”

“잠시 도사의 본분을 잊고 용봉표국을 위험에 빠트린 점, 부디 용서해 주길 바라오. 향후 빈도가 할 수 있는 최선을 다해 재차 사과하고 보상할 것을 약속하지.”

노호검객은 나에게, 태을무정검은 주화란에게 고개를 숙였다.

그리고 이 놀라운 광경을 지켜본 종남파의 제자들의 반응은 제각각이었다.

누군가는 분한 듯 입술을 깨물었고, 누군가는 옅은 미소를 입가에 띄웠으며, 사문의 존장(尊丈)들이 외부인에게 사과하는 모습을 차마 똑바로 보지 못하고 모른 척 눈을 감거나 시선을 돌리는 이 또한 있었다.

하지만 그들 중 대부분은 몰랐을 것이다.

오랫동안 다른 이에게 굽히지 않았던 탓에 뻣뻣하기 그지없는 그 고갯짓이, 미세하게 달싹이는 입술을 감추었음을.

― 그래, 그 말이 옳다. 한 번 이어진 악연은 그리 쉽게 지울 수 없지. 그렇게 말하는 너 또한 우리와 크게 다르지 않음을 알고 있느니라.

― 하나 지금은 힘을 모아 대적(大敵)과 맞서 싸워야 할 때. 그렇기에 빈도들은 대 종남파의 일원으로서, 무림의 명숙으로서 천하를 위해 싸우고자 하니 단지 그뿐이다.

동시에 양쪽 귓가로 전해져 오는 전음.

그리고 이것이 저들의 온전한 진심이라면, 나로서는 거부하지 않을 이유가 없다.

저벅.

종남파와 맞닥트린 직후, 처음으로 말안장에서 내린 내 눈짓을 따라 주화란 역시 땅을 밟고 섰다.

그 후?

우리는 두 노도사를 향해 포권을 취했다.

그 누구도 흠잡을 수 없을 정도로 공손하게.

그리고 의미를 알 수 없는 묘한 미소를 머금은 채, 그런 내 모습을 말없이 지켜보던 적천강이 풍운검군을 향해 어깨를 으쓱해 보였다.

“좋은 게 좋은 거지. 안 그런가? 풍운검군 공일중.”

부드럽게 마무리된 상황 속, 십 년 감수한 표정을 짓고 있던 풍운검군이 한숨을 내쉬었다.

“필중. 공필중라고 제가 벌써 몇 번을 말씀드렸…….”

“공필중? 공일중 아니었나?”

“……?”

“……?”

“아.”

“뭐가 문제지?”

그제야 뭔가 이상함을 알아차린 풍운검군이, 이내 귀신에 홀린 듯한 얼굴로 고개를 절레절레 흔들었다.



* * *



험악했던 분위기는 처음 잠시뿐이었다.

상황이 좋은 방향으로 일단락되자, 적천강의 현란한 개명신공에 잠깐 혼란스러워하던 풍운검군이 먼저 화두를 꺼냈다.

“어디로 향하시던 중인지 여쭈어봐도 되겠습니까?”

그리고 적천강은 단호하게 대답했다.

“물론 안 되지.”

“예?”

“노부가 아니라 다른 놈에게 묻게. 지금의 나는 단순히 동행을 자처한 빈객일 뿐이지, 좌장(座長)은 따로 있어.”

적천강이 누군가. 바로 그 화왕이다.

무림맹과 함께 새롭게 창설된 오왕전(五王殿)의 수장이기도 한 그가 단지 빈객이라니.

웃기지도 않는 이야기였지만 잠자코 고개를 끄덕인 풍운검군은 내게 다가왔다.

적천강이 그렇다면 그런거고, 아니라면 아닌 거다.

종남파라는 거대 방파의 수장인 만큼, 그는 적천강의 대답을 제자에게 힘을 실어 주기 위한 스승의 깊은 마음으로 해석했다.

물론 내 생각은 달랐지만.

“적 대협께서 자네를 많이 아끼시는군.”

“많이 귀찮으셨나 보네요.”

“……?”

“별로 친하지도 않은데 자꾸 말 걸면 싫어하십니다. 앞으로 반나절 동안은 어느 정도 거리를 두고 떨어져 계세요.”

“……!”

“괜히 오해하실까 봐 드리는 말씀인데, 지금 이거 농담 아닙니다.”

이게 실화인가 하는 표정으로 나와 적천강을 번갈아 보던 풍운검군이 떨떠름하게 대답했다.

“친절한 조언 고맙군.”

“별말씀을요.”

“더불어 일파의 장문인으로서 차마 공개적으로 말은 못 하겠지만, 다른 문제에 대해서도 고맙게 생각하네.”

다른 문제라.

실로 모호한 표현이었지만, 알아듣는 데에는 무리가 없었다.

분명 두 사형과의 분란을 원만하게 마무리한 것에 대한 나름의 감사 표현일 것이다.

“굳이 저한테까지 이러지 않으셔도 됩니다. 솔직히 말씀드리자면……. 두 분께서 먼저 말을 꺼내서 해결된 부분도 있고요.”

만약 노호검객이나 태을무정검이 아주 미세한 살기라도 흘렸다면 일이 어떻게 흘러갔을까.

상황이 상황인지라 엄청난 유혈사태까지는 벌어지지 않았겠지만, 나나 적천강이 가만히 두고 보지는 않았을 것이다.

아무리 암천의 칼날이 코앞까지 짓쳐 들었다 해도, 등 뒤에서 찔러 들어오는 비수를 좌시할 수는 없으니까.

“뭐, 덕분에 당장은 일이 어느 정도 마무리됐으니 다행입니다.”

“음. 그건 나로서도 의외였지. 비록 두 분 사형께서 아직 완전히 마음을 푸신 것은 아니겠지만.”

뜻밖이라는 눈빛으로 바라보자, 풍운검군이 피식 실소를 흘렸다.

“왜, 빈도가 모를 줄 알았나?”

“아닙니다. 그냥…….”

“열두 살에 종남에 입문하여 같은 스승님을 모시고, 지금까지 물경 오십 년이 넘는 세월을 함께 했네. 사형들에 관해서는 누구보다 잘 알아. 사제로서, 장문인으로서 더 이상의 말은 아껴야겠지만.”

말하는 것을 들어보니 사형들이 싸질러 놓은 똥을 한두 번 치운 게 아닌 모양이다.

나는 이참에 확실히 짚고 넘어가야겠다는 생각으로 입을 열었다.

“지원군이 제대로 오지 않은 것도 그 때문입니까?”

“……날카로운 질문이군.”

“단지 사실을 알고 싶을 뿐입니다. 추궁하는 것도 아니고요.”

물러섬 없는 내 눈빛에 풍운검군이 옅은 한숨을 내쉬었다.

“누구 한 사람만의 잘못이 아닐세. 당장 빈도만 하더라도 본파의 핵심 주력을 대거 파견할 엄두가 나지 않았으니.”

“그 말씀은.”

“종남의 안위를 염려하여 내린 결정일세. 그로 인해 자네와 태원진가의 심기가 불편해졌다 하더라도 어쩔 수 없는 일이지.”

때로는 직설적이고 담백한 대답이 정답일 때가 있다.

바로 지금처럼.

잠시 생각하던 나는 조용히 고개를 끄덕였다.

“무슨 뜻인가?”

“충분히 알아들었고, 이해했다는 뜻입니다.”

“그럼…….”

“도움을 받는 처지에 감 놓아라 배 놓아라 하는 것도 웃기지 않습니까. 지원군은 굳이 종남이 아니어도 충분했고, 그 이유가 궁금했을 따름입니다.”

“그렇군. 그렇다면 이것으로 된 건가?”

“물론입니다.”

일단은, 이라는 뒷말은 굳이 덧붙이지 않았다.

정마대전 당시 종남파와 남만야수궁 사이에 얽힌 악연의 고리도 구태여 더듬지 않았다.

현재로서는 이게 최선이다.

지금은 나뭇가지가 아니라 숲을 보아야 할 때, 굳이 종남파와 사이가 틀어져서 좋을 건 없었다.

‘서쪽을 위협하는 암천의 대군을 상대하기 위해서는, 종남파의 힘이 반드시 필요하니까.’

당장 이 자리에 있는 초절정 고수만 무려 셋.

게다가 저들이 이끄는 종남파의 제자들은 얼핏 보기에도 본산(本山)의 정예들로 채워져 있다.

이는 저들 역시 곧 벌어질 대전투에 최선을 다하겠다는 의미.

지난날의 악연은 기억하되, 계속해서 되새기지 않는 것이 올바른 판단이다.

그리고 지금의 이 판단이, 모두를 좋은 방향으로 이끌었으면 했다.

그래야만 며칠 내내 이어진 강행군 속, 짧은 휴식을 끝마치고 자리에서 일어나고 있는 화룡각 대원들을 멀쩡하게 고향으로 되돌려 보낼 수 있을 테니까.

‘아니, 저 중에 두 명은 이미 고향으로 돌아가고 있지.’

내가 잠시 상념에 빠져 사마표와 태산을 바라보던 그때.

풍운검군이 입을 열었다.

“하여, 어디로 갈 생각인가? 이미 우리를 앞질러 간 화산파가 그랬듯이 청해? 아니면…….”

“감숙. 감숙으로 갑니다.”

뒤이어 종남파가 어디로 향할지 물어보려던 나는, 굳이 대답을 듣지 않아도 된다는 것을 깨달았다.

확연히 밝아진 풍운검군의 낯빛은, 그들의 행선지가 우리와 같음을 알려 주고 있었으니까.
```

## Final English reading copy

```markdown
# Chapter 1000

If the Roaring Fury Swordsman and the Taeeul Merciless Sword had shown even a hint of displeasure at that moment—or if they’d been unable to keep their itching hands still and started fiddling with their sword hilts—something serious might have happened.

Me aside, Jeok Cheongang was not the sort of man to stand by and let that happen.

And the Zhongnan Sect Leader, the Wind-and-Cloud Sword Lord Gong Pil—no, Gong Iljung—shared that concern.

—Tell me, Friend Jin. Are you just going to watch?

A low voice slipped into my ear through Sound Transmission.

At the same moment, Jeok Cheongang’s brow twitched as he sensed the sound waves.

“Is there anything we can do to earn your forgiveness?”

Everyone’s eyes widened. Mine included.

Why?

Simple.

Someone we never expected had said something we never expected to hear.

The Roaring Fury Swordsman, Song Il.

The arrogant old Daoist, a man whose pride went beyond mere stubbornness, had opened his tightly sealed lips and spoken the word *forgiveness*.

And the “we” he’d mentioned included another person, too.

“I’ve thought about it countless times over the past few months. About the mistakes I’ve made, and about what came of them.”

The Taeeul Merciless Sword, Hwangbo Eom.

Along with the Roaring Fury Swordsman, he was one of the Wind-and-Cloud Sword Lord’s only two Senior Brothers, and the highest-ranking member of the Zhongnan Sect. He looked at me as he continued.

“It was my fault. There’s no denying it.”

His gaze sank. His voice trembled.

I watched him in silence, then suddenly spoke.

“Did you mean what you just said?”

“You doubt my sincerity?”

“Of course not.”

I drew a deep breath before adding,

“I believe you. At the same time, I’ll put the unpleasant memories of the past behind me. I can’t say I was blameless in the trouble that happened that day, either.”

Everyone’s eyes widened at my calm reply. The people who knew me well were probably the most surprised.

Even I found the voice coming out of my mouth so unfamiliar that it felt like someone else’s.

But another voice slipped out at the same time—and that one was different.

It was the truth I couldn’t say aloud in front of everyone.

— I don’t believe you. No, I won’t believe you.

— …!

— If Great Hero Hwangbo truly regretted what he did, I can’t explain what we saw just a moment ago. I think you both know what I mean.

I sent the Sound Transmission and looked calmly at the Roaring Fury Swordsman and the Taeeul Merciless Sword.

Only moments had passed since they’d clenched their teeth and trembled with their fists balled tight. That wasn’t long enough to forget.

And yet it must have been a long, painful road for them to stand here on their own two feet.

*There’s still resentment. Of course there is.*

I wasn’t telling them to erase it completely.

People don’t change easily.

Not me. Not them.

But this was the moment to set aside the bad blood between us and move forward. Everyone knew that.

— What answer do you want from us?

— The truth. What you genuinely think—not something meant to be shown or said for someone else’s benefit.

— …!

— You don’t have to understand each other. But you have to acknowledge what you feel and accept the distance between you before you can join hands. I think you both know that already.

Silence that lasted too long would invite suspicion.

In the brief hush, the two old Daoists looked at each other, then clasped their hands toward us.

“I, Song Il, bow my head and apologize for the disrespect I showed the Jin Family of Taiyuan.”

“Please forgive me for forgetting my duty as a Daoist and putting the Yongbong Escort Bureau in danger. I promise to apologize again and make amends to the best of my ability.”

The Roaring Fury Swordsman bowed to me. The Taeeul Merciless Sword bowed to Ju Hwaran.

The Zhongnan Sect Disciples who witnessed the astonishing sight reacted in all sorts of ways.

Some bit their lips as if they were angry. Some wore faint smiles. Others couldn’t bear to watch their elders apologize to outsiders, so they closed their eyes as if they hadn’t seen it or turned away.

But most of them probably didn’t notice that the elders’ stiff, unpracticed bows hid the slight movement of their lips.

—Yes, you’re right. Bad blood doesn’t disappear so easily once it’s there. And I know that you, who say so, aren’t much different from us.

—But now is the time to gather our strength and face our great enemy. That is why we, as members of the great Zhongnan Sect and respected masters of the Murim, will fight for the world. Nothing more.

Their Sound Transmissions reached both my ears.

And if those were their genuine feelings, I had no reason to refuse.

Step.

For the first time since we’d come face-to-face with the Zhongnan Sect, I dismounted. Ju Hwaran followed my cue and set her feet on the ground.

Then?

We clasped our hands toward the two old Daoists.

As respectfully as anyone could.

Jeok Cheongang watched me in silence, a curious smile on his face. Then he shrugged at the Wind-and-Cloud Sword Lord.

“Let bygones be bygones. Right, Wind-and-Cloud Sword Lord Gong Iljung?”

The Wind-and-Cloud Sword Lord had looked like he’d just aged ten years. Now, as the situation came to a gentle close, he let out a sigh.

“Piljung. I’ve told you several times already, it’s Gong Piljung…”

“Gong Piljung? Wasn’t it Gong Iljung?”

“…?”

“…?”

“Ah.”

“What’s the problem?”

Only then did the Wind-and-Cloud Sword Lord realize something was off. He shook his head as if he’d seen a ghost.

* * *

The tense atmosphere had lasted only a little while at the start.

Once things had settled in a good direction, the Wind-and-Cloud Sword Lord—briefly thrown into confusion by Jeok Cheongang’s dazzling name-changing skill—was the first to bring up a subject.

“May I ask where you’re headed?”

Jeok Cheongang answered flatly.

“Of course not.”

“Pardon?”

“Ask someone else. I just tagged along as a guest. Someone else is in the presiding chair.”

Who was Jeok Cheongang? The Fire King himself.

He was also the head of the Five Kings Hall, newly established alongside the Murim Alliance. The idea that he was merely a guest was ridiculous.

But the Wind-and-Cloud Sword Lord quietly nodded and came over to me.

If Jeok Cheongang said so, then that was how it was. If he said otherwise, then it wasn’t.

As the leader of a great sect like the Zhongnan Sect, he took Jeok Cheongang’s answer to mean that his Master wanted to give his Disciple the authority to speak.

My thoughts were different, of course.

“Great Hero Jeok cares for you a great deal.”

“You must have bothered him quite a bit.”

“…?”

“He doesn’t like it when people he isn’t close to keep talking to him. Stay some distance away from him for the next half day or so.”

“…!”

“I’m telling you so you don’t misunderstand. I’m not joking.”

The Wind-and-Cloud Sword Lord looked back and forth between me and Jeok Cheongang as if he couldn’t believe what he was hearing, then replied awkwardly,

“Thank you for the kind advice.”

“Don’t mention it.”

“And as Sect Leader, I can’t say this in public, but I’m grateful to you for the other matter, too.”

The other matter.

It was a vague way to put it, but I had no trouble understanding him.

He was clearly thanking me, in his own way, for settling things peacefully with his two Senior Brothers.

“You don’t have to thank me. Honestly… the two of them were the ones who brought it up, and that helped resolve things.”

What would have happened if even the slightest killing intent had slipped from the Roaring Fury Swordsman or the Taeeul Merciless Sword?

Given the situation, it probably wouldn’t have turned into a massive bloodbath. But neither Jeok Cheongang nor I would have stood by and done nothing.

No matter how close Dark Heaven’s blade was to our throats, we couldn’t ignore a dagger coming at us from behind.

“Well, things are more or less settled for now, thanks to them. That’s a relief.”

“Mm. It surprised me, too. Though I doubt my Senior Brothers have entirely let go of their feelings.”

I looked at him in surprise. The Wind-and-Cloud Sword Lord gave a faint, wry laugh.

“What, did you think I wouldn’t know?”

“No. I just…”

“I joined Zhongnan when I was twelve. We served the same Master, and we’ve been together for well over fifty years. I know my Senior Brothers better than anyone. As their Junior Brother and as Sect Leader, I should say no more.”

From the sound of it, he’d cleaned up the mess his Senior Brothers made more than once.

I decided to settle the matter once and for all and spoke up.

“Is that why the reinforcements never really came?”

“…That’s a sharp question.”

“I just want to know what happened. I’m not accusing you.”

The Wind-and-Cloud Sword Lord let out a quiet sigh at my unwavering gaze.

“It wasn’t any one person’s fault. Even I didn’t dare send a large portion of our sect’s main force.”

“Meaning?”

“It was a decision made out of concern for Zhongnan’s safety. If that upset you and the Jin Family of Taiyuan, there was nothing to be done.”

Sometimes a direct, plain answer is the right one.

Like now.

I thought for a moment, then quietly nodded.

“What do you mean?”

“I mean I understand. Completely.”

“Then…”

“Isn’t it ridiculous to tell someone helping you what to do? We had enough reinforcements even without Zhongnan. I was only curious about the reason.”

“I see. Then is that enough?”

“Of course.”

I didn’t bother adding *for now*.

Nor did I bring up the bad blood between the Zhongnan Sect and the Nanman Beast Palace during the Great Faction War.

This was the best we could do at the moment.

Now was the time to look at the forest, not the branches. There was nothing to gain from falling out with the Zhongnan Sect.

*We need Zhongnan’s strength to face Dark Heaven’s army threatening the west.*

There were three Supreme Peak masters here alone.

And the Zhongnan Sect Disciples they led were clearly the elite of the main sect.

That meant they, too, intended to do everything they could in the great battle to come.

It was right to remember the bad blood of the past without constantly dredging it up.

I hoped this decision would lead everyone in a better direction.

That was the only way we could send the Fire Dragon Pavilion members back home in one piece after a short rest—one they were getting up from now, after days of marching without respite.

*Well, two of them are already on their way home.*

I was lost in thought, looking at Sama Pyo and Taishan, when the Wind-and-Cloud Sword Lord spoke.

“So, where are you headed? Qinghai, like the Huashan Sect that passed us earlier? Or…”

“Gansu. We’re going to Gansu.”

I’d been about to ask where the Zhongnan Sect was headed, but realized I didn’t need to.

The Wind-and-Cloud Sword Lord’s face had brightened considerably. That told me they were going the same way we were.
```
