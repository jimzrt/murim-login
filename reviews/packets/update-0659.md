<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0659.txt",
      "sha256": "c2b80b8a9bb3e7ed57d47fd8c43794b1564c120fbeb6b1c0751ae7463d07e701",
      "bytes": 12632
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "38e402c71ef71c57a0a2905a9cfcfeb3bd60806a75da0059b5070b0b9fd21ce3",
      "bytes": 2358
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3b4f8c9b2e59618b6f0d53903359699b59b215e9a54328cc26998ba4a6b6ece8",
      "bytes": 200959
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "f0fbdd4f08488ea8c74fff0748672711e4a0871c0ee7b4ad2208cf59de95976b",
      "bytes": 589
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1c479360e0f49259d3487be8b714f82d04c29ea231e9d4f45fa36676665a2626",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c222e6efac5a020a3f50dfb14d9c304752153768fd2d00e91a0f1b0053e854f5",
      "bytes": 1347
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8508b82a8ba7307e98f0434db58fa7c3bc0f13086960b408f7501d59ba0c5238",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "58ad760e1e9f2a53c3809a7a612fe010bf28c453457c0909db623ccab1636e5b",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a7de65fdf23ac2e2ffc4c95215d5ca369122e48cbbc55656c9dfa20fb52cab13",
      "bytes": 1131
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "0007860291cd8567fa1f34b58cd71b5dbe7b73c65577d4408524d917b7315222",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "45896a5a561fa811f79e75a172d539171ca61e896c23f32bf9a69bb5d8f20ea2",
      "bytes": 957
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "098a1ce01242254b7502f0c5a38e3cfbec98f3242da5d957ce843b30d6ce6e8b",
      "bytes": 206298
    }
  ],
  "estimated_tokens": 10984
}
-->

# Durable State Update — Chapter 659

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 659. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 659. Profile updates may replace only one
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
  "chapter": 659,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 659,
    "continuity_sources": [659],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Yohi's Western Yao Estate was attacked by a Supreme Peak master, killing more than a hundred Yao warriors and beasts.",
    "Jin and Yayul Mok believe Dark Heaven directly intervened and likely deployed a Supreme Peak master, but the motive is unknown.",
    "Baeksang and the Beast Miao King are the only two known Supreme Peak masters in Nanman.",
    "Heugung genuinely loves Yohi and had promised to cooperate with Jin.",
    "Heugung and Yohi remain missing after the attack, and Heugung's apparent death remains unconfirmed.",
    "Faint footprints indicate that a third party abducted or confronted Heugung and Yohi rather than the incident being their staged attack.",
    "Yohi's nearly scentless pouch remains a possible clue.",
    "Baeksang has publicly accused Jin of the Inner Palace massacre and now relies on Utu-ri's eyewitness testimony and circumstantial evidence to demand his arrest.",
    "The Beast Miao King has halted Baeksang's attempted arrest, but Baeksang threatens pursuit across Nanman and reprisals against Jin's Han Chinese subordinates.",
    "Jin has chosen apparent surrender to protect his companions, but punched Baeksang immediately before declaring it."
  ],
  "continuity_sources": [
    658
  ],
  "open_questions": [
    "Who was the Supreme Peak attacker, and what did Dark Heaven seek by intervening directly?",
    "Are Heugung and Yohi alive, and where were they taken?",
    "What can be learned from Yohi's nearly scentless pouch?",
    "Is Baeksang truly colluding with Dark Heaven despite the evidence of third-party intervention?",
    "What consequences will follow Jin's punch and declared surrender under the Either-Or Quest?"
  ],
  "safe_through": 658,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음.",
    "Retain Either-Or for 양자택일.",
    "Retain bad move for 악수 when used in the Go metaphor.",
    "Retain underground prison for 뇌옥 and iron balls for 철구."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 남만야수궁  | **Nanman Beast Palace**          |
| 살기     | **killing intent**                               |                                                       |
| 소국주    | **Young Bureau Head**                        |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 청해     | **Qinghai**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

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
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |

## Listed compact profiles

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 658
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 658
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 658
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 658
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 658
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 658
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 658
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃659화



파슥.

털로 뒤덮인 커다란 발이 바싹 마른 잎사귀를 밟았다.

벌어진 입가 사이로 언뜻 모습을 드러내는 커다란 송곳니. 풀숲 사이에 한껏 웅크린 날렵한 몸뚱어리는 이미 만반의 준비를 끝마친 상태였다.

오늘은 어떤 고기를 먹게 될까.

눈에 띄는 사냥감을 발견하면, 빠르게 달려가서 목덜미에 송곳니를 박아넣으면 그걸로 끝이다.

눈치 없이 나타나는 독물(毒物)만 조심한다면 남만에서 사냥감을 구하는 것은 그리 어렵지 않았다.

적어도 치열한 먹이사슬의 상층부에 위치하는 흑표(黑豹)에게는 그랬다.

그르릉…….

샛노란 눈동자로 주위를 살피던 흑표가 문득 낮은 울음소리를 토해 냈다.

저 멀리에서부터 느껴지는 수많은 기척과 바람을 타고 흘러든 냄새를 맡았기 때문이었다.

킁킁.

흑표는 맹수답게 날카로운 감각의 소유자. 생각보다 일찍 걸려든 사냥감의 정체를 파악하는 데까지는 그리 오랜 시간이 걸리지 않았다.

인간.

정확히는 인간들이라고 해야 옳다. 어림잡아 일백을 헤아리는 인간의 무리가 이곳을 향해 다가오고 있었다.

크릉.

흑표는 저도 모르게 언짢은 울음소리를 흘렸다.

그도 그럴 것이, 흑표에게 있어 인간은 그리 썩 달갑지 않은 존재였다.

몸집도 작은 주제에 훨씬 덩치가 큰 맹수를 역으로 사냥하기도 하고, 머릿수가 많을수록 더 강한 힘을 발휘했으니까.

바로 지금처럼.

스윽.

흑표는 한껏 웅크렸던 몸뚱어리를 일으켰다.

홀로 인간들을 사냥하는 건 멍청한 놈들이나 하는 짓이다. 이럴 때는 자리를 바꿔 다른 사냥감을 찾는 것이 훨씬 영리한 행동이었다.

그렇게 나름대로의 결론을 내린 흑표가 걸음을 옮기려던 찰나였다.

“어후. 어후우.”

돌아서려던 흑표는 움직임을 멈춘 채 풀숲 너머를 주시했다.

이상한 소리를 내며 헐레벌떡 달려온 인간 하나가 잡초 사이에 쭈그려 앉는 것이 보였다.

“아흐으. 죽을 뻔했네.”

동시에 맹수들도 학을 뗄 만한 소리와 냄새가 이어지자, 세로로 쭉 찢어진 흑표의 동공에 기광이 스쳤다.

확실하다. 저 인간은 배변 활동을 위해 무리에서 떨어져 나온 것이다.

이곳이 자신의 무덤이 될 줄도 모르고.

크릉.

표적은 하나. 그것도 멍청해 보이는 인간.

흑표의 판단과 움직임은 신속했다. 네 개의 다리를 잇는 근육이 한껏 수축되었고, 곧이어 검게 물든 몸뚱어리가 화살과도 같은 속도로 쏘아졌다.

탁, 쉬이이익!

수 장의 거리에 단숨에 지워지고, 그제야 뭔가를 알아차린 인간의 고개가 이쪽을 향해 움직인다.

하지만 반응은 한 박자 늦었고, 쩍 벌어진 흑표의 아가리에서 날카로운 송곳니가 번쩍 빛났다.

- 크아아앙!

푸푹! 콰득!

우렁찬 포효와 함께 울려 퍼지는 파육음. 서로를 향해 뒤섞인 크고 작은 동체가 땅을 나뒹굴었다.

그리고 잠시 후, 이 짧지만 치열했던 전투의 생존자가 살아 있음을 알렸다.

“푸하!”

검은 털들 사이로 얼굴을 내민 사내의 얼굴은 피로 흠뻑 젖어 있었다. 바로 흑표의 피였다.

마지막 순간, 이 근방을 호령하던 맹수의 머리통에 검을 꽂아 넣은 사내는 거칠게 숨을 몰아쉬었다.

“후욱. 훅. 시발. 싸다가 죽을 뻔했네.”

볼일 보는 와중에 기습이라니. 다시 생각해도 정말 아슬아슬했다.

만약 일이 년 전의 자신이었다면 꼼짝없이 흑표의 한 끼 식사가 되었을 것이다.

하지만 씨앗이 싹을 틔우듯, 사내도 과거에 비해 부쩍 성장한 상태였다.

“하도 처맞다 보니까 반사 신경이 늘었…… 그런데 어떻게 빠져나가지?”

사내가 육중하기 짝이 없는 흑표의 사체에 짓눌린 채, 계속해서 낑낑거리고 있던 그때였다.

“희한하군. 잠깐 보러 간다는 볼일이 혹시 이런 거였나?”

귓가를 파고드는 익숙한 목소리에, 사내의 안색이 환하게 밝아졌다.

“오! 송 대협!”

목소리의 주인, 송일섬이 한숨을 내쉬었다.

“대협이라고 부르지 말라니까.”

“왜요. 어려움에 처한 사람을 도와주면 그게 대협 아닙니까.”

“상관을 닮아서 그런지, 말은 아주 청산유수군.”

“저야 기분 좋은 말이긴 한데, 조장님 앞에서는 그런 말 하지 마세요. 아무리 송 대협이라고 해도 청산유수처럼 처맞는 수가 있습니다.”

사내, 아니 혁무진의 영혼에서 우러나오는 충고를 들은 송일섬이 고개를 끄덕였다.

“……음. 참고하지.”

“잘 생각하셨습니다. 그런데 저 이것 좀 치워 주실래요? 슬슬 숨넘어갈 것 같은데. 눈앞에 자꾸 아버지 얼굴이 보여요.”

“그래? 언제 돌아가셨나?”

“무슨 소리세요. 아직 멀쩡하게 살아 계신데.”

“……?”

미친놈인가.

잠깐 진지하게 고민하던 송일섬은 이내 생각을 포기하고 흑표의 시체를 붙잡았다.

어쩌다가 그가 몸담게 된 화룡각에는 제정신인 사람이 드물었다. 물론 그중에서도 각주가 가장 미친놈이다.

스륵. 쿵.

가까스로 압사(壓死)의 위기에서 빠져나온 혁무진이 흙투성이가 된 옷을 털어내며 물었다.

“후우, 죽을 뻔했네. 다른 사람들은요?”

“야영 준비 중이다. 소국주도 그곳에 남아 있고. 벌써 쉬지 않고 열 시진 가까이 달렸으니 휴식이 필요하다고 판단한 모양이야. 네 녀석이 잠깐 자리를 비운 사이에 때마침 전서(傳書)도 도착했고.”

“전서요?”

“그래. 남만야수궁에서 전서응을 보낸 것 같더군. 추가적으로 지시할 게 있었나 보지.”

“어쨌든 반가운 소식이네요. 안 그래도 맹수들 움직임이 너무 거칠어서 엉덩이가 박살 날 뻔했는데.”

“그 녀석들도 쉬어야지. 그래도 남만인들이 평소에도 조련을 잘해 두었는지 체력 하나는 좋더군. 초원마 못지않아.”

지금으로부터 약 하루 전, 척후대와 함께 외궁을 빠져나온 그들은 강행군을 이어 가고 있었다.

혈승(血僧)이라는, 지금까지 듣도 보도 못한 노괴가 언제 광서 땅을 넘어 남하할 줄 모르니 당연한 선택이었다.

“언제쯤 도착한답니까?”

“두 부족장의 말에 의하면 빠르면 이틀. 늦어도 사흘 내에는 도착할 듯싶다. 아마 소국주도 비슷하게 생각하는 것 같고.”

“무슨 일이 있어도 이틀 안에 가야 한다는 소리로 들리는데, 이거 기분 탓입니까?”

“제대로 들었다. 혈승을 막기 위해서는 최대한 빨리 이동해야겠지.”

“지금처럼요?”

“어쩌면 지금보다 더 급하게 움직일 수도.”

“……지금보다 더는 좀.”

떨떠름한 표정을 짓던 혁무진이 이내 고개를 끄덕였다.

“젠장. 뭐 어쩔 수 없죠.”

“생각보다 포기가 빠르군.”

“송 대협도 한 이 년쯤 조장님 따라다녀 보세요. 그 후에는 뭐든 자포자기하게 될 테니까. 물론 목숨도 포함해서요.”

“안타깝지만 그럴 일은 없다.”

“왜요?”

“소국주가 아니었다면 여기까지 오지도 않았을 테니까. 그게 내가 이 지긋지긋한 남만에 있는 단 하나의 이유다.”

칼 같은 대답에 혁무진이 어깨를 으쓱해 보였다.

“음. 그럼 앞으로도 자주 보겠네요.”

“뭐?”

“방금 그 입으로 직접 말씀하셨잖아요. 여기까지 따라온 이유가 주 소저 때문이라고. 그런데 주 소저께서는 앞으로도 조장님과 함께하실 걸요?”

“……!”

“송 대협, 생각보다 머리가 나쁘신 것 같은데요.”

잠시 굳어 있던 송일섬이 담담한 목소리로 물었다.

“죽고 싶나?”

“아뇨. 죄송합니다.”

냉큼 대답한 혁무진이 슬금슬금 눈치를 살피며 흑표의 머리에 박혀 있던 검을 뽑았다.

푸확.

쩍 벌어진 단면에서 솟구치는 핏물. 대충 검신을 닦아 납검(納劍)한 혁무진이 문득 고개를 들어 하늘을 바라봤다.

“벌써 밤이네.”

분명 밤에 출발했던 것 같은데, 정신없이 이동하는 사이 두 번째 밤이 찾아왔다.

그리고 앞으로도 몇 번의 밤이 지나야 다시 남만야수궁으로 돌아갈 수 있을 것이다.

“그래도 가급적이면 혈승은 안 만났으면 좋겠는데. 조장님도 안 계셔서 영 불안하고. 송 대협도 그렇게 생각하시죠?”

하지만 대답은 돌아오지 않았다.

그리고 잠시 후. 짧은 침묵 끝에 들려온 것은, 송일섬의 목소리가 아닌 날붙이의 서늘한 마찰음이었다.

스릉.

등 뒤에서 울려 퍼지는 소리의 정체를 알아차린 혁무진이 마른침을 꿀꺽 삼켰다.

“어, 그. 머리 나쁘다고 해서 죄송합니다. 화 많이 나셨어요?”

차갑게 식은 목소리가 돌아왔다.

“……입 닥치고 돌아서.”

“송 대협. 제발. 부탁드릴게요.”

“나야말로 부탁하지. 제발 입 닥치고 돌아서라. 검도 다시 뽑고.”

이 인간이 진짜 눈깔이 뒤집혔구나.

혁무진은 눈물을 머금은 채, 후들거리는 다리로 돌아섰다.

그리고 그 순간 깨달았다. 왜 송일섬의 목소리가 그토록 차가웠는지. 자신에게 검을 뽑으라고 한 이유가 무엇이었는지.

“분명히 아군이라고 생각했는데…… 내 착각이었나?”

스스슥.

어둠에 잠긴 풀숲이 흔들렸다.

지금껏 함께 이동했던 백여 명의 척후대. 그 선두에서 모습을 드러낸 두 명의 부족장이 착잡한 표정으로 그들을 바라보고 있었다.

“자네만의 착각이 아니었네. 다만 일이 이렇게 되어 유감이야.”

“전서(傳書)를 받았네. 궁의 직인이 찍힌. 우리로서는 결코 거부할 수 없는 명령이지.”

전서.

그 두 글자를 들은 송일섬은 어렴풋이 직감했다. 그들이 떠난 내궁(內宮)에서 무언가 큰일이 벌어졌다는 것을.

하지만 그 무엇보다 중요한 것은, 단 한 사람의 존재였다.

“소국주는 어디 있느냐.”

진득한 살기가 스며든 물음.

친(親) 궁주파이자 대회의 때부터 진태경에게 호의를 품고 있던 장 족장이 한숨을 내쉬며 대답했다.

“생각 이상으로 검이 매섭더군. 눈치도 빠르고.”

“마지막으로 다시 묻는다. 그녀는 어디 있지?”

화아아악!

송일섬의 전신에서 광폭한 살기가 흘러넘쳤다. 척후대에 포함된 맹수들마저 뒷걸음질 칠 정도의 흉포한 기파.

그의 분노를 느낀 또 다른 부족장이 황급히 입을 열었다.

“그, 그녀는 무사하네. 점혈(點穴)로 제압해 두었을 뿐이야.”

송일섬은 자신도 모르게 이를 악물었다. 안도감과 동시에 후회가 물밀듯이 밀려들었다.

‘무슨 일이 있어도 곁을 지켰어야 했는데.’

아군에서 적으로 돌변한 척후대의 규모를 생각한다면, 설령 송일섬이 남아 있었더라도 결과는 크게 달라지지 않았을 것이다.

하지만…… 홀로 분투했을 주화란의 모습이 자꾸만 눈앞에 그려지는 듯했다.

“……빌어먹을.”

씹어뱉는 듯한 욕설과 함께, 송일섬은 손아귀에 쥐고 있던 애병을 천천히 늘어트렸다.

그리고 그것은 그보다 늦게 상황을 알아차린 혁무진 역시 마찬가지였다.

스륵, 푸푹.

공들여 벼려 낸 검신이 지면을 파고든다.

착잡한 눈빛으로 그 광경을 바라보던 장 족장이 손짓하자, 그의 명령을 따르는 척후대의 전사들이 달려와 무기를 회수하고 두 사람을 포박했다.

“……송 대협. 저희 아무래도 좆 된 것 같은데요.”

혁무진의 중얼거림에, 이번에도 송일섬은 대답하지 않았다. 아니, 대답할 수 없었다.

투두둑.

전신 곳곳을 두드리는 누군가의 손길. 점혈과 함께 뻣뻣해지는 몸뚱어리를 느끼며, 송일섬은 마음속으로 뇌까렸다.

‘도대체 무슨 짓을 벌인 거냐, 진태경.’
```

## Final English reading copy

```markdown
# Chapter 659

Crack.

A large, fur-covered paw stepped on a brittle leaf.

Sharp fangs briefly showed between parted jaws. The sleek body crouched low among the grass had already finished preparing for the hunt.

*What kind of meat will I eat today?*

Once it spotted a noticeable target, all it had to do was sprint over and sink its fangs into the prey’s neck.

As long as it avoided venomous beasts that appeared without warning, finding prey in Nanman was not particularly difficult.

At least, that was true for the black leopard, which occupied the upper levels of the brutal food chain.

Grrrr…

The black leopard scanned its surroundings with bright yellow eyes before suddenly letting out a low growl.

It had sensed countless presences in the distance and caught a scent carried on the wind.

Sniff, sniff.

Like any predator, the black leopard possessed keen senses. It did not take long to identify the prey that had wandered into its territory earlier than expected.

Humans.

More accurately, it was a group of humans. Roughly a hundred of them were approaching this place.

Grrr.

The black leopard unconsciously let out an irritated growl.

Humans were not particularly welcome creatures in the black leopard’s eyes.

Despite their small bodies, they sometimes hunted predators much larger than themselves. And the more numerous they were, the greater their strength became.

Just like now.

Swish.

The black leopard rose from its crouch.

Only fools hunted humans alone. At times like this, it was much smarter to change locations and search for other prey.

The black leopard reached that conclusion and was just about to move when—

“Whew. Whew…”

The black leopard stopped and stared beyond the grass.

One human came running up, making a strange noise, then squatted down among the weeds.

“Ahh. I almost died.”

At the same time, sounds and smells that would have made even predators recoil filled the air. A glint flashed through the black leopard’s vertically slit pupils.

There was no doubt. That human had separated from the group to relieve himself.

Without realizing that this place would become his grave.

Grrr.

One target. And, what was more, a human who looked stupid.

The black leopard’s judgment and movements were swift. The muscles connecting its four legs contracted to their limit, and a moment later, its black body shot forward like an arrow.

Tap—whoosh!

Several dozen feet vanished in an instant. Only then did the human notice something and turn his head toward the leopard.

But his reaction was a beat too slow, and the sharp fangs inside the black leopard’s wide-open jaws flashed.

—Raaaar!

Thud! Crunch!

The sound of flesh being torn rang out beneath the beast’s thunderous roar. Large and small bodies tangled together and rolled across the ground.

Then, a short while later, the survivor of that brief but fierce battle announced that he was still alive.

“Phew!”

The face of the man emerging from among the black fur was drenched in blood.

The black leopard’s blood.

At the final moment, the man had driven his sword into the head of the predator that ruled this area. Now he was breathing heavily.

“Huff. Hah. Fuck. I almost died while taking a dump.”

Being ambushed while relieving himself. Even thinking about it again, it had been incredibly close.

If this had been him one or two years ago, he would have helplessly become the black leopard’s meal.

But just as a seed sprouted, the man had also grown tremendously compared to the past.

“I’ve been beaten so much that my reflexes have improved… But how am I supposed to get out of here?”

The man—Hyuk Mujin—was still trapped beneath the impossibly heavy carcass of the black leopard, struggling and grunting, when—

“That is strange. Was this the errand you said you were stepping away to take care of?”

At the familiar voice that pierced his ears, Hyuk Mujin’s face brightened.

“Oh! Great Hero Song!”

Song Ilseom, the owner of the voice, sighed.

“I told you not to call me Great Hero.”

“Why not? If you help someone in trouble, doesn’t that make you a Great Hero?”

“Perhaps you resemble your superior. Your words certainly flow like a mountain stream.”

“That’s a compliment, so I appreciate it. But please don’t say things like that in front of Captain. Even you, Great Hero Song, might get beaten into a babbling stream.”

Song Ilseom nodded at the advice that came straight from Hyuk Mujin’s soul.

“…I’ll keep that in mind.”

“Good thinking. But could you move this thing for me? I’m starting to feel like I’m about to stop breathing. I keep seeing my father’s face.”

“Really? When did he pass away?”

“What are you talking about? He’s still alive and well.”

“…?”

*Is this man insane?*

Song Ilseom seriously considered the question for a moment before giving up and grabbing the black leopard’s corpse.

There were few sane people in the Fire Dragon Pavilion he had somehow ended up joining.

Of course, the Pavilion Master was the craziest of them all.

Swish. Thud.

Hyuk Mujin barely escaped the threat of being crushed to death. He brushed the dirt from his clothes and asked,

“Whew, I almost died. Where are the others?”

“They’re preparing camp. The Young Bureau Head is there as well. We’ve already been running for nearly ten shichen without rest, so she seems to have decided we need a break. A missive arrived just as you stepped away.”

“A missive?”

“Yes. It seems the Nanman Beast Palace sent a messenger eagle. They must have had additional instructions for us.”

“Either way, that’s good news. The beasts have been moving so violently that I nearly shattered my rear end.”

“They need to rest too. Still, the Nanman people must train them well. Their stamina is impressive. They’re no worse than grassland horses.”

About a day earlier, they had left the Outer Palace with the reconnaissance squad and continued their forced march.

Since they had no idea when the unidentified old monster known as the Blood Monk might cross through Guangxi and head south, it was the obvious choice.

“When do they say we’ll arrive?”

“According to the two tribal chieftains, the earliest would be two days. At the latest, we should arrive within three. The Young Bureau Head seems to think the same.”

“It sounds like we absolutely have to get there within two days. Is that just me?”

“You heard correctly. To stop the Blood Monk, we need to move as quickly as possible.”

“Like this?”

“Perhaps even faster.”

“…Anything faster than this is a bit much.”

Hyuk Mujin made a displeased face, then nodded.

“Damn. It can’t be helped.”

“You give up quickly.”

“Follow Captain around for about two years, Great Hero Song. After that, you’ll give up on everything. Your life included.”

“Unfortunately, that won’t happen.”

“Why not?”

“If it weren’t for the Young Bureau Head, I wouldn’t have come this far. That is the sole reason I’m in this wretched Nanman.”

At that sharp reply, Hyuk Mujin shrugged.

“Hmm. Then I guess we’ll be seeing you often.”

“What?”

“You just said it yourself. The reason you followed us this far was Young Lady Ju. And Young Lady Ju will be with Captain from now on too, won’t she?”

“……!”

“Great Hero Song, you seem dumber than I expected.”

Song Ilseom stood frozen for a moment before asking in a calm voice,

“Do you want to die?”

“No. I’m sorry.”

Hyuk Mujin answered promptly, then cautiously watched Song Ilseom as he pulled the sword from the black leopard’s head.

Fwoosh.

Blood spurted from the gaping wound. Hyuk Mujin roughly wiped the blade clean, sheathed it, and suddenly raised his head to look at the sky.

“It’s already night.”

They had apparently set out at night, but while moving without a moment to think, the second night had already arrived.

And several more nights would have to pass before they could return to the Nanman Beast Palace.

“Still, I’d rather not meet the Blood Monk if possible. I’m uneasy without Captain here. You feel the same way, right, Great Hero Song?”

But no answer came.

And shortly afterward, following a brief silence, the sound that reached his ears was not Song Ilseom’s voice but the cold scrape of a blade.

Shing.

Hyuk Mujin recognized the sound coming from behind him and swallowed dryly.

“Uh, about that. I’m sorry for saying you were dumb. Are you very angry?”

A voice, cold as ice, came from behind him.

“…Shut up and turn around.”

“Great Hero Song. Please. I’m begging you.”

“I’m begging you too. Shut up and turn around. Draw your sword again.”

*This guy’s really lost his mind.*

With tears in his eyes, Hyuk Mujin turned around on trembling legs.

And in that moment, he realized why Song Ilseom’s voice had been so cold. He understood why Song Ilseom had told him to draw his sword.

“I was sure they were allies… Was I mistaken?”

Rustle, rustle.

The grass, cloaked in darkness, shook.

The hundred-strong reconnaissance squad had traveled with them until now. At its head, the two tribal chieftains emerged and stared at them with grim expressions.

“It wasn’t just your mistake. But I regret that things have come to this.”

“We received a missive. It bears the Palace’s seal. It is an order we cannot refuse.”

A missive.

The moment Song Ilseom heard those two words, he had a vague intuition that something serious had happened in the Inner Palace they had left behind.

But more important than anything else was the existence of a single person.

“Where is the Young Bureau Head?”

Killing intent seeped into his voice.

Chief Jang, who belonged to the pro-Palace Lord faction and had favored Jin Taekyung since the Tribal Grand Council, sighed as he answered,

“Her sword was fiercer than I expected. She was quick to catch on, too.”

“I’ll ask one last time. Where is she?”

Whoosh!

Fierce killing intent overflowed from Song Ilseom’s entire body. His brutal aura was so vicious that even the beasts among the reconnaissance squad took several steps back.

Another tribal chieftain, sensing his fury, hurriedly opened his mouth.

“Sh-she’s safe. We only subdued her with a Pressure-Point Strike.”

Song Ilseom clenched his teeth before he even realized it. Relief and regret surged through him at the same time.

*I should have stayed by her side, no matter what.*

Considering the size of the reconnaissance squad that had turned from allies into enemies, the result probably would not have changed much even if Song Ilseom had remained behind.

But… he could not stop picturing Ju Hwaran fighting alone.

“…Damn it.”

As he spat out the curse, Song Ilseom slowly lowered the cherished weapon in his hand.

Hyuk Mujin, who had realized what was happening slightly later, did the same.

Swish. Thud.

The carefully forged blade pierced the ground.

Chief Jang watched the scene with a troubled gaze, then gestured. Warriors from the reconnaissance squad obeyed his command, rushing over to retrieve the weapons and bind the two men.

“…Great Hero Song. I think we’re seriously fucked.”

Song Ilseom did not answer Hyuk Mujin’s mutter this time either.

No, he could not answer.

Tap, tap, tap.

Someone’s fingers tapped all over his body. As he felt his body stiffen under the Pressure-Point Strike, Song Ilseom muttered inwardly,

*What on earth have you done, Jin Taekyung?*
```
