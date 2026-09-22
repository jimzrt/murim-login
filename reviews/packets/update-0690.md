<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0690.txt",
      "sha256": "5ebd87026f5ace8d3b2c4924cc7a303b656ad4ac31062e8cede1633d16097182",
      "bytes": 15013
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "01b69a335e38630f7363a17abd70e6b13d4cf412239da07517a31e79866038bd",
      "bytes": 1400
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3bd36033a8e83ea76cb8345710c858f69987095efab9064f44135007a7214e6b",
      "bytes": 204372
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "397fa981d70354f5ca92977a7327d42ccc4064cf18e777c8d8d77f7fba754de6",
      "bytes": 942
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "bb6f90f9cd1a1a4b39cc107082d1a269314a3e54b05d8df76bb8e1546beedb6a",
      "bytes": 769
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f9764f89c654127c1bac120430a1e2a69b37144ece5be2dcefca45e6821f5b2c",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "95aa0d0e6adab58b250544cd9b5e8d4c90e35bd436b6483b75c677adb0e5ed57",
      "bytes": 784
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ca1a5d87443cafe496ffebac0cb1e0867f61acd8ab9287afa83438d2337931a7",
      "bytes": 1883
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dcd853a2885091de7cb3a2324ab83657ce67a665c6ead2916b7422e6e24b95c0",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "60b9132e024039d4416071f32b5c8a81a7dd5e0e5ce7a0c73cb8aced8d8afe84",
      "bytes": 613
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "88d4c603f32ff38de1a5783682550ac527698743ee808d3264e4ee923c1bb59e",
      "bytes": 770
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4506cae833ed25c6ef3d3e18ca271a3de42c25d153622332981ac6b0b58fa50f",
      "bytes": 787
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "200f5962ea16f23ea49728b7c0229f42391ea0b769c874ac120f605cdbfc66f3",
      "bytes": 670
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "115fe2ab39ec79fd7d1f1bb0fcd8446da618315aade3f81fc34873c82e51fdf2",
      "bytes": 212668
    }
  ],
  "estimated_tokens": 13265
}
-->

# Durable State Update — Chapter 690

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 690. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 690. Profile updates may replace only one
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
  "chapter": 690,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 690,
    "continuity_sources": [690],
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
    "Yohi is awake in an unexplained enclosed stone realm, with her internal energy seal removed and her flexible sword absent.",
    "Yohi cannot find an exit despite searching for more than two shichen, striking the stone, and climbing the vines.",
    "Muyaho can guide Yohi through the rock wall while carrying her on its back.",
    "Yohi and Muyaho are now in a bright, warm realm filled with living vegetation, flowers, and animals behaving peacefully together.",
    "Jin Taekyung lies unconscious and half-submerged in a pond within the realm.",
    "An unknown energy-laden wind and falling leaves preceded the appearance of a Black Tiger beneath a colossal tree."
  ],
  "continuity_sources": [
    689
  ],
  "open_questions": [
    "What is the enclosed stone realm and how does Muyaho pass through its walls?",
    "Why was Yohi's internal energy seal removed, and where are Heugung and the others?",
    "What is Jin Taekyung's condition, and can Yohi reach him?",
    "What is the identity and nature of the Black Tiger?",
    "Is the bright realm connected to the dark arts or to the unexplained energy in the wind?"
  ],
  "safe_through": 689,
  "temporary_decisions": [
    "Treat Yohi's afterlife conclusion as mistaken or unresolved until the realm is explained.",
    "Keep Black Tiger distinct from White Tiger in terminology."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 아문 | **Amun** | Acupoint |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 688
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the ruler directing Nanman's general mobilization and purge of disloyal tribes.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 688
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, and he now controls the Nanman Beast Palace through the Heugung identity.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 689
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 689
- **Aliases:** Beast Miao King
- **Role:** Heugung is the secret identity of the Beast Miao King, a Supreme Peak master and long-term Dark Heaven contingency who concealed himself through the Bone-Shrinking Technique.
- **Personality:** Heugung is calculating, patient, ruthless, and obsessive, masking coercion and strategic intent behind warmth and romantic devotion toward Yohi.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung is obsessed with Yohi and is willing to threaten her and the Yao people to force her compliance while secretly serving the Southern Heaven Demon Empress.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 689
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who is currently unconscious under the disguised Beast Miao King's control.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 689
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 689
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 688
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 679
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 689
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people, one of Nanman's four great tribes, and is currently separated from Heugung in an unexplained enclosed realm with her internal energy restored.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃690화



남만인들은 기본적으로 무(武)를 숭상한다.

중원의 한족들처럼 농사를 짓고, 가축을 키우고, 강과 산에서 금은을 캐지만 결국 그들에게 있어 가장 중요한 것은 무력이었다.

재물이 있으면 무얼 하나. 그해 농사가 풍년이 되고 울타리에 가축이 가득해도 결국 그것들을 지키기 위해서는 힘이 필요했다.

전사. 그리고 전사와 함께 싸움에 임할 수 있는 맹수.

이는 적의 가슴에 꽂아 넣을 수 있는 검인 동시에, 이 땅을 지킬 방패였다.

오랜 투쟁의 역사를 겪은 남만인들은 이 사실을 잘 알고 있었고, 오독문이 멸문하고 남만야수궁이 설립된 이후에도 전사와 맹수 양성에 상당한 힘을 기울였다.

거대 부족이든, 중소 부족이든 마찬가지였다. 결국 힘이 없으면 도태되고 몰락하는 법.

이런 생각은 사대 부족으로 꼽히는 요족의 대족장인 요희 역시 크게 다르지 않았다.

아니, 오히려 야망이 컸던 만큼 다른 부족장들보다 더한 열의를 보였다.

그녀는 백상의 행동을 묵인하는 대가로 받은 금은보화를 군사력에 투자했다.

젊고 재능 있는 청년들을 모집하여 전사로 육성했고 맹수들의 각 종류와 장단점을 파악, 교배를 통해 개량하기까지 했다.

하지만…….

스윽.

그늘 속에서 몸을 일으킨 ‘그것’을 마주한 순간, 지금껏 수많은 맹수를 마주했던 요희는 가슴이 덜컥 내려앉는 것을 느꼈다.

“……!”

벼락이 정수리를 관통한다면 이런 기분일까.

사실 크기와 힘이라면 그 어떤 맹수도 상(象:코끼리)을 따라올 수 없다.

마치 작은 동산과도 같은 크기에 길고 두꺼운 코는 나무마저 부러트릴 만큼 강하고, 날카로운 엄니는 갑옷마저도 관통해 버리니까.

그러나 ‘그것’은, 저 흑호(黑虎)는 달랐다.

요희는 느낄 수 있었다. 지금껏 본 적 없는 검은 호랑이로부터 뿜어져 나오는 거대하고, 압도적인 기세를.

‘이, 이건…….’

단순히 크기나 외형의 문제가 아니었다.

상이 작은 동산이라면. 저 흑호는 태산이다.

비록 상과 같이 길고 두꺼운 코도, 날카로운 엄니도 없었지만, 그저 우뚝 서 있는 그 자체만으로도 모든 것을 베고 짓누를 만큼 강대한 힘이 느껴졌다.

맹수라는 단어로는 표현할 수 없다. 영물(靈物)? 그것 역시 마찬가지다.

지금 그녀의 눈에 비친 저 흑호는 영물보다도 훨씬 깊고, 압도적인 기운을 발산하고 있었다.

‘저건 도대체…….’

요희가 침음성을 삼킨 그때, 흑호를 중심으로 흘러나온 한 줄기 서늘한 바람이 주위를 덮쳤다.

솨아아아.

사방을 가득 메운 풀과 꽃이 허리를 굽히고, 작은 연못을 채운 맑은 물이 출렁인다.

전신을 휩쓸며 지나가는 바람에 불현듯 떠오른 어떤 기억이 요희의 뇌리를 스쳤다.

‘이 바람, 느껴 본 적 있어. 그것도 두 번이나.’

당시에는 아무런 의미도 두지 않았지만, 이제는 알 것 같았다.

흑웅이 준 단환에 정신을 완전히 잃기 직전, 그리고 알 수 없는 거대한 공간에서 처음 눈을 떴을 때도 이와 같은 바람이 불었다는 것을.

‘그럼 혹시 흑웅으로부터 우리를 구한 것이…….’

거기까지 생각이 미치자 요희의 눈꺼풀이 파르르 떨렸다.

그러나 그녀가 채 입을 열기도 전에, 무야호를 닮은 청백색 눈동자로 낯선 불청객을 말없이 응시하던 흑호는 문득 몸을 돌려 거대한 나무 뒤로 모습을 감췄다.

솨아아.

그와 동시에 천천히 잦아드는 바람.

뒤늦게나마 요희가 조심스럽게 나무로 다가갔지만, 어찌 된 일인지 넓은 그늘 어디에도 흑호의 모습은 보이지 않았다.

사라진 것이다.

마치 유령처럼. 그 어떤 기척이나 흔적도 없이.

“……!”

어떻게?

마치 귀신에 홀린 것 같은 기분이다. 다음 순간 들려온 무야호의 울음소리가 아니었다면, 아마 그녀는 한참이나 넋 나간 얼굴로 제자리에 서 있었을지도 몰랐다.

- 그릉.

툭.

울음소리와 함께 축축한 코가 팔꿈치에 닿는다.

잠에서 깬 사람처럼 퍼뜩 고개를 든 요희는 잠시 잊고 있던 한 사람의 존재를 떠올렸다.

‘진태경.’

머릿속은 아직 해결되지 않은 생각들로 복잡했지만, 지금은 그보다 중요한 것이 남아 있었다.

황급히 연못으로 달려간 요희는 우선 진태경의 상태부터 살폈다.

코와 입을 통해 흘러나오는 옅은 숨결. 다행히 피로 누적으로 깊은 잠에 빠졌을 뿐, 그의 상태는 나쁘지 않았다.

아니, 오히려 요희가 마지막에 봤던 것보다 훨씬 나아진 듯했다.

‘기분 탓인가?’

고개를 갸웃거린 요희는 진태경의 양팔을 붙잡았다.

아무리 맑은 물이라도 상처에 스며든다면 상태가 호전되기 힘든 법. 이미 연못에 반쯤 잠겨 있던 그를 뭍으로 끌어올리기 위해서였다.

그리고 요희가 힘주어 그의 몸을 일으키려던 그때.

턱.

새하얀 털로 뒤덮인 앞발이 요희의 손등을 덮었다. 그 행동에 담긴 뜻을 얼핏 알아차린 그녀가 물었다.

“가만히 놔두라고?”

- 크릉.

“미안하지만 그럴 수는 없…….”

- 크르릉!

서걱, 첨벙!

그야말로 순식간에 벌어진 일이었다. 갑작스럽게 찾아온 고통을 느끼며 연못으로 쓰러진 요희는 놀란 눈으로 백호를 바라보았다.

손등에서 느껴지는 아릿한 고통.

맹수의 예리한 발톱이 스쳐 지나간 피부에서 흐른 핏물이 수면 위를 붉게 물들이고 있었다.

‘도대체 왜?’

그러나 예기치 못한 상황에 당황한 것도 잠시뿐. 얼마 지나지 않아 요희는 저 영특하기 짝이 없는 백호가 왜 이런 행동을 했는지 깨달았다.

스아아.

“상처가…… 아물고 있어?”

말 그대로다. 그녀는 맑은 수면 속에서 아물어 가고 있는 자신의 손등을 바라보며 눈을 부릅떴다.

베어졌던 살이 조금씩 이어 붙고, 흘러나오던 핏물이 멎어 간다.

느린 속도로, 그러나 확실하게.

아무는 과정에서 느껴지는 통증 따위는 잊힐 만큼 놀라운 현상.

요희가 그 경이로운 광경을 더 자세히 지켜보기 위해 손을 들어 올리자, 아물어 가던 살이 회복을 멈추고 다시 희미한 핏물이 흘러나오기 시작했다.

‘연못. 연못에서 손을 뺐기 때문이야.’

이번에 떠올린 짐작은 정확했다. 다시 연못에 손을 담그기 무섭게 아물기 시작하는 상처를 확인한 요희가 중얼거렸다.

“……상처를 회복시켜 주는 연못이라니.”

단 한 방울만으로 일 갑자의 공력을 얻는다는 전설의 영약, 공청석유(空淸石乳)보다도 허무맹랑한 이야기다. 그러나 이제는 더 이상 놀랍지도 않았다.

모든 것을 자신의 두 눈으로 똑똑히 보고, 느꼈으니까.

기문진법(機門陳法)이라는 네 글자로도 설명할 수 없는 이 기이한 공간. 정체 모를 흑호의 존재와 어느새 상처 하나 없이 완전히 아문 손등의 상처까지.

이제야 목덜미에 검상(劍傷)을 입었던 무야호가 멀쩡히 살아남은 이유를 알 것 같았다.

“이래서 날 막았던 거구나. 그가 연못에 있어야 더 빨리 회복될 테니까.”

- 그릉.

희미한 울음소리를 흘린 무야호가 천천히 손등을 핥았다.

나름대로 미안함을 전하는 영물의 모습을 바라보던 요희가 입을 열었다.

“그럼 조금 전 사라진 그 흑호가 우리를 구한 거니? 너와 진태경을 치료한 것도?”

크게 끄덕여지는 고개. 자신의 짐작이 맞았음을 확인한 요희가 연이어 질문을 쏟아 냈다.

“이유가 뭐야? 저 흑호가 어떤 존재인지, 주인이 누구인지는 알고 있어? 이곳이 어디인지는?”

잠시 머뭇거리던 무야호가 고개를 가로저었다.

불과 칠 주야 전. 야수묘왕과 진태경을 따라 애뇌산으로 향했던 무야호는 이미 흑호와 한 차례 마주친 적이 있었지만, 타고난 영물인 녀석에게도 흑호의 존재는 이해할 수 없는 불가해(不可解)의 영역이었다.

“후우. 너도 잘 모르는구나.”

- 끄으응.

“괜찮아.”

요희는 시무룩해진 무야호의 목덜미를 쓸어 주면서도 머릿속이 복잡했다. 무언가를 생각하기에는 정보가 너무나도 부족한 상황.

이곳이 어디인지. 시간이 얼마나 흘렀는지. 그리고…… 진태경은 언제쯤 의식을 회복할 수 있을지.

이 와중에도 한 가지 다행인 점은, 정체를 알 수 없는 저 흑호가 자신들에게 호의를 베풀었다는 점이었다.

‘최소한 암천과는 아무런 연관도 없어. 그랬다면 모두 죽은 목숨이었겠지.’

내심 중얼거린 요희의 시선이 문득 한 사람에게 닿았다.

반쯤 물에 잠긴 채 마치 죽은 사람처럼 미동도 하지 않는 그.

진태경은 주위에서 벌어지는 일을 아는지 모르는지, 평온하기 그지없는 표정으로 깊은 잠에 빠져 있었다.

‘만약 쓰러진 사람이 그가 아니라 나였다면…… 진태경이 깨어 있었다면 모든 문제가 해결되었을 텐데.’

막막함에서 비롯된 어설픈 생각일지도 모른다. 그러나 요희는 어느새 진태경을 마음 깊이 믿고 있었다.

두 명의 초절정 고수를 단신으로 처치할 만큼 뛰어난 무위와 인의(人意)를 갖춘 진태경이다.

대족장이라는 가죽을 뒤집어썼을 뿐. 사실상 변절자나 다름없는 자신과 달리, 남만을 위험에서 구하기 위해 누구보다 동분서주한 그를 믿지 않는다면 누굴 믿어야 한단 말인가.

‘백상과 암천이 본격적으로 움직이기 시작했다면, 야율 궁주 혼자만의 힘으로는 대적할 수 없을 터. 시간이 부족해.’

요희가 품은 불안감은 대부분 현실로 이루어지고 있었다.

그녀가 알 수 없던 시간의 흐름 속 배반자로 낙인찍힌 야수묘왕은 적지(敵地)로 돌변한 남만야수궁을 벗어나 종적을 감추었고, 남만 전체가 숯불 위 무쇠솥처럼 끓어오르고 있었다.

아니, 어쩌면 그것은 무쇠솥마저 녹여 버릴 용암일지도 몰랐다.

총동원령에 응한 각 부족의 전사들은 줄지어 외궁을 향해 움직였고, 모든 수뇌부가 투옥당한 묘족은 혼란에 빠진 채 숨을 죽였으며, 아무도 모르는 비처에서 대계(大計)의 완성을 목전에 둔 남천마후는 환하게 웃고 있었으니까.

그러나 요희는 그 사실을 알지 못했고, 알 수도 없었다. 정체 모를 기묘한 공간에 갇혀 기도할 뿐이었다.

‘하늘이 있다면 부디.’

부디 그를 한시라도 빨리 깨워 주기를. 자신이 죽어도 좋으니, 한 사람만큼은 깊은 잠에서 일으켜 세워 주기를.

하지만 간절한 바람과 함께 눈을 질끈 감은 요희는 보지 못했다. 그녀의 코앞에서 일어난 아주 작지만 선명한 변화를.

툭.

미세하게 움직이는 누군가의 손가락. 수면 위로 퍼져 나간 동심원(同心圓)이 조금씩, 그리고 멀리 퍼져 나가기 시작했다.



* * *



꿈을 꿨다.

이 모든 게 꿈이라는 걸 알아차릴 수 있었던 이유는 간단했다.

눈을 뜨자마자 한없이 낯익은 누군가의 얼굴이 보였기 때문이다. 시간 속에서 천천히 잊혀 가던 목소리도 함께.

“오, 웬일로 이 시간에 일어났어? 더 자지 않고.”

그 순간, 목이 꽉 막히고 가슴이 먹먹해졌다.

나는 왈칵 솟구치는 눈물을 참으며 인사를 건넸다.

오랜만이네요. 아버지.

하지만 내 의지와는 달리, 저절로 움직인 입술 사이로 흘러나온 목소리는 졸음에 잔뜩 취해 있었다.

“몰라. 그냥 깼어.”

그제야 알았다.

이 꿈속에서 내게 주어진 역할은, 그저 옛 기억을 지켜보는 관찰자에 불과하다는 것을.

그리고 그 사실을 알 리 없는 아버지는 그저 씩 웃어 보였다.

“짜식, 감동인데. 아빠 출근하는 건 어떻게 알고 이 잠꾸러기가 저절로 눈을 떴을까? 응?”

거친 손이 볼을 쿡쿡 찌른다. 사소한 장난에 과거의 내가 투덜거렸다.

“아, 하지 마아. 더 잘 거야.”

“인마. 뭘 또 자. 해가 중천인데.”

“몇 신데?”

“여섯 시. 하루를 시작하기에 딱 알맞은 시각 아니냐?”

“응. 진짜 아닌 것 같아.”

과거의 나는 베개에 얼굴을 파묻었고, 껄껄 웃은 아버지는 자리에서 일어났다.

“자라, 아들. 아빠는 회사 간다.”

“엥. 아직 여섯 신데 벌써?”

“일찍 지방 갈 일이 있어서. 오늘은 좀 늦게 올지도 모르겠네.”

나는 속으로 끊임없이 되뇌었다.

이대로 보내면 안 돼. 아버지, 제발 가지 마세요. 제발.

하지만 과거의 나는 달랐다. 어렸고, 철이 없었다.

지금 이 순간이, 아버지와의 마지막 기억이 되리라는 것 역시도.

“예에. 안녕히 다녀오세요.”

잠에 취한 목소리로 내뱉은 한 마디.

그런 내 모습을 보며 씩 웃은 아버지는, 애정 어린 손길로 머리를 헝클어트렸다.

“그래. 이따 보자.”

그게 전부였다. 아버지는 돌아설 테고, 곧이어 문이 닫힌다. 그리고 몇 시간 뒤 나는 담임 선생님께 불려갈 것이다.

내 기억대로라면, 분명 그럴 터였다.

하지만…….

“그런데 아들.”

“……!”

갑작스럽게 귓가를 파고드는 목소리에 나는 몸을 벌떡 일으켰다.

그것은 과거의 내가 아닌, 어느덧 이십 대 후반에 접어든 나 자신의 의지로 벌어진 일이었고, 아버지는 손목에 찬 시계를 툭툭 두드리며 웃음 섞인 한 마디를 건넸다.

“이제 슬슬 일어나야 하는 거 아니냐?”

그 순간.

쩌적.

나를 둘러싼 모든 것이 무너지고 깨져 나갔다.

익숙한 천장과 방. 아버지의 얼굴. 그 모든 것들이. 그리고 동시에 차가운 무언가가 전신을 덮쳤다.

촤아아악!

사방으로 비산 하는 물보라 속, 한 여자의 부릅뜬 눈동자가 보인다. 곧이어 파르르 떨리는 목소리가 귓가를 파고들었다.

“……어떻게.”

글쎄.

나는 마음속으로 뇌까렸다. 아직도 선명하게 느껴지는 꿈속, 어리고 철없던 소년처럼.

몰라. 그냥 깼어.
```

## Final English reading copy

```markdown
# Chapter 690

At heart, the Nanman people revered martial prowess.

Like the Han Chinese of the Central Plains, they farmed, raised livestock, and mined gold and silver from the rivers and mountains. But in the end, the thing that mattered most to them was military might.

What good was wealth? Even if the harvest was plentiful and the fences were packed with livestock, strength was still needed to protect them.

Warriors.

And ferocious beasts capable of fighting alongside those warriors.

They were swords that could be driven into the chests of their enemies, but also shields that protected this land.

The Nanman people, who had endured a long history of struggle, understood this well. Even after the Five Poisons Sect was destroyed and the Nanman Beast Palace was established, they continued devoting considerable effort to training both warriors and beasts.

It was the same for the great tribes and the smaller ones alike. In the end, anything without strength was destined to be weeded out and brought to ruin.

The Yao people's Great Chieftain, Yohi, one of the leaders of Nanman's four great tribes, was no different.

No—if anything, her great ambition drove her to pursue it with even more zeal than the other tribal chieftains.

She invested the gold and silver she had received in exchange for turning a blind eye to Baeksang's actions into military power.

She recruited young men and women with talent and trained them as warriors. She studied the strengths and weaknesses of every species of beast and even improved them through selective breeding.

But…

Swoosh.

The moment she came face-to-face with *that thing* as it rose from the shadows, Yohi—who had encountered countless ferocious beasts until then—felt her heart sink.

“……!”

*Would this be what it felt like to be struck by lightning through the crown of the head?*

In terms of sheer size and strength, no beast could compare to an elephant.

It was as large as a small hill, its long, thick trunk strong enough to snap trees, and its sharp tusks capable of piercing even armor.

But *that thing*—that Black Tiger—was different.

Yohi could feel it.

A tremendous, overwhelming aura emanated from the black tiger unlike anything she had ever seen before.

*Th-This is…*

It was not simply a matter of size or appearance.

If an elephant was a small hill, then that Black Tiger was Taishan.

It had neither an elephant's long, thick trunk nor its sharp tusks. Yet simply by standing there, it radiated such immense strength that it seemed capable of cutting through and crushing everything.

The word *beast* could not express it.

A spiritual creature? That was no better.

The Black Tiger reflected in her eyes now radiated an aura far deeper and more overwhelming than that of any spiritual creature.

*What in the world is that…?*

Just as Yohi swallowed a low groan, a cool breeze flowed outward from the Black Tiger and swept through the surrounding area.

Swoooosh.

The grass and flowers filling every direction bent at the waist, and the clear water filling the small pond rippled.

As the wind swept over her entire body, a memory suddenly flashed through Yohi's mind.

*I've felt this wind before. Twice, in fact.*

She had attached no meaning to it at the time.

But now, she thought she understood.

Just before she had completely lost consciousness from the pill Heugung gave her, and when she had first opened her eyes in that enormous, unknown space, a wind like this had blown.

*Then could it be that the one who saved us from Heugung was…*

When her thoughts reached that point, Yohi's eyelids trembled.

But before she could even open her mouth, the Black Tiger—which had been silently staring at the unfamiliar intruder with blue-white eyes resembling Muyaho's—suddenly turned around and disappeared behind the enormous tree.

Swoosh.

At the same time, the wind slowly died down.

Yohi belatedly approached the tree with caution, but for some reason, the Black Tiger was nowhere to be seen beneath the broad shadow.

It had vanished.

Like a ghost.

Without a single trace or sign of its presence.

“……!”

*How?*

It felt as though she had been bewitched. If not for Muyaho's cry reaching her ears the next moment, she might have stood there in a daze for quite some time.

—Grrr.

Tap.

Along with the growl, a damp nose touched her elbow.

Yohi raised her head abruptly, like someone waking from sleep, and remembered the existence of someone she had temporarily forgotten.

*Jin Taekyung.*

Her mind was still tangled with unresolved questions, but there was something more important right now.

Yohi hurried to the pond and first examined Jin Taekyung's condition.

A faint breath flowed from his nose and mouth.

Fortunately, he had merely fallen into a deep sleep from accumulated fatigue. His condition was not bad.

No, he seemed to be doing much better than when Yohi had last seen him.

*Is that just my imagination?*

Yohi tilted her head and grasped both of Jin Taekyung's arms.

No matter how clear the water was, if it seeped into his wounds, his condition would have difficulty improving. She intended to pull him onto dry land, since he was already half-submerged in the pond.

And just as Yohi began exerting force to raise his body—

Thump.

A snow-white forepaw covered the back of her hand.

Yohi vaguely understood the meaning behind the gesture and asked,

“You want me to leave him alone?”

—Grrr.

“I'm sorry, but I can't do th—”

—Grrrr!

Slash. Splash!

It happened in an instant.

Yohi fell into the pond, feeling a sudden burst of pain, and stared at the White Tiger with startled eyes.

A sharp sting lingered across the back of her hand.

Blood flowed from the skin grazed by the beast's sharp claws, dyeing the surface of the pond red.

*Why?*

But her confusion at the unexpected situation lasted only a moment.

Before long, Yohi realized why that extraordinarily intelligent White Tiger had done this.

Hiss.

“The wound… Is it healing?”

That was exactly what was happening.

Yohi's eyes widened as she watched the wound on the back of her hand heal within the clear water.

The cut flesh slowly knitted back together, and the bleeding gradually stopped.

Slowly, but surely.

It was such an astonishing phenomenon that she forgot the pain she felt during the healing process.

When Yohi lifted her hand to watch the miraculous sight more closely, the healing flesh stopped recovering, and a faint trickle of blood began flowing once more.

*The pond. It stopped because I took my hand out of the pond.*

Her guess was correct.

The instant Yohi dipped her hand back into the pond, she confirmed that the wound began healing again and muttered,

“…A pond that heals wounds.”

It was a more preposterous story than the legend of gongcheong seokyu, the elixir said to grant a jiazi's worth of internal energy from a single drop.[^1]

And yet she was no longer surprised.

She had seen and felt everything clearly with her own two eyes.

This bizarre space, which could not be explained even by the four words *Mystic Gate Formation*. The existence of the unknown Black Tiger. And the wound on the back of her hand, which had already healed completely without leaving a trace.

Only now did Yohi think she understood how Muyaho had survived after suffering a sword wound across the nape of its neck.

“So that's why you stopped me. He'll recover faster if he stays in the pond.”

—Grrr.

Muyaho let out a faint growl and slowly licked the back of her hand.

Yohi watched the spiritual creature convey its apology in its own way, then opened her mouth.

“Then did that Black Tiger that vanished a moment ago save us? Was it the one that treated you and Jin Taekyung too?”

Muyaho nodded emphatically.

After confirming that her guess had been correct, Yohi fired off one question after another.

“Why? Do you know what kind of creature that Black Tiger is, or who its master is? Do you know where this place is?”

Muyaho hesitated for a moment, then shook its head.

Only seven days ago, Muyaho had followed the Beast Miao King and Jin Taekyung to Ailao Mountain and already encountered the Black Tiger once. Yet even to an innate spiritual creature like Muyaho, the Black Tiger's existence was an incomprehensible mystery.

“Haah. You don't know much either.”

—Whiiine.

“It's all right.”

Yohi stroked Muyaho's nape as it drooped dejectedly, but her mind remained tangled.

There was far too little information to figure anything out.

Where was this place?

How much time had passed?

And… when would Jin Taekyung regain consciousness?

Even so, there was one fortunate thing in all of this.

That unknown Black Tiger had shown them goodwill.

*At least it has nothing to do with Dark Heaven. If it did, we'd all be dead by now.*

Yohi muttered inwardly, and her gaze suddenly settled on someone.

He lay half-submerged in the water, utterly motionless, like a dead man.

Whether he knew what was happening around him or not, Jin Taekyung slept deeply, his expression utterly peaceful.

*If I had been the one who collapsed instead of him… If Jin Taekyung had been awake, every problem would have been solved.*

It might have been a clumsy thought born from helplessness.

But at some point, Yohi had come to trust Jin Taekyung from the bottom of her heart.

He possessed martial prowess great enough to defeat two Supreme Peak masters on his own, as well as humanity and moral conviction.

Unlike Yohi, who merely wore the hide of a Great Chieftain while being little better than a traitor, he had rushed from place to place more than anyone else to save Nanman from danger.

If she could not trust him, then who could she trust?

*If Baeksang and Dark Heaven have begun moving in earnest, Palace Lord Yayul won't be able to oppose them with his strength alone. There's not enough time.*

Most of the anxiety Yohi felt was becoming reality.

During the passage of time she could not know about, the Beast Miao King had been branded a traitor, escaped the Nanman Beast Palace after it turned into enemy territory, and vanished without a trace.

All of Nanman was boiling like an iron cauldron over a bed of charcoal.

No—perhaps it was lava capable of melting even that iron cauldron.

The warriors of each tribe that had answered the general mobilization order moved in lines toward the Outer Palace.

The Miao people, whose entire leadership had been imprisoned, held their breath in the midst of chaos.

And in a secret refuge known to no one, the Southern Heaven Demon Empress smiled brightly as she stood on the verge of completing her grand plan.

But Yohi did not know any of this.

Nor could she know.

Trapped in this strange, unknown space, all she could do was pray.

*If there is a heaven, please…*

*Please wake him as soon as possible.*

*Even if I have to die, please wake at least one person from this deep sleep.*

But with her eyes squeezed shut and her desperate wish spilling from her heart, Yohi failed to see the tiny yet unmistakable change taking place right in front of her.

Tap.

Someone's finger moved faintly.

Concentric ripples spread across the surface of the water, gradually traveling farther and farther away.

* * *

I dreamed.

The reason I could tell that everything was a dream was simple.

The moment I opened my eyes, I saw a face that was endlessly familiar.

Along with a voice that had slowly faded with time.

“Oh, what got you up at this hour? Why aren't you sleeping more?”

At that moment, my throat closed up and my chest felt heavy.

Holding back the tears surging into my eyes, I greeted him.

*It's been a long time, Dad.*

But contrary to my will, the voice that slipped between my automatically moving lips was thick with sleep.

“Dunno. I just woke up.”

Only then did I realize.

In this dream, the role I had been given was nothing more than that of an observer watching an old memory.

And my father, who had no way of knowing that, merely flashed me a broad grin.

“You little punk, I'm touched. How did this sleepyhead know Dad was leaving for work and wake up all on his own? Huh?”

A rough hand poked my cheeks.

The younger me grumbled at the harmless teasing.

“Ah, stop it. I’m going back to sleep.”

“You punk. Why are you sleeping again? The sun’s already high in the sky.”

“What time is it?”

“Six o’clock. Isn’t that the perfect time to start the day?”

“Yeah. It really doesn’t sound like it.”

The younger me buried his face in the pillow, and my father rose from his seat with a hearty laugh.

“Go to sleep, son. Dad’s going to work.”

“Huh? Already? It’s only six.”

“I have to go out of town early today. I might be home late.”

I repeated the same words endlessly in my heart.

*I can’t let him go like this. Dad, please don’t go. Please.*

But the younger me was different.

He was young and immature.

He had no idea that this moment would become his last memory with his father.

“Yeees. Have a good day.”

The words came out in a voice thick with sleep.

My father grinned at me, then affectionately tousled my hair.

“Okay. See you later.”

That was all.

My father would turn around, and the door would soon close.

A few hours later, I would be summoned by my homeroom teacher.

According to my memories, that was definitely what should have happened.

But…

“By the way, son.”

“……!”

At the sudden voice that pierced my ear, I shot upright.

It was not the younger me who had done it.

It happened through the will of my present self, now in my late twenties.

My father tapped the watch on his wrist and spoke with a laugh in his voice.

“Shouldn’t you be getting up soon?”

At that moment—

Crack.

Everything surrounding me collapsed and shattered.

The familiar ceiling and room. My father’s face. All of it.

And at the same time, something cold washed over my entire body.

Splaash!

Through the spray of water scattering in every direction, I saw a woman’s wide-open eyes.

A trembling voice soon pierced my ears.

“…How?”

*Who knows.*

I muttered inwardly, just like the young, immature boy in the dream that still felt so vivid.

*I don’t know. I just woke up.*

[^1]: *Gongcheong seokyu* is a legendary martial-arts elixir; a *jiazi* is a traditional sixty-year cycle.
```
