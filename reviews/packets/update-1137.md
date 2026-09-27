<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1137.txt",
      "sha256": "c56133eb96cd9f13d3278225b80c2a2102a1ecf791db78bb63cb9b992da3c131",
      "bytes": 12303
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f6f4c10c1011a9e414a20f163a6b581ca0b0d609932c6af7919b106f9c2ce96f",
      "bytes": 638
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a77573feec836df54e35248f8b975bf7696cac58abec08a1c5a945ccb8c3d729",
      "bytes": 245575
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "96bc51f4fee09306b57411fe2e2692f9724a85cfd76fc5f1c4e3a394036e3c46",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "1563f95b2140ea041ec825cc7a399cd05f677520e124dc6126894c446113df7a",
      "bytes": 554
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "33df747413772c6c9cceb8f34a817fda6d9e0684924e9641a6efb88f740998fa",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3565c5af412481991dd6b243781c4fb0bedd9a5818c7e978f3f61bc0691154a2",
      "bytes": 623
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "59677d7750136ce4930c607147780ec104ea7bd1dd18befa3a2909c72d5e6d4a",
      "bytes": 847
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "273352dce0dc2c629b4bf5b4995278e9d4ee00ee65b28c3eade8c2a052258315",
      "bytes": 1084
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "e28123f99bba8f760415ac7762c5a9711679b91798bd6cc6c8858eaa8bab103b",
      "bytes": 684
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "78ff98de9e0fee6b3128325758bb5177a0deacd375f44e917bd83fd62f04a560",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5895951d60d69a56331fdfdc592502035283d3a48acfa6cb07fdeb7d2eb418c2",
      "bytes": 291096
    }
  ],
  "estimated_tokens": 10991
}
-->

# Durable State Update — Chapter 1137

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
1 and safe_through 1137. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1137. Profile updates may replace only one
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
  "chapter": 1137,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1137,
    "continuity_sources": [1137],
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
    "The Son of Heaven has declared Great Ming and ordered a personal expedition to Xinjiang, vowing not to return to the palace until the traitors are rooted out.",
    "Zhuge Feng says forces have gathered at every Moving Formation found; the Azure Sky Sword King leads the forces in Shanxi."
  ],
  "continuity_sources": [
    1136
  ],
  "open_questions": [
    "How will the campaign against the Lord of Heaven and the forces in Xinjiang unfold?"
  ],
  "safe_through": 1136,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 화산파    | **Huashan**                      |
| 무림맹    | **Murim Alliance**               |
| 제갈세가   | **Zhuge Clan**                   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 형장      | **Brother** / **Brother [Name]**                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 마봉진 | **Demon-Sealing Formation** | Zhuge Feng's formation for sealing the Gate's mana. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 천자 | 마삼보 | Emperor addressing his former servant and traitor | traitor | familiar and imperious | The Son of Heaven asks whether Ma Sanbao enjoyed his rebellion. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1136
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1134
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1136
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1136
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1135
- **Aliases:** None
- **Role:** Ma Sanbao was a sorcerer and Supreme Peak martial artist who used the White Illusion Jiangshi Art; the Son of Heaven killed him.
- **Personality:** He is ambitious and confident in his usefulness to the Lord of Heaven, dismissive of his former master’s weakness, and pragmatic about losing subordinates.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao served the Eastern Heaven Demon Lord as his disciple and now serves the Lord of Heaven; he was once an imperial servant before rebelling against the Son of Heaven.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1134
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1136
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor of Great Ming and Zhu Bao’s elder brother; he has ordered a personal expedition to Xinjiang and will not return to the palace until the traitors are rooted out.
- **Personality:** Coldly strategic and imperious, he is willing to break taboos to remain with his younger brother.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1128
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1137화



수많은 이들이 중원(中原)을 가리켜 천하의 중심이라 말하지만, 그 안에 담긴 정확한 뜻은 따로 있다.

진정한 천하의 중심지는 바로 황도(皇都)다.

만백성의 어버이이며 무소불위의 권위를 지닌 천자가 바로 그곳에 있기에.

그리고 이와 같은 의미에서, 무림의 첫 태동과 역사를 함께 했던 하남(河南)은 더는 무림맹의 총단이라 부를 수 없었다.

중요한 것은 장소가 아닌 사람이니까.

특정한 장소에 담긴 상징성이란, 바로 사람에 의해 만들어지는 것이니까.

검성(劍聖) 매종학은 매일같이 천하 곳곳에서 날아드는 서신들을 통해 그러한 사실을 여실히 느끼고 있었다.

곳곳에 쌓인 서류 더미가 높아질수록, 누군가의 방문을 간절히 기다리게 된다는 것 역시도.

“들어오시오.”

굳게 닫힌 문밖, 잠시 멈칫하던 희미한 인기척의 주인이 이내 집무실 안으로 들어섰다.

“잠시 실례하…….”

문득 말꼬리를 흐린 손님이, 매종학의 퀭한 눈가와 사방을 뒤덮은 서류 더미를 번갈아 바라보며 말을 이었다.

“음. 바쁘신 모양이군.”

“괜찮으니 차 한잔하고 가시오.”

“아니오. 다음에 오겠, 헉.”

쉭, 덥석!

그야말로 섬광 같은 속도.

화산파의 절기인 암향표(暗香飄)를 펼쳐 단숨에 공간을 가로지른 매종학이 손님의 소매를 붙잡았다.

그리고 간절한 열망이 담긴 눈빛과 목소리로 입을 열었다.

“차 한잔하고 가시오.”

“…….”

“제발.”

소매로 안 되면 멱살이라도 잡을 기세.

번뜩이는 매종학의 눈동자에서 심상찮은 광기를 느낀 손님이 마른침을 삼켰다.

“알겠소. 알겠으니 이것 좀 풀고 얘기합시다.”

“만약 거짓말이면 죽어서도 원망할 거요.”

“아니 뭐 그렇게까지…… 그리고 원망해 봤자 무슨 소용이요? 어차피 죽었는데.”

“그것도 그렇구려. 그럼 차는 무엇으로?”

“용정(龍井)으로 주시오.”

“사실 종류가 하나밖에 없소. 그냥 그거 드시오.”

혹여 마음이 바뀔세라 후다닥 소매를 놓은 매종학이 찻주전자를 준비하는 모습을 지켜보며, 손님은 내심 생각했다.

‘이럴 거면 도대체 왜 물어본 거지……?’

물론 그도 이미 알고 있었다. 어떤 종류의 사람은, 이해하려고 하면 할수록 본인 손해라는 것을.

그건 지난 몇 달간 어느 미친놈과 함께하며 깨달은 이치이기도 했다.

“……제대로 판박이군. 분명 친손주는 아니라고 했던 거 같은데.”

“응? 지금 뭐라 하셨소?”

“아니오. 그냥 혼잣말이었소.”

“이해하오. 늙을수록 혼잣말이 많아지는 법이지.”

아직 새파랗게 젊어 보이는 청년과 그보다도 몇 살은 어려 보이는 소년이 나누는 대화라고는 믿기 어려웠지만, 겉으로 드러난 것이 전부는 아닌 법.

살성(殺星)은 그 사실을 누구보다 잘 알고 있는 사람 중 하나였다.

“맹주께서도 그러신다니, 사람 사는 게 비슷하구려.”

“음? 비슷하다니?”

“방금 얘기하지 않았소? 나이가 들수록 혼잣말이 많아진다고.”

“아, 그거. 통상 그렇다는 얘기요. 나는 어릴 적부터 혼잣말이 습관이었던 터라 딱히 공감은 안 되오만.”

“……차는 아직 멀었소?”

살성이 급격한 피로를 느끼고 있던 그때, 마침내 김이 모락모락 피어오르는 찻잔을 탁자에 내려놓은 매종학이 입을 열었다.

“드시오. 비록 내 것은 아니지만, 향은 제법 좋을 거요.”

매종학의 말은 사실이었다.

명색이 성주씩이나 되는 이가 즐기던 차라 그런지, 그 향과 품질은 매우 훌륭한 축에 속했다.

비록 숱한 비리를 저지른 그는 형장의 이슬이 되어 사라졌지만, 찻잎은 물론 호화로운 집무실 역시 여전히 이곳에 남아 있었다.

무림맹의 임시 맹주전(盟主殿)으로.

“귀한 시간을 빼앗는 것은 아닌지 모르겠소.”

당장이라도 와르르 무너질 듯한 서류 더미를 힐끗 바라보는 살성의 모습에, 매종학이 뜨거운 찻잔을 기울이며 대답했다.

“시간은 늘 귀한 법이지. 칠주야(七晝夜) 전의 전투에서 패배했다면 이런 호사도 누리지 못했을 거요.”

아지랑이처럼 솟아오르는 연기를 바라보며, 살성이 혼잣말처럼 중얼거렸다.

“칠주야라, 벌써 그리되었나.”

바빴던 것은 매종학만이 아니다.

지난 일주일은, 살성을 포함한 모든 이에게 있어 눈코 뜰 새 없는 하루하루였다.

육체와 정신의 피로를 제대로 풀기도 전에 뒷수습을 시작해야만 했으니까.

그리고 부상자들을 치료하는 것만으로도 바쁜 살성이 아무런 목적 없이 찾아올 사람이 아니라는 사실을, 매종학은 이미 꿰뚫고 있었다.

“다향(茶香)은 충분히 즐기신 것 같은데, 어떻소?”

당연하게도 차의 선호 유무를 묻는 것이 아니다.

빙긋 웃는 매종학의 모습을 말없이 바라보던 살성은 문득 몸 속 깊숙이 잠들어 있던 공력을 깨웠다.

우우웅.

공기를 울리며 뻗어 나가는 파장.

소리를 차단하는 무형(無形)의 막이 두 사람을 완전히 감싼 후에야, 살성은 굳게 닫혀 있던 입술을 뗐다.

“내가 맹주를 찾아온 것은, 일전에 말한 문제 때문이오.”

일순간, 매종학의 눈빛이 깊게 가라앉았다.

“이리 직접 걸음 하신 것을 보니…… 결과가 좋지 않은 모양이구려.”

살성 역시 무거워진 음성으로 대답했다.

“그렇소.”

“결국, 찾지 못한 거요?”

“현재까지의 정황으로는.”

아직 일말의 가능성이 남아 있다는 뜻이었지만, 듣고 있던 매종학은 물론, 그 말을 입에 담은 당사자인 살성조차도 회의적인 눈빛이었다.

전투가 끝난 직후 살아남은 무림인들과 관군, 거기에 더해 수많은 백성까지 뒷수습에 총력을 기울였다.

적과 아군을 합쳐 십만 이상의 사상자를 낸 엄청난 격전이었으나, ‘그것’을 칠주야 동안 찾아내지 못했다면 앞으로의 가능성 역시 희박했다.

“더 이상의 수색은 무의미하겠군.”

“그렇다는 건.”

“전면 중단하겠다는 것은 아니오. 수색은 계속하되, 괜한 인력 소모는 줄이는 것이 맞겠지.”

살성이 조용히 고개를 끄덕였다.

매종학의 말이 맞다.

그가 생각하기에도 별다른 가망이 보이지 않는 일에 매달리는 것보다는, 앞으로의 일에 치중하는 것이 옳은 방향이었다.

그런데도 가슴 한구석을 짓누르는 불안감의 무게는 여전했지만.

“나 역시 우려되지 않는 것은 아니오. 하지만…….”

살성의 얼굴에 드리워진 그림자를 본 매종학이 말을 이었다.

“이미 대세(大勢)가 기울었소. 중원의, 아니, 천하의 창칼이 마침내 하나로 모였지.”

매종학이 나직한 음성과 함께 손을 뻗자 서류 더미 사이로 불쑥 솟구친 수십여 장의 전서가 두 사람의 앞으로 날아들었다.

구주팔황과 사해오호.

광활한 하늘과 땅을 가로질러 마침내 서녕에 닿은 전서에는 각기 다른 직인(職印)이 찍혀 있었으나, 끝자락에 적힌 마지막 문장은 동일했다.

“멸마정천(滅魔正天).”

마귀를 멸하고, 하늘을 바로 세운다.

그것은 옛 무림맹이 세운 기치이자, 작금의 천하를 관통하는 네 글자였다.

심지어는 대명(大明)이라는 이름으로 새롭게 태어난 제국조차도 그랬다.

“그들이 오고 있소. 우리와 같은, 단 하나의 목적을 위해서.”

격전 끝에 대승을 거둔 지 칠주야.

그러나 지난 시간 동안 하루를 촌각처럼 보낸 것은, 비단 서녕에 머무르고 있는 이들만이 아니었다.

서녕에서 핏물이 강을 이루었던 그 날, 하남성과 산서성에는 적들의 시체가 산처럼 쌓였다.

마삼보의 목은 황도로 돌아갔고, 남은 사지는 갈기갈기 찢겨 천하 곳곳으로 흩어졌다.

이미 만반의 준비를 끝마치고 있던 창천검왕(蒼天劍王) 역시 단 하나의 사상자 없이 적들을 쓸어 버렸으며, 남아 있던 십여 개의 이동진 역시 날이 밝기 전 폐쇄되었다.

제갈세가의 진법가들이 펼친 마봉진(魔封陳)이 사라지지 않는 한, 이동진의 위험성은 사실상 제거된 것이나 다름없었다.

과거 호북에서 처음으로 일어난 ‘균열’을 틀어막을 수 있었던 것도 전부 마봉진의 효력 덕분이었으니.

그리고 그로 인해 보장된 안전은, 차갑게 식어 있던 도화선에 불을 붙였다.

황실과 무림맹의 깃발 아래, 본격적인 서진(西晉)이 시작된 것이다.

친히 대군을 이끌고 역도들을 토벌하겠다는 천자의 황명(皇命)에 십만의 정예 금위군이 집결했고, 구파일방과 오대세가를 필두로 한 무림인들은 말할 것도 없었다.

그뿐만이 아니다.

힘없는 백성들마저 불의에 맞서고자 의병(義兵)을 조직하니, 마침내 천하의 뜻이 하나로 모였다.

“신강(新疆). 사막 너머의 그 저주받은 땅에서, 모든 것을 끝낼 수 있소.”

매종학은 낮지만 힘 있는 음성으로 입을 열었다.

“이 수레바퀴를 멈출 수 있는 방법은, 천주(天主)를 쓰러트리는 것뿐이니.”

이 모든 것의 시작이자 끝. 동시에 중심.

천주는 그런 존재다.

단 한 번도 본연의 모습을 드러내지 않았으나, 그 거대한 그림자만으로도 천하를 뒤덮은 절대자.

그러나 천하가 합심하여 천주를 향해 칼끝을 겨눈 이상, 하늘의 뜻은 이미 그들에게 있었다.

아니, 그렇다고 믿었다.

‘……하지만, 어째서일까.’

천자라는 두 글자로부터 전해지는, 알 수 없는 불길함.

살성은 어느덧 차갑게 식어 버린 찻잔을 기울였다.

혹여 자신의 마음 깊은 곳에 자리 잡은 불안감을 들키지 않기 위해서.

그와 더불어, 오늘 매종학을 찾아온 또 다른 이유를 곱씹으며.

‘그때 궁성(弓星)이 보인 언행은, 나로서는 도무지 이해하기 어려운 것이었다.’

정확히는, 그뿐만이 아니라 다른 누구라도 그랬을 것이다.

그렇기에 살성은 더더욱 뇌리에서 떨쳐 내기 어려웠다.

진태경이 절체절명의 위기에 처했음에도 방관에 가까운 태도를 취했던 그녀의 모습을.

그 누구도 모르는 또 다른 의도를 지닌 듯한, 그 알 수 없는 언행들을.

‘뭔가를 숨기고 있다. 분명히.’

그러나 이미 그로부터 칠주야라는 시간이 흘렀음에도, 살성은 의문에 대한 답을 찾지 못하고 있었다.

전투가 끝난 직후 궁성은 쉽게 모습을 보이지 않았고, 당사자인 진태경은 여전히 의식을 되찾지 못하고 있었으니.

‘어찌한다.’

살성은 깊어지는 고민과 함께 남아 있던 찻물을 깨끗이 비웠다.

그리고 무언가를 느낀 듯, 말없이 자신을 응시하는 매종학을 향해 신중히 입술을 뗐다.

아니, 떼려고 했다.

쿵쿵쿵쿵!

다음 순간 육중하면서도 다급한 발걸음과 함께, 엄청난 덩치의 거한이 집무실로 난입하기 전까지는.

콰직!

삽시간에 문을 박살 낸 거한이 외쳤다.

“맹주님! 태산이가 봤다! 이 두 눈으로 똑똑히!”

낯익은 얼굴을 확인한 살성은 한숨과 함께 입을 다물었고, 잠깐의 여유가 끝장났음을 온 피부로 똑똑히 깨달은 매종학은 슬픈 어조로 대꾸했다.

“그렇군. 무엇을 봤나?”

그리고 이어진 태산의 한 마디에, 두 거인의 눈이 크게 뜨였다.

“각주! 각주가 깼다!”

“……!”

“……!”
```

## Final English reading copy

```markdown
# Chapter 1137

Many people call the Central Plains the center of the world, but the phrase has a more precise meaning.

The true center of the world is the Imperial Capital.

Because that is where the Son of Heaven resides—the father of all his people, wielding absolute authority.

And in that same sense, Henan, which had shared in Murim’s earliest beginnings and history, could no longer be called the Murim Alliance’s headquarters.

What mattered was not the place, but the people.

The symbolism attached to a place was created by people.

Sword Saint Mae Jonghak felt that truth keenly every day, through the letters arriving from every corner of the realm.

And the more the piles of papers all around him grew, the more desperately he found himself hoping for a visitor.

“Come in.”

Beyond the firmly shut door, the owner of a faint presence hesitated briefly before entering the study.

“Pardon me for a moment…”

The visitor trailed off, glancing between Mae Jonghak’s sunken eyes and the piles of papers that filled the room.

“Hmm. You seem busy.”

“It’s all right. Have a cup of tea before you go.”

“No. I’ll come back later, urk.”

*Whoosh. Grab!*

Mae Jonghak moved at the speed of a flash.

Using Huashan’s secret technique, Dark Fragrance Drift, he crossed the room in an instant and seized the visitor’s sleeve.

Then he spoke, his eyes and voice filled with desperate longing.

“Have a cup of tea before you go.”

“……”

“Please.”

If the sleeve wasn’t enough, he looked ready to grab the man by the collar.

The visitor sensed a disturbing madness in Mae Jonghak’s glittering eyes and swallowed nervously.

“All right. All right, just let go so we can talk.”

“If you’re lying, I’ll resent you even after I’m dead.”

“What good would resenting me do? You’d be dead.”

“That’s true. Then what kind of tea would you like?”

“Longjing, please.”

“To be honest, it’s the only kind I have. Just drink that.”

Worried the man might change his mind, Mae Jonghak hurriedly let go of his sleeve. As he watched him prepare the teapot, the visitor thought to himself:

*Then why did you even ask…?*

Of course, he already knew. With some people, the more you tried to understand them, the more you only hurt yourself.

It was a lesson he’d learned over the past few months, spent with a certain madman.

“……You’re the spitting image of him. I could’ve sworn I heard he wasn’t your biological grandson.”

“Hm? What did you say?”

“Nothing. Just talking to myself.”

“I understand. The older you get, the more you talk to yourself.”

It was hard to believe this conversation was between a young man who still looked fresh-faced and a boy who looked several years younger still. But appearances weren’t everything.

The Slaughter Saint knew that better than almost anyone.

“So the Alliance Leader does it too. I suppose we’re all much the same.”

“Hm? Much the same?”

“Didn’t you just say that people talk to themselves more as they get older?”

“Oh, that. I meant people in general. I’ve talked to myself since I was a child, so I can’t say I relate.”

“……Is the tea going to take much longer?”

Just as the Slaughter Saint was feeling his energy rapidly drain away, Mae Jonghak finally set a steaming cup on the table.

“Drink. It isn’t mine, but the aroma should be quite good.”

Mae Jonghak was right.

Perhaps because it was the tea enjoyed by a man who had been a City Lord, both its aroma and quality were excellent.

The man, who had committed countless acts of corruption, had vanished like dew on the execution grounds. But his tea leaves—and his lavish study—remained.

The room now served as the Murim Alliance’s temporary Alliance Leader’s Hall.

“I hope I’m not taking up too much of your precious time.”

The Slaughter Saint glanced at the towering piles of papers, which looked ready to collapse at any moment. Mae Jonghak tilted his hot teacup and answered.

“Time is always precious. If we’d lost the battle seven days ago, I wouldn’t be enjoying this luxury.”

Watching the wisps of steam rise like heat haze, the Slaughter Saint murmured as if to himself.

“Seven days. Has it really been that long?”

Mae Jonghak wasn’t the only one who’d been busy.

The past week had been a whirlwind for everyone, the Slaughter Saint included.

They’d had to begin dealing with the aftermath before they could properly recover from the physical and mental exhaustion.

And Mae Jonghak already knew that the Slaughter Saint, busy treating the wounded, wouldn’t have come for no reason.

“You seem to have enjoyed the tea’s aroma. What do you think?”

Naturally, he wasn’t asking whether the man liked the tea.

The Slaughter Saint silently watched Mae Jonghak smile, then awakened the internal energy that had lain deep within him.

*Wooooom.*

A wave spread out, making the air tremble.

Only after an invisible barrier that cut off sound had completely enclosed the two of them did the Slaughter Saint part his tightly closed lips.

“I came to see you about the matter I mentioned before.”

Mae Jonghak’s eyes immediately turned grave.

“Since you came all this way yourself…… I take it the result wasn’t good.”

The Slaughter Saint answered, his voice heavy as well.

“That’s right.”

“You couldn’t find it after all?”

“Based on what we know so far.”

There was still a faint possibility, but both Mae Jonghak, who was listening, and the Slaughter Saint, who had spoken the words, looked doubtful.

As soon as the battle ended, the surviving martial artists, government troops, and countless civilians had all thrown themselves into dealing with the aftermath.

It had been a massive clash, leaving more than a hundred thousand dead or wounded on both sides. But if they hadn’t found *it* in the seven days since, the chances of finding it later were slim.

“Further searches would be pointless.”

“You mean…”

“I’m not saying we should call them off entirely. We should keep looking, but cut down on wasting manpower.”

The Slaughter Saint nodded quietly.

Mae Jonghak was right.

He, too, thought it better to focus on what lay ahead than to cling to something that showed little sign of success.

And yet, the unease pressing down on his heart remained.

“I can’t say I’m not worried either. But…”

Seeing the shadow on the Slaughter Saint’s face, Mae Jonghak continued.

“The tide has already turned. The blades of the Central Plains—or rather, the whole realm—have finally converged.”

At Mae Jonghak’s quiet words, he reached out. Dozens of missives suddenly rose from between the piles of papers and flew before them.

From the Nine Provinces and Eight Wastes to the Four Seas and Five Lakes.

The missives had crossed the vast sky and earth to reach Xining. Each bore a different seal, but the final words at the end were the same.

“Exterminate the Demons and Set Heaven Right.”

Exterminate the demons and set heaven right.

It was the banner raised by the old Murim Alliance, and the four words that now ran through the whole realm.

Even the empire, newly reborn under the name Great Ming, had embraced them.

“They’re coming. For the same purpose as us—one and only one.”

Seven days had passed since their decisive victory after a fierce battle.

But those who had spent the time since living each day as if it were a mere moment were not only the people in Xining.

On the day rivers of blood had flowed through Xining, the enemies’ corpses had piled up like mountains in Henan Province and Shanxi Province.

Ma Sanbao’s head had been taken back to the Imperial Capital, while the rest of his body had been torn to pieces and scattered across the realm.

The Azure Sky Sword King, who had already made every preparation, had wiped out the enemies without a single casualty. The dozen or so remaining Moving Formations had also been shut down before daybreak.

As long as the Demon-Sealing Formation cast by the Zhuge Clan’s formation masters remained in place, the danger posed by the Moving Formations had effectively been eliminated.

After all, the formation’s power had been what allowed them to seal the first rift that had opened in Hubei.

And the safety that brought had lit the fuse that had lain cold.

Under the banners of the Imperial House and the Murim Alliance, the westward advance had begun in earnest.

At the Son of Heaven’s imperial decree that he would personally lead a great army to punish the rebels, a hundred thousand elite Imperial Guards assembled. And it went without saying that martial artists were gathering too, led by the Nine Sects and One Gang and the Five Great Families.

That wasn’t all.

Even the powerless common people formed volunteer militias to stand against injustice. At last, the will of the realm had become one.

“Xinjiang. We can end everything in that accursed land beyond the desert.”

Mae Jonghak spoke in a low but powerful voice.

“The only way to stop this wheel from turning is to defeat the Lord of Heaven.”

The beginning and end of it all. Its very center.

That was what the Lord of Heaven was.

An absolute being who had never once revealed his true form, yet whose immense shadow had spread across the whole realm.

But now that the realm had joined forces and pointed its blades at the Lord of Heaven, heaven’s will was already on their side.

Or so they believed.

*……But why?*

For some reason, the words “Son of Heaven” filled him with an inexplicable sense of foreboding.

The Slaughter Saint tilted his teacup, now gone cold.

Perhaps to keep the unease deep in his heart from showing.

And as he did, he turned over the other reason he’d come to see Mae Jonghak today.

*I can’t understand the Bow Saint’s behavior back then.*

To be precise, no one else would have been able to understand it either.

That was why the Slaughter Saint found it even harder to shake from his mind.

The way she’d stood by, almost indifferent, even when Jin Taekyung was in mortal danger.

Her inscrutable actions, as if she had some hidden purpose no one else knew about.

*She’s hiding something. She definitely is.*

Yet even though seven days had passed, the Slaughter Saint still hadn’t found an answer.

The Bow Saint had been hard to find since the battle ended, and Jin Taekyung himself still hadn’t regained consciousness.

*What should I do?*

With his thoughts growing heavier, the Slaughter Saint drained the rest of his tea.

Then he carefully opened his mouth to speak to Mae Jonghak, who was watching him in silence as though he had sensed something.

Or tried to.

*Thud-thud-thud-thud!*

Then heavy, hurried footsteps sounded, and a massive man burst into the study.

*Crash!*

The brute smashed through the door and shouted.

“Alliance Leader! Taishan saw it! I saw it with these two eyes!”

Recognizing the familiar face, the Slaughter Saint sighed and fell silent. Mae Jonghak felt in every inch of his skin that his brief respite had come to an end, and replied in a sorrowful voice:

“I see. What did you see?”

At Taishan’s next words, both men’s eyes widened.

“The Pavilion Master! The Pavilion Master woke up!”

“……!”

“……!”
```
