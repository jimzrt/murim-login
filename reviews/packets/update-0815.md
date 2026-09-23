<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0815.txt",
      "sha256": "4b8866e9da0dd6b187843fafb99ad6646cf078a358878fa3663c7a9e7a58c185",
      "bytes": 13154
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d66cdd61cfadbde7a936ba06972360fdc097e91fb11bf402035565c09218cc3c",
      "bytes": 1227
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c8fff61ffde9ce550b4d1184cab823120a209474f19e6e8c4529997f78f8d1ba",
      "bytes": 225894
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4adb05a4cc0e98bf1d21d7e9be0f2186f825238e85dd0ffdd089b2373b422eeb",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "37dfd24645957df68523e9faeb302fb022b8ce29536b2ccc1f39e3a355a8decd",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0b475604468d81bed554749064f4215d346dacf180b9d4e1fb7e52329ae8da34",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "cf8c3d88c3d836285e0261b9ebab007b1c6ec431a176d6d017b84ce2c9ed32c6",
      "bytes": 645
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "2b13fd737a8941c4e948cd9d786823cbadd48cc1c5e232d89ef161ba8c6a25bf",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "129974e6f11f14cc393ae3bd0f5641ba588160bd005872ba6c36f3b8580fa33e",
      "bytes": 249016
    }
  ],
  "estimated_tokens": 9980
}
-->

# Durable State Update — Chapter 815

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 815. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 815. Profile updates may replace only one
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
  "chapter": 815,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 815,
    "continuity_sources": [815],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss” and has concealed itself for decades, including under the name Muninn.",
    "The Prophet can revive by drawing on the lives of its victims and can reproduce their appearances, abilities, and memories.",
    "Jin destroyed the Doppelganger's Level 120 Yamamoto Genji identity with Scorching Yang Qi, but The Prophet survived in another appearance.",
    "Fanatics are advancing through the canyon; Hunters arrive as reinforcements on eagles and griffins.",
    "Magic Johnson says he helped Jin because they are friends; whether Johnson is human remains uncertain."
  ],
  "continuity_sources": [
    813,
    814
  ],
  "open_questions": [
    "Why does The Prophet want Jin to flee, and what does it ultimately want?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 814,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 알라 | **Allah** | Deity invoked by the Middle Eastern terrorist groups' rhetoric. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 814
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 814
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 814
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 810
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 814
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃815화



쉬이이익.

차가운 밤바람이 전신을 스친다. 흩날리는 머리카락을 쓸어넘긴 최민우는 빠르게 가까워지는 협곡을 내려다보았다.

‘저곳이다.’

시린 빛을 토해 내는 창날은 짙은 어둠 속에서도 단번에 알아볼 수 있었다.

지금껏 수많은 명품 무기와 아티펙트를 수집한 그였지만, 백염(白炎)이라 이름 붙여진 저 창의 강도와 예리함에는 매번 놀라움을 금치 못했다.

‘물론 그 주인보다는 아니지만.’

최민우는 문득 진태경을 떠올렸다.

처음 그를 보았을 때만 해도 상상하지 못했다. 짐꾼 역할로 함께 레이드에 참여했던 또래의 청년이, 불과 일 년도 채 되지 않아 전 세계 모든 헌터들의 정점에 서리라는 것을.

그러나 진태경은 누구도 상상할 수 없던 일을 현실로 만들었다.

수많은 재앙을 막아 냈고, 험난했던 그 과정에서 눈부신 성장을 이뤄 냈다.

위기마다 그가 보여 주는 과감함과 용기는 가장 가까이에서 지켜봐 온 최민우의 예상마저 아득히 뛰어넘고는 했다.

바로 오늘처럼.

‘평소와는 다르다고 느끼긴 했지만…… 진태경 씨는 점점 더 한발 앞서가시는군요.’

스켈레톤 킹이 보낸 언데드를 통해 상황을 전달받았을 때는 놀라움과 섭섭함을 동시에 느꼈지만, 그 감정들은 머지않아 기쁨으로 바뀌었다.

다른 이들이 풀지 못한 난제(難題)를 홀로 해결했다는 것은, 그가 한 단계 성장했다는 증거였으니까.

‘그와 함께라면 우리는 승리할 수 있다.’

진태경은 모두를 이끄는 총사령관이면서 전장을 진두지휘하는 장군이요, 또한 누구보다 앞서 적을 향해 달려 나가는 선봉장이다.

신뢰하지 않을 수 없고, 사랑하지 않을 이유가 없었다.

설령 진태경이 가는 길에 무수히 많은 장애물과 위험이 도사리고 있다 하더라도, 그 사실은 변하지 않는다.

‘많이도 몰려왔군.’

최민우는 침착한 눈빛으로 지상을 응시했다.

수백 미터 아래 지상에서는 새카맣게 몰려든 적들이 파도처럼 협곡으로 쏟아지고 있었다.

헤아릴 수 없을 만큼 무수한 적들.

그들의 발걸음이 지축을 울리고, 거대한 함성이 사방에서 울려 퍼졌다.

- 알라 후 아크바르!

- 형제자매들이여, 돌격하라! 약속의 땅으로!

- 신께서 내리신 구원이 우리를 기다리고 있다!

세상의 눈을 피해 숨어 있던 광신도들이 부르짖었다.

아이러니하게도 신의 구원을 입에 담는 그들의 손에는, 피와 죽음을 부르는 병장기가 들려 있었다.

‘저들은 우리와 같은 사람이 아니라, 단지 쓰러트려야 할 적이다.’

최민우는 다짐하듯 마음속으로 되뇌었다. 아니, 그 광경을 바라보고 있는 헌터들 모두가 마찬가지였다.

그들은 이미 보았다. 뼈저리게 겪었다.

인간은 그 어떤 생명체보다 선해질 수도, 악해질 수도 있는 동물이라는 것을.

이 세상을 위협하는 것은 단지 몬스터뿐만이 아니라는 것을.

마왕 아스모데우스가 강림하기 이전. 숱한 전쟁과 죽음을 불러온 일으킨 이들 역시 그들과 같은 인간이었다.

인류는 그로 인하여 고통받았고, 고통 속에서 잊지 말아야 할 교훈을 깨달았다.

‘세상에는, 붉은 피를 지닌 괴물도 있지.’

그리고 이 자리에 있는 헌터들의 존재 이유이자 유일한 의무는, 그 괴물들을 사냥하는 것이다.

스릉.

곳곳에서 모습을 드러낸 날붙이들이 서늘한 예기(銳氣)를 토해 낸다.

앞서 치른 몬스터 군단과의 전투로 인해 평소보다 지친 기색이 역력했지만, 헌터들의 눈동자에 깃든 의지는 그 어느 때보다 굳셌다.

쐐애애액!

더욱더 맹렬해진 바람. 그리고 가파르게 뛰는 심장.

수십여 마리의 독수리와 그리핀들이 거대한 날개를 비스듬히 세우며 지상을 향해 떨어져 내린다.

저 멀리에서 되돌아오는 메아리처럼 들리던 광신도들의 함성은, 지금 이 순간 모두의 귓가를 쩌렁쩌렁하게 울리고 있었다.

“최후의 한 사람까지 싸워라! 물러서지 마라!”

최민우는 숨을 삼켰다. 전장의 바람이 따끔거린다. 광신도들은 손에 만져질 듯한 광기를 흘리며 협곡을 향해 쏟아지고 있었다.

거구의 대마도사와 수백의 언데드를 거느린 스켈레톤 킹이 있었으나, 그 누구도 두려워하지 않았다.

저들에게 있어 이 전투는 성전(聖戰)이었다. 설령 죽더라도 거룩한 순교자의 일원으로 신의 곁에 설 수 있을 터다.

이미 각성이라는 기적을 경험한 신의 전사들은 낙타의 등을 박차고 눈부신 속도로 쏘아졌다.

삼백 미터. 백 미터. 오십 미터.

가파르게 좁혀지는 거리.

그리고…….

격돌.

퍼엉! 콰아아아앙!

크아아악!

불꽃이 어둠을 살라 먹는다.

매직 존슨의 공격 마법에 직격당한 선봉대가 비명과 함께 타올랐고, 죽음과 함께 찾아온 잠깐의 공백을 순식간에 채워 낸 또 다른 광신도들은 망설임 없이 언데드들을 덮쳤다.

우직, 콰드드득!

터무니없이 좁은 협곡은 아니지만, 그렇다고 해서 넓은 것도 아니다.

그러나 오랜 세월 동안 도플갱어가 육성한 광신도들은 단번에 언데드로 이루어진 전열(戰列)을 허물어트렸다.

광신도들이 품은 뜻과 마음은 이미 괴물과 다름없다 해도, 몬스터들과는 근본적으로 달랐다.

그들은 여느 헌터처럼 강하고 영리했으며, 무엇보다 훌륭한 지휘관이 둘이나 있었으니까.

“타락한 악마들이다! 모조리 쓸어 버려라!”

“인샬라.”

거친 외침과 함께 선두에서 날뛰는 한 사내. 그리고 후미에서 침착한 표정으로 전장을 주시하는 노인.

혼란스러운 전장 속에서도 유독 눈에 띄는 두 사람의 모습을 확인한 최민우는 본능적으로 깨달았다.

그들이 지닌 힘의 크기를.

‘S급 헌터, 아니 광신도라고 해야 하나?’

지금의 그로서는 상대할 수 없는 강자들.

그러나 희한하게도 두려움은 들지 않았다.

다음 순간, 문득 하늘을 응시한 노인과 시선이 마주쳤음에도 최민우의 마음은 한 치의 흔들림도 없었다.

쉭, 서걱!

그야말로 섬광 같은 일격.

노인의 허리춤에서 솟구친 한 줄기의 오러가 최민우가 올라탄 그리핀의 목을 깔끔하게 가른다.

힘을 잃은 거대한 비행 몬스터의 몸뚱어리가 힘을 잃고 기울었다.

슈화악. 드드득!

흉폭해진 바람과 함께 거칠게 흔들리는 신형.

하지만 최민우는 동요하지 않았다. 급강하에서 추락으로 상황이 변했음에도, 어째서인지 입꼬리가 올라갔다.

등뼈를 붙잡고 버티던 다른 헌터들이 내지르는 비명도, 그를 미친놈처럼 바라보는 시선들도 상관없었다.

‘지금까지의 선택에 후회는 없다. 그저 최선을 다해 싸울 뿐.’

마음이 고요하다. 손에 들린 검은 깃털처럼 가볍다. 오늘이라면 무슨 일이든 할 수 있을 것 같았다.

성큼 가까워진 지상과 함께 어느 이름 모를 광신도의 고함이 고막을 후려쳤다.

“위대한 신을 위하여, 선지자를 위하여!”

소리 내어 웃은 최민우가 문득 입을 열었다.

“우리의 맹주를 위하여.”

낮지만 힘 있는 목소리. 그것이 곧 신호였다.

파팟!

최민우가, 아니 헌터들 모두가 지상을 향해 수직으로 처박히던 그리핀의 몸뚱어리를 박차며 솟구쳤다.

탁. 가장 먼저 지면에 내려앉은 그의 손에 들린 검이 흐릿해졌다.

쉬익! 촤아악!

검을 타고 일어난 날카로운 바람이 사방에서 달려들던 광신도들의 사지를 베어 가른다.

핏물을 뿜어내며 허물어지는 몸뚱어리들 사이로 한 줄기 빛이 쇄도했다.

쐐액, 쾅!

빠르게 검을 들어 막았지만, 그것이 최선이었다.

엄청난 힘을 이기지 못하고 몇 걸음이나 밀려난 최민우의 귓가에, 착 가라앉은 누군가의 목소리가 닿았다.

“어디서 본 얼굴인가 했더니. 이제야 알겠어, 스카이의 핏줄.”

흉흉한 눈빛.

오러에 휘감긴 한 자루의 검을 든 채 다가오는 아랍인 사내를 바라보며, 최민우는 이 혼잡한 전장의 틈바구니에서 보이지 않는 한 사람을 향해 마음속으로 말을 건넸다.

‘모르겠습니다. 제가, 우리가 얼마나 버틸 수 있을지.’

그러나 한 가지 사실만큼은 누구보다 잘 알고 있었다.

싸워야 한다. 적들보다 먼저 쓰러져서는 안 된다.

설령 그것이 자신보다 훨씬 강한 상대라 해도.

스윽.

최민우는 사내를 향해 검을 겨누었다. 선명한 오러가 깃든 [영웅의 검]이 환한 빛을 토해 낸다.

허공에서 떨어져 내린 팔백여 명의 헌터들이 어둠 사이로 번져가는 광휘를 중심으로 뭉쳤다.

“빌어먹을 이교도 놈들. 지옥으로 보내 주마.”

흉흉한 미소를 띤 사내의 몸이 시야에서 사라진다. 동시에 터져 나온 검격이 본능적으로 고개를 숙인 최민우의 목덜미를 스쳤다.

사방에서 몰려드는 광신도들을 막아 내던 스켈레톤 킹이 사내를 향해 쏘아졌다.

콰앙!

무수한 굉음과 비명이 협곡을 휩쓸었다. 지면이 들썩이고 견고한 암반이 갈라진다.

수백여 년간 겪은 적 없던 피바람과 충격은 양옆으로 늘어선 절벽을 향해 고스란히 전해졌다.

입구로부터 수십 미터를 지나야 도달할 수 있는 협곡의 중심지까지도.

그리고 그 미세한 균열은, 풀려나서는 안 될 누군가가 자유를 되찾는 것을 조금이나마 도왔다.

투두둑. 쾅!

창처럼 길고, 창보다 두꺼운 뼛조각이 폭발하듯 튕겨 나간다. 동시에 수없이 으스러지고 끊어진 사지의 단면으로부터 새로운 피와 살이 차올랐다.

스륵. 뿌드득.

눈으로 보고도 믿을 수 없는 초고속 회복.

아니, 재생.

일백하고도 마흔다섯 번째 부활을 끝마친 도플갱어가 피에 젖은 이빨을 드러내며 웃었다.

“이런. 지금부터가 시작인데, 벌써 지쳤나?”

푸푹!

대답 대신 날아든 섬광이 미간을 관통한다. 창을 쥔 청년이 물기 하나 없이 메마른 입술을 달싹였다.

“아니. 이제 힘이 좀 날 것 같은데.”

그리고 그 순간.

띠링.

오직 한 사람만이 들을 수 있는 종소리가, 맑게 울려 퍼졌다.



* * *



초절정의 경지에 오른 직후, 나는 이미 초인(超人)의 반열에 들었다. 그것 하나만큼은 누구도 부정할 수 없는 사실이다.

그러나 초인이라 불리는 이들도 결국 한 사람의 인간에 불과하다.

부상을 입으면 고통스러워하고, 강한 상대를 만나면 긴장하고, 끊임없이 움직이다 보면 언젠가는 지치는. 그런 인간.

나도 바로 그 인간 중 하나다.

한 가지 차이점을 제외한다면.

띠링.



- [Lv.78 브로디 우즈]를 처치했습니다!

- 극소량의 경험치를 획득했습니다!

- 레벨 업!

- 레벨 업의 효과로 치유의 힘이 깃듭니다!

- 특별 디버프, [부서진 신체]가 치유의 힘을 거부합니다!

- 상태 이상, [피로]가 해제되었습니다!

- 상태 이상, [근육통]이 해제되었습니다!

- 상태 이상, [공력 고갈]이…….

.

.

.

줄줄이 떠오르는 시스템 메시지와 함께 흐릿해지던 시야가 선명해진다.

나는 눈 녹듯 사라지는 신체의 피로와 차오르는 공력을 느끼며 중얼거렸다.

“브로디 우즈. 브로디 우즈…….”

끝까지 기억해야 할 이름이다. 슬슬 한계에 다다르고 있던 나를 구해 준 영웅이니까.

두 번이나 죽음을 맞이한 희생자들 한 사람, 한 사람도 마찬가지였다.

그런 의미에서.

“죽어.”

서걱.

창날이 그린 궤적을 따라 비틀거리며 일어나던 도플갱어의 상반신이 비스듬히 미끄러진다.

그리고 동시에 이미 지긋지긋하게 봤던 그 광경이 다시 한번 눈앞에 펼쳐졌다.

스르륵.

무서운 속도로 차오르는 피와 살. 멀쩡하게 일어나는 도플갱어의 얼굴은 어느 때보다 여유로웠다.

“그만하지. 슬슬 한계일 텐데.”

“아냐. 할 만해.”

푹!

“얼마 안 남았군. 허세 부릴 필요 없어.”

“괜찮다니까.”

퍼걱, 촤아악!

“이제 진짜 마지막…….”

“어허.”

서걱!

다시 한번 부활한 도플갱어가 중얼거렸다.

“아니, 뭐 이런 씨발놈이…….”
```

## Final English reading copy

```markdown
# Chapter 815

*Whoooosh.*

The cold night wind swept over him from head to toe. Choi Minwoo brushed back his windblown hair and looked down at the canyon rushing toward them.

*There it is.*

The spearhead, spilling a frigid light, stood out at a glance even in the deep darkness.

He had collected countless masterpieces and artifacts over the years, but he still couldn’t help marveling at the strength and sharpness of the spear named White Flame.

*Though not as much as its owner.*

Choi Minwoo thought of Jin Taekyung.

When he first met him, he never could have imagined that the young man his age who’d joined a raid as a porter would reach the pinnacle of Hunters around the world in less than a year.

But Jin Taekyung had made the unimaginable real.

He had prevented countless disasters and achieved dazzling growth through the arduous journey.

The boldness and courage he showed in every crisis had time and again far outstripped even Choi Minwoo’s expectations, though he’d watched him from closer than anyone.

Just like today.

*I could tell something was different from usual…but Mr. Jin keeps moving another step ahead.*

When the Skeleton King’s undead had relayed what was happening, Choi had felt both surprised and a little left out. Before long, though, those feelings had turned to joy.

Solving alone a problem no one else could crack was proof that Jin had grown to the next level.

*With him, we can win.*

Jin Taekyung was the commander in chief leading them all, the general directing the battlefield—and the vanguard charging toward the enemy ahead of everyone else.

There was no way not to trust him, and no reason not to love him.

Even if countless obstacles and dangers lay along the path Jin Taekyung walked, that would never change.

*That’s a lot of them.*

Choi Minwoo gazed down at the ground, his eyes calm.

Hundreds of meters below, a black mass of enemies poured into the canyon like a wave.

Too many to count.

Their footsteps shook the earth, and a tremendous chorus of shouts rang out from every direction.

“—Allahu Akbar!”

“—Brothers and sisters, charge! To the promised land!”

“—The salvation God has granted us awaits!”

The fanatics who’d hidden from the world bellowed.

Ironically, the weapons in the hands of those crying out for God’s salvation were instruments of blood and death.

*They’re not people like us. They’re just enemies we have to bring down.*

Choi Minwoo repeated the thought to himself like a vow. No—all the Hunters looking down at the scene felt the same way.

They’d already seen it. They’d learned it the hard way.

Humans could be more good—or more evil—than any other living creature.

And monsters weren’t the only things that threatened this world.

Before Demon King Asmodeus descended, the people who had brought about countless wars and deaths had also been human, just like them.

Humanity had suffered because of them, and through that suffering learned a lesson it must never forget.

*There are monsters with red blood, too.*

And the Hunters gathered here existed for one reason, with one duty alone: to hunt those monsters.

*Shing.*

Blades appeared here and there, their cold edges gleaming.

The Hunters were visibly more exhausted than usual after their battle against the monster horde, but the determination in their eyes was stronger than ever.

*Fwoooosh!*

The wind grew fiercer. Their hearts pounded faster.

Dozens of eagles and griffins tilted their enormous wings and plunged toward the ground.

The fanatics’ shouts, which had sounded like an echo returning from far away, now thundered in everyone’s ears.

“Fight to the last person! Don’t fall back!”

Choi Minwoo swallowed. The wind of the battlefield stung his skin. The fanatics poured into the canyon, their madness so palpable it seemed he could reach out and touch it.

A massive Grand Mage and the Skeleton King, with hundreds of undead at his command, stood in their way. But not one of them was afraid.

To those people, this battle was a holy war. Even if they died, they would join the ranks of holy martyrs and stand by God’s side.

The warriors of God, who had already experienced the miracle of awakening, kicked off their camels and shot forward at blinding speed.

Three hundred meters. One hundred meters. Fifty meters.

The distance closed in a rush.

And then…

Impact.

*Boom! Kaa-boooom!*

“Graaagh!”

Flames devoured the darkness.

The vanguard, struck head-on by Magic Johnson’s attack magic, went up in flames with a scream. The brief gap left by their deaths was instantly filled by other fanatics, who charged the undead without hesitation.

*Crunch, craaack!*

The canyon wasn’t absurdly narrow, but it wasn’t wide, either.

Even so, the fanatics whom the Doppelganger had cultivated for many years shattered the undead battle line in an instant.

The fanatics’ convictions and hearts might already have been no different from a monster’s, but they were fundamentally unlike monsters.

Like any Hunter, they were strong and clever—and, most of all, they had two excellent commanders.

“Those are fallen demons! Wipe them all out!”

“Inshallah.”

One man rampaged at the front, shouting roughly. An old man watched the battlefield with a composed expression from the rear.

The two stood out amid the chaos. The moment Choi Minwoo spotted them, he instinctively understood.

The scale of their power.

*S-rank Hunters—or should I call them fanatics?*

They were powerful foes he couldn’t take on as he was now.

And yet, strangely, he wasn’t afraid.

The next moment, the old man glanced up at the sky, and his gaze met Choi’s. Still, Choi’s heart didn’t waver in the slightest.

*Shhk. Slice!*

The strike was a flash of light.

A streak of aura sprang from the old man’s waist and cleanly severed the neck of the griffin Choi Minwoo was riding.

The huge flying monster, its strength gone, tilted to one side.

*Fwoosh. Rattle!*

The wind turned violent, and Choi’s body pitched wildly.

But he didn’t panic. The dive had become a fall, and for some reason, the corners of his mouth lifted.

He didn’t care about the screams of the Hunters clinging to the griffin’s spine or the way they stared at him as if he were crazy.

*I don’t regret any of the choices I’ve made. I’ll just fight as hard as I can.*

His mind was calm. The sword in his hand felt as light as a feather. He felt as if he could do anything today.

The ground rushed closer, and the roar of some nameless fanatic struck his eardrums.

“For the great God, for the Prophet!”

Choi Minwoo laughed aloud, then suddenly spoke.

“For our Alliance Leader.”

His voice was low but powerful. It was the signal.

*Papat!*

Choi Minwoo—and all the Hunters—kicked off the body of the griffin plummeting straight toward the ground and soared away.

*Tap.*

His feet touched the ground first. The sword in his hand blurred.

*Whoosh! Chaaash!*

A sharp wind rose along the blade, cutting through the limbs of fanatics rushing at him from all sides.

A streak of light shot between the bodies collapsing in sprays of blood.

*Whoosh—bang!*

Choi raised his sword in time to block it, but that was all he could do.

Unable to withstand the tremendous force, he was driven back several steps. A voice, sunk low, reached his ears.

“I thought I knew that face. Now I see—you’re Sky’s blood.”

The Arab man approached, a sword wrapped in aura in his hand, his eyes full of malice.

Amid the chaos of the battlefield, Choi Minwoo spoke in his heart to someone he couldn’t see.

*I don’t know. I don’t know how long I—or we—can hold out.*

But there was one thing he knew better than anyone.

He had to fight. He couldn’t fall before the enemy did.

Even against an opponent far stronger than himself.

*Swish.*

Choi Minwoo pointed his sword at the man. The **Hero’s Sword**, imbued with brilliant aura, shone brightly.

The eight hundred or so Hunters who’d dropped from the sky gathered around the light spreading through the darkness.

“Damn heretics. I’ll send you all to hell.”

The man’s body vanished from sight, a vicious smile on his face. The sword strike that burst forth at the same time grazed Choi’s neck as he instinctively ducked.

The Skeleton King, who’d been holding off the fanatics swarming from all directions, shot toward the man.

*Boom!*

Countless roars and screams swept through the canyon. The ground heaved, and the solid bedrock split apart.

The wind and shock of a battle unlike anything the cliffs had experienced in hundreds of years traveled all the way to them.

Even to the center of the canyon, dozens of meters beyond its entrance.

And those tiny cracks helped, if only a little, to free someone who should never have escaped.

*Thud-thud. Bang!*

A bone shard as long as a spear and thicker than one blasted outward. At the same time, new flesh and blood welled up from the severed ends of countless shattered limbs.

*Slide. Crack.*

A high-speed recovery impossible to believe, even with his own eyes.

No—Regeneration.

The Doppelganger, having completed its one hundred and forty-fifth resurrection, grinned, baring teeth stained with blood.

“Oh. I thought this was just getting started. Are you tired already?”

*Thwack!*

A streak of light pierced the space between its eyes instead of answering. The young man holding the spear moved his dry, cracked lips.

“No. I think I’ve got a little more in me now.”

And at that moment—

*Ding.*

A bell rang out clearly, audible to one person alone.

* * *

The moment I reached the Supreme Peak realm, I’d already entered the ranks of the superhuman. That much was a fact no one could deny.

But even those called superhuman were ultimately just human beings.

They felt pain when injured, tensed up when facing a strong opponent, and eventually grew tired if they kept moving without rest.

I was one of those people, too.

Except for one thing.

*Ding.*

> **System**
>
> Lv. 78 Brody Woods defeated!
>
> Gained a tiny amount of EXP!
>
> Level Up!
>
> The effects of leveling up fill you with healing power!
>
> Special Debuff: Broken Body rejects the healing power!
>
> Status Effect: Fatigue removed!
>
> Status Effect: Muscle Pain removed!
>
> Status Effect: Internal Energy Depletion…
>
> …
>
> …

As System messages appeared one after another, my fading vision cleared.

I felt the fatigue melting away and my internal energy filling back up as I muttered:

“Brody Woods. Brody Woods…”

That was a name I had to remember to the end. He was a hero who’d saved me when I was nearing my limit.

So were each and every one of the victims who’d faced death twice.

With that in mind…

“Die.”

*Slice.*

The Doppelganger, staggering back to its feet, had its upper body slide diagonally away along the path traced by the spearhead.

And at the same time, the sight I’d grown sick of seeing played out before my eyes once again.

*Slither.*

Blood and flesh welled up at a terrifying speed. The Doppelganger rose, whole again, looking more relaxed than ever.

“That’s enough. You must be close to your limit by now.”

“Nope. I’m doing fine.”

*Thrust!*

“You can’t have much left. No need to bluff.”

“I told you, I’m fine.”

*Thud, splatter!*

“This really is the last—”

“Hey.”

*Slice!*

The Doppelganger, resurrected yet again, muttered:

“What the fuck is wrong with this bastard…?”
```
