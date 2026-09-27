<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1034.txt",
      "sha256": "ace1cc78bba15ce28d61fc9cd004752f147cb0b8713c74eafb0a8446d9816d41",
      "bytes": 13805
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a08b1000999b3547e8286b1344b98d7f1bd067d2d643167e77a03af650294b52",
      "bytes": 1428
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2067dd2b7fa33b1fa5ed0aadd49d6f2d144d2878b5e0ef369f14bcd34c117262",
      "bytes": 240195
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "1c26f6e188be8ef820032642bd253567467dc9d539285c29a425d458b285a05a",
      "bytes": 928
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "3823c72a49d84df8a0570d19ba468c87e3d603febd6de2182af1d6080b8a025b",
      "bytes": 932
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5cf5264a88aa5166ab7e4ceebc57df0ce464267297d4885f8ddc4c3a6b0ee82e",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "0dd683b29b966e15d0de98e71b7876f61ccee35d7bbdf3ded2078517e23431b5",
      "bytes": 839
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f157d23c41a0cf49392fd415715b4e27916b3a56a92866fd168bad614440abb5",
      "bytes": 1502
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "bd133613fccd72dfda99f4c06df65570f9d13c2e3ebdd9b7237cb00118818afc",
      "bytes": 779
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "4e82793467edf51f9eb10257ba0ea0623da9c2737d3332e8b0ddf6a449ef3d30",
      "bytes": 716
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "bef041df6142cd06189f1c6581ad6c618a795153a9f5db59e8f9dc843734132f",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7bef61cf3c1189d52da85c19602897ae067265e940f6ef0566c1baf640ee2182",
      "bytes": 279224
    }
  ],
  "estimated_tokens": 11785
}
-->

# Durable State Update — Chapter 1034

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
1 and safe_through 1034. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1034. Profile updates may replace only one
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
  "chapter": 1034,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1034,
    "continuity_sources": [1034],
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
    "The Blood-Sword Demon Lord commands seven Black Ghosts and has ordered them not to kill Jin Taekyung.",
    "The Black Ghosts feel neither pain nor emotion and can regenerate from severe injuries.",
    "Four Black Ghosts are fighting Jin Taekyung and Jeok Cheongang; two likely headed toward the Zhongnan Sect, and one remains unaccounted for.",
    "The Zhongnan Sect fields one thousand elite main-sect forces, including three Supreme Peak masters, in the battle at the Great Snow Mountain.",
    "The Blood-Sword Demon Lord’s new master gave him authority over tens of thousands.",
    "White-robed figures under heavy guard are near the Blood-Sword Demon Lord; their strength may rival or exceed the Black Ghosts.",
    "Jin Taekyung and Jeok Cheongang are fighting on the battlefield."
  ],
  "continuity_sources": [
    1032,
    1033
  ],
  "open_questions": [
    "Who are the seven Black Ghosts, and what were their identities before becoming Black Ghosts?",
    "What is the Lord of Heaven’s identity and purpose?",
    "Did Dark Heaven cause the Great Faction War?",
    "How did the Black Axe Fiend return from the dead, and who is the other Black Ghost present?",
    "Who are the guarded white-robed figures?"
  ],
  "safe_through": 1033,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 정마대전   | **Great Faction War**         |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 적천강 | former battlefield adversaries | Fire King | calm and familiar | Addresses Jeok Cheongang as 화왕 while asking him not to rush. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1025
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1033
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung, and he admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1033
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1027
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1033
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1019
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1025
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 1031
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃1034화



머리부터 발끝까지, 이질적으로 느껴질 만큼 새하얀 백의(白衣)를 차려입은 그들은 온통 칠흑과도 같은 암천의 교도들 중에서 단연 눈에 띄는 존재들이었다.

풍성하다 못해 땅에 끌릴 만큼 길게 늘어진 소매와 얼굴 대부분을 가린 면사(綿絲).

의복이라기보다는 커다란 비단에 가까운 그것으로 전신을 빈틈없이 감싼 채 말없이 전장을 주시하는 그들의 모습은, 혈검마군의 입장에서도 썩 익숙하지 않았다.

아니, 한편으로는 불편하기까지 했다.

과거 한솥밥을 먹던 동료에서 이제는 맹목적인 살인 병기로 거듭난 흑귀(黑鬼)들과는 달리, 저들의 지휘권은 혈검마군이 아닌 ‘그분’께 있었으니까.

‘단지 그 정도에 그쳤다면, 차라리 나았을 수도 있겠지.’

피로 뒤덮여 가는 전장을 바라볼 때만 해도 생기가 감돌던 혈검마군의 눈빛에 문득 언짢음이 스쳤다.

‘이토록 훌륭한 전장을 코앞에 두고 구경만 해야 한다니.’

언짢은 정도를 넘어, 이제는 불쾌하기까지 한 기분.

고작 스무 명에 불과한 백의인들을 스쳐 지나간 그의 시선이 한 사람에 이르러 우뚝 멈췄다.

그리고 그와 동시에, 혈검마군은 떠올렸다.

불과 일각 전, 흥에 겨워 선두에 나선 자신을 가로막았던 나직한 음성을.



‘마군께서는 조금 더 인내하시지요. 아직은 때가 무르익지 않았습니다.’



만약 정마대전 당시의 혈검마군에게 누군가가 저런 말을 했다면, 그는 즉시 헛소리를 지껄인 놈의 주둥이를 찢고 혀를 뽑았을 것이다.

하지만 오십여 년은 참으로 긴 세월이었고, 그사이 혈검마군은 조금 더 성숙해졌다.

보다 정확히는, 새로운 주인인 천주(天主)를 향한 두려움과 경외가 그의 발걸음을 붙잡고 살심을 억누르게 만들었다.

‘빌어먹을.’

지금 이 순간에도 혈검마군이 뚫어져라 응시하고 있는 저 호리호리한 체구의 백의인이, 감히 그의 행사를 방해하고도 살아남을 수 있었던 이유는 실로 간단명료했다.

‘그분만 아니었더라면.’

모든 백의인들의 우두머리 격인 동시에, 심지어 혈검마군 자신보다도 가까이에서 천주를 모셨던 자.

그러니 살귀(殺鬼)의 기질을 타고난 혈검마군으로서도 단순한 수틀림을 명분 삼아 쉽사리 손을 쓸 수 없었다.

물론 그렇다 한들, 한 번 뒤틀린 심기까지도 꾹꾹 눌러 삼킬 인내심은 혈검마군에게 없었다.

“놈들이 제법 잘 버티는군. 진즉 내가 나섰다면 이미 전황이 크게 기울었을 텐데 말이야.”

시선과 음성에 담긴 것은 노골적인 이죽거림.

하지만 표적이 된 백의인은 물론, 그를 둘러싼 누구도 혈검마군의 말에 대꾸하지 않았다.

그리고 그 사실은 혈검마군이 애써 참고 있던 마음속 분노를 자극하기에 충분했다.

“희한하지 않나. 나서지 말아야 할 때는 아랑곳하지 않고 나서더니, 정작 지금은 꿀 먹은 벙어리 행세를 하는 모습이.”

마치 뱀의 그것처럼 세로로 길게 찢어진 동공이, 줄곧 시선이 고정되어 있던 백의인을 향해 한층 더 가늘어졌다.

“아니면, 앞으로도 영영 벙어리가 되고 싶다는 뜻인가?”

착 가라앉은 목소리가 울려 퍼진 그 순간, 마침내 그가 굳게 닫혀 있던 입술을 열었다.

아니, ‘그녀’가.

“마군께서는 제게 어떤 대답을 원하십니까.”

한 치의 떨림도 느껴지지 않는 차분한 대답.

자신과는 상반되는 침착한 음성에, 혈검마군의 눈썹이 꿈틀거렸다.

“이곳의 수장은 나다. 그분의 뜻을 받들어 여기까지 왔지.”

“압니다. 저 또한 그 자리에 있었으니까요.”

“한데, 감히 너 같은 계집 따위가 내게 명령을 내린단 말이냐?”

“명령이 아니라, 단지 만류했을 뿐입니다.”

얼굴에 드리워진 새하얀 비단 아래, 앵두 같은 입술이 다시 한번 달싹였다.

“그리고 그것이, 곧 그분께서 바라시는 바이기도 합니다.”

“……!”

순간 들려온 예상치 못한 대답에, 혈검마군의 얼굴이 딱딱하게 굳었다.

“지금…… 뭐라고?”

“그분께서 이를 원하실 것이라 말씀드렸습니다.”

“그분께서, 위대하신 천주께서 내가 나서기를 원치 않는다니. 도대체 그게 무슨…….”

믿을 수 없다는 듯한 얼굴로 말꼬리를 흐리는 혈검마군을 향해, 여인은 고개를 작게 내저었다.

그런 그녀의 고갯짓을 따라, 아름다우면서도 한편으로는 기이하게 느껴지는 무늬가 수실로 새겨진 순백색의 면사가 부드럽게 흔들렸다.

“오해가 있으시군요. 그분께서는 가급적 마군께서 해를 입지 않기를 바라실 뿐입니다.”

“해를 입는다고? 다른 누구도 아닌 내가?”

혈검마군은 순간 자신의 귀를 의심했다.

그것은 한 사람의 무인으로서, 열과 성을 다해 누군가를 섬기는 수하로서 더없이 치욕적인 말이었다.

물경 삼만을 넘어가는 마병(魔兵)과 비록 이제는 쓸모없어졌지만 천산삼노라는 세 마리의 사냥개.

거기에 더해 일곱 기나 되는 흑귀들까지 거느린 그다.

뿐인가.

아직 온전한 전력을 모두 드러내지 않았을 뿐, 혈검마군 스스로도 등봉조극(登峰造極)의 경지에 오른 최고수였다.

반면 적들은?

무엇하나 비교할 수 없을 만큼 모든 면에서 뒤떨어진다.

전장의 향방을 뒤바꿀 수도 있는 초절정 고수의 숫자, 병력 개개인의 질, 마지막으로 기세까지도.

이미 저울추는 기울었다.

전투를 시작하기 전에도, 지금 이 순간에도 빠르게 기울고 있다.

한데, 한데 어째서 저 계집은 이런 헛소리를 지껄이는 것일까.

그저 전폭적인 신뢰를 받고 있다 굳게 믿었던 자신의 마음에, 어찌 이리 커다란 바위를 던져 균열을 일으키는 것일까.

“지금 한 말, 목을 걸고 책임질 수 있겠느냐?”

어느새 차갑게 식은 눈빛과 목소리.

하지만 그런 혈검마군의 모습에도, 뒤이어 되돌아온 여인의 대답은 조금 전과 크게 다르지 않았다.

“그분께서 마군을 아끼시는 마음이 하해와 같으니, 부디 뜻을 헤아려 주시지요.”

사실상 시인이나 다름없는 한 마디.

혈검마군의 입가에 흐릿한 미소가 맺혔다.

“그분께서 나를 아끼신다라. 그래, 그럼 마땅히 헤아려 드려야지.”

분명 웃고 있으나, 도무지 웃는 것 같지 않은 그의 미소에 여인의 목소리가 다급해졌다.

“잘 아시겠지만 이미 앞서 네 분의 마군, 마후께서 유명을 달리했습니다. 그분께서는 당신의 위대한 대업(大業)을 맡아 이뤄낼 충직한 종이 한 사람이라도 더…….”

“그만. 결국 네가 하고 싶은 말은 섣불리 나서지 말라는 것이 전부 아니더냐.”

“……마군. 그것이 아니오라.”

“되었으니 그 입 다물어라. 이제 그분의 뜻은 충분히 알았으니.”

혈검마군은 담담하게 뇌까렸지만, 이미 한바탕 폭풍이 휩쓸고 간 뇌리에 남아 있는 생각은 달랐다.

‘당신께서 직접 지켜보시기에, 속하는 고작 이 정도의 그릇밖에 되지 않았습니까?’

우둑.

어느샌가 있는 힘껏 말아쥔 손에서 뼈마디 어긋나는 소리가 들렸다. 새하얗게 물든 주먹 사이로, 손톱이 조금씩 살갗을 파고들기 시작했다.

‘속하는…… 온 힘을 다해 충성했습니다. 그 누구보다도 당신을 따랐습니다.’

그는 천주를 처음 만났던 그 날을 떠올렸다.

상상할 수도 없던 아득한 경외와 두려움으로 인한 그 떨림을, 심장이 멎어 버릴 것만 같았던 충격을 마치 어제 일처럼 또렷하게 기억했다.

‘비록 속하가 원했던 중책을 맡지는 못했으나, 장장 오십여 년의 세월을 오직 당신의 대업을 받들기 위해 살았습니다.’

정마대전.

그 길었던 대전쟁의 끝자락에서 천마가 무신에게 최후를 맞이했을 때, 혈검마군은 조금도 동요하지 않았다.

당연한 일이었다.

그가 지켜본 천마도 결국 한낱 인간에 불과했으니까.

한때나마 거대하다고 느꼈던 포부도, 젊은 시절의 혈검마군을 압도적으로 무릎 꿇렸던 고강한 무위도, 전부 천주를 만난 이후로 빛이 바래져 버렸으니까.

그렇기에 그는 조금도 슬프지 않았다.

오히려 진정으로 섬길 자격이 있는 주인을 찾았다는 사실이 기뻤다.

암천이라는 이름으로 새롭게 태동한 그곳에서, 또 다른 다섯 명의 거마(巨魔)가 자신보다 윗줄에 앉게 되었다는 사실을 앉기 전까지는.

‘그때에도, 속하는 그저 당신께 복종했습니다.’

그는 말없이 이해했다.

본래 마교 내에서의 서열이 그보다 높았던 서천마군에게는 그럴 만한 명분이 있었고, 동천마군과 북천마군은 중원 깊숙이 심어 놓은 비수였기에 그 중요성에 따라 높은 대우를 받을 만했다.

남천마후도, 혈주도 이해할 수 있었다.

마음속에는 불만이 싹텄지만, 그것이 곧 주인의 뜻이었으니까.

하지만…….

‘이제는, 더 늦기 전에 조금은 속하를 믿어 주셨어야지요.’

천주가 그토록 신뢰했던 네 명의 마군과 마후는 끝끝내 최후를 맞이했다. 그들은 맡은 바 임무를 보기 좋게 실패했고, 죄를 추궁하기도 전에 이승을 떠났다.

그리하여 마침내 혈검마군의 차례가 왔다.

질기게도 살아남은 혈주와 함께 그는 마침내 천주의 양팔이 되었다.

오른팔이든 왼팔이든, 그건 크게 중요하지 않았다.

혈검마군이 그 무엇보다 중요하게 생각했던 것은, 주인의 신뢰와 자신에게 주어진 기회뿐이었다.

단지 그뿐이었다.

‘한데, 무엇이 그토록 우려되셨단 말입니까.’

이미 죽고 없는 마군과 마후 중, 그 누구도 지금의 자신과 같은 대군세를 이끌지는 못했다.

그들에게는 일곱 기나 되는 흑귀도, 수만에 달하는 병력도 없었다.

그러나 그들조차 가지지 못했던, 승리를 위한 모든 조건을 완벽하게 갖춘 자신을 주인은 온전히 믿지 못하고 있었다.

눈처럼 새하얀 백의를 걸친 저 계집의 입을 통해, 그는 자신을 향한 주인의 불신(不信)을 읽을 수 있었다.

“속하가, 그리도 못 미더우셨나이까.”

마음속에만 머물러야 할 탄식이 마침내 소리가 되어 입술 사이로 흘러나온 그 순간.

콰아아아!

하늘이 쪼개지는 듯한 굉음과 함께, 불의 기둥이 솟구쳤다.

혈검마군이 위치한 수십여 장 밖에서도, 아니 전장의 그 어디에서도 선명하게 확인할 수 있는 그것은 맹렬하면서도 거대했다.

더불어, 그 무엇보다 무자비했다.

드드드드득!

거센 진동이 지면을 타고 전해진다.

그리고 굉음이 울려 퍼지기도 전, 불현듯 느껴지는 힘의 파동에 한발 앞서 고개를 돌린 혈검마군은 모든 것을 확인하고 담담하게 뇌까렸다.

다시 한번, 이곳에 없는 자신의 주인을 향해.

“당신께서 조금만 더 속하를 믿어 주셨다면, 이 전투는 이미 끝나 있었을지도 모르지요.”

“마군……!”

“왜, 나는 이 정도의 투정도 부리지 못하느냐?”

등 뒤에서 들려오는 여인의 다급한 외침에, 고개도 돌리지 않은 채 대답한 혈검마군은 저 멀리 피어오르는 아지랑이를 바라보았다.

정확히는, 그 무수한 아지랑이를 만들어 낸 끔찍한 열기 속을 섬광처럼 누비고 있는 두 인영을.

콰드득, 펑!

화왕(火王) 적천강.

그의 일권, 일장에 거무스름한 안개가 터져 나간다.

그 심대한 타격을 회복하기 위해 안개가 모여드는 찰나, 검푸른 강기가 온 사방을 베어 갈랐다.

서걱, 콰아아아!

네 기나 되는 흑귀들이 쉴 새 없이 비틀거린다.

사지가 잘려 나간 단면에서 뭉클뭉클 솟아오르는 어둠의 기운은 색이 다른 핏물과도 같았고, 그 모습은 영락없이 죽음을 앞둔 인간을 닮아 있었다.

아니, 혈검마군은 본능적으로 깨달았다.

그들에게도 마침내 영원한 죽음이 찾아오고 있다는 사실을.

고오오옹.

불현듯 일그러지기 시작하는 공간. 백색의 창날을 휘감으며 솟아오른 거대한 강기가 넘실거렸다.

마치…….

‘한 마리의 용처럼.’

그리고 혈검마군이 자신도 모르게 마음속으로 중얼거린 그 순간, 주인과 하나가 된 창이 한 줄기의 벼락이 되어 흑귀들을 향해 떨어져 내렸다.

솨아아악!

천격(天格).

반경 수십여 장을 물들이고 뒤흔든 그 아득한 섬광과 파괴력이 스쳐 지나간 자리에 남아 있는 것은 아무것도 없었다.

네 마리의 흑귀도. 끊임없이 두 사승을 향해 덤벼들던 교도들도.

그러나 아직 남아 있는 것이 있다면, 그것은 주인에게 자신을 입증하고자 하는 어느 살귀(殺鬼)의 결심뿐이었다.

스릉.

날 선 소음이 혈검마군의 귓가를 간질였다.
```

## Final English reading copy

```markdown
# Chapter 1034

From head to toe, they were dressed in white so pure it felt out of place. Among the followers of Dark Heaven, clad in pitch black, they stood out at once.

Their sleeves were not merely voluminous—they trailed so long they dragged on the ground. A veil hid most of each face.

Wrapped head to toe in garments less like clothes than great swaths of silk, they silently watched the battlefield. Even to the Blood-Sword Demon Lord, they were unfamiliar.

No—in a way, they made him uncomfortable.

Unlike the Black Ghosts, his former comrades who had shared a bowl with him before becoming blind killing machines, those people took their orders not from the Blood-Sword Demon Lord, but from “that person.”

*If that had been all there was to it, perhaps I could have lived with it.*

The Blood-Sword Demon Lord’s eyes had been alive with excitement as he watched the battlefield turn red with blood. Now, a trace of displeasure crossed them.

*To have such a magnificent battlefield right before me, and do nothing but watch.*

It was more than displeasure. He was beginning to feel downright offended.

His gaze passed over the twenty or so white-robed figures, then came to a sudden stop on one of them.

And at the same moment, the Blood-Sword Demon Lord remembered.

A mere fifteen minutes earlier, he had eagerly stepped to the front, only for a quiet voice to stop him.

*“Demon Lord, please be patient a little longer. The time is not yet ripe.”*

If anyone had said that to the Blood-Sword Demon Lord during the Great Faction War, he would have torn the mouth off the fool spouting such nonsense and ripped out his tongue.

But fifty years was a very long time, and in the meantime, the Blood-Sword Demon Lord had grown a little more mature.

More precisely, fear and reverence for his new master, the Lord of Heaven, had held him back and suppressed his murderous impulse.

*Damn it.*

The reason that slender white-robed figure—whom the Blood-Sword Demon Lord was still glaring at—had survived after daring to interfere with him was simple.

*If not for that person.*

The figure led the white-robed group and had served the Lord of Heaven even more closely than the Blood-Sword Demon Lord himself.

So even a born killer like him couldn’t easily strike over a mere slight.

Of course, that didn’t mean the Blood-Sword Demon Lord had the patience to swallow down the irritation festering inside him.

“They’re holding up rather well. If I’d stepped in sooner, the tide of battle would already have turned.”

The words dripped with open mockery.

But neither the white-robed figure he’d singled out nor anyone nearby answered.

That was more than enough to stir the anger he’d been struggling to keep in check.

“Isn’t it strange? When you shouldn’t have stepped in, you did so without a care. But now you’re acting like you’ve swallowed your tongue.”

His pupils, slit vertically like a snake’s, narrowed further at the white-robed figure he’d been watching all along.

“Or does that mean you’d like to stay silent forever?”

At the sound of his low, flat voice, the figure’s tightly closed lips finally parted.

No—*her* lips.

“What answer do you want from me, Demon Lord?”

Her reply was calm, not a tremor in her voice.

Her composure was the opposite of his, and the Blood-Sword Demon Lord’s brow twitched.

“I’m in command here. I came this far to carry out that person’s will.”

“I know. I was there, too.”

“And yet you, a mere woman, dare to give me orders?”

“I did not give you an order. I only tried to dissuade you.”

Beneath the pure-white silk veil covering her face, her cherry-red lips moved again.

“And that is what that person wants, too.”

“……!”

At the unexpected reply, the Blood-Sword Demon Lord’s face went rigid.

“What…… did you say?”

“I said that is what that person wants.”

“That person—the great Lord of Heaven—doesn’t want me to step in? What in the world does that……?”

The Blood-Sword Demon Lord trailed off, unable to believe what he was hearing. The woman gave a small shake of her head.

With the motion, the pure-white veil, its beautiful yet uncanny pattern embroidered in colored thread, swayed softly.

“You misunderstand. That person only wishes for you to avoid harm, if possible.”

“Avoid harm? Me, of all people?”

For a moment, the Blood-Sword Demon Lord thought he’d misheard.

It was an unbearably humiliating thing to hear—as a martial artist, and as a subordinate who had devoted himself wholeheartedly to serving someone.

He commanded more than thirty thousand demonic soldiers and, though they were useless now, the Three Elders of Tianshan—the three hunting dogs.

On top of that, he had seven Black Ghosts at his command.

And that wasn’t all.

He hadn’t yet revealed the full extent of his strength, but the Blood-Sword Demon Lord himself had reached the realm of Supreme Mastery, making him one of the greatest masters alive.

And the enemy?

They were inferior in every way, with nothing that could compare.

The number of Supreme Peak masters who could turn the tide of battle. The quality of each soldier. And, finally, their momentum.

The scales had already tipped.

They had been tipping rapidly before the battle began, and they were still tipping rapidly now.

So why was that woman saying such nonsense?

Why was she hurling a boulder into his heart, cracking his conviction that he had his master’s complete trust?

“Can you stake your life on what you just said?”

His voice and gaze had gone cold.

But the woman’s reply was hardly different from before.

“That person’s care for you is as vast as the sea. Please try to understand their intentions.”

It was as good as an admission.

A faint smile came to the Blood-Sword Demon Lord’s lips.

“That person cares for me. Fine. Then I ought to understand.”

The smile on his face didn’t look like a smile at all. The woman’s voice turned urgent.

“As you know, four Demon Lords and Demon Empresses have already met their ends. That person needs at least one more loyal servant to carry out their great cause…….”

“Enough. All you’re trying to say is that I shouldn’t rush in.”

“……Demon Lord, that isn’t what I—”

“Enough. Hold your tongue. I understand that person’s wishes perfectly well now.”

The Blood-Sword Demon Lord spoke calmly, but his thoughts, after the storm that had swept through his mind, were anything but.

*You are watching me yourself, and this is all you think I’m capable of?*

Crack.

The joints in the hand he’d clenched with all his strength popped. His nails began to dig into his skin, drawing blood from his whitening fist.

*I…… have been loyal to you with everything I have. I followed you more faithfully than anyone.*

He remembered the day he first met the Lord of Heaven.

He remembered as clearly as if it had happened yesterday the tremor brought on by a fear and reverence beyond imagining, the shock so great it felt as if his heart might stop.

*Though I never received the important post I wanted, I spent more than fifty long years living solely to serve your great cause.*

The Great Faction War.

When the Heavenly Demon met his end at the Martial God’s hands, near the close of that long war, the Blood-Sword Demon Lord hadn’t been shaken in the slightest.

Of course he hadn’t.

The Heavenly Demon he’d watched was only human, after all.

The grand ambition that had once seemed so vast, the formidable martial might that had crushed the young Blood-Sword Demon Lord to his knees—it had all faded after he met the Lord of Heaven.

That was why he hadn’t felt even a trace of sorrow.

He’d been glad, instead, to have found a master truly worthy of his service.

Until, in the new power that had arisen under the name Dark Heaven, five other great fiends had taken seats above him.

*Even then, I simply obeyed you.*

He’d understood without a word.

The Western Heaven Demon Lord had once outranked him within the Demonic Cult, and had a valid claim to his position. The Eastern Heaven Demon Lord and North Heaven Demon Lord were daggers planted deep in the Central Plains, and deserved their high standing for the importance of their roles.

He understood the Southern Heaven Demon Empress, too. And the Blood Lord.

Discontent had taken root in his heart, but that had been his master’s will.

But……

*Now, before it was too late, you should have trusted me at least a little.*

The four Demon Lords and Demon Empress the Lord of Heaven had trusted so deeply had all met their ends. They had failed their missions spectacularly, then left this world before anyone could even call them to account.

At last, it was the Blood-Sword Demon Lord’s turn.

Together with the Blood Lord, who had stubbornly survived, he had finally become one of the Lord of Heaven’s two arms.

Whether he was the right arm or the left didn’t matter much.

What mattered more than anything to the Blood-Sword Demon Lord was his master’s trust and the opportunity he’d been given.

That was all.

*But what was there to worry about so much?*

None of the Demon Lords and Demon Empresses who were now dead had commanded an army like the one he led. They hadn’t had seven Black Ghosts, or tens of thousands of soldiers.

Yet their master didn’t fully trust him—the one who had everything needed for victory, conditions none of them had possessed.

Through the mouth of that woman in snow-white robes, he could read his master’s distrust of him.

“Was I really so unworthy of your trust?”

The sigh that should have stayed in his heart finally became a sound, slipping between his lips.

KWA-BOOOOM!

A pillar of fire shot skyward with a roar that seemed to split the heavens.

It was visible even from dozens of *jang* away, where the Blood-Sword Demon Lord stood. In fact, there was nowhere on the battlefield it couldn’t be seen. It was immense and raging.

And more merciless than anything else.

GRRRRRR!

A violent tremor traveled through the ground.

Before the roar even reached him, the Blood-Sword Demon Lord sensed a sudden wave of power and turned his head. He took in the scene and murmured calmly.

Once again, he spoke to the master who wasn’t there.

“If you’d trusted me just a little more, this battle might already have been over.”

“Demon Lord……!”

“Why? Am I not allowed to grumble this much?”

Without turning at the woman’s urgent cry behind him, the Blood-Sword Demon Lord replied as he watched the distant haze rising into the air.

More precisely, he watched the two figures streaking through the terrible heat that had given rise to all that haze.

KRAK, BOOM!

Fire King Jeok Cheongang.

With each punch and palm strike, the murky black fog burst apart.

The moment the fog gathered to recover from those devastating blows, dark-blue Force slashed in every direction.

SHHK—KWA-BOOOOM!

Four Black Ghosts staggered without pause.

Dark energy welled from the severed ends of their limbs like blood of a different color. Their appearance was unmistakably that of humans on the verge of death.

No—the Blood-Sword Demon Lord realized it instinctively.

Eternal death was finally coming for them, too.

Goooooong.

Space suddenly began to distort. Great Force surged around the white spearhead, rising and rolling in waves.

Like……

*A dragon.*

And at the moment the Blood-Sword Demon Lord muttered those words to himself, the spear, now one with its master, fell toward the Black Ghosts like a bolt of lightning.

SHWAAASH!

Heavenly Strike.

When that distant flash and its devastating force had passed, painting and shaking everything within dozens of *jang*, nothing remained.

Not the four Black Ghosts. Not the followers who had kept charging at the master and his disciple without pause.

And yet something remained: the resolve of a certain born killer, determined to prove himself to his master.

SHING.

A sharp sound brushed the Blood-Sword Demon Lord’s ear.
```
