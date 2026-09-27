<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1114.txt",
      "sha256": "8460077a6e7e4822efb9e26348a12368a02346f62c28f0195af080287ad04b2d",
      "bytes": 17701
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5571803096c0f0574f7d568a47146f4b6bafc6e76bab0569484bd95b6c2e53d0",
      "bytes": 1733
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b11a3900716c29bbb12566605a5b2b29b815bc855f6d7ff2496ddb57f4d9e13b",
      "bytes": 244401
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "d5a75f9226f054a2bbba0e54c7b24bb58f5f89f131fcbf1b21c353f9715b36ba",
      "bytes": 915
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "15ab82076eb733e95e97ac57c3f7e71e061f086f8b7dbd8d6311978e944c2718",
      "bytes": 544
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "9a0fe256dc39cae5d32d80b32ba6ba8c5ba74b810251508356321bc6ea5e4d33",
      "bytes": 797
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e2fcf1dd6f0cc6d9608bfc5c80992cf5c6daf2e12e328c9974f37e03f3d20496",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fe022fec4517035afedd6525ad58fe61752347563af0350ad8240eb5964399de",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eb4b634b75c7b394511bc81782da15d9ead97621a792532d65fa7f009afabc7c",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9afa45b80b07543afbfba97ce946b215d2ccddadb56cb70263ae9704a5d64cbb",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "81e3c508f36bdbbfec37f028da5e1c420204474ec94d34d895078f395893cbb1",
      "bytes": 288671
    }
  ],
  "estimated_tokens": 13980
}
-->

# Durable State Update — Chapter 1114

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
1 and safe_through 1114. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1114. Profile updates may replace only one
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
  "chapter": 1114,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1114,
    "continuity_sources": [1114],
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
    "The West Gate has fallen; more than half its garrison are casualties, and some survivors retreated to the Inner City.",
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung is still alive and has forced himself to stand.",
    "Jeong Hogun died defending others; Taekyung remembers him as a steadfast officer.",
    "Taekyung has rallied those around him to keep fighting for the Inner City's people.",
    "The Slaughter Saint remains at the South Gate to support its defense; the Bow Saint’s motives are unclear.",
    "Jeok Cheongang killed the Dalai Lama at the North Gate; Jeok is badly injured, and Perfected Being Hyeoncheon is alive but barely conscious.",
    "The Potala Palace’s vendetta against the Fire Gate Clan began with Songhak’s destruction of its forces more than two hundred years ago; the Dalai Lama allied with Dark Heaven to seek revenge.",
    "The Blood Lord is advancing toward the Inner City and has slaughtered a hundred defenders on the way.",
    "An unidentified flash stopped the Blood Lord’s advance."
  ],
  "continuity_sources": [
    1112,
    1113
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "Can the South Gate hold against the Grand Mage and the four Black Ghosts?",
    "Who or what stopped the Blood Lord’s advance?"
  ],
  "safe_through": 1113,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 일격     | **One Strike**                         |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 상태               | **Status**                     |
| 곤륜     | **Kunlun**             |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 주체 | **Zhu Di** | The Emperor names himself as Zhu Di. |
| 육부 | **Six Ministries** | The central government ministries. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 십이밀승 | **Twelve Secret Monks** | The Potala Palace’s twelve top fighters. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |
| 청허자 | 적천강 | younger martial artist to senior martial artist | Senior | polite | Cheongheoja refers to Jeok Cheongang as 노 선배 while politely declining his offer. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 달뢰라마 | 적천강 | hostile leader confronting a rival martial master | donor | formal and controlled | Addresses Jeok as 시주 while blocking his departure for the West Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1113
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1099
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1112
- **Aliases:** Palace Lord
- **Role:** The former Dalai Lama led the Potala Palace and its Twelve Secret Monks until Jeok Cheongang killed him at the North Gate.
- **Personality:** Driven by the Potala Palace’s inherited vendetta against the Fire Gate Clan, he pursued greater power and an alliance with Dark Heaven despite the contradiction between his cause and his use of demonic power.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He led the Potala Palace’s vendetta against the Fire Gate Clan and allied with Dark Heaven to gain the strength needed to pursue it.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1113
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1112
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1113
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1113
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1114화



찰나지간 공간을 가로지른 빛줄기는 눈부셨고, 동시에 파괴적이었다.

적수공권의 상태에서도 수비군들을 무참히 도륙하던 혈주가, 허리춤에 얌전히 잠들어 있던 자신의 애도(愛刀)를 움직였을 만큼.

콰아아앙!

커다란 굉음과 함께 사방으로 흩뿌려지는 핏물.

그러나 지금까지와는 달리, 그 피의 근원지는 수비군이 아닌 혈주를 따르던 광신도들이었다.

“쿠, 쿨럭. 혈주시여…….”

과연 운이 좋았다고 해야 할까, 아니면 나쁘다고 해야 할까.

기습적으로 날아든 섬광의 여파에 휩쓸려 비명조차 지르지 못하고 절명한 수십여 명의 동료와는 달리, 가까스로 목숨을 보전한 광신도는 혈주를 향해 기어갔다.

천주의 선택을 받은 위대한 사도(使徒)가, 이 고통을 조금이라도 덜어 주길 바라면서.

그리고 혈주는 그 간절한 부름에 응답했다.

천근(千斤)의 무게가 실린 발끝으로.

콰득!

척추가 으스러지는 소리가 났고, 그것으로 끝이었다.

그가 꺼져 가는 생명의 지푸라기라도 잡고 싶었는지, 아니면 죽음을 통한 안식을 원했는지는 혈주도 몰랐다.

아니, 소모품이나 다름없는 조무래기의 죽음 따위는 애초부터 관심 밖의 일이었다는 것이 옳은 표현이었다.

혈주의 시선은 처음부터 줄곧, 자욱하게 피어오른 먼지구름 너머에 고정되어 있었으니까.

“나와.”

서늘한 목소리가 혈주의 입술 밖으로 흘러나온 그 순간.

슈확!

불현듯 뻗어 나온 섬광이 먼지구름을 쪼개며 혈주를 향해 쇄도했다.

정확히는, 섬광처럼 빛나는 열기가.

화륵, 콰아아아아!

이글거리며 공간을 휩쓸어오는 불길.

의심을 확신으로 만드는 그 끔찍할 열기는 느끼며, 혈주는 전력을 다해 적도(赤刀)를 내리그었다.

서걱!

예리한 절삭음과 함께 좌우로 갈라지는 화염.

그 폭만 이십여 장에 달하는 대로변이 삽시간에 불길에 휩싸이고, 거세게 피어오르는 아지랑이 사이로 한 사람의 그림자가 일렁였다.

“어딜 그리 급하게 가느냐.”

착 가라앉은 음성.

그리고 아지랑이 속에서도 또렷하게 빛나는, 화염을 쏟아내고 있는 두 눈동자.

화왕(火王) 적천강.

바로 그였다.

아직은 나타나지 못할 것이라 여겼던, 혹은 어쩌면 영영 두 번 다시 보지 못하리라 생각했던 그의 모습에 혈주의 눈매가 가늘어졌다.

“정파 놈들이 그토록 칭송하던 십왕(十王)의 수좌도 결국 한낱 무부였군. 하나뿐인 제자를 살리고 싶어 그 많은 아군을 버렸나?”

북문을 버리고 왔다고 확신한 혈주의 비아냥에, 적천강이 거친 숨을 가다듬으며 입을 열었다.

“칭송해 달라고 부탁한 적도 없지만, 모든 것에는 그만한 이유가 있는 법이지.”

“뭐?”

“일천의 마병(魔兵)을 쓰러트린 그 날부터 천하는 노부를 화왕이라 부르기 시작했지. 하도 오래되었다 보니 별호가 슬슬 지겨워지던 참인데…… 어쩌면 오늘 이후로 바뀔 수도 있겠다는 생각이 드는군.”

“……!”

일순간, 비로소 적천강의 등장이 무엇을 의미하는지 깨달은 혈주의 얼굴이 일그러졌다.

북문으로 향한 포달랍궁의 전력은 분명 강력했다.

서장 제일의 고수인 달뢰라마와, 비록 애송이에 불과하지만 초절정 고수가 둘이나 포함되어 있던 십이밀승.

거기에 혹시 모를 상황을 대비하여 두 기의 흑귀를 보냈으니, 적천강의 발을 묶는 것을 넘어 그의 숨통을 끊어도 이상하지 않을 정도였다.

‘그런데, 도대체 어떻게?’

자신도 모르게 뇌리를 스친 그 의문에 대한 답을, 혈주는 쉽게 찾을 수 없었다.

아니, 어쩌면 앞으로도 영영 알 수 없을 것이다.

무언가를 지키기 위해 싸우는 자와, 오로지 복수에 눈이 먼 자의 싸움은 종종 예상을 한참 빗나가기도 한다는 것을.

그리고 화왕 적천강에게는, 자신의 모든 것을 바쳐서라도 지켜야 할 사람이 있었다.

“고작, 그따위 땡중들로 노부의 발걸음을 막을 수 있으리라 생각했더냐.”

귓가를 파고드는 나직한 음성에, 혈주는 이를 악물었다.

“미친 늙은이 같으니. 네놈이 아무리 발악해 봤자 달라지는 건 아무것도 없다.”

“지켰고, 지킬 것이다.”

“지금 이 순간에도 죽어 가고 있을, 그 소중한 제자를 말이냐?”

“……뭐라?”

본능적으로 멈칫한 적천강을 향해, 혈주는 입매를 비틀며 웃었다.

“아니. 아니지. 어쩌면 이미 죽었을 수도 있겠군. 마지막으로 보았을 때 이미 사경을 헤매고 있었으니.”

“네놈이 감히……!”

그리고 제자의 위기를 전해 들은 적천강이 도무지 감출 수 없는 격동에 휩싸인 그 순간.

쉭!

희미한 파공성과 함께, 허깨비처럼 사라진 혈주의 신형이 십여 장의 거리를 지우며 들이닥쳤다.

서걱!

마치 두부처럼 갈라지는 지면.

그와 동시에, 가까스로 신형을 비틀어 공격을 피해 낸 적천강의 몸 곳곳에서 핏물이 솟구쳤다.

투두둑!

스치는 것만으로도 피해를 불러일으키는 막강한 검압(劍壓).

그러나 허공으로 비산하는 저 핏물에 담긴 의미가 무엇인지, 적천강 본인은 누구보다 잘 알고 있었다.

‘몸이……!’

천근처럼 무겁다. 감각을 통한 반응 역시 늦었다.

적천강은 분노와 다급함으로 인해 잠시 잊고 있었던 중요한 사실을 깨달았다.

북문에서의 힘겨운 전투를 끝마친 자신의 육신이 얼마나 지쳐있었는지.

찰나지간 주체할 수 없을 만큼 흔들려 버린 마음이, 지금 같은 생사결에서 얼마나 심각한 악영향을 초래하는지.

그리고 이와 같은 적천강을 상황을, 혈주는 정확히 꿰뚫어 보았다.

콰아아아아!

폭풍처럼 휘몰아치는 도격(刀擊)이 공간을 난도질한다.

수십, 아니 수백 합에 달하는 공격이 시간마저 쪼개며 서로를 향해 퍼부어졌고, 이미 지칠 대로 지친 적천강은 이 싸움의 끝이 얼마 남지 않았다는 사실을 본능적으로 직감할 수 있었다.

그 끝에 기다리고 있을 싸움의 결과가 자신의 죽음이며, 이를 뒤바꿀 수 있는 유일한 패가 남아 있다는 것 역시도.

‘화신귀무(火神鬼武).’

스스로의 모든 것을 장작 삼아 피워 올리는 최후의 불꽃.

열화문 대대로 전해져 내려오는, 그러나 동시에 그 끔찍한 여파로 인해 금기(禁忌)시되어 온 신공.

이미 그로 인해 죽을 고비를 넘긴 적천강이었으나, 이제 그에게 남은 것은 그것뿐이었다.

회복을 넘어 재생에 가까운 힘을 발휘하는 혈주를 쓰러트릴 방법은.

하지만 그 짧은 고민의 시간조차, 매 순간이 위기나 다름없는 지금의 적천강에게는 사치였을지 몰랐다.

‘빈틈!’

혈주의 안광이 번뜩인 그 찰나의 순간.

후우웅!

지면에 깊게 박힌 적도 대신, 전력을 다해 휘두른 일권(一拳)이 적천강의 옆구리를 향해 포탄처럼 쏘아졌다.

진태경의 일섬에 의해 위기에 빠진 이후, 어째서인지 더욱 강력해진 힘과 속도로.

“……!”

적천강에게는 헛숨을 삼킬 시간조차 주어지지 않았다.

이미 육신은 지쳤고, 감각은 무뎌졌으며, 공력은 어느덧 바닥을 드러내고 있는 상황.

그저 온 힘을 다해 강기가 담긴 두 팔을 교차시키는 것만이, 그가 할 수 있는 최선이었다.

콰아아앙!

거대한 굉음과 함께 뒤집히는 시야.

순식간에 십여 장에 달하는 공간을 가로질러 내쏘아진 적천강의 신형이, 한때는 사람들로 붐볐을 커다란 객잔을 뚫고 처박혔다.

콰드드득!

기둥이 무너지고, 나뭇조각이 비산한다.

객잔을 시작으로 무려 일곱 채에 달하는 건물을 박살 낸 뒤에야, 적천강은 뱃속에서 울컥 치밀어오르는 뜨거운 무언가를 토해 냈다.

푸화악.

어딘지 모를 뒷골목을 적시는, 까맣게 죽은 사혈(死血).

그리고 흐릿해지는 시야 속, 질풍처럼 쇄도하는 혈주의 모습이 그의 시야에 들어왔다.

그 핏빛 눈동자에 담긴, 희열과 살기도 함께.

“적천강-!”

포효하듯 부르짖은 혈주가 적도를 내리그은 그 순간이었다.

카아아앙!

날카롭게 울려 퍼지는 굉음.

예상치도 못한 시점에 사각(斜脚)에서 쏘아진, 다섯 줄기의 섬광을 튕겨 내며 뒷걸음질 친 혈주가 믿을 수 없다는 듯이 눈을 부릅떴다.

우우웅.

손아귀를 통해 전해지는 울림.

부르르 떨리는 적도(赤刀)는 금세 안정을 되찾았지만, 이미 악귀처럼 일그러진 혈주의 얼굴은 펴지지 않았다.

“제법이긴 한데…… 그만큼 나이를 처먹었으면 나설 때 안 나설 때 정도는 구분해야지. 그렇지 않나?”

으르렁거리는 듯한 음성과 함께 서서히 돌아가는 고개.

동시에 혈주의 핏빛 안광이, 어느덧 적천강의 앞을 가로막은 다섯 명의 노인을 향해 번뜩였다.

“사지가 찢겨 뒈지기 싫으면.”

그러나 그 막강한 살기에도, 그들의 중심에 선 호리호리한 체구의 노 도사는 조용히 적천강을 부축했다.

화아악.

부축과 동시에 스며드는 공력에, 창백하기 그지없던 얼굴 위로 감돌기 시작하는 혈색.

다시 한번 울컥 피를 토해 내는 적천강에게, 노도사가 담담한 음성으로 입을 열었다.

“고생하셨습니다. 지금부터 이곳은 저희가 맡지요.”

“쿨럭, 자네들은…….”

“진태경, 그 아이에게 남아 있는 시간이 그리 길지 않을지도 모릅니다.”

“……!”

“가십시오, 어서. 이것이 모두를 위한 길이기도 합니다.”

물론, 노 도사의 입술 사이로 흘러나온 ‘모두’라는 단어에는 한 사람의 존재가 빠져 있었다.

“허, 미친 늙은이가 여섯으로 늘어났군.”

비웃음과 함께, 혈주는 적도를 비스듬히 내리그었다.

“그렇다면, 전부 죽어라.”

슈화악!

반월의 형태를 한 핏빛 강기가 적도를 타고 쏘아졌다.

강기의 크기만 무려 일장에 달하는, 끔찍하리만치 강대한 기운이 담긴 일격.

그리고 바로 다음 순간.

꽈아아앙!

하늘이 쪼개지는 듯한 굉음과 함께, 반경 십여 장의 공간 전체가 가루가 되어 흩날렸다.

어느샌가 아득한 허공을 밟고 서 있는, 여섯 개의 인영 아래에서.

“……!”

혈주의 눈빛이 깊게 가라앉은 그때, 예의 그 호리호리한 노 도사가 자신이 부축하고 있던 적천강을 향해 작게 고개를 숙였다.

“부디, 이 까마득한 후배의 무례를 용서하시길.”

이미 북문에서부터 누적된 극심한 피로와 내상을 입은 적천강은 대답조차 할 수 없었다.

아니, 그럴 시간조차 없었다는 것이 정확한 표현이었다.

그가 뭐라 대답하기도 전에, 노 도사의 두 팔이 힘차게 회전했으니까.

“이런 미친……!”

혈주의 다급한 외침이 터져 나왔을 때는, 이미 모든 것이 늦어 버린 후였다.

쐐애애액!

맹렬한 파공성과 함께 허공을 가로질러 내성으로 쏘아지는 적천강의 신형.

그리고 분노에 휩싸인 혈주가 그 뒤를 쫓기도 전에, 부드럽게 지면에 내려앉은 다섯 명의 노 도사가 앞을 가로막았다.

신선과도 같은 풍모와 고고한 학을 닮은 기운.

거기에 더하여, 앞서 보인 놀라운 신법까지.

그제야 비로소 불청객들의 정체를 깨달은 혈주가 서늘한 음성으로 입을 열었다.

“곤륜오선(崑崙五仙).”

“우리를 알고 있나?”

“어찌 모를까. 진작 뒈졌어야 할 늙은이들이 곤륜파의 쌀만 축내고 있다는 가슴 아픈 이야기를.”

당연하게도, 혈주가 말하는 것과 세간에 알려진 그들의 인식은 하늘과 땅만큼의 격차가 있었다.

곤륜오선은 현 장문인인 청허자의 사숙(師叔)들이자 팔순이 훌쩍 넘은 지금까지도 곤륜파를 지탱하고 있는 장로들.

비록 저마다의 무위는 초절정의 문턱에서 멈춰 섰으나, 어린 시절부터 친형제처럼 자란 우애를 바탕으로 펼치는 합격술(合格術)은 초절정 고수조차 깨트릴 수 없다는 것이 세간의 평이었다.

물론, 지금 이 순간 혈주의 눈에 비친 그들의 모습은 조금 더 까다롭고 늙은 부나방들에 불과했지만.

“당장 눈앞에서 꺼져라. 마음 같아서는 단숨에 찢어 죽이고 싶으나, 그럴 시간조차 아까우니.”

호리호리한 체구의 노 도사, 곤륜오선의 대형이라 할 수 있는 태청진인(太淸眞人)이 고개를 저었다.

“응할 수 없는 제안이군. 하여 빈도가 다른 대안을 제시할까 하는데.”

“대안은 없다. 그리고 네놈들은 방금 마지막 남은 기회마저 걷어차 버렸지.”

혈주는 적도를 비스듬히 늘어트린 채 곤륜오선을 향해 발걸음을 내디뎠다.

진태경에 이어 적천강까지.

다 잡은, 심지어 반드시 죽여야 할 먹잇감을 벌써 두 번이나 놓친 그다.

어째서인지 세상에 알려진 것보다 훨씬 강하게 느껴지는 저들의 기운이 의문스럽기는 했지만, 초절정 고수도 상대한다는 합격술이라고 해 봤자 자신의 앞에서는 촌각이면 무너질 사상누각(沙上樓閣)에 불과할 터였다.

분명, 그렇게 생각했다.

“자네가 틀렸어. 우리에게는 아직 기회가 남아 있네.”

“뭐?”

“이게 우리가 생각해 낸 대안일세.”

그제야 태청진인의 입가에 걸린 담담한 미소를 발견한 혈주가 무언가 이상함을 알아차린 그때.

스아아아아.

태청진인, 아니 곤륜오선 전원을 중심으로 막강한 기운이 솟아올라 공간을 뒤흔들었다.

절정의 끝자락에서 멈췄다고 알려진 무위가 믿어지지 않을 정도의, 동시에 신선이라는 뜻이 담긴 별호가 무색해질 정도의 거친 기세가.

그리고 혈주가 그 왠지 모를 익숙함의 정체를 깨닫기까지는, 그리 오랜 시간이 필요하지 않았다.

“네놈들. 설마?”

“듣던 대로 흉흉한 물건이로군. 이 잠력단(潛力團)이라는 것은.”

“……!”

“그리 놀랄 것 없네. 일평생 마공(魔功) 따위는 익힌 적 없었으니, 이것을 복용하기 위해 우리도 그만한 대가를 치러야 했지.”

태청진인의 말은 사실이었다.

잠력단은 주로 사마외도(邪魔外道) 계열의 무공, 그중에서도 초절정의 경지에 도달하지 못한 불완전한 이들에게만 허락되는 힘.

그렇기에 설령 암천의 교도들이 지니고 있던 여분의 잠력단을 손에 넣어 복용한다 하더라도, 정순한 기운을 익힌 이들은 큰 효력을 발휘하지 못했다.

단 한 가지.

팔십여 년이 넘는 긴 세월 동안 쌓아 올린 선천지기(先天眞氣)를 깨트려, 잠력단에 담긴 기운을 억지로 흡수하는 미친 짓을 벌이지 않는 이상은.

“괴물을 막기 위해서라면…….”

우우우웅.

깊은 울림과 함께 흐려지는 말꼬리.

그와 동시에 불안하고도 희뿌연, 그러나 틀림없는 강기(罡氣)가 태청진인의 손에 들린 검을 뒤덮었다.

아니, 곤륜오선 전원의 검을 타고 솟구쳐 올랐다.

“우리 역시, 기꺼이 괴물이 되는 수밖에.”

그 순간.

쉭!

공간이 갈라지고, 여섯 개의 신형이 뒤얽혔다.



* * *



일각(一刻).

곤륜오선이 두 다리로 서 있을 수 있었던 시간은 고작 일각뿐이었다.

그러나 동시에, 누군가에게는 무려 일각이나 되는 시간이기도 했다.

아마도 그래서였을 것이다.

콰드득!

태청진인이 두 다리가 뽑혀 나가는 아득한 고통 속에서도 웃을 수 있었던 것은.

서걱!

이어 양팔이 잘려 나가고.

퍼엉!

몸 안의 오장육부가 찢겨 나가는 와중에도 비명을 삼킬 수 있었던 것은.

그리고 마침내 드리워지는 죽음의 그림자 앞에서, 끝까지 도의(道意)를 지킨 노 도사는 이미 자신보다 숨이 끊어진 사제들을 향해 마지막 인사를 건넸다.

“기억……하게. 우리의 죽음은 결코 헛되지 않…….”

퍼걱!

끔찍한 파열음과 함께 뇌수가 튀었다.

산산이 부서진 태청진인의 머리에서 발을 뗀 혈주가 서늘한 목소리로 속삭였다.

“아니, 이건 개죽음이야.”

천천히 고개를 드는 그의 귓가에는, 어느덧 더욱 크고 가까워진 함성이 온 사방에서 들려오고 있었다.

아니, 그건 정확히 여덟 글자의 교언(敎言)이었다.

천상천하 만마앙복.

하늘 위, 하늘 아래. 모든 것이 무릎 꿇을지어다.

“……분명, 그리되리라.”

나직한 뇌까림을 남겨둔 괴물의 발걸음이, 내성을 향해 이어졌다.

끈적한 핏물과 함께.
```

## Final English reading copy

```markdown
# Chapter 1114

The beam of light that cut through space in an instant was dazzling—and devastating.

Even barehanded, the Blood Lord had been mercilessly slaughtering the defenders. The flash had been powerful enough to make him draw the beloved blade that had rested quietly at his waist.

KABOOM!

A deafening crash—and blood sprayed in every direction.

But this time, unlike before, the blood hadn’t come from the defenders. It came from the fanatics who followed the Blood Lord.

“C-cough. Blood Lord……”

Had the man been lucky, or unlucky?

Unlike the dozens of comrades who had been caught in the sudden flash and died without even a chance to scream, this fanatic had barely survived. He crawled toward the Blood Lord, hoping the great Apostle chosen by the Lord of Heaven would ease his pain, even a little.

And the Blood Lord answered his desperate plea.

With a foot weighted by a thousand geun.

CRUNCH!

His spine broke. That was the end of it.

The Blood Lord didn’t know whether the man had been clinging to the last thread of life or hoping to find peace in death.

No—that wasn’t quite right. The truth was that the death of a nobody, little more than a disposable pawn, had never interested him in the first place.

The Blood Lord’s gaze had been fixed all along on the other side of the thick cloud of dust.

“Come out.”

The instant his cold voice left his lips—

Swoosh!

A flash of light burst out of nowhere, splitting the cloud of dust as it surged toward him.

To be precise, it was heat shining like a flash of light.

Fwoosh—KABOOOOOM!

Flames roared through the air, sweeping toward him.

The dreadful heat made his suspicions certain. The Blood Lord swung the Red Blade down with all his might.

Slice!

With a keen cutting sound, the flames split in two.

The avenue, more than twenty jang wide, was engulfed in fire in an instant. Through the shimmering heat rising in waves, a person’s shadow wavered.

“Where are you in such a hurry to go?”

His voice was low and steady.

And even through the heat haze, his eyes shone clearly as flames poured from them.

Fire King Jeok Cheongang.

It was him.

The Blood Lord’s eyes narrowed at the sight of Jeok Cheongang. He hadn’t expected the man to appear yet—and had thought he might never see him again.

“So the head of the Ten Kings, whom the orthodox faction praises so highly, is no more than a mere warrior after all. You abandoned all those allies to save your one and only Disciple?”

The Blood Lord spoke with scorn, certain Jeok Cheongang had abandoned the North Gate to come here.

Jeok Cheongang caught his breath before replying.

“I never asked anyone to praise me. But everything has its reasons.”

“What?”

“Since the day I defeated a thousand demonic soldiers, the world has called me the Fire King. It’s been so long that I was starting to grow tired of the title…… But perhaps that will change after today.”

“……!”

The Blood Lord’s face twisted as he finally realized what Jeok Cheongang’s appearance meant.

The Potala Palace forces sent to the North Gate had certainly been formidable.

The Dalai Lama, the greatest master in Xizang, and the Twelve Secret Monks, who included two Supreme Peak masters—even if they were still greenhorns.

And, to prepare for any unforeseen circumstances, they had sent two Black Ghosts as well. It wouldn’t have been surprising if they’d done more than hold Jeok Cheongang in place—if they’d even taken his life.

*But how?*

The Blood Lord couldn’t find an answer to the question that had crossed his mind without his realizing it.

No. Perhaps he would never find one.

The battle between those fighting to protect something and those consumed entirely by revenge could often defy expectations by a wide margin.

And Fire King Jeok Cheongang had someone he would protect, even if he had to give everything he had.

“Did you really think a few bald monks like that could stop this old man?”

At the low voice that burrowed into his ear, the Blood Lord clenched his teeth.

“You crazy old bastard. No matter how hard you struggle, nothing will change.”

“I protected him. And I will again.”

“You mean that precious Disciple of yours, who might be dying even as we speak?”

“……What did you say?”

Jeok Cheongang instinctively hesitated. The Blood Lord twisted his mouth into a smile.

“No. That’s not right. Perhaps he’s already dead. Last I saw him, he was hovering at death’s door.”

“You dare……!”

The moment Jeok Cheongang heard his Disciple was in danger and was swept up in an emotion he couldn’t hide—

Whoosh!

With a faint whistle of air, the Blood Lord’s figure vanished like an illusion. He crossed more than ten jang in an instant and came crashing down on him.

Slice!

The ground split as easily as tofu.

At the same time, Jeok Cheongang twisted just enough to evade the attack, but blood burst from several places on his body.

Thud-thud-thud!

The overwhelming Sword Pressure caused damage with nothing more than a near miss.

Yet Jeok Cheongang knew better than anyone what the blood scattering through the air meant.

*My body……!*

It felt as heavy as a thousand geun. His senses were slow to respond, too.

Jeok Cheongang realized he’d forgotten something important in his anger and desperation: how exhausted his body was after the grueling battle at the North Gate.

And how severely his momentarily uncontrollable emotions could hinder him in a life-and-death duel like this.

The Blood Lord saw right through Jeok Cheongang’s condition.

KABOOOOOM!

A storm of blade strikes tore through the air.

Dozens—no, hundreds—of attacks rained down on each other, as if even time itself were being sliced apart. Jeok Cheongang, already exhausted, instinctively sensed that the fight was nearly over.

He knew the end would bring his death. He knew, too, that he had only one card left that could change it.

*Dance of the Fire God and Demon.*

A final flame, kindled by burning everything he was.

A divine art passed down through the generations of the Fire Gate Clan—and forbidden because of its terrible aftermath.

Jeok Cheongang had already once faced death because of it. But now, it was all he had left.

The only way to defeat the Blood Lord, whose power could do more than heal—it could Regenerate.

But perhaps even the brief moment he spent considering it was a luxury. Every instant was a crisis for Jeok Cheongang now.

*An opening!*

The Blood Lord’s eyes flashed in that split second.

Whoom!

Instead of the Red Blade, which was embedded deep in the ground, a fist swung with all his might toward Jeok Cheongang’s side like a cannonball.

Since falling into danger after Jin Taekyung’s One Annihilation, the Blood Lord’s strength and speed had somehow grown even greater.

“……!”

Jeok Cheongang didn’t even have time to gasp.

His body was exhausted, his senses dulled, and his internal energy had all but run dry.

The best he could do was cross his Force-clad arms with all the strength he had.

KABOOM!

His vision flipped with the deafening crash.

Jeok Cheongang’s body shot across more than ten jang and smashed through a large inn that had once been crowded with people.

CRASH!

A pillar fell. Wooden splinters flew everywhere.

Only after he’d smashed through seven buildings, starting with the inn, did Jeok Cheongang cough up something hot rising violently from his gut.

Puhak.

Blackened blood stained some back alley or other.

Through his blurring vision, he saw the Blood Lord rushing toward him like a gale.

There was joy in those blood-red eyes, along with killing intent.

“Jeok Cheongang!”

The Blood Lord roared his name and swung the Red Blade down—

CLANG!

A sharp crash rang out.

The Blood Lord was forced back, eyes wide with disbelief, after deflecting five streaks of light fired from an unexpected angle.

Whoooom.

A vibration traveled through his grip.

The Red Blade trembled, then quickly steadied. But the Blood Lord’s face, twisted like a Fiend’s, did not.

“Not bad…… But if you’re old enough to have lived this long, you should know when to stay out of it. Don’t you think?”

His growling voice came with the slow turn of his head.

The Blood Lord’s blood-red gaze flashed toward the five old men standing in front of Jeok Cheongang.

“If you don’t want to be torn limb from limb and die.”

But even in the face of that overwhelming killing intent, the slender old Daoist at their center quietly helped Jeok Cheongang to his feet.

Fwoosh.

As internal energy flowed into him, color began to return to Jeok Cheongang’s deathly pale face.

Jeok Cheongang coughed up another mouthful of blood. The old Daoist spoke calmly.

“Thank you for all you’ve done. We’ll take it from here.”

“Cough. You’re……”

“Jin Taekyung may not have much time left.”

“……!”

“Go. Quickly. It’s for everyone’s sake, too.”

Of course, the word “everyone” in the old Daoist’s mouth left out one person.

“Ha. Now there are six crazy old men.”

With a sneer, the Blood Lord tilted the Red Blade down at an angle.

“Then die, all of you.”

Swoosh!

A crescent of blood-red Force shot along the Red Blade.

The strike carried a horrifyingly immense power, its Force stretching a full jang in size.

And the very next moment—

KABOOM!

A crash like the sky splitting apart rang out. The entire area within a ten-jang radius crumbled to dust.

Beneath the six figures standing in midair, high above the ground.

“……!”

As the Blood Lord’s gaze darkened, the slender old Daoist—the same one who had been supporting Jeok Cheongang—bowed his head slightly toward him.

“Please forgive the impertinence of someone so far your junior.”

Jeok Cheongang was already suffering from severe exhaustion and Internal Injury, accumulated since the North Gate. He couldn’t even answer.

No—that wasn’t quite right. There was no time.

Before he could reply, the old Daoist’s arms swung with force.

“You crazy—!”

By the time the Blood Lord’s frantic shout rang out, it was already too late.

Whoooosh!

Jeok Cheongang’s body shot through the air toward the Inner City with a fierce whistle.

Before the enraged Blood Lord could chase after him, the five old Daoists landed softly on the ground and blocked his way.

They had the bearing of immortals and an aura like noble cranes.

And their astonishing movement technique, which they had just displayed.

Only then did the Blood Lord realize who the uninvited guests were. He spoke in a chilly voice.

“The Kunlun Five Immortals.”

“You know us?”

“How could I not? It’s a heartbreaking story: old men who should have died long ago, still eating up the Kunlun Sect’s rice.”

Naturally, the Blood Lord’s idea of them was worlds apart from how they were known to the public.

The Kunlun Five Immortals were the Martial Uncles of Cheongheoja, the current Sect Leader, and Elders who had sustained the Kunlun Sect well into their eighties.

Though each of them had stopped just short of Supreme Peak, their reputation was that the cooperative technique they’d developed through a bond like that of brothers, having grown up together since childhood, could not be broken even by a Supreme Peak master.

Of course, right now, to the Blood Lord, they were nothing but a few more troublesome, aged moths.

“Get out of my sight. I’d like to tear you apart and kill you in an instant, but you’re not worth the time.”

The slender old Daoist, the eldest of the Kunlun Five Immortals, Perfected One Taecheong, shook his head.

“I cannot accept that offer. Allow me to propose an alternative.”

“There is no alternative. And you just threw away your last chance.”

The Blood Lord let the Red Blade hang at an angle and stepped toward the Kunlun Five Immortals.

First Jin Taekyung, then Jeok Cheongang.

Twice now, he’d lost prey he’d nearly caught—prey he had to kill.

Their aura felt far stronger than what was known to the world, which was puzzling. But their cooperative technique, said to let them face even Supreme Peak masters, would be no more than a house of cards before him. It would collapse in an instant.

Or so he’d thought.

“You’re mistaken. We still have a chance.”

“What?”

“This is the alternative we came up with.”

The Blood Lord noticed the calm smile on Perfected One Taecheong’s lips and sensed something was wrong.

Shaaaaa.

An overwhelming power rose around Perfected One Taecheong—or rather, around all five of the Kunlun Five Immortals—and shook the space around them.

Their fierce aura was hard to believe in men whose skill was said to have stopped at the very edge of Peak. It was so rough, it made the immortal meaning of their title seem absurd.

And the Blood Lord didn’t need long to recognize what felt so familiar about it.

“You…… No way.”

“As I’d heard, this is a fearsome thing. This Temporary Strength Pill.”

“……!”

“Don’t be so surprised. We’ve never practiced demonic martial arts in our lives. To take this, we had to pay a price.”

Perfected One Taecheong was telling the truth.

The Temporary Strength Pill was a power usually reserved for those who practiced demonic, heterodox arts—especially those whose skill was incomplete and who had not reached Supreme Peak.

So even if those who practiced righteous energy got their hands on one of the spare pills carried by Dark Heaven’s followers and took it, it wouldn’t have much effect.

There was only one way.

To break the innate qi they’d built up over more than eighty years, forcing themselves to absorb the energy in the pill.

Unless they did something mad like that.

“To stop a monster……”

Whoooom.

His voice trailed off amid a deep rumble.

At the same time, a restless, pale Force—undeniably Force—covered the sword in Perfected One Taecheong’s hand.

No. It surged up along the swords of all five Kunlun Five Immortals.

“If that’s what it takes, then we’ll gladly become monsters, too.”

At that moment—

Whoosh!

Space split, and six figures clashed in a tangle.

* * *

Fifteen minutes.

That was all the time the Kunlun Five Immortals could stay on their feet.

But to someone else, it was a full fifteen minutes.

Perhaps that was why Perfected One Taecheong could smile even through the distant pain of having both his legs torn off.

Slice!

Why he could swallow his screams as his arms were cut off.

Boom!

Why, even as his internal organs were torn apart, the old Daoist could hold to his Daoist principles and offer a final farewell to his Junior Brothers, who had already stopped breathing.

“Remember…… Our deaths will not be in vain……”

CRACK!

His brain matter burst out with a horrible pop.

The Blood Lord lifted his foot from Perfected One Taecheong’s shattered head and whispered coldly.

“No. This is a meaningless death.”

As he slowly raised his head, he heard a roar from all around him—louder and closer than ever.

No. It was a creed of exactly eight characters.

Above heaven and below heaven, ten thousand demons bow in homage.

Above heaven and below heaven, let all things kneel.

“……So it shall be.”

Leaving those low words behind, the monster continued toward the Inner City.

With sticky blood at his feet.
```
