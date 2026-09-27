<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1156.txt",
      "sha256": "bb212309d00d2960f24b5be2fdfdad0b1fbee86cc6ca467646275c4e9bafbf86",
      "bytes": 15914
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8366c9b689a5f083442ba661a51c808537bcd22e8a6618a660b4e8114c1990b0",
      "bytes": 1538
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7d4396d9a6330a70203162cea821340cc43f73d0c5754dfb3c6a8bfa46a5b17d",
      "bytes": 247107
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "1d2ca5b9e43b23ee720bd4257dc604d8f91eddc9a1894c3a3b9fd0865265e62a",
      "bytes": 777
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "9b630ad131901443eb1b825907551c7bcbd42805b3668b762ba65a9599a3756b",
      "bytes": 545
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "282eaca3d873de8430df0fdf14e56bea32d9f6cf53f21403acc8468079e1035b",
      "bytes": 1774
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e422c0c1421ee189b9aef5c53aaa908c843ccf547477326b307a3e000e2e6b37",
      "bytes": 1725
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "64a61f1e7516ab353e489f9b780c36ed4bd010667024241d091c7a02257e0d97",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "c4b8333704c3dd222ce83eba2c554c0d23b9214b627b3947410fc64dd90c3ae0",
      "bytes": 796
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "8e1eed31c632478bdb51e36a883a1dccf2670ee125db6db13f59da5340ec1600",
      "bytes": 939
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "16566e877dadf9962fe159288f6ea33982316e564820ffc96780a69ffc446c9a",
      "bytes": 703
    },
    {
      "path": "characters/The Helper.md",
      "sha256": "c406d25c8fac618f7383f3ab579a747e31ce0152ca0818603ed0cea27bb5d464",
      "bytes": 593
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2cf1fde5dbf865897b3caf0136bb60cad574dbf3ce03be66f6e4ae675193cb8d",
      "bytes": 293256
    }
  ],
  "estimated_tokens": 12297
}
-->

# Durable State Update — Chapter 1156

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
1 and safe_through 1156. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1156. Profile updates may replace only one
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
  "chapter": 1156,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1156,
    "continuity_sources": [1156],
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
    "Morgoth destroyed Moscow and opened a Gate from the Demon Realm above its ruins; a vast monster army has invaded Earth and is advancing across Russia.",
    "Morgoth accepted Russia’s surrender; Russia will disarm and retain its government, as have more than twenty other surrendering countries.",
    "Morgoth demands Cheon Taemin and Jin Taekyung as tribute; Cheon Taemin remains unconscious, and Jin Taekyung is widely regarded as a new-age savior.",
    "Monster Waves and Gate mutations are occurring worldwide at rising rates; magical power distribution is approaching Great Cataclysm levels.",
    "Public calls for Jin Taekyung and Sky to sacrifice themselves may grow; the Skeleton King fears Jin may accept, while Chuck Hagel believes Morgoth is overwhelmingly likely to betray them."
  ],
  "continuity_sources": [
    1155
  ],
  "open_questions": [
    "How will humanity respond to Morgoth’s surrender offer and demand for tribute?",
    "Can Jin Taekyung stop Morgoth and the invading army?",
    "What did the System notification shown to Jin Taekyung say?",
    "What thought occurred to the Skeleton King at the chapter’s end?"
  ],
  "safe_through": 1155,
  "temporary_decisions": [
    "Render 은빛 산 as “Silver Mountains” and 마계의 대공 as “Archduke of the Demon Realm.”",
    "Render 모르고스’s command ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ as “Answer the call.”",
    "Render 건법 as “gun-fu” for the chapter’s joke."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 천태민    | **Cheon Taemin**  |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 대주     | **Squad Leader** / **Commander**             |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 도사      | **Daoist**                                                      |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도우미 | **The Helper** | Taekyung’s name for the mysterious being who first taught him to circulate qi. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 마법진 | **Magic Formation** | The formation that transports Ma Sanbao and his followers. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |
| 송송이 | 최민우 | guild_member_to_guild_master | Team Leader Choi | formal-polite | Song Song addresses Choi by his former title while urging him to rest. |
| 임꺽정 | 최민우 | guild_member_to_guild_master | Team Leader Choi | casual-but-concerned | Im Kkeokjeong uses Choi's former title while warning him about overwork. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1154
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1149
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 773
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1155
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1155
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1153
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; Taekyung now suspects The Helper was the Martial God and that the Martial God was Cheon Taemin, though both identities remain unconfirmed.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 773
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 1148
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, whom he regards as a model of taking responsibility in a crisis; he is the maternal grandson of Cheon Taemin.

### The Helper.md

# The Helper (도우미)

- **Safe through:** Chapter 1144
- **Aliases:** None
- **Role:** A mysterious being who inhabits an enduring gray-white space and first taught Jin Taekyung to circulate qi.
- **Personality:** He chose to remain in his solitary prison and places his trust in Taekyung.
- **Voice:** Calm and instructive, he uses reflective questions and concise guidance.
- **Relationships:** He guided Taekyung from the beginning of his time in Murim and gave him the pocket watch of unknown make as his final gift.

## Korean source

```text
＃1156화



스켈레톤 킹이 척 헤이글과의 대화에서 무언가를 떠올린 그때, 그들의 대화 속 주인공은 최고의 보안을 갖춘 펜타곤(Pentagon)에서도 가장 깊고 비밀스러운 공간에 홀로 서 있었다.

아니, 어쩌면 홀로 서 있다는 표현에는 약간의 어폐가 있을지도 몰랐다.

엄밀히 말한다면, 그는 ‘혼자’가 아니었으므로.

“자주 찾아뵀어야 했는데, 사정이 있어서 좀 늦었습니다.”

문득 입을 연 진태경은 주위를 천천히 둘러보았다. 수백 개의 조명을 켜 놓은 듯이 환하고, 공허하게 느껴질 만큼 드넓은 백색 공간을.

“얼마 전에 이사하셨다는 얘기는 들었습니다. 이런 곳일 줄은 몰랐지만요.”

그래. 정말 몰랐다. 그래서 이곳에 처음 발을 디딘 순간 놀랄 수밖에 없었다.

그만큼 닮아 있었으니까.

그가 인벤토리(Inventory)라고 부르는, 얼마 전 생각지도 못한 만남이 있었던 그 미지의 공간과.

“단순한 우연의 일치겠죠. 아마도.”

틀림없이 그럴 것이다. 오직 한 사람을 위해 심혈을 기울여 이 비밀 공간을 설계한 거구의 대마도사는, 인벤토리의 형태는커녕 그 존재조차 모르고 있을 테니.

하지만…….

“솔직히 이제는 아무것도 모르겠습니다. 제가 정확히 어떤 것을 알고 있는지, 무엇이 진실이고 거짓인지조차도요.”

어느 날인가부터 모든 상식이 파괴되기 시작했다. 불가해(不可解)와 맞닿은 현실 앞에서 이성은 흐려졌고, 그 빈자리를 직감이 채웠다.

진태경 그 자신조차도 쉽게 이해할 수 없는, 어설픈 공상에 가까운 직감이.

그리고 이 모든 것의 시작이자 끝이라 할 수 있는 존재가 지금 이 순간 그의 망막에 비치고 있었다.

“듣고 있습니까. 보고 있습니까.”

진태경은 고개를 숙여 내려다보았다.

온갖 마법진과 기계 장치로 연결된 타원형의 회복 캡슐을.

살아 있는 자를 위해 마련된 관(棺)과 같은 그곳에서, 누구도 깨울 수 없는 깊은 잠에 빠진 한 노인을.

“그렇다면, 대답해 주십시오.”

물론 진태경은 알고 있었다. 아무리 오랫동안 묻고 또 기다려도 돌아오는 대답은 없으리라는 것을.

하지만 그럼에도, 물어봐야만 했다.

“당신이, 제가 짐작하는 그 사람이 맞습니까?”

인류가 낳은 가장 위대한 영웅.

본명은 천태민, 이명은 슬레이어(Slayer) 혹은 스카이(Sky).

그리고.

“무신(武神).”

진태경은 참았던 숨을 토해 냈다.

뜨거운 숨결에 닿아 수증기가 낀 반투명한 막 너머로, 평온하게 잠든 천태민의 얼굴을 응시했다.

“나는 느낄 수 있었습니다. 그때 그곳에서 만난 사람은…… 당신이었습니다. 분명히.”

칙. 치지직!

어느덧 한층 높아진 목소리가 공간을 울리고, 자연스럽게 힘이 들어간 손이 캡슐을 둘러싼 무수한 방어 마법과 충돌한다. 그러나 피부로 전해지는 통증에도 진태경은 개의치 않았다.

그는 얼마 전에야 떠올린 반쪽짜리 확신에 대한 답을 들어야 했다.

눈앞의 천태민과 도우미 노인이 같은 사람이라는 것을 확인해야 했고, 그 역시 자신과 같은 플레이어(Player)였다는 사실을 알아야 했으며 어찌하여 지금의 상황에 이르렀는지.

그리고 무엇보다.

“왜, 왜 깨어나지 않는 겁니까.”

아무리 억누르고 또 억눌러도, 계속해서 들끓어 오르는 가슴 속 분노를 토해 낼 곳이 필요했다.

“……도대체 어째서.”

당신에 비하면 턱없이 부족한 내가, 이런 무거운 짐을 감당해야 하는 겁니까.

그 순간.

치익.

차마 끝까지 내뱉지 못한 목소리와 함께, 진태경은 캡슐에서 손을 뗐다.

그리고 돌아서며 불쑥 입을 열었다.

“뭐야, 면회 인원은 한 번에 한 명만 되는 거 아니었어요?”

앞서 말을 멈춘 것은, 비단 통제할 수 없을 정도로 출렁이던 감정 때문만이 아니다.

조금 전 도착한 두 번째 면회객이 대답했다.

“글쎄요, 제가 알기론 그런 규정은 없습니다. 설령 있다 하더라도 가족은 예외로 둬야죠.”

“와, 그렇게 말씀하시니까 뭐라 할 말이 없네.”

“참고로 말씀드리자면, 전 지금 막 왔습니다.”

“도둑이 제 발 저린다더니, 누가 뭐래요?”

앞서 보인 모습이 무색할 만큼, 평소와 다를 것 없이 장난기가 묻어 나오는 표정과 어조.

그런 진태경을 물끄러미 바라보던 최 팀장, 최민우가 이내 어깨를 으쓱하며 말을 받았다.

“노크라도 할 걸 그랬군요. 어차피 결계 마법이라 아무런 소리도 안 나겠지만.”

“뭐 그럴 것까지야.”

“갑자기 외조부님 생각이 나서 미스터 존슨을 찾았더니, 이미 진태경 씨와 함께 가셨다는 얘길 들었습니다. 실례가 됐다면 미안합니다.”

“실례는 무슨, 이 경우는 오히려 내가 방해한 거지.”

웃으며 손을 내저은 진태경이 걸음을 뗀 그때였다.

“혹시, 어떤 이유로 외조부님을 찾아뵈러 온 건지 물어봐도 되겠습니까?”

잠시 침묵하던 진태경이 피식 웃었다.

“왜요, 우려할 만한 상황이라도 일어날까 봐?”

지금 같은 상황에서 우려할 만한 상황이라면 한 가지뿐이다.

바로 진태경이 천태민과 함께 단둘이 드래곤 레어로 향하는 것.

물론 천태민은 이미 오래전부터 의식불명 상태였고, 그런 상황은 펜타곤의 그 누구도 원하지 않으니 이와 같은 일이 벌어진다면 그것은 사실상 진태경의 독단에 의한 것일 터였다.

하지만 농담처럼 던진 진태경의 물음과 달리, 곧이어 돌아온 최민우의 목소리는 낮게 가라앉아 있었다.

“네.”

“……!”

“솔직히 말씀드리자면, 매우 우려되는군요.”

눈을 크게 뜬 진태경이 뭐라 대꾸하기도 전에, 최민우가 담담하게 덧붙였다.

“당신이, 진태경 씨가 홀로 모르고스와 맞서 싸우려는 멍청한 선택을 할까 봐 우려됩니다.”

“…….”

“대답해 주십시오. 부정하고 싶으면 그래도 됩니다.”

최민우를 말없이 응시하던 진태경이 입을 열었다.

“좋아요. 이 기회에 확실하게 말하자면, 절대 그럴 일 없어요.”

“그렇군요.”

“예. 그럼 이걸로 된 거죠?”

“아뇨.”

“아니, 왜?”

“그 말을 전혀 믿지 못하겠으니까요.”

“……!”

“진태경 씨를 잘 아는 사람이라면 누구나 그럴 겁니다. 곁에서 지켜보면 자연스럽게 깨닫게 되거든요. 당신이 얼마나 무모하고 바보 같은 선택을 하는지.”

가까이 다가온 최민우가 회복 캡슐 안에 잠들어 있는 외조부를 바라보며 말을 이었다.

“제 외할아버지도 그런 분이셨겠죠. 그만큼 두 분은 서로를 닮았으니까.”

“닮았다고요?”

“예. 그 덕분에 조금은 개인적인 위안을 얻기도 했습니다. 그것도 아주 최근에요.”

“그게 무슨…….”

“진태경 씨는 중동에서 돌아오신 이후에도 가족분들을 찾지 않으시더군요. 바로 이곳 펜타곤에 머무르고 계시는데도 말입니다.”

가족.

그 짧은 한 단어에 진태경의 눈동자가 파르르 떨렸다.

맞다. 어머니와 여동생. 그에게 있어 세상 그 무엇보다 소중한, 피로 이어진 가족들은 이미 한참 전부터 펜타곤에서 보호받고 있다.

하지만 단 한 번도 찾지 않았다.

아니, 만나서는 안 되었다.

만약 그들을 만난다면, 자신을 가까스로 지탱하고 있는 보이지 않는 기둥이 무너져 버릴 테니까.

이대로 허물어져 버린다면, 정말 한 줌의 용기조차 쥐어 짜내지 못할 테니까.

“다른 길드원들과의 만남을 거부하시는 것도, 분명 그런 이유일 테고요.”

그간 수많은 헌터와 인연을 맺어 왔지만, 진태경과 최민우에게 있어 길드원이라 부를 수 있는 사람은 이제 둘뿐이다.

송송이와 임꺽정.

그리고 진태경은 그들과의 만남도 회피했다.

그가 걸어가야 하는 길은 무수한 위험이 도사린 사지(死地).

죽음은 모두에게 공평하나, 죽음이 찾아오는 속도는 그렇지 않다.

그렇다면 S급 헌터도, 초절정 고수도 아닌 그들이 곧 벌어질 대전투에 참여한다면 어떻게 될까.

‘죽겠지. 분명히.’

이건 비단 진태경 자신만이 아닌, 수십억 인류의 목숨이 판돈으로 걸린 거대한 도박판이다.

삼성(三星)도, 화왕(火王)도 없는 이 세상에서 오직 홀로 짊어져야 하는 그 막중한 무게를 그는 감당할 수 없었다.

그래서 도망쳤다.

가족들에게서, 친구들에게서.

주위의 모두에게서 도망쳐 이곳으로 왔다.

이런 자신을 이해할 수 있는 유일한 사람. 모든 것의 해답이자 열쇠가 될 수 있는 천태민을 이렇게라도 다시 한번 마주하고 싶어서.

그리고 다음 순간 귓가로 흘러들어오는 최민우의 음성에, 진태경은 불현듯 깨달았다.

“그런 진태경 씨의 모습을 보고 있자니, 그제야 문득 알 것 같았습니다. 하나뿐인 손주를 찾지 않았던 외할아버지의 마음을.”

지금까지 미처 알아차리지 못했던 한 가지 사실을.

“어떻게든 이유를 찾고 싶은 저만의 바램일지도 모릅니다만…… 이제는 그렇게 생각하려고 합니다. 그분만이 느끼고 계셨을 어떠한 위험 때문에 애써 저를 멀리하실 수밖에 없었다고요.”

저 쓴웃음 섞인 목소리에 담긴, 최민우조차도 알아차리지 못한 진짜 의미를.

‘오직 그만이 느끼고 있었을 위험, 이라고?’

그럴 리 없다. 당시의 인류에게 더 이상의 위험은 존재하지 않았으니까.

그토록 강대하던 마왕 아스모데우스는 육신조차 남기지 못한 채 가루가 되어 소멸했고, 오대양 육대주를 피로 물들이던 몬스터 군단 역시 한낱 사냥감으로 전락한 상황.

하지만 어째서인지 이 위대한 업적을 이루어 낸 영웅은, 평화가 찾아옴과 동시에 스스로를 세상과 격리시켰다.

그는 모두를 멀리했다.

그 누구도 예외는 없었다.

의형제나 다름없던 최측근들도, 세상 그 무엇보다 소중하게 여겼다는 딸도.

심지어 그 딸이 불의의 사고로 인해 남편과 함께 세상을 떠났을 때도, 어린 외손자를 가까이에서 돌보는 대신 김 집사에게 맡겼다.

그리고 어느 날, 아무런 예고도 없이 의식을 잃었다.

그것도 무려 십수 년 동안이나.

‘……당신도 그만큼 두려웠던 겁니까.’

혀끝에서 삼켜 낸 한마디와 함께, 진태경은 깊게 가라앉은 눈빛으로 천태민을 바라보았다.

자신이 옳았다.

여전히 확실한 증거도, 증언도 없었지만 방금 최민우가 한 말을 통해 다시금 깨닫게 되었다.

천태민과 무신은 처음부터 동일 인물이었다는 것을.

죽은 듯이 잠들어 있는 저 늙은 영웅의 그림자는, 두 세계에 걸쳐 드리워져 있다는 사실을.

‘그는 알고 있었던 거야. 아직 모든 게 끝나지 않았다는 걸. 아스모데우스가 완전히 소멸한 게 아니라는 걸.’

아직 밝혀 내지 못한 사실도, 묻고 싶은 말도 너무나도 많다.

하지만 이것만으로도 충분하다.

적어도 지금 당장, 그가 어떤 선택을 내려야 할지는 명확해졌으니까.

저벅.

망설임 없이 돌아선 진태경은 걷기 시작했다.

그리고 채 몇 걸음을 옮기기도 전에, 아주 미세하지만 중요한 한 가지 변화를 알아차리고 걸음을 멈췄다.

문.

문이 없다.

정확히는, 흔적도 없이 사라져 버렸다.

고도의 마법으로 생성된 이 비밀 공간을 드나들 수 있는 유일한 출구가.

“팀장님.”

나직한 부름과 함께 고개를 돌리자, 흔들림 없는 표정을 한 최민우의 모습이 시야에 들어왔다.

“죄송합니다.”

짧지만 담담한 사과에, 진태경은 모든 상황을 이해할 수 있었다.

“처음부터 이럴 생각이었습니까?”

“앞서 말씀드렸다시피, 우리는 진태경 씨가 어떤 사람인지 아주 잘 알고 있으니까요.”

“우리?”

“당연하게도, 이건 저만의 독단적인 판단이 아닙니다. 이미 저와 미스터 존슨을 포함한 대다수가 이 계획에 동의했습니다.”

“대다수라면 분명히 이런 말도 안 되는 계획에 반대하는 사람도 있었을 텐데.”

“아뇨, 없습니다. 혹시 모를 변수를 대비하여 문제의 소지가 될 사람들에게는 아예 처음부터 알리지 않았거든요. 그 외에도 할 수 있는 모든 준비를 완벽히 처리해 놨습니다.”

지금쯤 아무것도 모르고 있을 척 헤이글과 스켈레톤 킹을 떠올리며, 최민우는 침착한 어조로 말을 이었다.

“그러니…… 남은 시간 동안 진태경 씨는 저와 함께 이곳에 머무르시면 됩니다.”

수많은 이들이 동참한 이 계획의 목표는 단 하나뿐이었다.

모르고스가 전 세계에 선언한 사흘의 기간이 끝날 때까지 할 수 있는 모든 수단과 방법을 동원해서라도 진태경을, 그들의 유일한 희망을 붙잡아 둘 것.

다행히도 때마침 진태경이 찾은 이 비밀 공간은 계획을 실행하기에 안성맞춤인 장소였다.

천태민의 안전을 위해 무수한 결계 마법이 설치되어 있었으니까.

하지만 그럼에도 유일한 변수가 남아 있다면, 그건 바로 진태경이라는 인간 그 자체에 있었다.

새로운 시대의 구원자.

그 누구도 대신할 수 없었던 천태민의 뒤를 이은, 세계 최고이자 최강의 헌터.

그런 그였기에 결코 덧없이 희생시킬 수 없었고, 최민우는 이를 위한 마지막 조치까지 잊지 않았다.

“진태경 씨가 아무리 강하다고 해도, 이곳을 빠져나갈 수는 없을 겁니다.”

“글쎄요.”

진태경이 담담한 대꾸와 함께 허공으로 손을 뻗자, 지금껏 보이지 않던 은빛 창 한 자루가 그의 손아귀에 잡혔다.

화아악.

검푸른 불길이 백염(白炎)의 창날을 타고 솟구쳤다.

최민우가 마지막으로 보았을 때와는 비교도 되지 않는 열기를 머금은, 극도로 정제된 화염이.

그러나 최민우는 조금도 동요하지 않았다.

“지금 생각해 보니, 한 가지 말씀드리지 않은 게 있군요.”

그가 이 계획을 위해 준비한 마지막 조치는, 애당초 진태경의 무력에 대비한 것이 아니었으니까.

“만약 이 공간에 설치된 결계 마법들을 강제로 부수려 한다면, 그 여파로 펜타곤 전체가 무너질 수도 있습니다.”

적어도.

뒤이어 들려온 진태경의 대답을 듣기 전까지는 그랬다.

“정말 그렇게 생각해요?”

그그그극.

끔찍한 열기를 따라 일그러지는 공간 속, 진태경의 나직한 음성이 메아리처럼 울려 퍼졌다.

“내 생각은, 조금 다른데.”

“……!”

최민우의 눈이 부릅떠진 그 순간.

서걱.

오직 한 사람만이 볼 수 있는 결(結)을 따라, 수백 개의 마법을 잇고 유지하던 거대한 마나의 파도가 갈라졌다.
```

## Final English reading copy

```markdown
# Chapter 1156

At the very moment the Skeleton King thought of something during his conversation with Chuck Hagel, the subject of their conversation stood alone in the deepest, most secret part of the Pentagon, a place with the highest security.

Or perhaps “stood alone” wasn’t quite right.

Strictly speaking, he wasn’t “alone.”

“I should have come to see you more often, but things came up, and I’m late.”

Jin Taekyung spoke out of the blue and slowly looked around at the vast white space, bright as though hundreds of lights had been switched on, and so empty it felt almost hollow.

“I heard you moved not long ago. I just didn’t expect it to be somewhere like this.”

That was right. He really hadn’t expected it. So when he first set foot inside, he couldn’t help being surprised.

It was that similar.

Similar to that unknown space he called the Inventory, where he’d had an unexpected encounter not long ago.

“Just a coincidence, I’m sure. Probably.”

It had to be. The massive Grand Mage who had painstakingly designed this secret space for a single person wouldn’t even know the Inventory existed, let alone what it looked like.

But…

“Honestly, I don’t know anything anymore. Not even exactly what I know, or what’s true and what’s false.”

At some point, everything he’d taken for granted had begun to fall apart. Faced with a reality brushing against the incomprehensible, reason had grown hazy, and instinct had filled the void.

An awkward instinct, closer to a delusion—one even Jin Taekyung himself could hardly understand.

And the being who could be called the beginning and end of all this was reflected in his eyes at that very moment.

“Are you listening? Can you see me?”

Jin Taekyung lowered his head and looked down.

At the oval recovery capsule, linked to countless Magic Formations and machines.

Within that place, a coffin prepared for the living, lay an old man sunk in a deep sleep no one could wake him from.

“If so, please answer me.”

Of course, Jin Taekyung knew. No matter how long he asked and waited, no answer would come.

Even so, he had to ask.

“Are you the person I think you are?”

The greatest hero humanity had ever produced.

His real name was Cheon Taemin. His titles were Slayer and Sky.

And…

“The Martial God.”

Jin Taekyung let out the breath he’d been holding.

Through the translucent membrane fogged by his warm breath, he stared at Cheon Taemin’s peaceful sleeping face.

“I could feel it. The person I met there, back then… was you. I’m sure of it.”

Crackle!

His voice had grown louder without him noticing, echoing through the space. His hand, tensing on its own, struck the countless protective spells surrounding the capsule. But Jin Taekyung paid no mind to the pain in his skin.

He needed an answer to the half-formed conviction he’d reached only recently.

He needed to confirm that Cheon Taemin and the old man called The Helper were the same person, to learn that he too had been a Player like himself, and to find out how things had come to this.

And more than anything…

“Why—why won’t you wake up?”

No matter how hard he tried to suppress it, he needed somewhere to release the anger that kept churning in his chest.

“……Why?”

Why did someone like me, so far beneath you, have to bear such a heavy burden?

At that moment—

Hiss.

Along with the words he couldn’t bring himself to finish, Jin Taekyung took his hand off the capsule.

Then he turned and blurted out, “What, wasn’t it one visitor at a time?”

The reason he’d stopped speaking earlier wasn’t just that his emotions had been threatening to overwhelm him.

The second visitor, who had just arrived, answered him.

“Well, as far as I know, there’s no such rule. And even if there were, family should be an exception.”

“Wow. When you put it like that, I’ve got nothing to say.”

“For the record, I just got here.”

“They say a guilty conscience needs no accuser. Who said anything?”

His expression and tone were as playful as ever, so different from the person he’d been moments earlier.

Team Leader Choi, Choi Minwoo, watched Jin Taekyung for a moment, then shrugged.

“I should’ve knocked. Not that you would’ve heard me, with the barrier magic.”

“It’s not like you had to go that far.”

“I suddenly thought of my grandfather and went looking for Mr. Johnson. I heard you’d already come here with him. Sorry if I intruded.”

“Don’t be. If anything, I’m the one who interrupted you.”

Jin Taekyung smiled and waved a hand as he started walking.

“May I ask why you came to see my grandfather?”

Jin Taekyung paused for a moment, then gave a short laugh.

“What, worried something might happen?”

There was only one thing to worry about in a situation like this.

Jin Taekyung going to the Dragon Lair alone with Cheon Taemin.

Of course, Cheon Taemin had been unconscious for a long time, and nobody in the Pentagon wanted that to happen. If it did, it would effectively be Jin Taekyung acting on his own.

But unlike the joking question Jin Taekyung had tossed out, Choi Minwoo’s reply came in a low, steady voice.

“Yes.”

“……!”

“To be honest, I’m very worried.”

Before Jin Taekyung could answer, eyes widening, Choi Minwoo added calmly, “I’m worried that you, Mr. Jin Taekyung, might make the stupid choice of fighting Morgoth alone.”

“……”

“Please answer me. You can deny it if you want.”

Jin Taekyung stared at Choi Minwoo in silence, then spoke.

“Fine. Let me make this perfectly clear. I would never do that.”

“I see.”

“Yeah. So, that settles it, right?”

“No.”

“What? Why not?”

“Because I don’t believe you at all.”

“……!”

“Anyone who knows you well would feel the same. Spend enough time around you, and it becomes obvious how recklessly and foolishly you choose to act.”

Choi Minwoo stepped closer and looked at his grandfather sleeping inside the recovery capsule.

“My maternal grandfather must have been the same. The two of you are so alike.”

“Alike?”

“Yes. That’s given me a little personal comfort. Very recently, too.”

“What do you mean…?”

“Even after you came back from the Middle East, you haven’t gone to see your family. Even though you’re staying right here in the Pentagon.”

Family.

At that short word, Jin Taekyung’s eyes trembled.

That was right. His mother and younger sister—his family by blood, more precious to him than anything in the world—had been under the Pentagon’s protection for quite some time.

But he hadn’t gone to see them once.

No, he couldn’t see them.

If he did, the invisible pillar barely holding him up would collapse.

And if he crumbled now, he wouldn’t be able to summon even the smallest shred of courage.

“You’ve also refused to meet with the other Guild members. I’m sure it’s for the same reason.”

Over the years, he’d made connections with countless Hunters, but only two people could still be called Guild members by Jin Taekyung and Choi Minwoo.

Song Song and Im Kkeokjeong.

And Jin Taekyung had avoided them, too.

The path he had to walk was a deadly one, riddled with countless dangers.

Death came for everyone, but it didn’t come at the same speed.

So what would happen if they joined the coming great battle—not S-rank Hunters, not even Supreme Peak masters?

*They’d die. Without a doubt.*

This was a massive gamble with the lives of billions of people at stake, not just Jin Taekyung’s. In a world without the Three Saints or the Fire King, he couldn’t bear that immense weight alone.

So he ran.

From his family. From his friends.

He’d fled from everyone around him and come here.

He wanted, if only for a moment, to face Cheon Taemin again—the only person who could understand him, the answer and key to everything.

And at the next words that drifted into his ears, Jin Taekyung suddenly understood.

“Watching you, Mr. Jin Taekyung, finally made me understand how my grandfather felt when he never came to see his only grandson.”

Something he hadn’t noticed until now.

“Maybe I’m just looking for a reason to believe that. But… I’m going to think of it that way now. That he had no choice but to keep me at a distance because of some danger only he could sense.”

The real meaning in that voice, touched with a bitter laugh—a meaning even Choi Minwoo himself hadn’t realized.

*Some danger only he could sense?*

That couldn’t be. There had been no danger left for humanity at the time.

The Demon King Asmodeus, once so powerful, had been reduced to dust and vanished without even leaving a body. The monster legions that had stained the Five Oceans and Six Continents with blood had become nothing more than prey.

And yet, as soon as peace arrived, the hero who had achieved that great feat had isolated himself from the world.

He’d kept everyone at a distance.

No one was an exception.

Not even his closest companions, practically sworn brothers, or the daughter he’d cherished above all else.

Even when that daughter died in an accident along with her husband, he’d left his young grandson in Butler Kim’s care instead of raising him himself.

Then, one day, without warning, he lost consciousness.

For more than a decade.

*……Were you that afraid, too?*

With those words swallowed on the tip of his tongue, Jin Taekyung gazed at Cheon Taemin, his eyes sinking into darkness.

He’d been right.

He still had no definite proof or testimony, but what Choi Minwoo had just said made him realize it once again.

Cheon Taemin and the Martial God had been the same person from the very beginning.

The shadow of that old hero, sleeping as if dead, stretched across two worlds.

*He knew. He knew it wasn’t over yet. That Asmodeus hadn’t been completely erased.*

There was still so much he hadn’t uncovered, so much he wanted to ask.

But this was enough.

At least now, it was clear what choice he had to make.

Step.

Jin Taekyung turned without hesitation and started walking.

He’d taken only a few steps when he noticed one tiny but important change and stopped.

The door.

There was no door.

More precisely, the only exit from this secret space, created with advanced magic, had vanished without a trace.

“Team Leader.”

At his quiet call, he turned his head. Choi Minwoo stood there, his expression unwavering.

“I’m sorry.”

The brief, calm apology was enough for Jin Taekyung to understand the whole situation.

“Was this your plan from the beginning?”

“As I said earlier, we know exactly what kind of person you are, Mr. Jin Taekyung.”

“We?”

“Of course, this wasn’t a decision I made on my own. Most of them, including Mr. Johnson and me, have already agreed to the plan.”

“Most of them? That means someone must’ve opposed this ridiculous plan.”

“No. No one did. We didn’t tell the people who might have caused trouble from the start, in case they became an unexpected variable. We’ve also made every other preparation we can.”

Thinking of Chuck Hagel and the Skeleton King, who by now knew nothing about this, Choi Minwoo continued in a composed tone.

“So… for the time we have left, you’ll stay here with me, Mr. Jin Taekyung.”

The plan, involving so many people, had only one goal.

Use every means at their disposal to keep Jin Taekyung—their only hope—here until the three days Morgoth had given the world were up.

Fortunately, the secret space Jin Taekyung had found was perfectly suited to carry out the plan.

Countless barrier spells had been installed to keep Cheon Taemin safe.

Even so, there was one variable left: Jin Taekyung himself.

The savior of the new age.

The world’s greatest and strongest Hunter, successor to Cheon Taemin, whom no one else could replace.

That was exactly why they couldn’t let him throw his life away, and Choi Minwoo hadn’t forgotten to take one final measure to stop him.

“No matter how strong you are, Mr. Jin Taekyung, you won’t be able to get out of here.”

“Is that so?”

As Jin Taekyung calmly reached into the air, a silver spear that hadn’t been visible until then appeared in his grasp.

Whoosh.

Dark blue flames surged along the White Flame spearhead.

A refined fire, carrying heat beyond comparison with the last time Choi Minwoo had seen it.

But Choi Minwoo didn’t waver in the slightest.

“Now that I think about it, there’s one thing I didn’t mention.”

The final measure he’d prepared for this plan hadn’t been meant to counter Jin Taekyung’s strength in the first place.

“If you try to forcibly break the barrier spells installed in this space, the resulting damage could bring down the entire Pentagon.”

At least, that was what he thought—

Until he heard Jin Taekyung’s answer.

“You really think so?”

Grgrgrk.

As the space warped beneath the unbearable heat, Jin Taekyung’s quiet voice echoed through it like a distant refrain.

“I think differently.”

“……!”

At the instant Choi Minwoo’s eyes widened—

Slice.

Along a seam only one person could see, the massive wave of mana binding and sustaining hundreds of spells split in two.
```
