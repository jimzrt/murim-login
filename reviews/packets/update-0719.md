<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0719.txt",
      "sha256": "0a2d5e8c33536b833d8c37c4690bae68f01110484ff61fef3e89b97588f596b0",
      "bytes": 13800
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a7001b2f4f3a3895747a43261b569d42c38c7bfc3fa31336403413ed8106890f",
      "bytes": 1894
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91a3a66cd8c4494676c8e3729299c8ac8ec06db73a599c8c8a4efc8085c6d7d5",
      "bytes": 208479
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "4e2027fe698cc600f3f84dd016dd40e11eb87fddd630bb021677490c6aea891b",
      "bytes": 846
    },
    {
      "path": "characters/Guardian Spirit.md",
      "sha256": "0af395f8d266e7784c2d8116da8ab76d1d6a532f47f2a6b4abc87c59e1ae8793",
      "bytes": 645
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "532e33e1bbd09f3aa296ed8e7fdd91326496aa609bbcac2b33476744fd40bb33",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e4cca24f23443fe03313a01caf638e908a5e9b1e276cd20f965d1f47b9eb35d6",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "aed8b09365283f1c99df12fa9505afac3a67f6c0fe8ea8d5f56693caec1100db",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "41451fbcb303b91e11f3912ea1af46c6fe45a20a3431e2aea2700f197d007d06",
      "bytes": 667
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "af290afc496aac0866baf0965924384cb42cacad7edebd160c375a37e2a8daea",
      "bytes": 715
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "090ed3ec369aa0e8c47dcbef84d23ceff50ef3b8e4654707804b7f280de7befc",
      "bytes": 676
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "225069fa427f3f46fb581272df035aac52235bc4f834a28416412650761168fc",
      "bytes": 659
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "519eee7ae98e06be8e02af11b42f6310924447705f52480f04f6d656428a5a6a",
      "bytes": 219004
    }
  ],
  "estimated_tokens": 12390
}
-->

# Durable State Update — Chapter 719

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 719. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 719. Profile updates may replace only one
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
  "chapter": 719,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 719,
    "continuity_sources": [719],
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
    "The Beast Miao King has returned to the Inner Palace and resumed leadership of Nanman after withdrawing to grieve.",
    "The Beast Miao King wanted to save Baeksang, his sworn younger brother, but Baeksang refused to be spared and chose his own death.",
    "The Beast Miao King feels grief and self-reproach over allowing personal feelings to conflict with his duty as Palace Lord.",
    "Jin Taekyung told the Beast Miao King that Nanman still needs him as its forest keeper.",
    "Two unnamed memorial tablets were placed in the shrine for Baeksang and Baekhwi, and Jin bowed before them.",
    "Jin Taekyung feels sympathy for Baeksang because he can imagine himself taking a similar path under comparable circumstances.",
    "The Nanman leadership regained stability after the Beast Miao King's return.",
    "The guardian spirit's sacred stone absorbed the demonic qi from the rift and became a demonic stone.",
    "The Beast Miao King is currently suppressing the demonic qi within the demonic stone.",
    "The Beast Miao King summoned Jin Taekyung and Jeok Cheongang to decide how the demonic stone should be handled.",
    "The System displayed the acceptance prompt for the Quest [Corrupted Divine Artifact]."
  ],
  "continuity_sources": [
    718
  ],
  "open_questions": [
    "How will Jin Taekyung and the others handle the demonic stone?",
    "Will Jin Taekyung accept the Quest [Corrupted Divine Artifact]?"
  ],
  "safe_through": 718,
  "temporary_decisions": [
    "Render 마석 as demonic stone, distinct from 신석 as sacred stone.",
    "Render 타락한 신물 as Corrupted Divine Artifact.",
    "Render 적 노 as Old Master Jeok, consistent with the established rendering of 노야.",
    "Retain established renderings for 대형 as Big Brother, 남만당 as Nanman Party, and 각주 as Pavilion Master."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 중원     | **Central Plains**                               |                                                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 진태경 | 무야호 | human ally to intelligent spiritual beast | Muyaho | quiet and familiar | Jin whispers that they should go as Muyaho advances with the guardian spirit. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 수호령 | 적천강 | guardian_spirit_to_legendary_martial_master | old human | terse and contemptuous | The guardian spirit addresses Jeok as 늙은 인간 while recognizing that his essence has not changed. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 718
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people who has resumed leadership of Nanman after the rift disaster.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Guardian Spirit.md

# Guardian Spirit (수호령)

- **Safe through:** Chapter 718
- **Aliases:** None
- **Role:** The Guardian Spirit was a divine-beast-like tiger that sacrificed itself to seal the rift and was killed after becoming corrupted.
- **Personality:** The Guardian Spirit was self-sacrificing and chose death rather than allow its corruption to continue.
- **Voice:** The Guardian Spirit communicates through roars and terse cries; no sustained speech is established.
- **Relationships:** The Guardian Spirit asked Jin Taekyung and Jeok Cheongang to kill it if corruption overcame it.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 718
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 718
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 718
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 708
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature advancing with Jin Taekyung, Yohi, and the beast army.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 717
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 712
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit and protector of the land; after absorbing the sacred stone, it entered the rift to seal it despite the risk of corruption and death.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger shared a roughly three-hundred-year friendship with Yayul Cheon, once refused his request for aid, and now trusts Jin Taekyung and Jeok Cheongang to kill it if the rift corrupts it.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 716
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who returned to the Nanman Beast Palace with Jin Taekyung and voluntarily entered the underground prison after siding with Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃719화



퀘스트, [타락한 신물]을 수락하시겠습니까?

Y / N



갑작스럽게 눈앞에 떠오른 홀로그램 창은 이뿐만이 아니다.

나는 새롭게 생성된 퀘스트 정보를 빠르게 눈으로 훑었다.



퀘스트



[타락한 신물]



한때 이 땅을 수호하던 신석(神石)은 이미 본래의 모습을 잃어버렸습니다.

마기에 잠식당한 그것은 또 다른 재앙의 불씨와 같으며, 당신은 어떤 방식으로든 이 타락한 신물을 처분해야 합니다.



등급 : 초절정

제한 : 진태경

임무 : [타락한 신물] 처분 (미완료)

보상 : 임무 수행 방식에 따라 변동

실패 : [타락한 신물]의 마기 증가





퀘스트 정보창을 끝까지 읽은 나는 조용히 마음속으로 뇌까렸다.

‘수락.’



- 퀘스트, [타락한 신물]을 수락하셨습니다!



지금까지 반강제로 진행되었던 몇몇 퀘스트와는 달리 이번에는 버젓이 선택지가 있었지만, 내게 있어 이건 거부할 수 없는 제안이나 마찬가지였다.

‘언제까지 마기를 억누르고 있을 수만은 없어.’

신석. 아니, 마기에 잠식당한 [타락한 신물]은 언제 터져도 이상하지 않을 폭탄이나 다름없다.

그나마 갖고 있던 인물이 야수묘왕이라 다행이었지, 어지간한 절정 고수라 해도 저것에 담긴 마기를 감당할 수 없었을 것이다.

‘퀘스트 정보창에 적혀 있는 내용처럼, 어떻게든 처리해야 한다.’

균열을 닫기까지 얼마나 많은 희생을 치러야 했던가.

마지막 순간 스스로 몸을 내던졌던 수호령을 생각해서라도 저 폭탄이 터지는 것만큼은 막아야 했다.

그리고 지금 이 순간, 이와 같은 생각을 떠올린 것은 나 혼자만이 아니었다.

“이 정도의 마기라니, 안 되겠군.”

눈살을 찌푸린 채 중얼거린 적천강이 나와 야수묘왕을 향해 손짓했다.

“빠져 있어라. 노부가 처리할 테니.”

적천강이 한 말의 의미를 짐작한 듯, 야수묘왕의 눈동자가 크게 뜨였다.

“적 노, 그 말씀은 설마.”

“네놈이 생각하는 그 설마가 맞다. 화근이 될 가능성이 있다면 아예 싹을 뽑아 버려야지.”

“하지만 이건…… 결코 쉽게 파괴할 수 있는 성질의 것이 아닙니다.”

그리고 우려를 표하는 야수묘왕에게 돌아온 적천강의 대답은, 실로 짧고 간결했다.

“그건 네놈이나 그렇고.”

“…….”

“난 돼.”

그야말로 씹상남자식 화법.

짤막한 한마디로 남만 최고의 짐승남인 야수묘왕마저 입 닥치게 만든 적천강이 천천히 손을 뻗었다.

화아악.

그의 손을 타고 모여들기 시작한 열양지기가 끔찍한 열기를 토해 낸다. 사방에서 피어오르는 아지랑이에 흡사 공간이 일그러지는 듯한 착각마저 들 정도다.

하지만…….

“노야.”

고심 끝에 불쑥 튀어나온 한 마디.

막 출수(出手)하려던 적천강이 문득 움직임을 멈췄다.

“뭐냐?”

“안 하는 게 좋을 것 같은데요. 그거.”

“왜?”

“나름대로 좀 생각해 봤는데, 함부로 건드리면 재미없을 것 같아서요.”

“뭐라?”

내 진중한 목소리에, 적천강이 눈을 크게 떴다.

“아니, 네놈이 생각이란 걸 했단 말이냐?”

“…….”

말문이 턱 막히네, 아주.

짜게 식은 내 표정을 바라보며 헛기침한 적천강이 입을 열었다.

“이대로 두면 언제고 화근이 된다. 한시라도 빠르게 처리하는 것이 맞아.”

“그건 저도 알죠.”

“아는 놈이 왜 그러느냐? 노부가 못 미더워서?”

“어허. 말씀을 왜 그렇게 하세요. 제가 노야 아니면 누구를 믿는다고.”

대답은 이렇게 했지만, 사실 절반 정도는 그런 마음이 없지 않아 있다.

좀 더 정확히 말하자면, 적천강이 못 미더워서가 아니라 혹시나 하는 우려 때문이다.

‘만약에 완전히 파괴하지 못한다면?’

지금의 [타락한 신물]은…… 예를 들자면 내 앞에 놓여 있는 찻잔 같은 거다.

잔이 온전하다면 찻물은 흘러넘치지 않는다. 그러나 찻잔이 깨지면, 찻물은 사방으로 넘쳐 흐를 것이다.

‘마기를 억누르지 못하게 되면, 그땐 또 한 번 지랄 나는 거고.’

미친 호랑이 한 마리가 아무리 날뛰어 봤자 때려잡으면 그만이다. 하지만 마기가 퍼져 나간다면 골치가 아파진다.

아니, 그때는 골치 아픈 정도로 끝나면 다행이겠지.

그래서 적천강을 말려야 했다.

내가 얼마나 그를 신뢰하느냐와는 관계없이, 이런 도박에 다른 사람의 목숨을 판돈으로 밀어 넣을 수는 없으니까.

‘그게 천분의 일. 만분의 일밖에 되지 않는 확률이라 해도 지금은 안 돼.’

이미 너무 많은 피를 흘렸다.

장렬히 싸우다 죽고, 이지를 상실한 괴물이 되어 죽고, 칼 한 번 잡아본 적 없는 이들조차 그 지옥도를 탈출하는 과정에서 적지 않게 죽어 나갔다.

아마 수호령이 스스로를 희생하여 균열을 닫지 않았다면, 지금쯤 피해는 눈덩이처럼 불어났을…… 잠깐.

‘수호령?’

문득 떠오른 기시감과 함께 그 세 글자가 뇌리에서 빙글빙글 맴돈다.

녀석을 처음 만난 날부터 지금까지의 기억들이 차례차례 눈과 귀를 스치고, 마침내 한 줄기 깨달음을 향해 달려 나갔다.

그리고 어느 순간.

“아.”

나도 모르게 입술을 비집고 흘러나온 외마디 탄성.

이놈이 갑자기 왜 이러나, 하는 표정으로 나를 바라보던 적천강과 야수묘왕이 차례대로 입을 열었다.

“그래, 갑자기 왜 또 혼자서 지랄 염병이냐? 노부도 좀 알자.”

“무슨 묘책(妙策)이라도 떠오른 게 아니겠습니까?”

글쎄. 이걸 묘책이라고 부를 정도인지는 모르겠다.

적어도 아직까지는.

하지만 지금 내가 품고 있는 짐작이 사실이라면…… 충분히 시도해 볼 만하다.

‘적어도 손해 볼 건 없겠지.’

내심 중얼거린 나는, 아직 닫지 않은 퀘스트 창과 대답을 기다리고 있는 두 사람의 얼굴을 차례대로 바라보았다. 그리고 어깨를 으쓱하며 입을 열었다.

“두 분 모두, 잠깐 저랑 같이 바람 좀 쐬시죠.”



* * *



두두두두!

일제히 바람을 가르며 달려나가는 일단의 무리는 조촐했다. 아니, 머릿수만 보면 ‘무리’라는 단어 자체부터 어불성설일지도 모른다.

호랑이 셋에 사람 셋.

하지만 가까이에서 그 면면을 살피면 이야기는 달라진다. 당장 내 양옆으로 달려 나가는 두 사람만 해도 그렇다.

“짐승이 빨라 봤자 얼마나 빠를까 싶었는데, 이것도 썩 나쁘진 않구먼. 안장도 편안하고.”

흥미로운 눈빛으로 열심히 달려나가는 호랑이를 요모조모 뜯어보는 적천강의 모습에, 왼편에서 달려 나가던 야수묘왕이 넙죽 대답했다.

“저희 남만야수궁에서도 가장 용맹하고 빠른 녀석 중 하납니다. 정마대전 당시에 저와 함께 참전한 녀석의 후손이기도 하지요.”

“오호. 그 막사 앞에 웅크려 앉아있던 커다란 놈? 기억나는군. 왠지 낯이 익다 싶었지.”

그래. 좌청룡 우백호가 별거냐.

좌화왕 우묘왕이라는 이 미친 라인업에 가슴이 절로 웅장해진다.

설령 남천마후가 살아 돌아와도 발라 먹을 수 있는 무시무시한 전력.

국밥보다 더한 든든함을 느끼는 내 귓가로 이어진 두 사람의 대화가 두런두런 들려왔다.

“이놈 보면 볼수록 괜찮은데. 체력 좋고. 발도 빠른 데다 딱 봐도 영특해 보이고.”

야수묘왕이 흐뭇하게 웃었다.

“제가 특별히 공들여 키웠지요. 새끼 시절에는 워낙 입이 짧아 고생했는데, 그럴 때마다 제가 손수 젖까지 먹여 가며 키운 녀석입니다.”

“뭣이? 네놈이 직접?”

“……말이 그렇다는 거지. 지금 적 노께서 생각하시는 그런 건 아닙니다.”

야수묘왕의 우람한 대흉근을 유심히 살피던 적천강이 고개를 끄덕였다.

“뭐, 그렇다 치지.”

“아니, 그렇게 말씀하시면 뭔가 이상…….”

“여하튼 됐다. 이놈은 노부가 데려가는 것으로 하지.”

그 순간, 야수묘왕의 입가에 맺혀 있던 미소가 사라졌다.

“예?”

“뭘 되물어? 그럼 중원까지 돌아가는 길에도 뭐 빠지게 뛰게 할 생각이었느냐?”

“그, 그건 당연히 아닙니다만, 지금 타고 계신 녀석은 후배가 늘그막에 자식처럼 기른 놈이라…….”

“줘.”

“아니 그.”

“해 줘.”

“…….”

“정 싫으면 저 녀석을 데려가지. 딱 봐도 영물 같은데.”

적천강이 지목한 ‘저 녀석’을 바라본 야수묘왕이 황급히 고개를 내저었다.

“헉. 저 녀석만큼은 안 됩니다. 애당초 잠시 빌려온 거고요.”

“노부가 된다면?”

“제, 제가 직접 기른 것도 아니고, 아비가 되어 자식놈이 형제처럼 생각하는 놈을 어떻게 보내겠습니까.”

“오늘따라 하늘이 맑구나. 혓바닥은 길고.”

잠시 침묵하던 야수묘왕이 침울한 목소리로 대답했다.

“……알겠습니다. 지금 타고 계신 녀석을 내어 드리지요.”

“그렇게 권하니 어쩔 수 없지. 네 호의를 받아들이마.”

“…….”

웅장하긴 개뿔이.

그 노망났던 화왕이 맞나. 화왕은 진짜 전설이다…….

그리고 내가 조촐해진 가슴을 애써 가다듬고 있을 때, 나를 태우고 열심히 달려가던 ‘저 녀석’이 낮은 울음소리를 흘렸다.

크르릉.

슬쩍 눈까지 마주치는 모습을 보아하니, 저놈도 자신이 지금 막 화왕이라는 개장수 손아귀에서 간신히 벗어났다는 걸 아는 모양이다.

불쌍한 마음이 든 나는 파르르 떨리는 새하얀 털을 부드럽게 쓸어 주었다.

“괜찮아, 인마. 넌 살아남았어.”

끼이잉.

어미 잃은 강아지처럼 처연한 울음소리를 흘린 무야호가 슬그머니 걸음을 늦추었다.

적천강 앞에서 뛰어난 모습을 보여 봤자 중원 땅까지 끌려갈 확률만 높아진다는 걸 본능적으로 깨달은 것이 분명했다.

다행히도, 적천강의 관심은 다른 곳으로 옮겨 간 직후였다.

“저건……?”

서서히 흐려지는 말꼬리.

적천강이 바라보는 방향의 끝에는, 완전히 전소(全燒)되다시피 한 민둥산이 있었다.

아니, 저 볼품없는 민둥산에도 이름은 있다.

애뇌산(哀牢山)이라는, 이 땅에서 살아가는 이들이라면 모를 수 없는 이름이.

그리고 내가 막 그에 관하여 설명하려던 그 순간, 적천강이 눈을 부릅뜨며 외쳤다.

“감히 어떤 호로 개잡놈의 새끼가 소중한 산천초목을 태워 먹었단 말이냐!”

“…….”

“…….”

찰나지간. 나는 야수묘왕과 뜨겁게 눈빛을 교환했다. 그리고 분노에 가득 찬 목소리로 대답했다.

“암천이요.”

간혹 어떤 종류의 진실은, 알려지지 않는 것이 아름답다.



* * *



비로소 저 볼품없는 민둥산이 우리의 목적지라는 것을 알게 된 적천강은. 대뜸 눈살부터 찌푸렸다.

“나무 심으러 여기까지 온 게냐?”

“……그. 진심으로 궁금해서 여쭤보는 건데, 혹시 절 어느 정도로 미친놈으로 생각하시는 겁니까?”

말도 안 되는 소리다.

오늘은 식목일도 아니고, 식목일이라 해도 나무는 안 심을 거다. 내가 이들과 함께 민둥산이 되어 버린 애뇌산을 찾은 목적은 처음부터 정해져 있었다.

“이쪽으로.”

그리고 내가 향하는 곳이 어디인지, 야수묘왕은 얼마 지나지 않아 깨닫게 되었다.

“독혈지로군. 아니. 이제는 성지(聖地)라고 불러야 하나?”

야수묘왕이 모르는 것이 더 이상하다. 그 내용이 상세하지는 않더라도, 무슨 일이 있었는지 정도는 요희에게 대강 들었을 테니까.

하지만 그의 뇌까림을 들은 나는 고개를 저었다.

“다릅니다. 독혈지는 독혈지고, 성지는 성지일 뿐이에요.”

두 공간은 엄연히 분리되어 있다. 독혈지가 인간에 의해 세워진 죽음의 땅이라면, 성지는 남만의 심장이자 생명의 땅이다.

‘그래, 생명 그 자체지.’

내심 중얼거린 나는 손에 쥐고 있던 [타락한 신물]을 땅에 내려놓았다.

안개와도 같은 마기가 흘러나오고, 무야호가 낮은 울음소리를 흘린다.

그러나 어둠에 잠식당했을지라도, 그 본질은 변하지 않았다.

스아아아아.

마치 심장이 뛰듯이 맥동하는 땅. 그와 함께 아득한 세월 동안 감춰져 있던 또 다른 세상이 한 꺼풀 벗겨진다.

동시에 보였다.

따스한 광휘가 온 사방에 가득한 또 다른 공간이. 그 중심에서 그 어떤 것보다 찬란하게 빛나는 자그마한 연못이.

“아.”

“저건…….”

적천강과 야수묘왕이 토해 낸 탄성이 끝을 맺지 못하고 흩어진다.

하지만 나는 알고 있다. 그들이 무엇을 느꼈는지. 그리고 이제 내가 무엇을 해야 하는지.

‘정화(淨化).’

오늘이 바로, 새로운 신석(神石)이 탄생하는 날이다.
```

## Final English reading copy

```markdown
# Chapter 719

> **System**
>
> **Quest:** Corrupted Divine Artifact
>
> Will you accept?
>
> **Y / N**

The holographic window that suddenly appeared before me wasn’t the only one.

I quickly skimmed the information for the newly created Quest.

> **System**
>
> **Quest**
>
> **Corrupted Divine Artifact**
>
> The sacred stone that once protected this land has already lost its original form.
>
> Consumed by demonic qi, it is like the spark of another calamity, and you must dispose of this Corrupted Divine Artifact by some means or another.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Dispose of Corrupted Divine Artifact (Incomplete)
>
> **Reward:** Varies according to how the mission is carried out
>
> **Failure:** Increase in the Corrupted Divine Artifact’s demonic qi

After reading the Quest information window to the end, I muttered quietly to myself.

*Accept.*

> **System**
>
> You have accepted the Quest **Corrupted Divine Artifact**!

Unlike the several Quests I’d been more or less forced to undertake until now, this one offered me an actual choice. But to me, it was no different from an offer I couldn’t refuse.

*I can’t keep suppressing the demonic qi forever.*

The sacred stone—or rather, the Corrupted Divine Artifact consumed by demonic qi—was no different from a bomb that could explode at any moment.

It was fortunate that the person in possession of it was the Beast Miao King. Even an ordinary Peak master wouldn’t have been able to withstand the demonic qi contained within it.

*Just like the Quest information says, we have to deal with it somehow.*

How many sacrifices had it taken to close the rift?

If only for the sake of the guardian spirit that had thrown itself into the breach at the final moment, I had to prevent that bomb from exploding.

And at that very moment, I wasn’t the only one thinking along those lines.

“Demonic qi of this magnitude… This won’t do.”

Jeok Cheongang muttered with a frown, then gestured toward the Beast Miao King and me.

“Stand aside. This old man will take care of it.”

As if he had guessed what Jeok Cheongang meant, the Beast Miao King’s eyes widened.

“Old Master Jeok, surely you don’t mean…”

“You thought it, didn’t you? If there’s even a chance it could become a source of trouble, we need to pull it out by the roots.”

“But this… isn’t something that can be destroyed easily.”

Jeok Cheongang’s answer to the Beast Miao King’s concern was extremely brief and simple.

“That’s true for you.”

“……”

“I can do it.”

That was some fucking macho-man talk.

With a single short sentence, Jeok Cheongang had even silenced the Beast Miao King—the most beastly man in all Nanman—as he slowly stretched out his hand.

*Whoosh.*

Scorching Yang Qi began to gather along his hand, radiating such dreadful heat that the air seemed to distort amid the haze rising from every direction.

But then…

“Old Master.”

The words slipped out after a moment of consideration.

Jeok Cheongang, who had been about to strike, suddenly stopped moving.

“What?”

“I don’t think you should do it. That.”

“Why?”

“I gave it some thought, and I have a feeling things could get ugly if we mess with it carelessly.”

“What?”

At my solemn voice, Jeok Cheongang’s eyes widened.

“You mean you actually thought about something?”

“……”

I was completely at a loss for words.

Jeok Cheongang looked at my thoroughly deflated expression, cleared his throat, and opened his mouth.

“If we leave it like this, it will become a source of trouble sooner or later. We need to deal with it as quickly as possible.”

“I know that.”

“Then why are you stopping me? Because you don’t trust this old man?”

“Oh, come on. Why would you put it that way? Who else would I trust if not you, Old Master?”

That was what I said, but truthfully, about half of me did feel that way.

To be more precise, it wasn’t that I didn’t trust Jeok Cheongang. I was simply worried about what might happen.

*What if he fails to destroy it completely?*

The Corrupted Divine Artifact before me was, for example, like the teacup sitting in front of me.

As long as the cup remained intact, the tea wouldn’t spill. But if the teacup broke, the tea would overflow in every direction.

*If the demonic qi can no longer be contained, then we’ll have another goddamn disaster on our hands.*

No matter how wildly a single mad tiger rampaged, it could simply be beaten down. But if the demonic qi spread, things would become much more troublesome.

No. If that happened, it would be a blessing if trouble was all it amounted to.

That was why I had to stop Jeok Cheongang.

Regardless of how much I trusted him, I couldn’t put someone else’s life on the table as the stake in a gamble like this.

*Even if the odds are only one in a thousand—or one in ten thousand—it’s still not worth it right now.*

We had already spilled too much blood.

Some had died after fighting to the bitter end. Some had died after losing their minds and becoming monsters. Even people who had never held a sword in their lives had died in considerable numbers while escaping that hellscape.

If the guardian spirit hadn’t sacrificed itself to close the rift, the casualties would have multiplied like a snowball by now…

Wait.

*The guardian spirit?*

Along with the sudden sense of déjà vu, that name began circling endlessly through my mind.

The memories from the day I first met it until now brushed past my eyes and ears one after another, racing toward a single thread of enlightenment.

And then, at some point—

“Ah.”

A short exclamation escaped between my lips before I realized it.

Jeok Cheongang and the Beast Miao King looked at me as though wondering what the hell had suddenly happened to me, then spoke in turn.

“Yeah, why the fuck are you suddenly throwing a fit all by yourself again? Let this old man in on it.”

“Have you perhaps thought of some brilliant strategy?”

I wasn’t sure whether it was brilliant enough to deserve that name.

At least, not yet.

But if my current suspicion was true… it was certainly worth trying.

*At least we won’t lose anything by trying.*

I glanced in turn at the Quest window that was still open and the faces of the two men waiting for my answer. Then I shrugged and opened my mouth.

“Why don’t both of you come outside with me for a bit?”

* * *

*Thud-thud-thud-thud!*

The party racing forward as it cut through the wind was a small one. In fact, judging by the head count alone, even calling them a *party* might have been an exaggeration.

Three tigers and three people.

But the picture changed when you looked closely at those three people. The two racing along on either side of me were enough to prove that.

“I wondered how fast a beast could really be, but this isn’t bad at all. The saddle’s comfortable, too.”

Jeok Cheongang was closely examining the tiger racing along beneath him with an intrigued gaze. The Beast Miao King, riding to my left, readily answered.

“He’s one of the bravest and fastest beasts in the Nanman Beast Palace. He’s also descended from a tiger that fought alongside me during the Great Faction War.”

“Oh-ho. That huge one crouching in front of the barracks? I remember him. I thought he looked familiar.”

Yeah. Who needs an Azure Dragon on the left and a White Tiger on the right?

My chest swelled at the thought of this insane lineup—Fire King on the left, Miao King on the right.

A terrifying force capable of devouring even the Southern Heaven Demon Empress if she somehow returned alive.

The feeling of security was more comforting than a bowl of gukbap could have been.[^1] The quiet conversation between the two men reached my ears.

“The more I look at him, the better he seems. Good stamina, fast on his feet, and he looks intelligent at a glance.”

The Beast Miao King smiled proudly.

“I raised him with particular care. He was such a picky eater as a cub that I had quite a time of it. Whenever that happened, I even fed him milk myself.”

“What? You did it yourself?”

“……That’s just how I put it. It isn’t what you’re thinking, Old Master Jeok.”

Jeok Cheongang studied the Beast Miao King’s massive pecs before nodding.

“Well, let’s say that’s what you meant.”

“No, when you put it that way, it sounds even more—”

“Whatever. I’ve decided to take this one with me.”

At that moment, the smile on the Beast Miao King’s lips vanished.

“Excuse me?”

“Why are you asking again? Were you planning to make him run his legs off all the way back to the Central Plains?”

“Th-that obviously wasn’t my intention, but the one you’re riding is a creature this junior raised like a son in his old age…”

“Give him to me.”

“No, wait—”

“Do it.”

“……”

“If you really don’t want to, I’ll take that one instead. He looks like a spiritual creature.”

Jeok Cheongang pointed toward the tiger he had called *that one*. The Beast Miao King hurriedly shook his head.

“Gasp. Anyone but him. I only borrowed him for a while in the first place.”

“What if this old man were to take him?”

“I-I didn’t raise him myself, and as a father, how could I give away someone my son regards as a brother?”

“The sky is awfully clear today. You do have a long tongue.”

After a brief silence, the Beast Miao King answered in a gloomy voice.

“……Understood. I’ll give you the creature you’re riding now.”

“Since you’re insisting so much, I suppose I can’t refuse. I’ll accept your kindness.”

“……”

So much for feeling grand.

Was this really the same senile Fire King? The Fire King truly was a legend…

As I tried to steady my suddenly shrunken chest, the creature carrying me let out a low growl.

*Grrr.*

Judging by the way he even met my eyes, it seemed he also knew that he had only just escaped the clutches of the Fire King—that dogcatcher.

Feeling sorry for him, I gently stroked his trembling white fur.

“It’s okay, buddy. You survived.”

*Whine.*

Muyaho slowed his pace, letting out a mournful cry like a puppy that had lost its mother.

He must have instinctively realized that showing off his abilities in front of Jeok Cheongang would only increase the chances of being dragged all the way to the Central Plains.

Fortunately, Jeok Cheongang’s attention shifted elsewhere moments later.

“What’s that…?”

His voice trailed off.

At the end of the direction Jeok Cheongang was looking stood a bare mountain that had been almost completely burned away.

No, even that pathetic bare mountain had a name.

Ailao Mountain—a name no one living in this land could possibly fail to recognize.

Just as I was about to explain that to him, Jeok Cheongang’s eyes flew open and he shouted,

“What shameless son of a bitch burned down these precious mountains, trees, and grass?”

“……”

“……”

For a brief moment, the Beast Miao King and I exchanged a heated glance. Then I answered in a voice filled with righteous fury.

“Dark Heaven.”

Some truths are beautiful when left unknown.

* * *

Only after finally realizing that the pathetic bare mountain was our destination did Jeok Cheongang immediately frown.

“Did we come all the way here to plant trees?”

“……I’m asking this sincerely because I’m genuinely curious. How crazy do you think I am?”

It was an absurd question.

Today wasn’t Arbor Day, and even if it had been, I wouldn’t have planted any trees. I had come with these two to Ailao Mountain, which had been reduced to a bare mountain, for a purpose that had been decided from the beginning.

“This way.”

It didn’t take long for the Beast Miao King to realize where I was heading.

“The Poisonblood Grounds. No. Should we call it the Sacred Land now?”

It would have been stranger if the Beast Miao King didn’t know. Even if Yohi hadn’t told him the details, she must have given him a rough account of what had happened.

But when I heard him mutter, I shook my head.

“They’re different. The Poisonblood Grounds are the Poisonblood Grounds, and the Sacred Land is the Sacred Land.”

The two spaces were distinctly separate. If the Poisonblood Grounds were a land of death created by humans, the Sacred Land was Nanman’s heart—the land of life.

*Yes. Life itself.*

I set the Corrupted Divine Artifact in my hand down on the ground.

Misty demonic qi began to flow from it, and Muyaho let out a low growl.

But even though darkness had consumed it, its essence remained unchanged.

*Whoosh…*

The land pulsed as though it were a beating heart. With it, another world hidden for countless ages shed a single veil.

At that same moment, I saw it.

Another space filled with warm radiance in every direction.

At its center was a small pond shining more brilliantly than anything else.

“Ah.”

“That’s…”

The exclamations from Jeok Cheongang and the Beast Miao King trailed off before scattering into silence.

But I knew what they had felt.

And I knew what I had to do now.

*Purification.*

Today was the day a new sacred stone would be born.

[^1]: Gukbap is rice served in a hot, hearty soup—a common comfort food in Korea.
```
