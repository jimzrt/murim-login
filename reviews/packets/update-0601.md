<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0601.txt",
      "sha256": "2a28c879461fc7bb82e170319bc9947ba360283977c275cce51aa7b76782b0f0",
      "bytes": 14606
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fec879a523abb357f0ec8e69456934d316f32821f9b78eb0302b69785469e6cc",
      "bytes": 1783
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e5a012a8d7d567e4e6b6b4fad787038996015e020a9fb92d22d419375952c7c6",
      "bytes": 186607
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "0ebde4e1a40d90f64e3843fb827a12c3643fcb926624538116bb994742b5f3ca",
      "bytes": 727
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "951b7f4bfabb22dcfe300404abe2b72cbee75a7e5ed4b9b2a03c1c149d4aa348",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "283e798db6d8556e860d8d4d4071c11b23d5339ad714f31ee59f46c188bc5556",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "c194cf4c3c9d034027a6470bdf38c2b9f929251b406ea957145522e693456f31",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d47e76009998e5a2d9ba01212e155720bcfa878a69d60697f0ad18deea2d4faa",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "19169f9cc739903a95ce9c86bec7129ee79c277a1b3714d817a3d04e7619eeb4",
      "bytes": 622
    },
    {
      "path": "characters/Park Daewon.md",
      "sha256": "e380dbd43fa09f18d63ade18c83d646ccb9b0bc64930d11c568599219c7dee5d",
      "bytes": 607
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "e01f713178564a28a4998b9abce64010fb5b964187961a5e76736446cde3eefe",
      "bytes": 1080
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "d958bb37c465ffb81e79f34da431d8ffc191a8c80df5c2682aa485093aca5414",
      "bytes": 966
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5b85243ff641dd9ca32121c53e2ec8c0dd2bad3fc0aea7084d2f84498d606441",
      "bytes": 184718
    }
  ],
  "estimated_tokens": 12066
}
-->

# Durable State Update — Chapter 601

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 601. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 601. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 601,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 601,
    "continuity_sources": [601],
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
    "Cheon Taemin has been unconscious for more than twenty years and is hidden in another secret area within Ares Guild's Area A.",
    "Lee Jungryong and Song Cheonwoo concealed Cheon Taemin's condition, but Choi Minwoo does not believe they caused it.",
    "Jin Taekyung, Choi Minwoo, and Go Se-won know about the hidden area; its exact location and access method remain unknown.",
    "Key insiders in the government's Area A investigation have joined forces with Choi Minwoo and Jin Taekyung.",
    "Choi Minwoo intends to lawfully take control of Ares Guild to halt the investigation and secure Cheon Taemin.",
    "Jin Taekyung has agreed to help Choi Minwoo's campaign against Ares Guild.",
    "Choi Minwoo will visit Ares Guild headquarters at six o'clock and hold a press conference.",
    "Park Daewon is Ares Guild's acting head and is hesitating under Choi Minwoo's pressure."
  ],
  "continuity_sources": [
    600
  ],
  "open_questions": [
    "What is the exact location of the second secret area within Area A, and how can it be accessed?",
    "What caused Cheon Taemin to lose consciousness and remain in a vegetative state for more than twenty years?",
    "Will Choi Minwoo lawfully gain control of Ares Guild and stop the government's investigation?",
    "What debt does Go Se-won mean to repay to Jin Taekyung?",
    "How will the authorities ultimately resolve the charges against Jin Taekyung?"
  ],
  "safe_through": 600,
  "temporary_decisions": [
    "Use Team Leader Choi for 최 팀장.",
    "Use Butler Kim for 김 집사.",
    "Use President's Security Service for 청와대 경호실.",
    "Use maternal grandfather for 외조부님.",
    "Use Vice President Park for 박대원 부사장님."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 박대원 | **Park Daewon** | Senior Ares Guild executive who became its acting head after Go Jun's death. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 검찰 | **prosecutors’ office** | Government prosecutorial institution that summons and investigates Taekyung. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 소격변 | **Small Cataclysm** | Name given to the Sichuan Province monster wave. |
| 지사장 | **Director** | Ares title used for Song Cheonwoo in 송 지사장. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |
| 송천우 | 천태민 | former subordinate to revered older brother by respect | Hyung | reverent and familiar; shocked | Song Cheonwoo recognizes Cheon Taemin's blood in Choi Minwoo and mutters 형님 while facing Choi. |
| 최민우 | 박대원 | prospective_Ares_Guild_claimant_to_acting_head | Vice President Park | formal, calm, and coercive | Orders Park to have all Ares executives present at headquarters by six o'clock. |
| 박대원 | 최민우 | acting_Ares_head_to_prospective_Guild_claimant | Team Leader Choi, then Mr. Choi | formal and hesitant | Initially uses Choi's title before switching to his name while asking for more time. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 600
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm; he has been unconscious for more than twenty years and is hidden from the world in a secret area within Ares Guild's Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 600
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 599
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 600
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 600
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 600
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Park Daewon.md

# Park Daewon (박대원)

- **Safe through:** Chapter 600
- **Aliases:** None
- **Role:** Senior Ares Guild executive who became the Guild's acting head after Go Jun's death and the prosecution of most executives holding real power.
- **Personality:** Hesitant and cautious when confronted by Choi Minwoo; no broader traits are established.
- **Voice:** Dark, formal, and hesitant over the phone.
- **Relationships:** An Ares Guild executive being pressured by Choi Minwoo to gather the remaining executives and decide the Guild's future.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 600
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 600
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and a formidable aura-wielding swordsman who wields Hero's Soul; he is now mobilizing government allies to secure Taemin and lawfully take control of Ares Guild.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃601화



복구가 진행되고 있는 아레스 길드 본사.

회의실 안의 공기는 무거웠다.

거대한 원형 테이블을 중앙에 두고 자리에 앉은 삼십여 명의 남녀들은 가라앉은 표정으로 한 사람의 입을 바라보는 중이었다.

“……해서, 이렇게 긴급회의를 소집하게 된 걸세.”

초조한 기색의 중년인. 박대원 부사장의 말이 끝나기가 무섭게 곳곳에서 동시다발적인 반응이 튀어나왔다.

“허, 참. 어지간히 얕보였군요. 그것도 서른도 안 된 어린놈한테.”

“뻔히 보이는 의도도 가소롭습니다. 이건 숫제 우리 아레스를 통째로 집어삼키겠다는 것 아닙니까.”

“아니, 형님. 왜 권한도 없는 외부인의 요청으로 긴급회의를 소집합니까? 아무리 형님이 부사장이어도 이건 아니죠.”

사방에서 쇄도하는 비난의 목소리에, 박대원 부사장은 손수건으로 반쯤 벗겨진 이마를 문질렀다.

어느덧 환갑을 코앞에 둔 그는 이 모든 상황이 당황스럽기만 했다.

‘후우. 이게 도대체 어떻게 된 일인지.’

전쟁에서는 두각을 드러냈지만, 정쟁(政爭)에는 영 소질이 없던 그다.

다행히 적을 만들지 않는 성격 덕분에 지금까지 허울뿐인 부사장 자리를 지킬 수 있었다.

그러나 불과 열흘 전, 은퇴를 앞두고 떠난 휴가 도중 믿지 못할 소식을 들었다.

바로 한 사람에 의해 아레스 길드 본사가 격파당하고, 부길드장인 석고준이 살해당했다는 이야기였다.

‘그럴 리가.’

그렇게 생각했다. 적어도 처음 십 분 동안은.

하지만 모든 것이 사실이었다. 삼십여 년간 공들여 세운 철옹성은 무너졌고, 새롭게 취임한 지 얼마 되지도 않은 신임 성주는 목이 달아났다.

그리고 검찰의 포승줄을 간신히 피한 신하들은 입을 모아 불만을 토로하고 있었다.

“말도 안 됩니다! 그런 헛소리, 들어 줄 필요도 없어요.”

“아레스라는 이름을 만든 것도 우리고, 지켜 낸 것도 우리요. 아직 세상 물정도 모르는 핏덩이가, 그것도 외부인이 무슨 자격으로 끼어들어?”

“박대원 부사장님, 이건 정말 아니지 않습니까!”

“…….”

박대원은 말없이 물잔을 들이켰다.

이 자리에 모인 이들은 최소 십 년, 최대 삼십여 년을 아레스 길드에 몸담은 중역이다.

길드 내의 실권을 틀어쥔 실력자들 대부분이 검찰 소환에 불려갔다 해도 저들의 힘은 절대 적지 않았다.

‘……하지만 그렇다고 해서, 그를 무시할 수도 없는 노릇이지.’

그, 최민우에 관해서는 박대원도 익히 알고 있었다.

아니, 모를 수가 없었다. 천태민의 사생활 및 가족 관계는 철저히 보호되어 있었지만, 측근으로 분류되는 소수의 인물에게는 달랐으니까.

창립 멤버에 포함되어 있던 박대원도 그중 하나였다.

‘돌잡이 때 처음 보고, 장례식 때가 마지막이었나.’

기억 속에서 서서히 잊혀 가던 그 아이가 어느덧 훌쩍 커서 돌아왔다. 오래전 자신이 잃어버린 것을 되찾기 위하여.

모든 상황에 그저 순응하며 살아왔던 박대원은 그 사실이 못내 가슴에 걸렸다.

그것은 길드 내에서 완전히 배제되었던 최민우를 외면했던 자신의 과거에서 오는 얄팍한 죄책감이었다.

‘어찌해야 하나.’

박대원이 고심에 잠겨 있던 그때, 불만을 토로하는 목소리들로 소란스럽던 회의장에 짧고 굵은 한마디가 울려 퍼졌다.

“어디까지 하나 지켜보려고 했는데, 갈수록 가관이라 더는 못 들어 주겠네.”

“……!”

“……!”

순간 회의장에 내려앉은 싸늘한 침묵. 눈을 부릅뜬 여러 쌍의 시선이 한 사람을 향해 집중되었다.

“김 상무님, 그게 무슨 망언이십니까!”

“상무님은 무슨. 야, 김광필이! 넌 무슨 개소리야!”

짧은 침묵 후 터져 나온 거친 외침에, 김 상무가 딱 벌어진 어깨를 으쓱해 보였다.

“제가 틀린 말이라도 했습니까? 가관이라서 가관이라고 한 것뿐인데. 그리고 백 전무님, 말조심합시다. 아무리 제가 후배여도 그런 말은 듣기 좀 거북합니다.”

“보자 보자 하니까 저 배신자 새끼가……!”

김 상무의 굵은 눈썹이 꿈틀거렸다.

“뭐요. 배신자?”

“그래, 이 새끼야! 너 같은 배신자 새끼들만 없었어도 이런 개 같은 상황도 없었어!”

“개같이 굴던 건 백 전무님 쪽 식구들 아닙니까. 그건 지금 누가 구치소에 있는지만 봐도 알 수 있는 문제 같은데?”

“뭐?”

“저와 몇몇 임원들이 진태경에게 합류했던 게 그리 거슬리셨던 모양인데, 결국 석 부길드장. 아니지, 석고준 그 인간이 무슨 짓거리를 벌이고 있었습니까? 아니면 혹시 백 전무님도 한 다리 걸치신 겁니까?”

“너, 너 이 새끼……!”

“어이, 김 상무! 말조심해!”

“말조심해야 하는 건 당신들이지!”

“옳소!”

“이 작자들이 감히 어디서!”

두 파로 나뉘어 온갖 고성이 오가는 회의장 내부. 홀로 침묵을 지키고 있던 박대원 부사장이 불쑥 입을 연 것은 그때였다.

“엄밀히 따지자면 외부인은 아니지.”

그 한 마디에, 핏대를 세워 가며 싸우던 중역들이 멈칫했다.

“예?”

“부사장님. 지금 뭐라고…….”

“최민우 그 친구 말일세.”

삼십여 명의 중역들을 천천히 훑은 박대원이 말을 이었다.

“그분, 천태민 길드장님의 하나뿐인 외손자가 아닌가.”

“……!”

“……!”

정확히 맹점을 찌르는 한 마디에 회의장이 정적에 잠겼다.

순간 김 상무를 비롯한 일파의 얼굴에는 밝은 빛이 떠올랐고, 내내 불만을 성토하던 이들의 얼굴은 흙빛으로 물들었다.

“그, 그건 단순한 루머 아닙니까.”

“마, 맞습니다. 형님. 아직 확인되지 않은 뜬소문이에요.”

소격변 이후부터 최민우의 신분에 관해서는 알음알음 이야기가 새어 나간 상황.

그러니 저들의 언행은 모른다기보다는 모르는 척하는 것에 가깝다.

하지만 적어도 박대원만큼은 아니었다.

“아니, 확실하네. 내 기억으로는 그분의 외손자가 틀림없어. 그리고…….”

누군가가 애써 반박하기도 전에, 박대원이 손에 쥔 스마트폰을 테이블 위로 올려놓으며 말을 이었다.

“이제 본인 스스로도 밝힐 생각을 굳힌 모양이야.”

“그게 무슨 소리…….”

“서로 치고받는 것도 좋지만, 바깥 상황 정도는 확인했어야지. 각자 데려온 비서들도 출입을 금지한 상황인데. 그렇지 않나?”

그 말에 뭔가를 깨달은 사람들이 황급히 각자의 스마트폰을 꺼내 들었다.

그리고 불과 일 분 남짓한 시간이 흐르기도 전에 헉, 하고 헛숨을 들이키는 소리가 곳곳에서 울려 퍼졌다.

수십여 대의 스마트폰에서 재생된 영상 속, 기자의 다급한 음성이 울려 퍼졌다.

- 최, 최민우 씨! 외조부님의 함자를 다시 한번 정확히 말씀해 주실 수 있으십니까?

그리고 곧이어 들려온 한 사람의 목소리가, 회의실 내부를 울렸다.

- 천, 태 자에 민 자. 천태민. 그분이 바로 제 외조부십니다.

- ……!

- ……!

끊임없이 들려오던 카메라 플래쉬 소리도, 웅성거리던 소음도 순식간에 사라졌다.

공식 기자 회견이 열린 영상 속 장소뿐만 아니라, 회의실 내부의 상황도 마찬가지였다.

모두의 마음속에 자리 잡은 짐작. 그러나 그 짐작이 사실로 변하고, 세상에 공표되었을 때의 파급력은 상상 이상으로 거대하다.

모든 것이 베일에 가려진 천태민의 유일한 핏줄에 관한 것이라면 더더욱.

더불어 회의실 안의 모두는 동시에 깨달을 수 있었다.

‘마침내 칼을 뽑았다.’

유배나 다름없던 이십여 년의 세월.

마침내 돌아온 왕손(王孫)은 가장 적절한 시점에서 가장 예리한 칼을 뽑았다. 자신이 잃어버린 것을 스스로의 힘으로 되찾기 위하여.

그러나 가장 중요한 것은, 그 칼날이 어디로. 또 누구를 향해 휘둘려질 것인지다.

꿀꺽.

그 누구도 쉽게 입을 열지 못했다. 보이지 않는 긴장의 끈이 팽팽하게 당겨진 분위기 속, 작은 속삭임들로 채워진 시간이 흘러가던 그때였다.

삑.

미세한 전자음과 함께 모두의 고개가 동시에 움직였다. 소리의 진원지는 넓은 회의실 벽면에 걸린 시계였다.

마치 위험을 알리는 듯한 붉은 LED에는 현재 시각이 떠올라 있었다.



PM 06 : 00



오후 여섯 시.

이들이 이곳에 모인 이유, 동시에 누군가의 등장을 의미하는 시간.

저벅, 저벅.

문밖 복도를 가로지르는 구둣발 소리를 모두가 들었고, 그들은 자신도 모르게 반사적으로 자리에서 일어났다.

그리고…….

달칵.

부드럽게 열린 문 너머로, 두 사람이 모습을 드러냈다.

“일찍 모여 계셨군요.”

“어, 여기 금방 고쳤네. 내가 지난번에 부쉈던 것 같은데.”

정중한 동시에 무례한, 그러나 피할 수 없는 점령군의 등장이었다.



* * *



내 어릴 적, 아버지는 입버릇처럼 말씀하시고는 했다.

아들아, 남자가 한 번 칼을 뽑으면 무라도 썰어야 한다.

그런 관점에서 보자면 최 팀장은 남자 중의 상남자였다. 무가 아니라 아레스 길드를 썰어 버리려고 이곳에 왔으니까.

“…….”

생각해 보니 내가 이미 한 번 썰어 버리긴 했었지만, 어쨌든.

“반갑습니다. 최민우입니다.”

최 팀장이 정중한 인사와 함께 목례를 취하자, 커다란 원탁을 중심으로 일어나 있던 아레스 길드의 중역들이 엉거주춤 인사를 받았다.

3초 후 세상이 멸망할 것처럼 어두운 표정을 짓고 있는 이들이 있는 반면, 입가에 한가득 미소를 띤 낯익은 얼굴들도 있다.

본사 습격 당시 내 편에 섰던 송천우 계파의 중역들이다.

하지만 판단하기 애매한 태도를 지닌 사람도 있었다.

가장 상석에 앉아 있던 늙수그레한 중년인. 박대원 부사장이 바로 그랬다.

“오셨습니까. 최민우 팀장님.”

복잡한 표정을 한 그를 물끄러미 바라보던 최 팀장이 고개를 끄덕였다.

“제가 늦은 건 아닌지 모르겠군요. 기자 회견이 생각보다 길어진 탓에 본의 아니게 결례를 저질렀습니다.”

예상은 했지만, 다들 표정을 보아하니 본방 사수를 철저히 한 모양이다.

물론 그중 절반 정도는 수신료의 가치를 느끼지 못했는지 분위기가 영 좋지 못했지만.

“그럴 리가요. 그럼 말씀 전에 우선 자리로…….”

“괜찮습니다.”

자리를 권하려는 박대원 부사장을 만류한 최 팀장이 부드럽게 덧붙였다.

“어차피 금방 끝낼 테니까요. 아직까지는 다른 분들도 절 외부인으로 생각하실 테니, 이야기가 길어지면 불편해지지 않겠습니까.”

“……크흠.”

뼈가 있는 말에 곳곳에서 헛기침이 튀어나온다.

그런 반응에도 아무렇지 않게 주위를 둘러본 최 팀장이 문득 입을 열었다.

“지금 보니 다섯 자리가 비는군요. 고문(顧問)직에 계신 세 분. 그리고 미국과 프랑스 지사장님은 어디 계십니까?”

꼬장꼬장해 보이는 중년인이 떨떠름한 표정으로 입을 열었다.

“우리 쪽 사람들에 대해 관심이 많으신 모양이군.”

“제 기억력이 좋은 편입니다, 백 전무님.”

“…….”

백 전무가 입을 다문 그때, 열흘 전 내 편에 붙었던 중역이 신속하게 대답했다.

“오지 않았습니다.”

“피치 못할 사정이 있는 모양입니다. 그렇죠?”

“세 분의 고문님들께서는 병환을 이유로 불참하셨고, 두 지사장은 참석을 거부한 것으로 압니다.”

“꼭 참석하라고 말씀드렸는데. 제 뜻이 제대로 전해지지 않은 모양이군요.”

최 팀장이 담담하게 뇌까린 그때, 백 전무가 재차 입을 열었다.

“이건 공식 회의가 아니라, 외부인의 요청에 의해 모인 자리요. 꼭 참석해야 할 이유는 없지. 설령 그 외부인이…….”

순간 머뭇거리던 그가 확연히 작아진 목소리로 말을 이었다.

“그분의 외손자라고 해도.”

“맞는 말씀입니다.”

고개를 끄덕여 수긍한 최 팀장이 품에서 자그마한 메모를 꺼내 건넸다.

“이게 뭐요?”

“병환을 앓고 계신 고문님들께 전해 드리는 처방전입니다. 아, 다른 지사장님 두 분께는 처방전 대신 다른 무언가가 갈 겁니다.”

아마도 아프다는 핑계로 참석하지 않은 당사자들은, 저 메모를 본 순간 모든 병에서 회복할 거다.

아직 드러나지 않은 범죄 사실이 낱낱이 적혀 있으니까.

메모를 확인한 백 전무도 침을 꿀꺽 삼켰다.

“이, 이거.”

“백 전무님도 안색이 좋지 않으신 것 같은데. 처방전을 따로 드릴까요?”

“아, 아니. 이 사람이 그게 무슨! 나, 난 괜찮아!”

팔짱을 낀 채 상황을 지켜보던 내가 중얼거렸다.

“괜찮아는 반말 아닌가?”

“괘, 괜찮소.”

“소리 없이 죽이는 101가지 방법, 저자 진태경.”

“괘, 괜찮습니다.”

음. 말귀가 어느 정도 트인 사람이 분명하다. 마른침만 꼴깍거리며 서 있는 그를 힐끗 바라본 나는 최 팀장을 향해 말을 건넸다.

“앉아서 얘기하면 안 됩니까? 다리 아픈데.”

“글쎄요. 자리가 마땅치 않아서…….”

말꼬리를 흐리는 그를 대신해, 나는 친절하게 상석을 가리켰다.

“저기. 자리 비었네.”

“아, 그렇군요. 그런데 제가 앉아도 되겠습니까?”

“투표하죠. 다수결의 원칙으로. 불만 있으신 분. 손?”

“…….”

아무도 손을 들지 않았다.
```

## Final English reading copy

```markdown
# Chapter 601

Ares Guild headquarters was still being repaired.

The atmosphere inside the conference room was heavy.

Around a massive round table, some thirty men and women sat with somber expressions, all watching one person’s mouth.

“…And that is why I called this emergency meeting.”

The moment Vice President Park Daewon finished speaking, several reactions erupted from every corner of the room.

“Well, well. They certainly looked down on us. And by a brat who isn’t even thirty, at that.”

“His intentions are laughably obvious. Isn’t he simply planning to swallow all of Ares whole?”

“No, hyung. Why would you call an emergency meeting at the request of an outsider who has no authority? Even if you are the Vice President, this is going too far.”

As voices of condemnation rushed at him from all sides, Vice President Park rubbed his half-bald forehead with a handkerchief.

Now nearing sixty, he found the entire situation bewildering.

*Phew. How had things come to this?*

He had distinguished himself on the battlefield, but had never possessed much talent for political infighting.

Fortunately, his personality—one that avoided making enemies—had allowed him to hold on to the largely ceremonial position of Vice President until now.

But just ten days earlier, while on vacation before his retirement, he had heard unbelievable news.

Ares Guild headquarters had been crushed by a single person, and Go Jun, the Vice Guild Master, had been murdered.

*That couldn’t be true.*

That was what he had thought. For at least the first ten minutes.

But every bit of it had been true. The impregnable fortress they had spent some thirty years building had fallen, and its newly appointed City Lord had lost his head before he had even settled into office.

And the retainers who had barely escaped the prosecutors’ handcuffs were now voicing their complaints in unison.

“This is absurd! There’s no need to listen to such nonsense.”

“We created the name Ares, and we were the ones who protected it. What right does some outsider—some bloody brat who still doesn’t know how the world works—have to interfere?”

“Vice President Park, this really isn’t right!”

“……”

Park Daewon silently took a long drink from his glass of water.

Everyone gathered here had spent at least ten years, and as many as thirty, working for Ares Guild.

Even if most of the people who held real power within the Guild had been summoned by the prosecutors’ office, these men and women were far from powerless.

*……But that doesn’t mean we can ignore him.*

Park Daewon knew all about Choi Minwoo.

No, he couldn’t not know. Cheon Taemin’s private life and family relationships had been protected with the utmost care, but things were different for the few people classified as his close associates.

Park Daewon, one of the founding members, was one of them.

*The first time I saw him was at his first-birthday ceremony, and the last was at the funeral…wasn’t it?*

The child who had been slowly fading from his memories had grown up and returned. He had come to reclaim what he himself had lost long ago.

Park Daewon, who had spent his entire life simply going along with every situation, couldn’t shake the discomfort in his chest.

It was a shallow sense of guilt born from the fact that he had turned away from Choi Minwoo when the boy had been completely excluded from the Guild.

*What should I do?*

While Park Daewon was lost in thought, a short, powerful voice rang through the noisy conference room.

“I was going to watch and see how far this went, but it gets more appalling by the minute. I can’t listen to any more of this.”

“……!”

“……!”

A chill fell over the conference room.

Several pairs of widened eyes focused on one person.

“Managing Director Kim, what kind of outrageous statement was that?”

“Managing Director, my ass. Hey, Kim Gwangpil! What the hell are you talking about?”

After the brief silence came a harsh outburst, and Managing Director Kim shrugged his broad shoulders.

“Was anything I said wrong? I only called it appalling because it is. And Executive Director Baek, watch your language. Even if I am your junior, those words are unpleasant to hear.”

“Just you wait, you traitorous bastard……”

Managing Director Kim’s thick eyebrows twitched.

“What? Traitorous bastard?”

“Yes, you bastard! If there hadn’t been traitors like you, we wouldn’t be in this goddamn situation!”

“Wasn’t it the people on Executive Director Baek’s side who acted like animals? We can figure that out simply by seeing who’s in the detention center right now.”

“What?”

“You seemed awfully bothered that a few executives and I joined Jin Taekyung. But in the end, what kind of shit was the Vice Guild Master—no, what was that man Go Jun—up to? Or did you have a hand in it too, Executive Director Baek?”

“You, you bastard……!”

“Hey, Managing Director Kim! Watch your mouth!”

“You’re the ones who should be watching your mouths!”

“Exactly!”

“How dare these bastards!”

The conference room split into two factions, with furious shouts flying back and forth.

That was when Vice President Park Daewon, who had remained silent by himself, suddenly spoke.

“Strictly speaking, he isn’t an outsider.”

At those words, the executives who had been shouting at one another stopped short.

“What?”

“Vice President Park. What did you just say……”

“I’m talking about Choi Minwoo.”

Park Daewon slowly looked over the thirty-some executives before continuing.

“Isn’t he Guild Master Cheon Taemin’s only maternal grandson?”

“……!”

“……!”

His single statement struck directly at the room’s blind spot, and silence descended over the conference room.

For an instant, bright light appeared on the faces of Managing Director Kim and his faction, while the executives who had been loudly voicing their complaints turned pale.

“But—but that’s just a rumor, isn’t it?”

“Th-that’s right, hyung. It’s an unconfirmed rumor.”

Ever since the Small Cataclysm, rumors about Choi Minwoo’s identity had been quietly spreading.

So their behavior was less a matter of not knowing than of pretending not to know.

But at least Park Daewon wasn’t pretending.

“No, I’m certain. As I remember it, he is definitely that person’s maternal grandson. And……”

Before anyone could force out another rebuttal, Park Daewon placed the smartphone in his hand on the table and continued.

“It seems he has decided to reveal it himself now.”

“What do you mean……”

“Fight among yourselves if you like, but you should at least have checked what was happening outside, especially with the secretaries you brought barred from entering. Isn’t that right?”

At those words, several people realized something and hurriedly pulled out their smartphones.

Before even a minute had passed, startled gasps rang out throughout the room.

A reporter’s urgent voice played from dozens of smartphones.

> “M-Mr. Choi Minwoo! Could you state your maternal grandfather’s honored name once more, clearly?”

And then another person’s voice rang through the conference room.

> “The Cheon character, the Tae character, and the Min character. Cheon Taemin. He is my maternal grandfather.”

> “……!”

> “……!”

The ceaseless camera flashes and the surrounding murmur vanished in an instant.

The same silence had fallen not only over the place where the official press conference was taking place, but also over the conference room.

Everyone had carried the same suspicion in their hearts. But when that suspicion became fact and was announced to the world, its impact was far greater than anyone could imagine.

All the more so when it concerned the only blood relative of Cheon Taemin, a man about whom everything was shrouded in mystery.

At the same time, everyone in the conference room realized the same thing.

*He has finally drawn his sword.*

More than twenty years of life that had been little different from exile.

At last, the royal grandson had drawn the sharpest sword at the most opportune moment. He had come to reclaim what he had lost through his own strength.

But the most important question was where that blade would be swung—and whom it would be aimed at.

Gulp.

No one could bring themselves to speak easily. As time passed in an atmosphere where an invisible thread of tension had been pulled taut, the room filled with faint whispers.

Then—

Beep.

Everyone’s head moved at once with the tiny electronic sound.

The source was the clock mounted on the broad wall of the conference room.

The current time glowed on its red LED display, as though warning them of danger.



**PM 06:00**



Six o’clock in the evening.

The time they had gathered here—and the time that signaled someone’s arrival.

Step. Step.

Everyone heard shoes crossing the hallway outside the door, and without realizing it, they reflexively rose from their seats.

And then……

Click.

Two people appeared beyond the smoothly opening door.

“You gathered early.”

“Oh, they fixed this place pretty quickly. I think I was the one who broke it last time.”

It was the arrival of an invading force—polite and rude at the same time, but impossible to avoid.



* * *



When I was young, my father used to say this like it was a proverb.

*Son, once a man draws his sword, he has to cut at least a radish.*

From that perspective, Team Leader Choi was a man among men. He had come here not to cut a radish, but to cut down Ares Guild.

“……”

Come to think of it, I had already cut it down once myself.

But still.

“Nice to meet you. I’m Choi Minwoo.”

With a polite greeting, Team Leader Choi bowed his head.

The Ares Guild executives who had been standing around the large round table awkwardly returned his greeting.

Some wore such dark expressions that one might think the world would end in three seconds. Others were familiar faces with smiles spread wide across their lips.

They were the executives from Song Cheonwoo’s faction—the ones who had sided with me during the assault on headquarters.

But one person’s attitude was difficult to judge.

The elderly middle-aged man seated at the head of the table.

Vice President Park Daewon.

“Welcome, Team Leader Choi Minwoo.”

Team Leader Choi studied Park Daewon’s conflicted expression for a moment, then nodded.

“I hope I’m not late. The press conference went longer than expected, so I ended up being discourteous despite myself.”

I had expected this, but judging by everyone’s expressions, they had watched the main broadcast live without missing a second.

Of course, about half of them didn’t seem to be enjoying the value of their license fees, judging by the atmosphere.

“Of course not. Then, before we begin, please take a seat……”

“That won’t be necessary.”

Team Leader Choi stopped Vice President Park as he gestured toward a seat, then continued in a gentle voice.

“We’ll be finished soon enough. Since everyone here still considers me an outsider, wouldn’t it make things uncomfortable if I let the conversation drag on?”

“……Ahem.”

His words had a barb in them, and awkward coughs erupted from several places.

Team Leader Choi looked around without the slightest concern for their reactions, then suddenly spoke.

“Now that I look around, five seats are empty. The three advisers. And where are the directors of the United States and French branches?”

A middle-aged man with a prickly appearance answered with an uncomfortable expression.

“You seem very interested in our people.”

“My memory is quite good, Executive Director Baek.”

“……”

Executive Director Baek closed his mouth.

Then one of the executives who had joined my side ten days earlier answered quickly.

“They didn’t come.”

“It seems they had unavoidable circumstances. Is that right?”

“I understand that the three advisers were absent because of illness, while the two branch directors refused to attend.”

“I specifically told them to attend. It seems my wishes weren’t conveyed properly.”

Team Leader Choi muttered this calmly, and Executive Director Baek spoke again.

“This isn’t an official meeting. It’s a gathering held at the request of an outsider. There’s no reason we had to attend. Even if that outsider is……”

After hesitating for a moment, he continued in a distinctly quieter voice.

“That person’s maternal grandson.”

“You’re right.”

Team Leader Choi nodded in agreement, then took a small note from inside his clothes and handed it over.

“What is this?”

“A prescription for the advisers who are suffering from illness. Ah, as for the two other branch directors, something else will be sent in place of a prescription.”

The people who had used illness as an excuse to skip the meeting would probably recover from every ailment the moment they saw that note.

They contained a detailed record of crimes that had not yet been revealed.

Executive Director Baek swallowed hard after reading the note.

“T-this……”

“Executive Director Baek, you don’t look well either. Should I give you a prescription as well?”

“N-no. What are you talking about? I-I’m fine!”

I stood with my arms crossed, watching the situation, and muttered.

“Wasn’t that ‘I’m fine’ a little too casual?”

“I—I am quite well.”

“One Hundred and One Ways to Kill Without a Sound, by Jin Taekyung.”

“I—I’m perfectly fine, sir.”

Hmm. He definitely seemed capable of understanding what people were saying.

I glanced at him as he stood there swallowing nervously, then spoke to Team Leader Choi.

“Can’t we sit down and talk? My legs hurt.”

“Well, there isn’t really a suitable seat…”

As he let his sentence trail off, I helpfully pointed toward the head of the table.

“There. The seat’s empty.”

“Oh, I see. But would it be all right for me to sit there?”

“Let’s vote. By majority rule. Anyone opposed, raise your hand?”

“……”

No one raised a hand.
```
