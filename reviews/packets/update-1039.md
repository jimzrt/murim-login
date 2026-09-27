<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1039.txt",
      "sha256": "3ae4415f685cac2ece4a9ed60ee8a913d4613fd21cddd6f4378e62136a1532db",
      "bytes": 14296
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a2765062f11648a68476b71849ff03a10e585bcfd078bed06d39707934190ed2",
      "bytes": 1133
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "383045aaa550afcd5ef9913b67eee36e7dfcbd478f5edeb7be10bfbb7930e01e",
      "bytes": 240741
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "6681c3cffbac61f1fd6f271d98f1d3d341c40905b586c61cb0f0559c615b0c10",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9a6fe4512b5107f5a86e43c5fac100abf440a07fd6427c2250d87030d1d16101",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "0cd0d5e3b2c920f316378cf18033e9a9aab2b06b2e2add3eddd879995966acaa",
      "bytes": 668
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fb6654e80c2c0590440ba93f0a776077281b780cf7b84013f03fd428cf8de687",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1e2b211b67c9fad0132078f99e27a6f0f96d6b326dfc38e1e1cd07a58f428789",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9c55c8394910a9f2d09c9a96b971c7f397831cd5ee4f0be0996c026ededca375",
      "bytes": 623
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "a602b2ca43af8c426db170b5bd76abe3b4bd0842a2d8857f93dd1ab60bb4038a",
      "bytes": 716
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "268f671250f0dca11ce670c9130911eb34314633a9b2a8c684419fc055e1dda3",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f78099b144ce0321743eec5fdf0c165083ec3e8ae3c8bf959eafb1b530843846",
      "bytes": 279561
    }
  ],
  "estimated_tokens": 12251
}
-->

# Durable State Update — Chapter 1039

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
1 and safe_through 1039. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1039. Profile updates may replace only one
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
  "chapter": 1039,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1039,
    "continuity_sources": [1039],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is seriously injured and engaging the Blood-Sword Demon Lord; Jin Taekyung is heading to attack the white-robed mages.",
    "The Blood-Sword Demon Lord is much stronger than Jin Taekyung and is being strengthened by the mages’ Magic.",
    "Jin Taekyung recognizes the mages’ power as Magic and suspects one may be a Grand Mage.",
    "The suspected Grand Mage has not unleashed a wide-area attack; the mages’ intentions and restraint remain unclear."
  ],
  "continuity_sources": [
    1037,
    1038
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what is the white-robed followers’ purpose?",
    "Is there a Grand Mage among the white-robed mages, and why has that mage not intervened fully?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1038,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 마법사     | **mage**              |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1038
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1037
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1020
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1038
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1037
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1037
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1034
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1038
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1039화



그건 말 그대로 눈 깜짝할 사이에 벌어진 일이었다.

툭, 쐐애애액!

거침없이 정면을 향해 쏘아지던 진태경의 신형이, 미세한 발끝의 뒤틀림을 따라 흘러가듯 옆으로 미끄러진다.

마치 처음부터 지금 이 순간만을 노린 듯한 움직임.

그리고 이 갑작스럽게 벌어진 상황 앞에서, 혈검마군은 적잖이 당황할 수밖에 없었다.

‘이게 무슨……!’

예상치 못했던 변수다.

아니, 비단 혈검마군뿐만이 아니라 다른 누구였어도 마찬가지였을 것이다.

이미 상대와의 격차가 어느 정도 명확하게 드러난 위험한 상황에서, 부상을 입은 스승을 두고 떠날 제자는 없을 테니까.

하지만 혈검마군이 이토록 당황할 수밖에 없던 가장 큰 이유는 따로 있었다.

‘놈이…… 술사(術士)들을 노리고 있다!’

틀림없었다.

혈검마군의 측면으로 방향을 틀어 재차 쏘아지는 진태경의 신형.

바람을 가르며 힘차게 나아가는 그의 발끝이 향하는 곳에는, 높은 언덕 아래에서 전장을 굽어보고 있는 이십여 명의 백의인들이 있었다.

‘도대체 놈이 왜, 아니 어떻게?’

찰나의 순간 여러 가지 생각으로 복잡하게 얽히는 머릿속.

그러나 이미 허를 찔린 이상 망설이고 있을 여유 따위는 없었다. 혈검마군은 그 모든 의문을 뒤로한 채, 온 힘을 다해 신형을 비틀며 손을 내뻗었다.

슈화악!

가공할만한 속도로 공간을 가로지르는 일검(一劍).

느려진 시간 속, 검신을 휘감은 핏빛 강기가 진태경의 등을 향해 쏘아졌다.

아니, 쏘아지려던 그 순간이었다.

화아악!

불현듯 들이닥친 그 끔찍한 열기에, 혈검마군은 흐트러진 평정심 속에서 잠시 잊고 있었던 한 사람의 존재를 떠올릴 수 있었다.

화왕(火王) 적천강을.

‘이런 개 같은……!’

미처 소리 내어 외칠 틈조차 없었다. 대경한 혈검마군은 가까스로 검의 방향을 틀어 코앞까지 들이닥친 화염을 가로막았다.

콰아아앙! 드드득!

엄청난 굉음과 함께 지진이라도 난 것처럼 뒤집히는 땅거죽.

매캐한 검은 연기와 더불어 피어오른 수증기가 사방을 뒤덮은 가운데, 눈부시도록 새하얀 광염(光焰)을 토해 내는 주먹이 혈검마군의 망막에 비쳤다.

콰드득.

핏빛 강기에 휩싸인 자신의 검을 조금씩 밀어 내는, 그 거대한 기운의 주인도.

“감히 한눈을 팔다니.”

가까스로 멸염신권(滅炎神拳)을 가로막은 채 부르르 떨리는 검신 너머, 흐릿하게 웃고 있는 적천강을 바라보는 혈검마군의 눈빛이 착 가라앉았다.

이미 늦었다.

찰나의 당황과 방심이 부른 실수였고, 그 결과로 진태경을 놓쳐 버렸으니.

“기운도 좋으시구려. 연배가 연배이니 이제 관에 들어가서 쉬셔도 될 터인데.”

“원래대로라면 그랬겠지. 하지만 어느 날 저 구름 위 어딘가에 있을 높은 누군가가 그러더군.”

화아아악.

앞서 입은 내상이 무색할 만큼, 더욱더 맹렬하게 일어나는 화염 속에서 적천강이 뜨거운 숨결을 토해 냈다.

“아주 천둥벌거숭이지만 대단한 핏덩이 하나를 제자로 내려 줄 터이니, 녀석이 어른 구실 할 때까지 다른 놈들 관짝이나 짜 주라고.”

“……!”

“한데, 노부에게 관짝이 무슨 필요가 있겠느냐. 싹 다 불살라버리면 그만인 것을. 그렇지 않으냐?”

지금 이 순간에도 혈검마군이 쥔 검이 서서히 밀리고 있는 이유는, 비단 적천강이 젖 먹던 힘까지 끌어냈기 때문만이 아니었다.

그것은 기세(氣勢)였다.

화왕이라는 두 글자에 담긴 역사. 한 세기를 넘게 살아온 늙은 거인이 어깨에 짊어지고 있던 세월의 무게.

그리고…….

“노부가 이곳에 있는 이유를, 설령 백번을 죽었다 깨어난다 하여도 네놈은 모를 것이다.”

누군가를 죽이기 위해서가 아니라, 소중한 것을 지키기 위해 목숨을 걸고 싸우는 이만이 보일 수 있는 기개(氣槪).

“그러니, 이번에 죽거든 두 번 다시 인간으로 태어나지 말거라”

지옥 불처럼 시퍼런 귀화(鬼火)가 일렁이는 한 쌍의 눈동자.

그런 적천강에게 순간 압도되는 듯한 느낌을 받은 혈검마군은 이를 악물었다.

“이 빌어먹을 노괴가 감히……!”

확연하게 뒤바뀐 호칭과 거칠어진 말투.

그러나 그런 혈검마군의 모습에도 적천강은 오히려 더욱 기껍게 웃어 보였다.

이는 곧 상대의 여유와 평정심이 허물어졌다는 증거였으니.

“훨씬 듣기 좋군. 네깟놈한테 계속 선배 소리 들을 바에야 칼 물고 뒈지는 게 낫지.”

“그 입 닥쳐!”

콰드득!

천천히 기울어지던 힘의 저울추가 단번에 뒤집힌다.

마법사, 아니 혈검마군이 술사라 부르는 그들에게서 부여받은 가공할 힘이 검신에 실리자 태산과도 같은 중압감이 적천강을 짓눌렀다.

‘흡.’

헛숨을 삼킨 적천강의 이마 위로 도드라지는 힘줄.

그러나 그는 지면 깊숙이 파고드는 발끝을 느꼈음에도 결코 물러나지 않았다.

아니, 물러날 수 없었다.

‘뭐? 고작 반 각만 버텨 달라고?’

혈검마군의 어깨너머, 하늘 같은 스승을 헌신짝처럼 내팽개친 채 멀어져 가는 어느 고얀 놈의 뒷모습을 본 적천강의 입가에 흐릿한 미소가 맺혔다.

‘노부를 힘없는 늙은이 취급하다니. 이런 건방진 녀석을 보았나.’

물론 현재의 상황이 혈검마군에게 훨씬 유리하다는 것은, 적천강 역시 잘 알고 있는 사실이었다.

그는 이미 앞서 흑귀들과 싸우며 상당량의 공력을 소진했고, 혈검마군은 지치긴커녕 과거 남천마후가 그러했듯이 자신의 한계를 초월한 힘을 얻은 상태였으니까.

하지만…….

‘보여 주마. 노부가 어찌하여 화왕(火王)이라 불리게 되었는지.’

장장 일백 년하고도 스무 해.

그 기나긴 세월이 온통 투쟁이었다.

적과 싸우고, 온갖 심마와 싸우고, 심지어는 적천강 그 자신과도 싸워야 했다.

한때는 극심한 외로움에 사무쳤으나, 이제는 아니다.

세상 그 누구보다 자신을 믿어 주는 이가 있다. 목숨을 걸고서라도 지켜야 할 것이 생겼다.

‘네가 원한다면, 반 각이 아니라 반년도 버텨 주마. 언제까지나 기다려 주마.’

그렇기에, 화왕 적천강은 꺾이지 않는다.

꺾일 수 없었다.

화륵, 드드드득!

맹렬하게 타오르는 광염이 거대한 핏빛 강기에 부딪혀 흔들린다.

그러나 하늘이 쪼개지는 듯한 굉음과 함께 거칠게 밀려드는 거력(巨力)조차도, 적천강의 입가에 맺힌 미소를 지울 수는 없었다.

“그래, 오너라.”

콰아아앙!

끊임없이 충돌하고 뒤섞이며, 이내 온 사방을 떨어 울리는 희고 붉은 두 줄기의 기운.

이 모든 것은 저 멀리, 날카로운 송곳이 되어 적진을 돌파하는 누군가의 등 뒤에서 벌어지고 있는 일이었다.



* * *



어느 순간부터 끊임없이 울려 퍼지는 굉음을, 그 거대한 힘의 여파를 나는 똑똑히 느낄 수 있었다.

‘노야.’

문득 머릿속에 떠오른 한 사람의 얼굴.

반 각.

차 한잔도 여유롭게 마시지 못할 만큼 짧은 시간.

반면 섬광과도 같은 일격을 주고받는 초인들 간의 싸움에서, 반 각이란 누군가의 목숨이 사라지기에 충분한 시간이기도 했다.

하지만 바로 그런 이유로, 나는 고개를 돌려 적천강의 상태를 확인하기보다 앞으로 나아가기를 택할 수밖에 없었다.

‘마법사를 죽이면, 혈검마군에게 부여된 마법도 풀린다.’

그것이 내가 적천강을 뒤로한 채 방향을 틀었던 이유 중 하나다.

마법이 유지되는 이상 혈검마군은 쉽게 쓰러지지 않는다.

아니, 오히려 계속해서 더욱 강해질 수도 있다.

그러나 놈이 저토록 강해질 수 있었던 이유인 마법이 도중에 끊어진다면, 충분히 전황을 뒤집을 수 있었다.

물론, 예상했다시피 상황은 그리 순조롭지 않았다.

쉬쉬쉬쉭!

쉼 없이 귓가를 파고드는 파공성과 아슬아슬하게 전신을 스쳐 지나가는 섬광.

도, 검, 창, 그리고 드문드문 보이는 낯선 형태의 병장기들.

그것들의 종류는 다양했지만, 두 가지 공통점이 있었다.

첫째로는 모두 나 한 사람을 노리고 휘둘려진 무기라는 것이었고.

두 번째는 그 수많은 날붙이 위로 형형하게 빛나는 빛이 흐르고 있다는 것이었다.

‘절정 고수……!’

비단 몇몇을 이야기하는 것이 아니다.

후방에 배치되어 있던 적들의 숫자는 불과 일백 남짓이었으나, 놈들 전부가 검기상인(劒氣傷人)의 경지에 오른 실력자들이었다.

그리고 그 중심에, 유독 강대한 기운을 뿜어내는 한 존재가 있었다.



[Lv.170 소군악]



전신을 칠흑과도 같은 검은 갑주로 빈틈없이 감싼 거한(巨漢).

당연하게도 나는 저자의 별호를 모른다. 설령 과거의 그를 알고 있었다 해도 크게 중요하지 않다.

눈앞의 적은, 이미 과거의 자신을 잃어버린 상태니까.

‘흑귀(黑鬼).’

불현듯 마음 한구석이 무거워진 이유는, 비단 까다로운 장애물이 나타났다는 사실 때문만은 아니었다.

전장에 모습을 드러내지 않았던 마지막 흑귀가 이곳에 남아 있다는 것은, 나로 하여금 믿고 싶지 않았던 한 가지 가능성을 떠올리게 만들고 있었다.

후웅!

다음 순간 들이닥친 묵직한 파공성이 현실을 일깨운다. 마음과는 달리 깃털처럼 가벼운 발끝을 느끼며, 나는 신형을 내쏘았다.

쉭! 콰아앙!

목표를 잃고 지면을 가른 대도(大刀)에 의해 높게 솟구치는 땅거죽. 그와 동시에 사방으로 비산하는 얼음과 흙 알갱이 사이로, 나는 힘차게 백염의 창날을 뻗었다.

서걱!

섬광 같은 궤적을 따라 베어져 나가는 목덜미의 살갗.

그러나 창대를 타고 손끝까지 전달된 특유의 감촉은, 지금의 공격이 상대의 숨통을 끊기에 역부족이라는 사실을 알려주고 있었다.

‘피해?’

멍청하게 방심 따위는 하지 않았다.

당장 일분일초가 급한 상황.

그렇기에 처음부터 전력을 다한 일격이었고, 창날의 궤적과 타이밍 모두 정확했다.

그럼에도 불구하고 내가 완벽하게 계산하지 못한 것이 있다면, 그건 바로 마법이라는 이능이 지닌 광범위한 변수였다.



[Lv.173 소군악]



3레벨.

누군가에게는 작게 느껴질 수도 있는 미묘한 수치였지만, 초인들의 영역에서는 달랐다.

후웅, 꽈아앙!

조금 전보다도 빠르고, 강해진 일격.

아니, 지금 이 순간에도 빨라지고 강해지는 일격.



[Lv.175 소군악]



쐐애애액!

무겁기만 하던 파공성이 날카롭게 변화한다. 거대하고 뭉툭한 도신이 벼락처럼 떨어져 내리며 공간을 난도질했다.

콰과과과광!

엄청난 파괴력에 움푹 꺼지는 지면. 그 여파를 피해 물러나는 내 귓가로 십여 줄기의 바람 소리가 울려 퍼졌다.

서걱! 피핏!

전신 곳곳에서 샘솟는 붉은 핏물.

위기를 느끼자마자 몸을 비틀어 피했지만, 이미 늦은 후였다.

아니, 정확히는 놈들이 빨랐다.

‘강해졌다. 조금 전보다.’

똑똑히 보았다.

마지막 순간, 돌연 속도와 힘이 더해져 섬광처럼 뻗어 나오던 날붙이들을.

동시에 느꼈다.

사방에서 조여오는 흑귀와 일백여 명의 절정 고수들. 그리고 그런 그들의 어깨 너머, 언덕 위에서 쏟아져 내린 선명한 기운의 파동을.

‘어떻게든 막아내겠다는 거겠지. 지금보다 더 거리가 좁혀지기 전에.’

지금 이 순간, 위기를 느끼는 것은 나뿐만이 아니었다.

동그랗게 원형을 갖춘 채 서 있는 스무 명의 백의인, 아니 마법사들.

놈들 또한 생명의 위협을 느끼고 있을 것이다.

‘하지만, 나와는 달라.’

죽음에 대한 두려움은 모두가 갖고 있다.

나도, 저들도.

그러나 그 두려움 속에서 차이를 만들어 내는 것은, 의지와 간절함의 크기다.

‘인벤토리 오픈.’

나는 마음속으로 읊조리며, 온 힘을 다해 신형을 뻗었다.

더욱 강해진 일백여 명의 절정 고수들을 향해.

반드시 넘어서야 할, 마지막 흑귀를 향해.

파팟!

단 한 걸음.

모든 거리가 지워지고 시간이 느려졌다.

그와 동시에 수십여 개의 빛줄기가 파괴적인 섬광을 뿜어내며 사방을 물들이고, 그 모든 것을 합친 것보다 더욱 거대한 한 줄기의 벼락이 나를 향해 떨어져 내렸다.

슈화아악!

그래. 나 역시 알고 있다.

일 대 다수. 지금 이 순간 드러난 힘의 차이는 명백하다는 것을.

그러나 눈에 보이는 것만이 전부가 아니다.

‘가야 한다. 무슨 수를 써서라도.’

넘으려는 자와 막아서는 자.

지키기 위해 싸우는 자와, 지켜야 할 것이 무엇인지조차 잊어버린 자.

저들에게는 의지가 없고, 간절함은 망각했으며, 사명이란 단어는 기억조차 하지 못한다.

하지만 나는 아니다.

그 모든 것을 알기에, 목숨을 걸고 나아갈 수 있다.

빗발치는 공격들을 향해 몸을 날리며, 영혼까지 다한 일격을 뻗어낼 수 있다.

바로 지금처럼.

슈확!

공간을 가르며 나아가는 백염의 창날.

그와 동시에, 나는 남겨 두었던 명령어를 속삭였다.

‘화룡갑, 소환.’

띠링.

콰아아아앙!
```

## Final English reading copy

```markdown
# Chapter 1039

It happened in the blink of an eye.

Tap—SHWEEEE!

Jin Taekyung’s figure, which had been hurtling straight ahead without hesitation, flowed sideways with a subtle twist of his foot.

A movement as if he’d been waiting for this exact moment all along.

Faced with this sudden turn of events, the Blood-Sword Demon Lord couldn’t help but be taken aback.

*What the…!*

An unexpected variable.

No—not just the Blood-Sword Demon Lord. Anyone would have been caught off guard.

With the gap between them already clear, and the situation so dangerous, there was no way a Disciple would leave his injured Master behind.

But that wasn’t the main reason the Blood-Sword Demon Lord was so startled.

*He’s… going after the mages!*

There was no doubt.

Jin Taekyung veered toward the Blood-Sword Demon Lord’s flank, then shot forward again.

The tips of his feet drove through the wind toward the twenty or so white-robed figures surveying the battlefield from beneath a high hill.

*Why in the world would he—no, how could he…?*

A jumble of thoughts tangled in the Blood-Sword Demon Lord’s mind in a fleeting instant.

But now that he’d been caught off guard, there was no time to hesitate. He pushed aside every question, twisted with all his might, and thrust out a hand.

SHWAAK!

A sword strike crossed the space at a terrifying speed.

In the slowed passage of time, blood-red Force coiling around the blade shot toward Jin Taekyung’s back.

No—in the very instant it was about to shoot forward—

FWOOSH!

That dreadful heat suddenly rushed in. In the disarray of his composure, the Blood-Sword Demon Lord remembered someone he’d momentarily forgotten.

The Fire King, Jeok Cheongang.

*You son of a bitch…!*

He didn’t even have time to shout. The horrified Blood-Sword Demon Lord barely managed to turn his sword and block the flames that had rushed right up to him.

KWA-BOOM! GRRRR!

The earth’s crust flipped up as if an earthquake had struck, accompanied by a tremendous roar.

Amid the acrid black smoke and steam billowing up to blanket the area, a fist spewing blindingly white light-flames appeared before the Blood-Sword Demon Lord’s eyes.

CRUNCH.

The owner of that immense power, steadily pushing back his sword, still wrapped in blood-red Force.

“Daring to take your eyes off me.”

Beyond the trembling blade, barely holding back the Flame-Extinguishing Divine Fist, the Blood-Sword Demon Lord stared at Jeok Cheongang’s faint smile. His gaze sank low.

It was already too late.

A moment’s surprise and carelessness had cost him Jin Taekyung.

“You’re full of energy, Senior. At your age, shouldn’t you be resting in a coffin by now?”

“Under normal circumstances, perhaps. But one day, someone high above the clouds told me this.”

FWOOSH.

Amid the flames rising even more fiercely, belying the Internal Injury he’d suffered earlier, Jeok Cheongang breathed out a scorching sigh.

“He said he’d send me one hell-raising but remarkable young brat as my Disciple, and that I should build coffins for the other bastards until the boy learned to act like an adult.”

“……!”

“But what use do I have for a coffin? I can burn the whole lot of you to ashes. Isn’t that right?”

Even now, the reason the Blood-Sword Demon Lord’s sword was slowly being pushed back wasn’t just that Jeok Cheongang was drawing on every last bit of strength he had.

It was his aura.

The history contained in the two words Fire King. The weight of the years borne on the shoulders of an old giant who’d lived for more than a century.

And…

“Even if you died and came back a hundred times, you’d never understand why I’m here.”

It was the spirit only shown by those who fought with their lives on the line—not to kill someone, but to protect something precious.

“So when you die this time, don’t be reborn as a human again.”

A pair of eyes shimmered with ghostly blue fire, like flames from hell.

The Blood-Sword Demon Lord clenched his teeth, momentarily overwhelmed by Jeok Cheongang.

“This damned old monster dares to…!”

His form of address had changed completely, and his tone had grown rougher.

But Jeok Cheongang only smiled more broadly at the sight.

It was proof that his opponent’s ease and composure were crumbling.

“Much better. I’d rather bite down on a sword and die than keep hearing ‘Senior’ from the likes of you.”

“Shut your mouth!”

CRUNCH!

The balance of power, which had been slowly tipping, flipped in an instant.

The fearsome power bestowed on him by the mages—or sorcerers, as the Blood-Sword Demon Lord called them—poured into his sword. A pressure as vast as Mount Taishan bore down on Jeok Cheongang.

*Hup.*

A vein stood out on Jeok Cheongang’s forehead as he sucked in a breath.

But even as he felt his toes dig deep into the earth, he didn’t retreat.

No—he couldn’t.

*What? Just hold him off for half a quarter-hour?*

Beyond the Blood-Sword Demon Lord’s shoulder, Jeok Cheongang watched the retreating figure of some insolent brat, leaving his Master—who was like the heavens to him—behind as though he were a worn-out rag. A faint smile touched the corner of Jeok Cheongang’s mouth.

*He treats this old man like some feeble old geezer. What a cheeky little brat.*

Of course, Jeok Cheongang knew perfectly well that the situation favored the Blood-Sword Demon Lord.

He’d already spent a considerable amount of internal energy fighting the Black Ghosts, while the Blood-Sword Demon Lord wasn’t tired at all. Just as the Southern Heaven Demon Empress had once done, he’d gained power that exceeded his own limits.

But…

*I’ll show you why they call me the Fire King.*

A full hundred and twenty years.

Every last one of those long years had been a struggle.

He’d fought enemies, every manner of inner demon, and even Jeok Cheongang himself.

Once, he’d been consumed by overwhelming loneliness. But not anymore.

There was someone who trusted him more than anyone else in the world. He had something he would protect even at the cost of his life.

*If you want, I’ll hold out for half a year, not half a quarter-hour. I’ll wait for you as long as it takes.*

That was why the Fire King Jeok Cheongang would not break.

He could not break.

FWOOSH—GRRRR!

The fiercely burning light-flames wavered as they crashed against the enormous blood-red Force.

But even the immense power surging forward with a roar like the heavens splitting apart couldn’t erase the smile on Jeok Cheongang’s lips.

“Come on, then.”

KWA-BOOM!

The two streams of energy, one white and one red, clashed and mingled without end, their collisions shaking everything around them.

All of this was happening far behind the back of someone who had become a sharp awl, piercing through the enemy lines.

* * *

From some point on, I could clearly feel the constant roars and the shock waves from the immense power.

*Old Master.*

One person’s face came to mind.

Half a quarter-hour.

A short stretch of time—not enough to leisurely finish a cup of tea.

But in a fight between superhumans, trading blows that flashed like lightning, half a quarter-hour was enough time for someone to lose their life.

And it was precisely for that reason that I had no choice but to keep moving forward instead of looking back to check on Jeok Cheongang.

*If I kill the mages, the Magic empowering the Blood-Sword Demon Lord will disappear.*

That was one of the reasons I’d changed direction, leaving Jeok Cheongang behind.

As long as the Magic remained in place, the Blood-Sword Demon Lord wouldn’t go down easily.

No—he might even keep getting stronger.

But if the Magic that let him grow so powerful were cut off, we’d have a chance to turn the tide.

Of course, as I’d expected, things weren’t going smoothly.

SHWISH-SHWISH-SHWISH!

Whistles of passing weapons relentlessly pierced my ears, and flashes of light skimmed past my body by the narrowest margin.

Sabers, swords, spears, and, here and there, weapons of unfamiliar shapes.

They varied, but shared two things in common.

First, every one of them had been swung at me.

Second, bright light flowed over the countless blades.

*Peak masters…!*

It wasn’t just a few of them.

There were only about a hundred enemies stationed in the rear, but every last one had reached the level of injuring others with Sword Energy.

And at their center was one being, radiating an especially powerful aura.

> **System**
> **Level:** 170
> **So Gunak**

A hulking figure, completely enclosed in jet-black armor.

Naturally, I didn’t know his title. Even if I’d known who he was in the past, it wouldn’t matter much.

The enemy in front of me had already lost his former self.

*Black Ghost.*

The reason my heart suddenly grew heavy wasn’t just the appearance of a troublesome obstacle.

The last Black Ghost, who hadn’t shown up on the battlefield, was still here. That made me think of one possibility I hadn’t wanted to believe.

WHOOOM!

The heavy whistle that rushed at me next snapped me back to reality. Feeling my feet, light as feathers despite my thoughts, I shot forward.

SWISH! KWA-BOOM!

The great saber missed its target and tore into the ground, sending the earth flying high. As ice and clods of dirt scattered in every direction, I thrust out White Flame’s spearhead with all my strength.

SLICE!

The flash-like arc cut the skin at the back of his neck.

But the distinctive feel that traveled up the shaft and reached my fingertips told me the attack hadn’t been enough to cut off his breath.

*He dodged?*

I hadn’t carelessly let my guard down.

There was no time to waste—not even a minute or second.

That was why I’d put everything into that first strike. The spear’s trajectory and timing had both been exact.

And yet, if there was one thing I hadn’t calculated perfectly, it was the sheer number of variables that came with the supernatural power of Magic.

> **System**
> **Level:** 173
> **So Gunak**

Three levels.

It might have seemed like a small difference to some, but not in the realm of superhumans.

WHOOOM—KWA-BOOM!

A strike faster and stronger than before.

No—a strike getting faster and stronger even now.

> **System**
> **Level:** 175
> **So Gunak**

SHWEEEE!

The heavy whistle sharpened. The massive, blunt blade of the great saber came crashing down like lightning, tearing through space.

KWA-KWA-KWA-BOOM!

The ground sank beneath the tremendous force. As I backed away to escape its shock wave, the sound of more than ten streaks of wind rang past my ears.

SLICE! SPLAT!

Red blood welled up from all over my body.

The moment I sensed danger, I’d twisted to dodge, but it was already too late.

No—more precisely, they were faster.

*They’d grown stronger. Stronger than they were a moment ago.*

I saw it clearly.

At the last moment, the blades had suddenly gained speed and force, shooting out like flashes of light.

And I felt it, too.

The Black Ghost and more than a hundred Peak masters closing in from every side. And beyond their shoulders, the clear pulse of energy spilling down from the hilltop.

*They’re trying to stop me somehow. Before I can get any closer.*

At this moment, I wasn’t the only one who sensed danger.

The twenty white-robed figures standing in a perfect circle—the mages.

They must have felt their lives were in danger, too.

*But I’m different.*

Everyone fears death.

Me, and them.

But what makes the difference in the face of that fear is the strength of one’s Will and desperation.

*Inventory open.*

I murmured inwardly and threw myself forward with all my strength.

Toward the more than a hundred Peak masters, who had grown even stronger.

Toward the last Black Ghost, whom I absolutely had to get past.

PAPAT!

One step.

Every distance vanished, and time slowed.

At the same time, dozens of streaks of light blazed destructively, coloring the world around me. And a single bolt of lightning, more enormous than all of them combined, came crashing down toward me.

SHWAAAK!

Yeah. I knew it, too.

One against many. The difference in strength revealed in this moment was undeniable.

But what the eye could see wasn’t everything.

*I have to get through. No matter what it takes.*

Those who try to cross over, and those who stand in their way.

Those who fight to protect something, and those who’ve forgotten what they’re supposed to protect.

They had no Will. They’d forgotten what it meant to be desperate, and they couldn’t even remember the word duty.

But I wasn’t like them.

Because I knew all that, I could move forward with my life on the line.

I could hurl myself at the relentless attacks and strike with everything I had—even my soul.

Just like now.

SHWAK!

White Flame’s spearhead tore through space.

At the same time, I whispered the command I’d held back.

*Fire Dragon Armor, summon.*

Ding.

KWA-BOOOOM!
```
