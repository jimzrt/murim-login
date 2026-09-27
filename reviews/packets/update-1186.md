<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1186.txt",
      "sha256": "4f344ff7ab7b0b139c6bec413b51fba9a5e6d890b0608cbeec0035df53bb7dba",
      "bytes": 13361
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f07e1efe13bddc89d7b53c3c143cccdaa2c081b3d59530bb43432c3427fe113e",
      "bytes": 2047
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f9c650f1d3d6b3e1b011dc4ede8fa9ce6d95503393c5d52b851c9771c7e1da91",
      "bytes": 760
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "c74da8980c9aba680995aee01b555163b2f227a5a60510949fb4622f2510cea1",
      "bytes": 670
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "add9af3a0625e8075d3ab190d4039d9e8ca6c71ad23d1098db70ea238eb3e7b2",
      "bytes": 1377
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f8cd4b2ff0dad3d78612cc68da9bab75b6aafef0038e87af9d102317e0dd2601",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9536d4529e6eccc44ec5d4d8cb695e203c3a490f17e5e741ccbdd6f89338e76e",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "82b1a9b183a9420c444a0c2b07cf428353e783037d65db9a47e4f60bc6c6b7a9",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "5df50d22163f8c74bbbd1473b483540a633a5992cb8b877ac9af57ec530662b3",
      "bytes": 974
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "6995887fc40829f3dca4a310a80d1f726662f7c2f1749e350ca960c7e5c9a077",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "42ef694bcfe65da4b853d792b043a1ddb86807253f11415a977d8c5a4589752f",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6592233b34dcd7f1d0f74935310ed387046c3f86f1869fa5f218139dd6824a3a",
      "bytes": 295903
    }
  ],
  "estimated_tokens": 13473
}
-->

# Durable State Update — Chapter 1186

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
1 and safe_through 1186. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1186. Profile updates may replace only one
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
  "chapter": 1186,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1186,
    "continuity_sources": [1186],
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
    "Jeok Cheongang’s group has entered Tianshan with Taekyung unconscious; the Slaughter Saint expects him to wake within two days.",
    "The group is following Mae Jonghak’s contingency plan to proceed to Tianshan after the allied forces missed their deadline; the Murim Alliance and Imperial Army are drawing Dark Heaven’s attention away from the desert.",
    "The group has supplies made from the eight exhausted horses; the terrain ahead is too rough for their carriage.",
    "Taekyung’s earlier strength during the fasting pill’s effects surprised the Slaughter Saint, who wonders whether Taekyung used his full strength.",
    "The fate and whereabouts of the separated companions and allied troops remain unknown.",
    "Taekyung experiences unexplained chest pain and difficulty sleeping.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1185,
    1184
  ],
  "open_questions": [
    "What happened to the separated companions and allied troops, and why did the Murim Alliance and Imperial Army miss the rendezvous?",
    "What is the source of Taekyung’s chest pain and sleeplessness, and did he use his full strength against the fasting pill’s effects?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1185,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |
| 궁성 | 대인 | Acquaintances traveling together; Bow Saint is wary of the mysterious Great Sir. | you | polite, controlled | Bow Saint questions him formally and apologizes after mistaking him for an enemy. |
| 대인 | 궁성 | Acquaintances traveling together; Great Sir calls Bow Saint “Young Lady” and “heroine.” | Young Lady; heroine | polite conversational, familiar and teasing | He alternates respectful titles with candid personal questions. |
| 살성 | 진태경 | senior allied martial artist to younger companion | you | familiar and blunt | Addresses Taekyung with 너 and 네가 while explaining that he anticipated Taekyung’s response. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1185
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1184
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1185
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1185
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1185
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1185
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1185
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1184
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1184
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃1186화



모든 것에는 시작이 있다.

호호백발의 노인에게도 갓난아이였던 시절이 있듯이, 길가에 놓인 돌멩이 하나조차 처음부터 그런 모습이었던 것은 아니다.

세상에 존재하는 만물은 정해진 조화에 따라 어우러지고, 시간이라는 물결 속에서 변화하는 것이다.

처음부터 완전한 것도, 영원한 것도 없다.

그것이야말로 자연의 법칙이자, 모두가 아는 이 세상의 순리(順理).

하지만 바로 지금, 희끄무레한 안개를 헤치며 나아가는 일단의 무리는 동시에 같은 생각을 떠올리고 있었다.

정확히는, 지금껏 자신들이 알고 있던 그 당연한 상식들이 어쩌면 전부 허상에 가까운 것이 아니었을까 하는 의문을.

화왕(火王) 적천강 역시 그중 한 명이었다.

‘빌어먹을.’

목 끝까지 차오른 욕설을 삼킨 그는 고개를 들어 주위를 둘러보았다.

사방을 휘감은 안개와 그 너머로 언뜻 드러났다가 사라지는 새카만 나뭇가지들. 거기에 더해 끝도 없이 위로 이어지는 험준한 산세까지.

순리와 법칙?

그런 것들 따위는 이미 뇌리에서 깨끗이 지워진 지 오래다.

처음부터 이 모습 그대로 완전했으며, 만 년 뒤에도 변함없을 것 같은 그 풍경 앞에 적천강은 바짝 마른 입술을 핥았다.

도산검림(刀山劍林)보다도 섬뜩하게 다가오는 눈앞의 광경을 보고 있노라면, 백년을 훌쩍 넘게 살아온 삶과 그간의 경험이 모두 덧없게 느껴질 정도였다.

그나마 약간의 위안이 있다면, 이는 비단 그 혼자만 느끼고 있는 감정이 아니라는 것일 터였다.

- 빌어먹을 천산(天山).

불현듯 귓가를 파고드는 한 줄기의 음성에, 적천강은 내심 공감하며 입술을 달싹였다.

- 그런 말 하지 말게. 어린 것들이 들으면 괜히 사기 떨어지니까.

애당초 지금 같은 상황에서 적천강에게 이런 전음을 날릴 사람은 한 명뿐.

곧장 살성의 대답이 되돌아왔다.



- 그래서 전음으로 하잖나.

- 전음도 쓰지 마.

- 어째서?

- 공력 아까워.



십여 걸음 앞서가던 살성이 어처구니없다는 얼굴로 적천강을 돌아보았다.



- 자네는 내가 무슨 저잣거리에 굴러다니는 삼류 칼잡이로 보이나? 그리고 그렇게 공력이 아까우면 본인부터 실천하지, 굳이 대답은 왜 해?

- 노부는 상관없지.

- 왜 상관이 없나?

- 공력이 심후하거든. 누구와는 다르게.

- ……이런 상황에서도 잘도 그런 농이 나오는군.

- 농이라도 해야지. 이런 상황에서는.



이번에는 살성이 공감해야 할 차례였다.

전음으로도 느껴지는 적천강의 가라앉은 어조에, 그의 시선 역시 착잡해졌다.

- 조금 전에도 말했지만, 정말 쉽지 않은 곳이야. 일찍이 천하 곳곳을 주유하며 적잖은 견문을 쌓았다고 생각했는데…… 이런 건 듣도 보도 못했네.

일생의 대부분을 구화산(九華山)에서 보낸 적천강과 달리 살수로서, 그리고 의원으로서 떠돌이와 같은 삶을 살았던 그다.

젊은 시절에는 누군가의 목숨을 거두기 위해 천 리 길을 떠났고, 늙어서는 누군가의 생명을 구하기 위해 만 리 밖의 약초를 찾아 헤매기도 했다.

나무를 베어 하루 벌어 하루 먹고 사는 젊은 나무꾼조차 그만의 경험과 삶이 있을 터인데, 생사(生死)라는 상반된 양극에서 일가를 이룬 그가 쌓아 올린 견문이라면 ‘적잖은’이라는 표현조차 지나친 겸손이었다.

물론, 같은 현실을 공유하고 있는 적천강에게는 더없는 진심으로 들렸지만.



- 어느 정도 예상은 했지만, 자네한테도 별다른 수가 없는 모양이군.

- 방법도, 도리도 없네. 당장 밤낮도 알 수 없는 상황에서 뭘 할 수 있단 말인가?



살성의 말은 사실이었다.

그들의 앞을 가로막은 운무(雲霧)는 지상에만 해당되는 것이 아니었다.

먹구름.

처음에는 그저 지나가는 것이라 생각했던 그 거대하고도 새카만 응집체는 하늘마저 가렸다.

처음에는 희미하게나마 그들의 머리 위를 비추고 있던 달과 별도, 심지어는 단 한 줄기의 햇빛마저 허락하지 않고 모조리 먹어 치웠다.

마치 자신의 허락도 없이 찾아온 이 무례한 불청객들에게 두려움을 심어 주려는 것처럼.



- 이런 현상들이 우연이라고 생각하나?

- 우연?



적천강은 자신도 모르게 헛웃음을 흘렸다.

- 과거의 노부라면 필시 그렇게 생각했겠지. 그래, 이 나이 먹도록 개고생하는 스승의 등에 업혀 있는 웬 괘씸한 녀석을 만나기 전이었다면 말이야.

적천강은 한쪽 어깨를 차지하고 있는 ‘괘씸한 녀석’의 얼굴을 물끄러미 바라보았다.

생각지도 못한 어느 날 불쑥 나타나, 늙고 병든 자신의 인생을 송두리째 뒤집어 놓은 제자를.

그리고 이제는 한 사람의 삶을 넘어 모두의 세상을 뒤바꾸고 있는 그를.

- 우리에게 더 이상의 우연이란 없네. 지금부터 벌어질 모든 일은 의도된 필연이고, 어쩌면…….

처음부터 정해져 있던 운명(運命)일지도 모르지.

덧붙이려던 뒷말을 적천강은 조용히 되삼켰다.

그가 운명 따위를 믿지 않는 사람이라서가 아니었다.

이것이 전부 운명이라면 진태경에게 너무나도 가혹한 일이며, 더 나아가 이 이야기의 결말이 어떻게 끝맺어질지 두려운 마음이 들었기 때문이었다.



- 어쩌면?

- 아니, 아무것도 아니야. 넘어가지. 그보다는 현재 우리가 처한 상황이 더 중요하니까.



적천강의 말과 행동은 누가 보기에도 부자연스러웠지만, 살성은 굳이 그 부분을 깊게 파고들지 않았다.

조금 섭섭하긴 해도 모든 이에게는 각자만의 고민이 있고, 그가 그동안 지켜본 적천강이란 인물은 세간에 알려진 인식보다 훨씬 더 섬세하고 깊은 사고방식을 지닌 사람이었으니까.

특히 진태경과 관련된 부분에서만큼은 더욱더.

‘하긴, 나도 이런 일로 남 말 할 처지는 아니로군.’

마음속 뇌까림과 함께 살성의 시선이 문득 적천강의 어깨너머를 향했다.

연신 거친 숨소리를 내뱉으며 험준한 산세를 내달리는 젊은이들, 그리고 그런 그들과 달리 평온한 얼굴로 후미를 지키고 있는 대인과 궁성을 향해서.

하지만 그들에게 시선이 머무른 것은 아주 잠깐의 찰나에 불과했고, 살성은 아무 일도 없었다는 듯 입을 열었다.

이번에는 전음이 아닌 자신의 목소리로.

“잠시 쉬어 가는 것이 좋겠군.”

어느덧 더욱 짙어진 안개 사이로 그의 음성이 퍼져 나갔다.



* * *



살성의 판단은 적절했다.

잠깐의 휴식 시간이 주어지기 무섭게 혁무진은 그 즉시 헛구역질을 시작했고, 궁기방은 그의 등을 두드려 주는 대신 육포를 꺼내 들었다.

“……이 배신자. 육포가 그렇게 맛있냐?”

결국 주화란의 도움으로 헛구역질을 멈춘 혁무진의 비난에, 궁기방이 한 치의 망설임도 없이 대답했다.

“당연하지.”

“…….”

“그나저나 이거 장난 아니네. 한혈보마로 만들어서 그런가? 맛이 굉장히 안정적이야.”

“…….”

“괜히 고리눈 뜨지 말고 얌전히 먹게. 먹어야 또 힘쓰지. 아니면 저 친구처럼 운기조식이라도 하던가.”

벌써 가부좌를 틀고 앉은 송일섬과, 말하는 순간에도 열심히 육포를 뜯고 있는 궁기방을 번갈아 바라보던 혁무진은 이내 굳은 얼굴로 결정을 내렸다.

“육포 하나 줘 봐. 얼마나 맛있길래 사흘 굶은 거지처럼 처먹는지 보게.”

처음 만났을 때만 해도 무림인으로서의 위치나 무위 면에서 상당한 차이가 있던 두 사람이었지만, 제법 오래 붙어 다니며 친구나 다름없는 사이가 된 지 오래.

궁기방은 누런 이를 드러내며 씩 웃었다.

“아주 좋은 판단일세. 아, 주 소저께서도 좀 드시겠습니까?”

“괜찮아요. 그보다는 잠시 운기조식을 해야 할 것 같아서.”

기력을 채우는 것과 공력을 가다듬는 것 모두 좋은 선택이었다.

산, 그것도 이 정도로 고지대인 험준한 산맥을 오르는 것은 평지를 내달리는 것과는 차원이 다른 피로를 불러일으키는 법이니까.

게다가 천산 전체를 둘러싼 무거운 공기와 기이하기 그지없는 현상들은, 동행하고 있는 노고수들에 비해 무공의 화후(火候)가 한참이나 떨어지는 그들 역시 충분히 느끼고 있었다.

“염병할, 마지막으로 뜨끈한 햇빛 받아 본 지가 언젠지 기억도 안 나네.”

궁기방의 투덜거림에 입안 가득 육포를 쑤셔 넣고 있던 혁무진이 입을 열었다.

“받았잖아. 사막에서.”

“그게 어떻게 뜨끈한 햇빛이야? 타 죽을까 봐 낮에는 돌아다니는 것도 무서울 지경이었는데. 물론 그마저도 중간쯤 가니 그리워졌지만.”

“하긴, 날씨가 좀 지랄 맞았어야지.”

사실, 지랄 맞다는 표현으로도 부족했다.

대관절 어느 사막이 선인장과 벌레도 없고, 보름이 넘도록 우박과 폭우가 번갈아 가며 쏟아진단 말인가.

하지만 이제는 이런 세상이 되어 버렸다.

그리고 변한 세상에서 살아남기 위해서는 그들 역시 변해야 했다.

“죽겠네. 이게 벌써 몇 번째 봉우리냐.”

“다섯 번째.”

“벌써? 생각보다는 많네.”

“죽어라 달린 거에 비하면 그렇지도 않지. 앞으로 얼마나 더 가야 할지도 모르고.”

천산산맥은 넓다.

아니, 단순히 넓다는 표현을 넘어서 광대(廣大)하다.

산맥의 총 길이만 천 리가 넘고, 그 모든 면적은 무려 신강 땅의 삼분지 일을 차지할 정도다.

그뿐인가. 옛 마교도들 중에서도 일부에 불과한 자들만이 출입을 허락받은 성지(聖地)요, 외인이라면 죽음을 면치 못하였기에 멸지(滅地)라.

수백 개에 달하는 봉우리 중 어디에 본거지가 있을지는 아직 까지도 미지수였다.

“끔찍하군.”

“끔찍하지.”

“그나마 아직 별일이 없어서 다행이야. 적어도 우리가 발각되진 않았다는 뜻일 테니.”

“조장님께서 들으셨으면 한 대 얻어맞았을 소리를 하는군.”

“왜?”

“그런 말은 질색하시거든. 재수 없다고. 클리? 굴리? 여하튼 구리쇠인지 뭔지 알 수 없는 말씀을 하신단 말이야.”

“하여간, 알다가도 모르겠군.”

“내 말이.”

혼잣말처럼 중얼거린 두 사람은 멍하니 자리에 누워 하늘을 바라보았다.

정확히는, 하늘을 빈틈없이 메운 먹구름을.

“이곳에 들어온 지 정확히 얼마나 됐지?”

“하루는 넘었고, 이틀은 안 지났을걸.”

“확실해?”

“확실해.”

“밤낮도 모르는 와중에 용케도 그리 말하네.”

혁무진이 단호하게 대답했다.

“그야, 조장님께서 아직 안 깨어나셨으니까.”

“아, 그렇군. 늦어도 이틀 안에는 깨어난다고 했으니.”

“그래, 그러니까 분명히 이틀은 안 지났어.”

그런 혁무진을 물끄러미 바라보던 궁기방이 문득 실소했다.

“왜?”

“아니, 뭐랄까. 자네도 참 어지간한 것 같아서.”

“어지간하다니?”

“거의 모든 게 진태경, 저 친구한테 맞춰져 있는 느낌이거든.”

“글쎄, 나는 잘 모르겠군. 그냥 나한테는 이게 너무 당연한 일이라서.”

“오해하지 말게. 이상하거나 이해가 안 된다는 게 아니야. 오히려 무슨 느낌인지 너무 잘 알아서 하는 소리인 거야.”

궁기방의 입가에 맺혀있던 미소가 흐릿해졌다.

“사문(師門)이란 그런 거지. 비록 피가 섞이지는 않았지만 가끔은 피보다도 진한 정이 있어.”

궁기방은 잠시 옛 생각에 잠겼고, 혁무진은 입을 다물었다.

마치 오랫동안 참고 있던 상처가 터진 느낌이었다.

태원진가. 그리고 개방.

그건 그들의 사문이자 또 다른 고향이며, 서로의 마음을 무겁게 짓누르는 커다란 두 바위의 이름이었다.

깃발을 높이 세운 채 서쪽으로 향했던 그들은 어찌 되었을까.

만약 살아 있다면, 다시 만날 수는 있을까.

겉으로는 실없는 소리를 주고받고, 입가에는 애써 미소를 띄워보아도 현실은 몸서리칠 만큼 차가웠다.

심지어는, 뼛속까지 스며드는 그 냉기를 물리칠 틈조차 허락해주지 않을 만큼 재빠르기까지 했다.

스아아아아.

돌연 느껴지는 위화감.

다음 순간 크게 뜨인 혁무진의 두 눈동자에, 마치 살아 있는 것처럼 꿈틀거리는 안개가 비쳤다.
```

## Final English reading copy

```markdown
# Chapter 1186

Everything has a beginning.

Even a white-haired old man was once a baby, and not even a pebble by the roadside had always looked the way it did now.

All things in the world blend together according to a fixed order and change in the flow of time.

Nothing is perfect from the start. Nothing lasts forever.

That is the law of nature, the proper order of the world everyone knows.

And yet, right now, the group pushing through the pale mist was thinking the same thing.

Or, more precisely, they were wondering whether everything they had always taken for granted might be little more than an illusion.

The Fire King, Jeok Cheongang, was one of them.

*Damn it.*

He swallowed the curse rising to his throat and looked around.

Mist coiled in every direction. Beyond it, black branches appeared and vanished in fleeting glimpses. And beyond those, the rugged mountains climbed without end.

Order and laws?

Those ideas had long since been wiped clean from his mind.

Facing a landscape that seemed perfect in its present form, as if it had always been this way and would remain unchanged ten thousand years from now, Jeok Cheongang licked his parched lips.

The sight before him was more chilling than a mountain of sabers and a forest of swords. Looking at it, he could almost feel that the life he had lived for well over a hundred years, and all the experience he had gained, amounted to nothing.

If there was any small comfort, it was that he wasn’t the only one who felt that way.

“Damn Tianshan.”

At the voice that suddenly reached his ear, Jeok Cheongang silently agreed and parted his lips.

“Don’t say that. The youngsters will lose heart if they hear you.”

There was only one person who would send Jeok Cheongang a Sound Transmission in a situation like this.

The Slaughter Saint’s reply came at once.

“That’s why I’m using Sound Transmission.”

“Don’t use it at all.”

“Why not?”

“It wastes internal energy.”

The Slaughter Saint, who was walking a dozen paces ahead, turned to Jeok Cheongang with an incredulous look.

“Do I look like some Third Rate sword-for-hire rolling around the marketplace? And if you’re so worried about wasting internal energy, why don’t you practice what you preach instead of answering me?”

“This old man doesn’t mind.”

“Why not?”

“My internal energy is profound. Unlike some people’s.”

“……You can still crack jokes at a time like this.”

“What else can you do in a situation like this?”

This time, it was the Slaughter Saint’s turn to agree.

Even through Sound Transmission, he could hear how subdued Jeok Cheongang sounded. His own gaze grew heavy.

“Like I said earlier, this place is truly something. I thought I’d seen a fair bit of the world after traveling all across the land, but…… I’ve never heard of or seen anything like this.”

Unlike Jeok Cheongang, who had spent most of his life on Mount Jiuhua, the Slaughter Saint had lived a wandering life—as an assassin, and then as a physician.

In his youth, he had traveled a thousand li to take someone’s life. In his old age, he had wandered ten thousand li in search of herbs to save one.

Even a young woodcutter who lived day to day cutting trees would have his own experiences and his own life. For someone who had made his mark at opposite ends of life and death, calling his experience “a fair bit” was an understatement born of extraordinary modesty.

Of course, to Jeok Cheongang, who shared the same reality, it sounded entirely sincere.

“So even you don’t have an answer, then, though I expected as much.”

“There’s no way forward, nothing we can do. We can’t even tell day from night. What can we possibly do?”

The Slaughter Saint was right.

The fog blocking their way wasn’t limited to the ground.

There were dark clouds.

At first, they had thought the enormous black mass was just passing by. But it had covered the sky, too.

The moon and stars, which had faintly lit the sky above them at first, disappeared. The clouds swallowed up every last one of them, and wouldn’t even allow a single ray of sunlight through.

As if they meant to frighten the rude intruders who had come without permission.

“Do you think these phenomena are coincidences?”

“Coincidences?”

Jeok Cheongang let out a hollow laugh before he knew it.

“If you’d asked the old me, I would’ve said they were. Yes—if I hadn’t met that impudent brat riding on his master’s back and giving the old man a hard time at this age.”

Jeok Cheongang gazed at the face of the “impudent brat” occupying one of his shoulders.

His Disciple, who had appeared out of nowhere one day and turned the life of an old, sick man upside down.

And now, the man who was changing the world for everyone, not just the life of one person.

“There are no more coincidences for us. Everything that happens from here on is intended, inevitable—and maybe……”

Maybe it was fate, decided from the very beginning.

Jeok Cheongang quietly swallowed the words he had been about to add.

It wasn’t because he didn’t believe in things like fate.

It was because if all of this was fate, then it was cruel beyond measure to Jin Taekyung—and, more than that, he was afraid of how this story would end.

“Maybe what?”

“No, nothing. Let’s move on. What matters more is our situation right now.”

Jeok Cheongang’s words and behavior were unnatural to anyone watching, but the Slaughter Saint didn’t press the matter.

He was a little disappointed, but everyone had their own worries. And the Jeok Cheongang he had watched over the years was far more thoughtful and introspective than people believed.

Especially where Jin Taekyung was concerned.

*Then again, I’m hardly in a position to judge him for that.*

With that thought, the Slaughter Saint’s gaze shifted past Jeok Cheongang’s shoulder.

The young men panting hard as they raced across the rugged mountain terrain, and the Great Sir and Bow Saint bringing up the rear with calm expressions.

But his gaze lingered on them only for a fleeting moment. Then, as if nothing had happened, he spoke.

This time, in his own voice rather than through Sound Transmission.

“We should take a short break.”

His voice spread through the increasingly dense mist.

* * *

The Slaughter Saint had judged well.

No sooner had they been given a brief rest than Hyuk Mujin began retching. Gung Gibang, instead of patting his back, pulled out some jerky.

“……You traitor. Is that jerky really so good?”

After Ju Hwaran helped him stop retching, Hyuk Mujin glared at Gung Gibang. The beggar answered without hesitation.

“Of course.”

“……”

“Still, this stuff is incredible. Maybe it’s because it came from sweat-blood horses? The flavor’s remarkably consistent.”

“……”

“Don’t just glare at me. Eat quietly. You need your strength. Or you could sit down and circulate your qi like that fellow.”

Hyuk Mujin glanced between Song Ilseom, who was already sitting cross-legged, and Gung Gibang, who was still tearing into his jerky. Then his expression hardened as he made up his mind.

“Give me a piece. I want to see what’s so good about it that you’re eating like a beggar who hasn’t had a meal in three days.”

When they had first met, the two had been worlds apart in martial prowess and status. But they had spent enough time together to become almost like friends.

Gung Gibang grinned, showing his yellow teeth.

“Excellent decision. Oh, Young Lady Ju, would you like some, too?”

“No, thank you. I think I’d better circulate my qi for a while.”

Replenishing one’s strength and refining one’s internal energy were both good choices.

Climbing mountains—and rugged mountains at this altitude, no less—caused a completely different kind of exhaustion from running across flat ground.

Besides, even they, whose martial arts were far less advanced than those of the masters traveling with them, could feel the heavy air hanging over all of Tianshan and the strange phenomena that defied explanation.

“Damn, I can’t even remember the last time I felt warm sunlight.”

At Gung Gibang’s grumble, Hyuk Mujin spoke with his mouth full of jerky.

“We got some in the desert.”

“How was that warm sunlight? During the day, I was too scared to even walk around in case I burned to death. Though, by the time we got halfway across, I was starting to miss it.”

“Fair enough. The weather was a real pain in the ass.”

In truth, “a real pain in the ass” didn’t begin to cover it.

What kind of desert had no cacti or bugs, and got alternating hailstorms and downpours for more than half a month?

But now, this was the world they lived in.

And to survive in a changed world, they had to change, too.

“I’m dying here. How many peaks have we climbed already?”

“Five.”

“Already? That’s more than I thought.”

“Not that many, considering how hard we’ve run. And we don’t know how much farther we have to go.”

The Tianshan Mountains were wide.

No, “wide” didn’t do them justice. They were vast.

The range stretched for more than a thousand li, and covered no less than a third of Xinjiang.

And that wasn’t all. It was a Sacred Land, where only a select few among the old Demonic Cult had been allowed to enter—and a Land of Ruin, where any outsider was sure to meet death.

They still had no idea which of the hundreds of peaks held the Cult’s headquarters.

“Terrible.”

“Terrible.”

“At least nothing’s happened yet. That should mean we haven’t been spotted.”

“If the Captain heard you say that, he’d smack you one.”

“Why?”

“He hates that kind of talk. Says it’s bad luck. Something like ‘cli’ or ‘guli’—anyway, it sounds like he’s talking about copper. I never know what he means.”

“Honestly, I can never figure him out.”

“Tell me about it.”

The two muttered as if to themselves, then lay on their backs, gazing blankly at the sky.

Or, more precisely, at the dark clouds that filled it completely.

“How long exactly have we been here?”

“More than a day, less than two.”

“Are you sure?”

“I’m sure.”

“Hard to believe you can say that when you can’t even tell night from day.”

Hyuk Mujin answered firmly.

“Because the Captain still hasn’t woken up.”

“Oh, right. The Slaughter Saint said he’d wake up within two days at the latest.”

“Yeah. So it definitely hasn’t been two days yet.”

Gung Gibang studied Hyuk Mujin for a moment, then suddenly gave a quiet laugh.

“What?”

“It’s just…… You’re something else.”

“Something else how?”

“Almost everything seems to revolve around Jin Taekyung.”

“I don’t know. This all seems perfectly natural to me.”

“Don’t get me wrong. I’m not saying it’s strange or that I don’t understand. I’m saying it because I know exactly how it feels.”

The smile lingering on Gung Gibang’s lips faded.

“That’s what a martial family is. You may not share blood, but sometimes the bonds are thicker than blood.”

Gung Gibang drifted into old memories for a moment, and Hyuk Mujin fell silent.

It felt like a wound he’d kept hidden for a long time had finally burst open.

The Jin Family of Taiyuan. And the Beggars’ Sect.

They were their martial families, their other homes—and the names of two enormous stones weighing down their hearts.

What had happened to the people who had headed west with their banners held high?

If they were still alive, would they ever meet again?

They traded silly remarks on the surface and tried to keep smiles on their lips, but reality was cold enough to make them shudder.

It was even quick enough to allow them no chance to fend off the chill seeping into their very bones.

*Shhhhhhhh.*

A sudden sense of wrongness.

In the next moment, the mist, twisting as if alive, was reflected in Hyuk Mujin’s suddenly widened eyes.
```
