<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1187.txt",
      "sha256": "ffefec1d56afa5e25edc6f839e5985252ad5bcc51af5101ca9cc8815c295a16c",
      "bytes": 11847
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "35d40bde97ea4455f556eed23b63c1e9cd13f5978c0bc3cebd6f7765ae37e059",
      "bytes": 2321
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "587ca3c339172ce1141564e4df02783e2904e19433378a113fb1e729abee4261",
      "bytes": 248769
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "0801774f9b79c6c384586e83d62309af60fbbd69a53bb4a7979888578b1985da",
      "bytes": 684
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "435b60df023a1a0e5c16324c181051324703cd40138081c519efb9461cb792e4",
      "bytes": 1393
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f69a75174bcef781b96840e1bde0790115adb0af37b768b5f7da1367fd8d9c23",
      "bytes": 1701
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "552a77ffed0d01e0b159e614928d9266a284c192b4488f0a3ac242aaf51b6900",
      "bytes": 974
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "c84f70d0b552a0fbd897318ce7ea028ac76cde3852f759ebc7e0ae310c695b46",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "78b534449c2fc9ac5e20862e80e667b2a6f09fb24efa6e78c61cabd9c907a54f",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6592233b34dcd7f1d0f74935310ed387046c3f86f1869fa5f218139dd6824a3a",
      "bytes": 295903
    }
  ],
  "estimated_tokens": 10918
}
-->

# Durable State Update — Chapter 1187

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
1 and safe_through 1187. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1187. Profile updates may replace only one
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
  "chapter": 1187,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1187,
    "continuity_sources": [1187],
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
    "Jeok Cheongang’s group is in Tianshan with Taekyung unconscious; the Slaughter Saint expects him to wake within two days.",
    "The group is following Mae Jonghak’s contingency plan after the allied forces missed their deadline; the Murim Alliance and Imperial Army are drawing Dark Heaven’s attention away from the desert.",
    "The group has supplies made from the eight exhausted horses, and the terrain ahead is too rough for their carriage.",
    "Taekyung’s earlier strength during the fasting pill’s effects surprised the Slaughter Saint, who wonders whether Taekyung used his full strength.",
    "The group has climbed five peaks in Tianshan, where darkness and strange phenomena persist; a mist has begun moving as if alive.",
    "The fates of the separated companions, allied troops, Jin Family, and Beggars’ Sect remain unknown.",
    "Taekyung experiences unexplained chest pain and difficulty sleeping.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1186,
    1185
  ],
  "open_questions": [
    "What happened to the separated companions, allied troops, Jin Family, and Beggars’ Sect, and why did the Murim Alliance and Imperial Army miss the rendezvous?",
    "What is causing Tianshan’s darkness and strange phenomena, and why does the mist appear to move as if alive?",
    "What is the source of Taekyung’s chest pain and sleeplessness, and did he use his full strength against the fasting pill’s effects?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1186,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1186
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares blunt, teasing friendships with Taekyung and Hyuk Mujin.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1186
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has warm friendships with fellow Fire Dragon Pavilion members Taishan and Gung Gibang; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1186
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1186
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1186
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1186
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃1187화



뱀.

꿈틀거리며 다가오는 안개를 본 순간, 모두의 머릿속에 가장 먼저 떠오른 단어였다.

음습하고 어두컴컴한 그것은 마치 사냥감을 포착한 거대한 포식자처럼 다가오고 있었고, 이미 석상처럼 굳어 버린 다리는 좀처럼 땅에서 떨어지지 않았다.

단지 눈에 보이는 것을 넘어선 무언가가, 인간의 원초적인 공포심을 자극하고 있었기 때문이었다.

그리고 화왕(火王) 적천강이야말로 저 안개에 담긴 힘의 본질을 누구보다 먼저, 동시에 명확히 알아차릴 수 있는 극소수의 인물 중 하나였다.

‘이건……!’

틀림없다.

마기(魔氣).

아니, 이제는 마력(魔力)이라고도 불리는 저 심연과도 같은 기운이 오감을 타고 흐르며 몸과 마음을 속박하고 있었다.

무섭도록 빠르고, 음험하게.

하지만 어째서일까. 마음 한구석에서 솟구치는 공포심과는 별개로, 적천강은 불현듯 이유를 알 수 없는 강렬한 이끌림을 느꼈다.

그것은 실로 묘한 느낌이었다.

이제는 기억도 나지 않는 어머니의 따뜻한 품처럼, 지금 이대로 안개에 몸을 맡기면 모든 것이 편해질 것만 같은 기분.

분명 저 희뿌연 세상 속에는 아무런 고난도, 번뇌도 없는 평화로운 낙원이 자신을 기다리고 있을-

으득!

아릿한 통증과 함께 터져 나오는 핏물.

찰나의 순간, 혀를 깨물어 이성을 되찾은 적천강은 입안 가득 차오르는 핏물을 내뱉으며 부르짖었다.

“갈(喝)-!”

강대한 공력으로 사방을 떨어 울리는 창룡후(蒼龍吼).

그리고 맹수의 포효와도 같은 일갈을 내지른 것은 비단 그 혼자만이 아니었다.

궁성과 살성.

적천강과 동시에 반응한 두 명의 초인은 잠시나마 주춤하는 안개를 보며 신음했다.

사술(邪術).

그것도 지금껏 본 적 없는, 지극히 강력하고도 요사스러운 힘이 이 공간을 잠식하고 있었다.

아니, 어쩌면 이 천산(天山) 전체를.

하지만 그들이 직면한 더욱 큰 문제는 따로 있었다.

아.

아아.

꿈을 꾸는 듯 몽롱한 눈빛과 넋 나간 목소리. 텅 빈 허공을 헤집는 손길에 맞춰, 안개를 향해 천천히 나아가는 발걸음까지.

단 한 명의 예외도 없었다. 안개에 가장 가까이 있던 궁기방과 혁무진은 물론, 비교적 거리가 있던 주화란과 송일섬까지도.

마치 이성을 상실한 실혼인(失魂人)처럼 변해 버린 일행들의 모습에, 위험을 직감한 세 명의 노고수는 그들을 향해 망설임 없이 신형을 내쏘았다.

그리고 빛살처럼 손을 뻗은 그 순간.

슈확!

날 선 파공성과 함께 공간이 뒤틀렸다.

어느새 거대한 짐승의 발톱처럼 날카롭게 휘어진 안개가, 그 안에 스며든 어둠이 적천강의 불그스름한 눈동자에 비쳤다.

“감히!”

화륵, 퍼어엉!

창노한 외침과 함께 터져 나온 화염신장(火焰神掌)의 불길이 마력의 발톱을 부수고 공기를 뜨겁게 달군다.

단 한 치의 접근도 허락하지 않는, 그야말로 업화의 열기.

하지만 이 찰나의 기습이 전부 의도된 것이었다는 사실을 알아차리기 전까지는 그리 오랜 시간이 걸리지 않았다.

솨아아악.

희뿌옇게 피어오른 수증기 속, 적천강은 자신도 모르게 눈을 부릅떴다.

보이지 않는다.

손만 뻗으면 닿을 수 있었던 궁기방의 닳아빠진 옷깃이, 보고만 있어도 한 대 쥐어박고 싶어지는 혁무진의 뒤통수가.

아니.

‘사라졌다.’

그래, 아마도 이것이 가장 옳은 표현일 것이다.

두 눈으로 똑똑히 보았으니까.

안개에 파묻힌 그들의 전신이 세상에서 지워지던 그 광경을.

‘이게 무슨.’

목 끝까지 차오른 침음성을 삼킨 적천강은 황급히 주위를 둘러보았다.

그리고 동시에 매우 중요한 한 가지 사실을 깨달았다.

안개와 함께 사라진 것은 저들뿐만이 아니었다는 것을.

“……허.”

적천강은 참고 있던 숨을 토해 냈다.

도대체 언제부터였을까.

앞서 느꼈던 그 묘한 기시감?

모르겠다. 눈앞에 펼쳐진 풍경은 변함없었지만, 그 외의 모든 것은 달라져 있었다.

없다. 아무도.

고작 삼 장 남짓한 거리에 있던 궁성과 살성의 모습도 어느덧 보이지 않았다.

응당 느껴져야 할 인기척은 물론, 그들이 지닌 한 터럭의 기운조차도.

‘환술(幻術)인가? 아니면 기문진(奇門陣)?’

지금껏 소문으로 들었던, 혹은 옛 정마대전 당시 전장에서 직접 겪었던 무수한 사술들이 뇌리를 스쳐 지나갔지만 적천강은 쉽사리 답을 내리지 못했다.

한 세기가 넘는 세월을 살았고, 한 시대를 풍미한 거인인 그조차도 이러한 종류의 사술은 처음 겪어보는 것이었으니까.

‘궤가 다르다.’

말 그대로였다.

환마(幻魔)나 귀곡자(鬼谷子) 따위의 별호로 불리며 숱한 악명을 떨치던 전대의 대마두들도 이 정도의 사술을 구사하지는 못했다.

정확히는, 적천강의 고강한 무위가 그것을 허락하지 않았다.

제아무리 강한 사술이라 해도 결국 정해진 한계는 있는 법.

마교 제일의 환술가였던 환마는 그렇게 두 눈이 뽑혔고, 정밀한 기문진으로 수백의 정파 무림인을 몰살시킨 귀곡자는 한 줌 핏물로 녹아내렸다.

단 한 사람, 화왕 적천강의 손에.

하지만…….

‘이러한 진법은 본 적도, 들은 적도 없다.’

적천강은 어느 때보다 날카롭게 곤두선 감각으로 탐색 영역을 넓혀갔으나, 시간이 흐를수록 생각은 확신으로 변해 갔다.

제아무리 기괴막측한 사술이라 할지라도 모든 것에는 기운의 흐름과 그 중심이 되는 핵(核)이 있는 법.

그러나 이 기묘한 공간에서 그가 느낄 수 있는 것이라고는 아무것도 없었다.

그저 마기 특유의 끈적하고 불쾌한 기운을 풍기며 다가오는 거무스름한 안개와, 등을 통해 전해지는 누군가의 일정한 호흡뿐.

“이 지경이 되도록 곯아떨어져 있다니. 팔자 좋은 놈이로고.”

투덜거리는 어조와는 달리 입가를 스치는 희미한 미소.

만약 깨어나 있었다면 억울한 표정으로 한바탕 하소연했을 제자의 얼굴을 힐끗 바라본 적천강은, 스스로에게 다짐하듯 뇌까렸다.

“걱정하지 말거라. 앞으로 무슨 일이 벌어지든, 네 녀석의 털끝 하나 상하지 않게…….”

문득 흐려지는 말꼬리.

무슨 이유에서인지 잠시 침묵하던 그가 이내 한숨 섞인 목소리로 덧붙였다.

“그냥 참아라. 털끝 하나 정도는 상해도 안 죽는다.”

이번에도 제자는 대답하지 않았고, 스승은 형형하게 빛나는 두 눈동자로 짙은 안개 너머를 응시했다.

“무엇 하느냐. 당장 쳐 기어 나오지 않고.”

거인의 부름에, 저 희뿌연 장막 밖의 존재들이 답했다.

- 크르르르.

물결이 되어 흐르는 안개 속.

이제야 비로소 번뜩이는 무수한 안광(眼光)을 보며, 적천강은 천천히 심호흡했다.

“개떼처럼 몰려왔군.”

사지 백해로 뻗어 나가는 극양의 기운을 따라 아지랑이가 피어오르고, 맹렬한 화염에 휩싸인 두 주먹이 이 세상의 것이 아닌 괴물들을 향해 겨누어진다.

“오너라.”

긴 밤의 시작이었다.



* * *



한 치 앞도 보이지 않을 만큼 짙은 안개와 그 사이로 쇄도하는 무수한 그림자.

그리고 그 모든 것의 중심에서, 더욱 맹렬하게 타오르는 화염.

퍼엉!

일장(一掌).

더도, 덜도 필요 없었다. 지극히 효율적이며 파괴적인 그 움직임 끝에는, 그저 바위도 녹여 버릴 열기와 죽음만이 존재할 뿐.

쿵!

결코 인간이라 부를 수 없는 거대한 몸뚱어리가 무릎을 꿇는다.

하나의 머리에 박힌 세 개의 붉은 눈은 여전히 사냥감을 향하고 있었지만, 이미 흔적도 없이 녹아 버린 가슴께는 둘 중 누가 사냥꾼이었는지 증명하고 있었다.

- 크륵.

최후의 단말마와 함께 빠르게 빛이 빠져나가는 눈동자.

하지만 괴물이 마지막 숨을 내뱉기도 전에 돌아선 사냥꾼은 이미 또 다른 생명들을 불사르고 있었다.

콰직!

쉴 새 없이 부수고, 터트리고, 짓뭉갠다.

손, 발, 다리, 무릎과 팔꿈치, 때로는 이마.

모든 것이 무기였고 곧 무언가의 죽음으로 이어졌다.

오척단구의 괴물도, 삼두육비(三頭六臂)의 괴물도 휘몰아치는 불의 장벽을 뚫지 못했다.

낫보다 날카로운 발톱과 인간이었다면 응당 달려 있어야 할 팔 대신 자리 잡은 녹슨 날붙이가 끊임없이 사지를 노렸지만, 적천강의 몸과 마음은 조금도 흐트러지지 않았다.

지금으로부터 수십 년 전, 구화산(九華山)이 화마에 휩싸였던 그 날처럼.

아니, 그때와는 비교도 할 수 없을 만큼 강하고 냉정한 상태였다.

화왕이라는 노괴를 구화산 밖으로 끄집어낸 일천의 마교도는 최소한 인간의 외관이라도 갖추고 있었으나, 눈앞의 괴물들은 인세(人世)에 나타나서는 안 될 저주받은 존재들이었으므로.



- 캬룩!

- 크아아아아!



그 어디에서도 느껴 본 적 없는 광기와 살기.

이미 오래전 이지를 상실한 채, 오직 주인의 명령만을 따라 움직이는 것이 분명한 그것들은 끊임없이 달려들었고.

콰드드드득!

쉴 틈 없이 죽어 갔다.

푸화악!

자욱하게 솟구치는 피 분수.

마치 벌레를 털어 내듯, 단 한 번 휘두른 손짓에 조각 조각난 수백 개의 육편이 사방으로 튀었다.

“고작 이 정도냐.”

일순간 생겨난 죽음과 공백의 틈바구니에서, 적천강은 나직한 뇌까림과 함께 주위를 쓸어보았다.

“이 정도로 노부를 쓰러트릴 수 있으리라 생각했더냐.”

문득, 이제는 얼굴마저 흐릿한 스승님께서 했던 말씀이 떠오른다.

‘천강아, 천하는 넓고 강자는 많다.’

그때 들었던 말처럼, 구화산 밖의 세상은 광활했다.

천하의 절반을 집어삼킨 천마와 그를 따르는 대마두들도, 중원을 차지하고 있던 도사와 땡중들도 강자였다.

그러나 스승께서 하신 말씀은 저것이 전부가 아니었다.

‘하지만, 네 녀석이라면 그중에서도 가장 강한 놈 중 하나가 될 수 있겠지.’

늘 그랬듯이, 스승님의 말씀은 옳았다.

그리고 거기에 더하여, 등 뒤에 업고 있는 어느 새파란 목숨의 존재가 지금의 그를 더욱 강하게 만들었다.

“너희가 오지 않으니, 이제는 내가 가도록 하마.”

치이익.

힘주어 내디딘 발끝을 따라 피어오르는 열기.

이지를 상실한 괴물들에게도 본능은 남아 있음인가.

압도적인 무력의 차이에 잠시 공세를 멈춘 괴물들을 향해, 적천강은 천천히 걸음을 옮겼다.

아니, 정확히는 옮기려고 했다.

결코 잊을 수 없는 누군가의 목소리가 귓가를 파고들기 전까지는.

“여전하시군요.”

일순간, 적천강의 신형이 얼어붙었다. 

그와 동시에 바람을 만난 등불이 꺼지듯, 힘없이 사그라지는 안광에 누군가의 모습이 비쳤다.

이곳에 있을 수도, 있어서도 안 되는 한 사람의 얼굴이.
```

## Final English reading copy

```markdown
# Chapter 1187

A snake.

That was the first word that came to everyone’s mind when they saw the mist writhing toward them.

It crept closer, gloomy and dark, like a huge predator that had spotted its prey. Their legs, already frozen stiff as statues, would hardly lift from the ground.

Something beyond what they could see was stirring the most primal fear in them.

And the Fire King, Jeok Cheongang, was one of the few people who could recognize the true nature of the power within that mist before anyone else—and understand it clearly.

*This is……!*

There was no doubt.

Demonic qi.

No—or magical power, as it was now called. That abyssal energy flowed through his five senses, binding his body and mind.

Terrifyingly fast. Insidiously.

But why? Separate from the fear surging in one corner of his mind, Jeok Cheongang suddenly felt an intense, inexplicable pull.

It was a truly strange feeling.

Like the warm embrace of a mother he could no longer remember, it made him feel that if he gave himself over to the mist now, everything would be easier.

Surely, in that hazy world, a peaceful paradise awaited him—one without hardship or anguish—

*Crack!*

Blood burst forth with a sharp sting of pain.

In that instant, Jeok Cheongang bit his tongue to regain his reason. He spat the blood filling his mouth and roared.

“Ha!”

His azure dragon’s roar shook the air in every direction with the force of his internal energy.

And he wasn’t the only one to unleash a battle cry like a beast’s roar.

The Bow Saint and the Slaughter Saint.

The two superhumans who had reacted at the same time as Jeok Cheongang groaned as they watched the mist falter, if only briefly.

Dark arts.

And not just any dark arts. A powerful, sinister force unlike anything they had ever seen was consuming the space around them.

No—perhaps all of Tianshan.

But they faced an even greater problem.

“Ah.”

“Ahhh.”

Dazed eyes, as if they were dreaming, and vacant voices. Hands reaching through empty air, feet slowly carrying them toward the mist.

Not a single person was spared. Gung Gibang and Hyuk Mujin, who were closest to the mist, and even Ju Hwaran and Song Ilseom, who were farther away.

As their companions turned into soulless people who seemed to have lost their reason, the three veteran masters sensed the danger and shot toward them without hesitation.

And the moment they reached out, hands moving like streaks of light—

*Whoosh!*

A sharp whistle cut through the air, and space warped.

The mist, now curved into a giant beast’s razor-sharp claw, and the darkness seeping through it reflected in Jeok Cheongang’s reddish eyes.

“How dare you!”

*Fwoosh—BOOM!*

With his furious cry, the flames of the Flame Divine Palm burst forth, shattering the claw of magical power and heating the air.

A searing blaze that allowed not so much as an inch of approach.

But it didn’t take long for him to realize that this momentary ambush had been entirely deliberate.

*Shhhhhhh.*

In the cloud of steam that rose pale and white, Jeok Cheongang’s eyes widened before he knew it.

He couldn't see them.

Gung Gibang’s threadbare collar, within reach if he stretched out a hand. Hyuk Mujin’s head, which made Jeok Cheongang want to smack him just looking at it.

No.

*They disappeared.*

Yes, that was probably the best way to put it.

He had seen it with his own eyes.

He had watched their bodies, swallowed by the mist, get erased from the world.

*What is this…?*

Jeok Cheongang swallowed the groan rising to his throat and hurriedly looked around.

At the same time, he realized something very important.

They weren’t the only ones who had vanished along with the mist.

“……Huh.”

Jeok Cheongang let out the breath he had been holding.

When had it started?

That strange sense of déjà vu he’d felt earlier?

He didn’t know. The scenery before his eyes hadn’t changed, but everything else had.

No one. There was no one.

Even the Bow Saint and the Slaughter Saint, who had been barely three yards away, were nowhere to be seen.

Not a trace of their presence—not even a hair’s breadth of their energy, which he should have been able to feel.

*An illusion technique? Or a Mystic Gate Formation?*

All manner of dark arts he had heard about in rumors, or experienced firsthand on the battlefields of the Great Faction War, flashed through Jeok Cheongang’s mind. But he couldn’t reach an answer.

Even he, a giant who had lived for over a century and made his mark on an era, had never encountered dark arts of this kind.

*This is on a different level.*

He meant it literally.

Even the great fiends of the previous generation, infamous under names like the Illusion Fiend and Guiguzi, couldn’t wield dark arts this powerful.

More precisely, Jeok Cheongang’s formidable martial prowess had never allowed them to.

No matter how powerful the dark arts, they still had limits.

The Illusion Fiend, the Demonic Cult’s greatest master of illusion, had had both eyes gouged out. Guiguzi, who had slaughtered hundreds of orthodox Murim warriors with his intricate Mystic Gate Formation, had melted into a pool of blood.

Both at the hands of one man: the Fire King, Jeok Cheongang.

But……

*I’ve never seen or heard of a formation like this.*

Jeok Cheongang expanded his search with senses sharper than ever. The longer he searched, the more his thoughts solidified into certainty.

No matter how bizarre the dark arts, everything had a flow of energy and a core at its center.

But in this strange space, he couldn’t sense a thing.

Only the dark mist approaching with the uniquely sticky, unpleasant energy of demonic qi—and someone’s steady breathing against his back.

“Sleeping soundly even after all this. You’ve got it easy, you know.”

His tone was gruff, but a faint smile brushed his lips.

Jeok Cheongang glanced at the face of the Disciple who would have complained bitterly if he were awake. Then, as if making a promise to himself, he muttered,

“Don’t worry. No matter what happens, I won’t let a hair on your head be harmed……”

His voice suddenly trailed off.

For some reason, he fell silent for a moment, then added with a sigh,

“Just bear with it. One hair getting hurt won’t kill you.”

This time, too, his Disciple did not answer. His Master gazed beyond the dense mist with eyes that shone fiercely.

“What are you waiting for? Crawl the hell out here!”

At the giant’s call, the beings beyond the pale veil answered.

*Grrrr.*

In the mist flowing like waves, countless eyes suddenly gleamed.

Jeok Cheongang slowly took a deep breath.

“You came in a pack.”

Heat shimmered out from the Extreme Yang energy extending through his limbs and every part of his body. His two fists, engulfed in fierce flames, pointed at the monsters that did not belong in this world.

“Come on.”

The long night had begun.

* * *

Mist so thick he couldn’t see an inch ahead. Countless shadows surged through it.

And at the center of it all, flames burned ever more fiercely.

*Boom!*

One palm strike.

No more was needed. At the end of that supremely efficient, devastating motion, there was only heat enough to melt rock—and death.

*Thud!*

A huge body that could hardly be called human sank to its knees.

Three red eyes embedded in its single head still fixed on their prey, but its chest, melted without a trace, proved which of them had been the hunter.

*Grrk.*

The last gasp escaped it, and light quickly faded from its eyes.

But before the monster had even breathed its last, the hunter had already turned away, setting other lives ablaze.

*Crack!*

He smashed, burst, and crushed without pause.

Hands, feet, legs, knees and elbows—sometimes even his forehead.

Everything was a weapon, and everything led to something’s death.

Neither the five-foot-tall monsters nor the three-headed, six-armed ones could break through the blazing wall of fire.

Claws sharper than scythes and rusty blades where human arms should have been relentlessly targeted his limbs, but neither Jeok Cheongang’s body nor his mind faltered.

It was like the day Mount Jiuhua had been engulfed in flames, decades ago.

No—the state he was in now was far stronger and colder than he had been then.

The thousand members of the Demonic Cult who had drawn the old monster called the Fire King out of Mount Jiuhua had at least looked human. The monsters before him were cursed beings that should never have appeared in the human world.

*Kyarruk!*

*Kraaaaah!*

A madness and killing intent he had never felt anywhere before.

They had clearly lost their reason long ago and moved only at their master’s command, yet they kept charging at him—

*RrrrCRUNCH!*

—and kept dying without respite.

*Splaaat!*

Blood sprayed high into the air.

With a single sweep of his hand, as if brushing away insects, he sent hundreds of pieces of flesh flying in every direction.

“Is that all you’ve got?”

In the gap of death and emptiness that had opened in an instant, Jeok Cheongang swept his gaze across the area and muttered,

“Did you really think you could take me down with this?”

Suddenly, the words of his Master, whose face had grown hazy with time, came to mind.

*“Cheongang, the world is vast, and there are many strong people.”*

Just as his Master had said, the world beyond Mount Jiuhua had been vast.

The Heavenly Demon, who had swallowed half the world, and the great fiends who followed him had been strong. So had the Daoists and Buddhist monks who occupied the Central Plains.

But that wasn’t all his Master had said.

*“But you could become one of the strongest among them.”*

As always, his Master’s words had been right.

And on top of that, the presence of a certain young life he carried on his back made him even stronger now.

“Since you won’t come to me, I’ll come to you.”

*Hiss.*

Heat rose with every forceful step.

Had even instinct survived in the monsters who had lost their reason?

The monsters, who had briefly halted their attack in the face of the overwhelming difference in strength, watched as Jeok Cheongang slowly walked toward them.

No—more precisely, he was about to.

Until a voice he could never forget pierced his ear.

“You’re as I remember.”

In an instant, Jeok Cheongang froze.

At the same time, the fierce light in his eyes faded like a lamp caught by the wind, and someone’s figure was reflected in them.

The face of someone who could not be here—and should not be.
```
