<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0620.txt",
      "sha256": "578713e4553ec13d2a6318bcc0ec261a90ffe0b7fa6253c78863940eb4246fa5",
      "bytes": 12745
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4d23c55d04ca00b352b254a413e8da3e62f29a344c9d7d8a69cd5476190e1f4d",
      "bytes": 1690
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3f0a67d8abea6401b0df94988ba26d4f3b599983f2aedb700c4911a8e523a377",
      "bytes": 192338
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "94157ecba4383b082594793febedfcca5c101fe5be58c02f34c062b35ab078a2",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2988fe5deb569d679ef89179b85c528a3b6db278f3c1ad79715b36dd5d2ee424",
      "bytes": 1206
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e79d4e1b80e68bf1e94c55f9def155a76330c202a1119df8a1ee38cc106c7bd1",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1716ef7d306b060affa130c6f05738942a25196a48832381cffc9ab5a227661f",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "adf1ed4ae1593070f48cfb9fcf9225a4db87c05411fb21038b5eec065f737e72",
      "bytes": 988
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "f710ce06ef00926fd48d2c9ae7df4971bd20adfd3c2ebabbb73c1c85490b6c11",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "51a4d63daea8eb9b5fb2549f73ec6301c4797858fc6415824c224bbd01187f78",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "54788583d95b291daae8c482fdd85f4098e072ab65594d7ed1f201322989403e",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "1c8b211a5b1fdf6a2b1019fceff59fe886528d7a3fe1bc3f4714a1b631279a63",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "692b720c4e0a64c9d34e66cdb655ddef2821d6f6435171e988fa2f5721d9fad9",
      "bytes": 194503
    }
  ],
  "estimated_tokens": 11845
}
-->

# Durable State Update — Chapter 620

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 620. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 620. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 620,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 620,
    "continuity_sources": [620],
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
    "The Fire Dragon Pavilion has reached Yeongin and is staying at Poison Flower Pavilion.",
    "The elderly Poison Flower Pavilion owner is the Hidden Shadow Pavilion agent planted in Yeongin and has identified Jin Taekyung.",
    "Yeongin’s inhabitants are hostile toward Han Chinese because a Heavenly Demon Escort Bureau group allegedly massacred approximately two hundred nearby villagers.",
    "The Heavenly Demon Escort Bureau group came from Sichuan, included one woman and nearly thirty men, and all of them later died from deadly venom.",
    "The woman in the Heavenly Demon Escort Bureau group may have been the Southern Heaven Demon Empress, but the innkeeper did not recognize her likeness and she may have used a disguise technique.",
    "The Nanman Beast Palace remains the Fire Dragon Pavilion’s primary mission objective.",
    "The Peak-grade Chain Quest requiring contact with a Hidden Shadow Pavilion agent in Nanman has reached its contact stage in Yeongin."
  ],
  "continuity_sources": [
    619
  ],
  "open_questions": [
    "Was the woman in the Heavenly Demon Escort Bureau group the Southern Heaven Demon Empress?",
    "Who poisoned and killed the Heavenly Demon Escort Bureau group, and why?",
    "What information or assistance will the Hidden Shadow Pavilion agent provide?",
    "What dangers and plans await the Fire Dragon Pavilion at the Nanman Beast Palace?"
  ],
  "safe_through": 619,
  "temporary_decisions": [
    "Render 天魔镖局 as Heavenly Demon Escort Bureau.",
    "Render 蛮族 as Man people.",
    "Continue rendering 永仁 as Yeongin and 毒华楼 as Poison Flower Pavilion."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 대격변     | **Great Cataclysm**   |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 독화루 | **Poison Flower Pavilion** | Derelict wooden building serving as the Hidden Shadow Pavilion contact location. |
| 천마표국 | **Heavenly Demon Escort Bureau** | A Sichuan group whose arrival preceded the Yeongin massacre; all members were later found dead from venom. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 617
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 619
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 619
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 619
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 619
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 619
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 619
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 619
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 619
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃620화



“반갑네. 열화신룡 진태경.”

“……!”

귓가를 파고드는 나직한 목소리에 퍼져 나가는 동요. 그러나 나는 놀라는 대신 물끄러미 노인을 응시했다.

혹여 그가 은영각 요원일지도 모른다는 것은 대화를 나누면서 어느 정도는 짐작했다.

‘그럴 만한 조건은 충분했으니까.’

눈앞의 노인은 천면호리가 알려 준 접선 장소의 주인장인 데다, 다른 이민족들과 달리 우리에게 별다른 적대감을 표출하지도 않았다.

하지만 발을 헛디디지 않으려면 돌다리도 두들겨 보고 건너야 하는 법이다.

시스템도 [남만행] 퀘스트를 통해 경고하지 않았나. 늘 주위를 경계하고 유연하게 행동하라고.

적어도 이번만큼은 나도 그 조언을 충실하게 따를 생각이었다.

스아아아.

보이지 않는 무형(無形)의 공력이 객잔 내부를 에워싼다. 외부로부터 모든 소음이 차단된 공간 속에서, 나는 조용히 입을 열었다.

“은영각 소속입니까?”

그건 나뿐만이 아니라 모두가 묻고 싶은 질문일 것이다.

자신을 향해 몰려드는 시선에, 노인이 지저분한 술잔을 매만지며 대답했다.

“어느덧 까마득한 과거가 되어 버렸군. 남호(南琥)라는 두 번째 이름을 얻은 것이.”

남호. 직역하자면 남쪽의 호박석이라는 뜻이다.

은영각은 첩보 단체인 만큼 요원들의 신분을 숨기기 위하여 일종의 코드네임을 부여했는데, 남호라는 이름은 천면호리가 사전에 알려 준 정보와 정확히 일치했다.

“어느 여우가 말하길, 남만에 세찬 바람이 분다더군요.”

“설령 태풍이 휘몰아쳐도 땅속 깊이 뿌리내린 독화(毒華)는 흔들리지 않을걸세.”

천면호리에게 전달받은 밀마(密摩)까지 확인하자 비로소 확신이 들었다.

나는 노인. 아니, 남호의 앞에 놓여 있는 술잔을 채워 주며 말을 건넸다.

“사실 마지막까지 의심의 끈을 놓지 않았었는데…… 은영각 소속이 틀림없군요.”

망설임 없이 술잔을 단번에 비운 남호가 물었다.

“왜. 무림맹 은영각 요원이 이민족일 거라고는 생각 못 했나?”

남호의 말처럼 그는 이민족이 맞았다.

남만의 무더운 햇볕에 의해 거무스름하게 그을린 피부와 특색 있는 용모는, 눈썰미가 조금이라도 있는 사람이라면 금세 알아차릴 수 있을 만큼 한족과 거리가 멀다.

작게 고개를 끄덕인 내가 대답했다.

“솔직히 아니라고는 말씀 못 드리겠네요. 무림맹 은영각 소속이라고 생각하기에는 중원과 워낙 거리도 멀고, 심지어 제가 느낀 바로는 무공도 안 익히신 것 같아서요.”

“누구나 저마다의 사연이 있는 법이라네. 중요한 건 대부분의 사람들이 자네처럼 생각한다는 것이고.”

“모두가 그렇게 받아들이기 때문에, 오히려 의심을 벗어날 수 있었다?”

“무공이라고는 일초반식도 익히지 않은 이민족 늙은이를 그 누가 의심하겠나. 가당치도 않은 소리지.”

마지막 남은 술병을 모조리 비워 낸 남호가 문득 생각났다는 듯 입을 열었다.

“아. 혹시 공력으로 소리를 차단했나?”

“물론입니다. 이야기가 밖으로 흘러나가면 안 되니까요.”

“그럼 잠깐 풀어 보게. 반드시 해야 할 일이 있으니.”

반드시 해야 할 일이라니. 그게 뭐지?

더 자세히 묻고 싶지만 남호의 표정은 한없이 진지했다.

그리고 내가 의문을 느끼며 사방을 틀어막고 있던 공력을 회수한 그 순간, 남호가 혁무진을 향해 불쑥 입을 열었다.

“거기 자네, 뒤에 누가 서 있는데?”

“예?”

콰창!

“썩 나가지 못하겠느냐. 이 버릇 없는 한족 새끼들아!”

그건 그야말로 순식간에 벌어진 일이었다.

정확히 뒤통수를 강타한 술병에 혁무진의 뚝배기가 깨져 나가고, 싸구려 술병이 산산 조각나며 사방으로 튀었다.

그리고 이 모든 사건의 용의자인 남호는 고래고래 고함을 내질렀다.

“이 찢어 죽여도 시원치 않을 놈들! 예가 어디라고 감히 행패를 부리냐!”

“……!”

“……!”

찰나 간에 벌어진 일에 나를 포함한 모두가 입을 딱 벌렸다.

물론 그중에서도 가장 놀란 건 혁무진이었다. 뒤통수를 움켜쥔 채 멍하니 남호를 바라보던 녀석이 버럭 외쳤다.

“이 늙은이가 미쳤나!”

“그래. 미쳤다! 이 애미, 애비도 없는 한족 놈아!”

“어어? 선 넘네? 선 넘어?”

“선을 넘은 건 너 같은 한족 놈들이 아니더냐! 감히 남만 땅에서 사람을 죽인 것으로도 모자라, 이제는 무전취식까지 하다니!”

“아니, 씨바. 아까 줬던 은전은 국 끓여 먹었소!”

“땡전 한 푼 안 줘 놓고 무슨 개소리냐! 그래도 측은한 마음이 들어 고심 끝에 식사를 내주었거늘, 당장 내 눈앞에서 꺼지지 못할까!”

후웅, 콰창!

술병과 그릇들이 사방으로 날아다닌다. 불과 몇 초 사이에 난장판으로 변한 객잔 내부.

입으로는 온갖 쌍욕을, 손으로는 닥치는 대로 온갖 물건을 집어 던지던 남호가 나를 향해 입술을 달싹였다.

‘반 시진 뒤. 십 리 밖에 있는 호숫가에서 보세.’

이제야 그가 하는 행동의 의미를 깨달은 내가 화룡각 대원들을 향해 눈짓했다.

눈치 빠른 주화란과 송일섬, 그리고 사마표가 자리를 박차고 일어나 탁자를 뒤엎고 물건을 부쉈다.

물론 각자 한마디씩 하는 것도 잊지 않았다.

“요리!”

“개!”

“줫같이 맛없네!”

와장창창!

콰직! 우두두둑!

재수 없게 걸려든 기둥 하나가 박살 나자 천장이 기울어진다.

안 그래도 허물어지기 직전의 독화루였는데, 이제는 정말 와르르 맨션으로 상호명을 갈아치울 때가 온 듯싶다.

나는 아직까지도 남호를 향해 고래고래 소리치는 혁무진과, 남은 요리를 입안에 쓸어 넣는 태산의 뒷덜미를 잡아채어 냅다 달렸다.

“이 미친 늙은이야! 나이는 똥구멍으로 처먹었…… 컥!”

“안 돼! 태산이가 아껴 뒀던 닭 다리!”

“지랄 말고 나가! 다 나가!”

우지끈!

비명과 흙먼지가 뒤섞여 난장판이 되어 버린 혼란의 틈바구니.

나를 필두로 독화루를 빠져나간 화룡각 대원들을 기다리고 있던 것은 어느덧 백 명으로 불어난 인파였다.

“한족 놈들이 나왔다!”

“감히 챠오 어르신을 공격하다니!”

“죽여!”

“아니다. 산 채로 뱀굴에 던져 넣자!”

물론 여기 있는 사람 중에 산 채로 뱀굴에 들어가고 싶은 정신 나간 인간은 단 한 명도 없다.

쉬이익, 퍽!

한숨을 내쉬며 곡괭이를 피하는 내 귓가에, 뒤늦은 시스템 알림이 파고들었다.

띠링.



- 임무 [은영각 요원과 접선]을 완료했습니다!

- 퀘스트, [남만에 심은 씨앗]을 성공적으로 완료했습니다!

- 퀘스트 완료 보상을 획득합니다!

- 소량의 경험치를 획득했습니다!

- 소량의 명성을 획득했습니다!

- 새로운 연계 퀘스트가 생성되었습니다!



아니, 그래서 호숫가가 어디라고?



* * *



남호는 자신이 말한 대로 정확히 반 시진 뒤에 모습을 드러냈다. 한 손에는 봇짐을, 다른 한 손에는 붕대를 칭칭 감은 채로.

“기둥. 누가 부쉈나.”

“…….”

“…….”

“사십 년간 운영했던 객잔이 무너졌네. 나는 유언도 못 남기고 뒈질 뻔했지.”

나는 조심스럽게 그를 위로했다.

“그렇게 될 줄은 저희도 몰랐습니다. 다 괜찮아질 거예요.”

“그걸 말이라고 하나? 괜찮다고 하면 다 괜찮아져?”

“나중에 충분히 보상해 드리겠습니다.”

“조금 괜찮아지는군.”

역시 이 세상에는 금융 치료만 한 게 없다. 순식간에 상태가 호전된 남호가 우리를 바라보며 입을 열었다.

“객잔에서 있었던 일은 이해하게. 마을 사람들의 의심을 피하려면 어쩔 수 없었어. 요즘은 워낙 흉흉한 분위기라 자네들을 비호했다면 나까지도 주목을 받게 되었을 거야.”

혁무진이 퉁명스럽게 말을 받았다.

“그래서 멀쩡히 살아 계신 저희 부모님을 죽인 겁니까?”

“애미, 애비 없다는 말은 내 사과하지. 어쩔 수 없었어.”

“똑같이 들었으면 기분이 어떠셨을 것 같습니까?”

“난 어릴 적부터 혼자 자랐네. 부모님이 일찍 돌아가셔서 얼굴도 기억나지 않아.”

“아.”

역시 은영각 요원 짬밥이 어디 가는 게 아니다.

짧은 대화로 혁무진의 입을 닥치게 만든 남호가 손에 든 봇짐에서 뭔가를 꺼내어 건넸다.

“이게 뭡니까?”

“목판일세. 지난 오십여 년간 틈이 날 때마다 남만 곳곳을 돌아다니며 지형과 부족들의 위치를 상세히 기록해 두었지.”

정마대전이 종결되고 오랜 세월이 흘렀지만, 모두가 평화에 젖어 있던 것은 아니다.

남호 역시 자신의 본분을 잊지 않고 활동을 이어 나가고 있었다.

“남만은 험지와 맹수, 독물로 가득한 땅이라 쉽지 않았을 텐데…… 정말 고생 많으셨겠군요.”

주화란의 탄성에 남호가 씁쓸한 표정을 지었다.

“해야 할 일을 한 것뿐이지. 사실 이 지도를 만들면서도 쓰일 만한 일이 없기를 바랐네.”

하지만 남호의 바람과는 반대로 평화는 끝났다.

마교라는 껍데기를 벗은 암천이 발호했고, 중원 곳곳이 피로 물들었으며 그 어두운 그림자는 중원 밖의 남만에까지 뻗어 나가는 중이다.

“전후 사정은 이미 알고 있네. 각주께서 우려가 크시더군. 자네들도 같은 생각인가?”

“예.”

나는 망설임 없이 고개를 끄덕였다.

호북에서 수신룡을 중심으로 일어난 일련의 사건들을 생각한다면, 남만은 그야말로 터지기 직전의 화약고나 다름없었다.

중원과는 비교도 안 될 만큼의 온갖 영물과 독물, 맹수들이 득실거리는 곳이니까.

“균열에 관한 소식은 이미 접하셨으리라 생각합니다.”

“남만은 외진 곳일세. 아직 그에 관한 소문이 이곳 사람들에게 전해지지 않았지만, 나는 전서응을 통해 전달받았지. 전서를 보낸 이가 각주가 아니었다면 믿지 못했을 이야기였어.”

비단 남호가 아니었더라도 누구나 마찬가지였을 것이다.

당장 수신룡에 관한 이야기를 들은 중원인들도 헛소문 취급하는 것이 현실이니까.

하지만 이 비현실적인 일들이, 곧 현실로 뒤바뀔 날이 머지않았다.

현대인들이 대격변이라 부르던 그 시기처럼.

“암천은 분명 남만을 노리고 있을 겁니다. 지금 당장 드러나지 않았더라도, 오래 지나지 않아 분명 일이 터질 거예요.”

확신에 찬 내 모습을, 남호가 침잠한 눈빛으로 응시했다.

“오래전, 나는 중원 상단에 의탁하여 스스로 남만을 떠났었네. 그리고 지난 오십여 년간 단 한 순간도 이 땅을 벗어난 적이 없지. 하지만 얼마 전의 그 일을 제외한다면 아무 일도 일어나지 않았다네.”

“천마표국에서 왔다는 중원인들이 인근 마을을 습격한 그 일 말입니까?”

“그래. 이민족들이 분노하고 분위기가 흉흉해졌지만 그뿐일세. 흔한 일은 아니지만 그렇다고 지금까지 없었던 일도 아니었지.”

“그 일이 암천과 무슨 연관이 있을지는 모르겠지만…….”

나는 나직한 목소리로 말을 이었다.

“앞으로는 그것과는 비교도 안 될 만큼의 참사가 일어날 겁니다.”

“……!”

남호의 눈빛이 파르르 떨렸다.

그에게는 이곳이 고향이고, 지금껏 살아온 터전이다. 짧은 침묵 끝에 그의 입술 사이로 늙수그레한 목소리가 흘러나왔다.

“짐을 챙겨 거처를 떠나면서도 믿기 싫었네. 하지만 이렇게 된 이상 어쩔 수 없지.”

손에 든 봇짐을 둘러멘 남호가 걸음을 내디디며 말을 이었다.

“가세. 자네들의 목표가 어디든, 내가 안내해 줄 테니.”
```

## Final English reading copy

```markdown
# Chapter 620

“Nice to meet you. Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

A low voice burrowed into my ears, and a ripple of agitation spread through the room. But instead of being startled, I stared quietly at the old man.

While speaking with him, I had already suspected to some degree that he might be an agent of the Hidden Shadow Pavilion.

*He certainly had the right conditions.*

The old man before me was the owner of the meeting place Thousand-Faced Fox had told us about. And unlike the other non-Han locals, he hadn’t shown us any particular hostility.

Still, if you didn’t want to misstep, you had to knock on even a stone bridge before crossing it.

The System had warned me through the *Journey to Nanman* Quest, too. To stay alert at all times and act flexibly.

At least this time, I intended to follow that advice faithfully.

Ssshhh.

Invisible internal energy spread around the inside of the inn. In a space where all sound from outside had been cut off, I quietly opened my mouth.

“Are you affiliated with the Hidden Shadow Pavilion?”

That was probably the question everyone wanted to ask.

As all eyes turned toward him, the old man stroked a filthy liquor cup and answered,

“It has already become a distant past—the time when I received a second name, Namho.”

Namho. Literally, it meant “amber from the south.”

The Hidden Shadow Pavilion was an intelligence organization, so it gave its agents codenames to conceal their identities. The name Namho matched the information Thousand-Faced Fox had given us exactly.

“One fox said a fierce wind was blowing in Nanman.”

“Even if a typhoon rages, the Poison Flower rooted deep in the ground will not be shaken.”

After confirming even the secret signal Thousand-Faced Fox had given me, I was finally certain.

I refilled the liquor cup sitting in front of the old man—no, Namho—and spoke.

“To be honest, I never let go of my suspicions until the very end… But you really are affiliated with the Hidden Shadow Pavilion.”

Namho drained his cup in one gulp and asked,

“Why? Did you never imagine that an agent of the Murim Alliance’s Hidden Shadow Pavilion might be one of the non-Han peoples?”

Just as Namho said, he was indeed not Han Chinese.

His dark, sun-browned skin from Nanman’s blazing heat and his distinctive features were far removed from those of the Han Chinese—so much so that anyone with even a little observational skill could tell at once.

I gave a small nod and answered,

“To be honest, I can’t say I didn’t think that. It’s just that you’re so far from the Central Plains that it was hard to believe you were with the Murim Alliance’s Hidden Shadow Pavilion. And from what I could sense, you didn’t seem to have learned martial arts, either.”

“Everyone has their own circumstances. What matters is that most people think as you did.”

“Because everyone accepted you that way, you were able to avoid suspicion?”

“Who would suspect an old non-Han man who hasn’t learned even a single martial arts move? It would be absurd.”

After emptying the last remaining bottle of liquor, Namho suddenly opened his mouth as if he had just remembered something.

“Oh. Did you block the sound with your internal energy?”

“Of course. We can’t let this conversation leak outside.”

“Then lower it for a moment. There’s something I absolutely must do.”

Something he absolutely had to do?

What was it?

I wanted to ask in more detail, but Namho’s expression was utterly serious.

And the moment I withdrew the internal energy that had sealed off every direction, Namho suddenly turned toward Hyuk Mujin.

“You there. Who’s standing behind you?”

“Huh?”

Crash!

“Get the hell out of here, you rude Han bastards!”

It happened in the blink of an eye.

A liquor bottle struck Hyuk Mujin squarely in the back of the head, cracking him over the skull. The cheap bottle shattered, sending fragments flying in every direction.

And Namho, the obvious culprit behind it all, began shouting at the top of his lungs.

“You bastards! Even tearing you apart wouldn’t satisfy me! How dare you cause trouble here!”

“……!”

“……!”

Everyone, myself included, stared with our mouths hanging open at the sudden turn of events.

Of course, no one was more shocked than Hyuk Mujin. Clutching the back of his head, he stared blankly at Namho before shouting,

“Has this old man gone insane?”

“Yeah, I’m insane! You motherless, fatherless Han bastard!”

“Whoa. That’s crossing a line. You’re crossing a line!”

“You Han bastards crossed the line! As if murdering people in Nanman weren’t enough, now you’re eating without paying!”

“No, fuck! What did you do with the silver coin I gave you earlier? Boil soup with it?”

“You didn’t give me a single penny, so what kind of bullshit are you spouting? I took pity on you and gave you a meal after agonizing over it, and now get the hell out of my sight!”

Whoosh! Crash!

Liquor bottles and bowls flew in every direction. Within only a few seconds, the inside of the inn had turned into a complete mess.

Namho hurled every object he could get his hands on while screaming every insult under the sun. Then his lips moved ever so slightly as he looked toward me.

*Half a shichen[^1] from now. Meet me by the lakeside ten li away.*

[^1]: A shichen is approximately two hours, while ten li is approximately five kilometers.

Only then did I understand the meaning behind his actions. I signaled to the members of the Fire Dragon Pavilion.

Ju Hwaran, Song Ilseom, and Sama Pyo, all quick to catch on, sprang to their feet, overturned tables, and smashed everything in sight.

Of course, they didn’t forget to shout a line each.

“Food!”

“Dog!”

“Tastes like shit!”

Crash-crash-crash!

Crack! Rumble!

When one unfortunate pillar was smashed to pieces, the ceiling tilted.

The Poison Flower Pavilion had already been on the verge of collapse. At this rate, it really was time to change its name to Crumble Mansion.

I grabbed Hyuk Mujin, who was still shouting at Namho at the top of his lungs, and Taishan, who was shoveling the remaining food into his mouth, by the backs of their necks and ran.

“You crazy old man! You ate your age through your asshole—cough!”

“No! Taishan’s chicken leg! He was saving it!”

“Quit your bullshit and get out! All of you!”

Crunch!

Screams and clouds of dust mingled together in the middle of the chaos.

The Fire Dragon Pavilion members rushed out of the Poison Flower Pavilion with me at the front. Waiting outside was a crowd that had grown to a hundred people.

“The Han bastards are out!”

“They dared attack Elder Chao!”

“Kill them!”

“No! Throw them alive into the snake pit!”

Of course, there wasn’t a single sane person among them who wanted to be thrown alive into a snake pit.

Sss! Thud!

As I dodged a pickaxe with a sigh, a delayed System notification pierced my ears.

Ding.

> **System**
>
> - Mission **Contact with a Hidden Shadow Pavilion Agent** completed!
> - Quest **Seeds Planted in Nanman** completed successfully!
> - Quest completion Reward acquired!
> - A small amount of EXP acquired!
> - A small amount of Fame acquired!
> - A new linked Quest has been generated!

*So where exactly is this lakeside?*

* * *

Just as he had said, Namho appeared exactly half a shichen later.

He had a bundle in one hand, while the other was wrapped tightly in bandages.

“The pillar. Who broke it?”

“…….”

“…….”

“The inn I operated for forty years collapsed. I nearly died without even getting the chance to leave a will.”

I cautiously tried to comfort him.

“We didn’t know that would happen. Everything will be all right.”

“Is that something to say? Does saying it’s all right make everything all right?”

“We’ll compensate you properly later.”

“That makes it a little better.”

As expected, nothing worked in this world like financial therapy. Namho’s condition improved in an instant as he looked at us and spoke.

“Understand what happened at the inn. I had no choice if I wanted to avoid the villagers’ suspicions. The atmosphere is so dangerous these days that if I had protected you, I would have drawn attention too.”

Hyuk Mujin answered sourly,

“So you killed off my parents when they’re both alive and well?”

“I apologize for saying you had no mother or father. It couldn’t be helped.”

“How would you feel if someone said the same thing to you?”

“I grew up alone from a young age. My parents died early, so I don’t even remember their faces.”

“Ah.”

As expected, years of experience as a Hidden Shadow Pavilion agent were no joke.

With only a brief exchange, Namho had silenced Hyuk Mujin. He took something out of the bundle in his hand and held it out to us.

“What is this?”

“A wooden map. For more than fifty years, whenever I had the time, I traveled all over Nanman and recorded the terrain and the locations of the tribes in detail.”

A long time had passed since the Great Faction War ended, but that didn’t mean everyone had been basking in peace.

Namho, too, had continued his work without forgetting his duty.

“Nanman is full of treacherous terrain, predators, and venomous beasts. It couldn’t have been easy… You must have gone through a great deal.”

Namho’s expression turned bitter at Ju Hwaran’s exclamation.

“আমি did nothing more than what needed to be done. In fact, while making this map, I hoped it would never be needed.”

But contrary to Namho’s wishes, peace had ended.

Dark Heaven had shed the shell of the Demonic Cult and run rampant. Blood had stained every corner of the Central Plains, and that dark shadow was now stretching beyond the Central Plains into Nanman.

“I already know what happened before and after. The Pavilion Master is deeply concerned. Do you feel the same way?”

“Yes.”

I nodded without hesitation.

Considering the chain of events centered around the Water God Dragon in Hubei, Nanman was nothing less than a powder keg on the verge of exploding.

It was a place crawling with countless spiritual creatures, venomous beasts, and wild animals beyond anything the Central Plains could compare with.

“I assume you’ve already heard about the rift.”

“Nanman is a remote place. Rumors about it haven’t reached the people here yet, but I received the news through a messenger eagle. If the Pavilion Master had not sent the letter, it would have been a story I couldn’t have believed.”

Anyone else would have felt the same, even if they weren’t Namho.

The Central Plains people who had heard about the Water God Dragon were treating it as a ridiculous rumor, after all.

But it wouldn’t be long before these impossible events became reality.

Just as they had during the period modern people called the Great Cataclysm.

“Dark Heaven is definitely targeting Nanman. Even if nothing has surfaced yet, something will happen before long.”

Namho stared at me with sunken eyes as I spoke with complete certainty.

“Long ago, I left Nanman of my own accord by entrusting myself to a Central Plains merchant caravan. And for the past fifty-odd years, I haven’t left this land even once. But aside from that incident a little while ago, nothing happened.”

“Do you mean the incident where the Central Plains people claiming to have come from the Heavenly Demon Escort Bureau attacked a nearby village?”

“Yes. The non-Han locals grew furious, and the atmosphere became dangerous, but that was all. It wasn’t common, but it wasn’t something that had never happened before, either.”

“I don’t know what connection that incident might have had with Dark Heaven, but…”

I continued in a low voice.

“From now on, a tragedy will occur that makes that look insignificant.”

“……!”

Namho’s eyes trembled.

This was his homeland, the land where he had lived all his life. After a short silence, an aged voice slipped between his lips.

“Even while packing my belongings and leaving my home, I didn’t want to believe it. But now that things have come to this, I have no choice.”

Namho slung the bundle over his shoulder and took a step forward.

“Let’s go. Wherever your destination is, I’ll guide you.”
```
