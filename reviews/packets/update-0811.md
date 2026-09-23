<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0811.txt",
      "sha256": "8c79267d5679eabede925dd22aa23564ed090fc3da70c0448741b883a29f34f8",
      "bytes": 14403
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bd508c795c6ce6bbfdf353ea12ddaa1d730297f67c343a70cacd037897ca1cd2",
      "bytes": 1352
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3e0066b207e48a33f064d3f052ca85030d9328740041c8d1bfc77f481ac6f9a8",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e70fa36e40e55a2dded7d5ab1185cf240252d0ddc063540ed528273c0ed512c3",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c4adfa4eda4903f8b9f7c7882b27bb1be4a4da9af46aed84769b57eef91d38ec",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "b28d95f60ef914588d3a8c9ed3e3c43b446478a3259d6160739c66fa371d5885",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "4ae3bfff23ac98c30cb177f9c4542a2e25b384ab9c018d69e5eae038866e6a1f",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "14674b8cad4ca54b120198c65b728a59ea2e39f29ddcb17a7b5684e05d54be2b",
      "bytes": 248340
    }
  ],
  "estimated_tokens": 9975
}
-->

# Durable State Update — Chapter 811

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 811. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 811. Profile updates may replace only one
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
  "chapter": 811,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 811,
    "continuity_sources": [811],
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
    "Jin is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Prophet within an unspecified time limit.",
    "The Prophet remains missing after the Hunter victory; Jin suspects the Prophet planned for the battle’s outcome, but the Prophet’s objective and location are unknown.",
    "Jin is preoccupied with unresolved questions about Michael Silbert and has not voiced them.",
    "The 185 Hunters killed in the battle have been buried in the desert; survivors vowed to return for their bodies and bring them to their families.",
    "The Ant Lion Jin interrogated said most fleeing monsters headed west and their leaders were dead; Jin told Johnson they went east, and the Skeleton King saw him."
  ],
  "continuity_sources": [
    809,
    810
  ],
  "open_questions": [
    "Where is the Prophet, what is his objective, and how is he directing events?",
    "What questions about Michael Silbert has Jin formed, and what is the single clue he has?",
    "Why did Jin lie to Johnson about the monsters’ direction, and how will the Skeleton King respond?"
  ],
  "safe_through": 810,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 810
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 810
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 810
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 810
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 808
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃811화



“동쪽. 동쪽이란 말이지.”

매직 존슨이 방향을 확인하기 위해 고개를 돌린 것은, 스켈레톤 킹에게 있어서 불행이었다.

그는 순간 얼굴 위로 드러난 경악을 숨기기 위해 안간힘을 써야 했다.

그러나 머릿속을 가득 채운 충격은 쉽게 사라지지 않았다.

‘도대체 어째서?’

몬스터인 스켈레톤 킹에게 마계어(魔界語)는 모국어나 다름없다.

대형의 후미를 맡아 경계하고 있던 매직 존슨과 달리, 줄곧 전방에서 진태경의 곁을 지켰던 그는 앞서 오간 대화를 충분히 알아들을 수 있었다.

‘놈은 분명 대부분의 몬스터들이 서쪽으로 갔다고 했다. 틀림없이 그렇게 말했어.’

머릿속이 혼잡하게 뒤섞였다.

얼굴색 하나 변하지 않은 진태경의 모습에 순간 착각이라도 했나 싶었지만, 틀림없었다.

몇 번이나 되새겨 보아도 조금 전의 기억은 변하지 않았다.

‘간악한 인간이…… 거짓말을 했다.’

그렇다면 진태경의 거짓말이, 지금의 이 상황이 의미하는 바는 무엇일까.

스켈레톤 킹은 짧은 고민 끝에 이 의문에 대한 답을 스스로 찾아냈다.

충분히 짐작하면서도, 애써 무시하고 있던 그 답을.

‘설마.’

마침내 믿기 힘든 현실을 마주한 스켈레톤 킹의 동공이 파르르 떨린 그때, 어둠에 잠긴 동쪽 어딘가를 향해 있던 매직 존슨의 시선이 그를 향해 움직였다.

“혹시 동쪽으로 네가 부리는 하수인들을…… 헤이. 지금 내 말 듣고 있나?”

“응? 아. 물론이다.”

“어딜 보고 있던 거야?”

자신도 모르게 진태경을 바라봤던 스켈레톤 킹이었지만, 곧이곧대로 대답할 수는 없다.

매직 존슨의 목소리를 듣는 순간 철렁 내려앉았던 가슴을 애써 수습한 그는 죽은 앤트 라이온의 사체를 향해 턱짓했다.

“저놈. 언데드로 되살리면 기동력이 괜찮을 것 같아서.”

“흠, 나쁘지 않네. 그런데 모래 깊숙이 파고 들어가는 특성이 있어서 우리 같은 인간들은 못 탈 거야. 지상에서 움직이면 몸집 때문에 너무 눈에 띌 테고.”

“그렇다면 포기해야지. 다시 생각해 보니 저런 놈을 부리려면 마력 소모가 심할 것 같군.”

제대로 대답한 걸까. 혹여 자신의 태도에서 이상한 점을 눈치챈 것은 아닐까.

천천히 턱을 쓰다듬는 매직 존슨의 모습에, 스켈레톤 킹은 마음속 불안함을 억누르며 빠르게 말을 이었다.

“그런데 무슨 말을 하려 했던 거지?”

“아, 그거. 네가 부리는 하수인들로 동쪽을 수색하지 않았는지 물어보려고 했지.”

“독수리와 그리핀들?”

“맞아. 이미 한 번 떠났다가 돌아오지 않았나? 몬스터들이 동쪽으로 도망쳤다면 눈에 띄었을 것 같은데.”

매직 존슨의 말은 사실이었다. 스켈레톤 킹은 이미 수하들을 동쪽으로 보냈다.

모두가 재정비하며 휴식을 취하고 있을 때 십여 마리의 독수리와 그리핀은 하늘을 가로질러 정신없이 도망치던 몬스터 군단을 쫓았다.

물론 금세 바닥을 드러낸 마력과 함께 언데드들의 추적도 아무런 소득 없이 멈췄지만, 최소한 동쪽으로 간 몬스터가 몇 없다는 사실쯤은 알고 있었다.

“그건…….”

스켈레톤 킹은 말꼬리를 흐렸다. 매직 존슨의 옆에 선 진태경이 깊게 가라앉은 눈빛으로 이쪽을 바라보는 것이 느껴졌다.

‘빌어먹을.’

모르겠다. 지금 하려는 선택이 맞는 것인지.

하지만 스켈레톤 킹은 언젠가 진태경이 했던 말을 떠올렸다. 자신뿐만 아니라 주위 사람들 모두의 불안감을 잠재웠던 그 한 마디를.



‘스스로를 믿지 못하겠다면, 날 믿어.’



떠올린다. 동시에 되새긴다.

그렇게 찰나의 망설임이 끝났다. 스켈레톤 킹은 담담하게 입을 열었다.

“금세 놓치긴 했지만, 대부분의 몬스터 군단이 동쪽으로 도망쳤을 확률이 높다.”

스켈레톤 킹은 진태경의, 아니 친구의 판단을 믿었다.

어쩌면 그 자신보다도 더.



* * *



앤트 라이온을 만나기 전부터, 이미 가슴 한구석에 남아 있던 갈등은 저 멀리 치워 버렸다.

이제 남아 있는 것은 이 의문의 실체를, 간신히 움켜쥔 이 실마리를 확인하기 위해 힘껏 잡아당기는 것뿐이었다.

‘하지만 지금 당장은 곤란하지.’

치밀해야 한다. 틈을 줘서는 안 된다.

빠르게 생각을 정리한 나는 수뇌부라 할 수 있는 몇몇 인물들을 한 자리에 불러 모았다.

“지금부터 병력을 나누어 이동합니다.”

불쑥 던진 첫 마디에 작은 동요가 사람들 사이로 번졌다. 가장 먼저 최 팀장이 이의를 제기했다.

“모두 함께 동쪽으로 이동하는 것 아니었습니까?”

대부분의 몬스터들은 동쪽으로 향했다.

그것이 스켈레톤 킹과 나를 제외한 다른 이들에게 알려진 사실이었고, 그런 의미에서 최 팀장의 말은 설득력이 있었다.

단, 그들이 아는 정보가 진실이라는 가정하에.

“최 팀장님.”

“예.”

“제가 언제 그런 말을 했습니까?”

“……하지만.”

“저도 압니다. 무슨 뜻으로 하신 말씀인지.”

스스로도 낯설게 느껴질 만큼, 평소와는 다른 건조한 목소리가 입술 사이로 흘러나온다.

나는 굳은 얼굴을 한 최 팀장을 응시하며 천천히 말을 이었다.

“하지만 앤트 라이온에게서 얻은 정보를 믿고 움직일 수는 없어요. 너무 위험합니다.”

“의도된 함정……일 수도 있다는 뜻입니까?”

“네.”

새삼 느꼈다. 나는 거짓말에 제법 소질이 있다.

더군다나 무림과 현대를 살아오며 깨달은 세상의 진리도 알고 있다.

‘권위.’

권위를 가진 자의 거짓말은 막강한 설득력을 지닌다. 그를 믿는 사람들의 믿음을 불러일으킨다.

바로 지금처럼.

“전투에서 패배하여 도망쳤다고는 하지만, 놈들의 머릿수는 아직도 우리의 다섯 배가 넘습니다.”

5천.

일만을 아득히 뛰어넘던 대군세가 단 한 번의 전투로 세 토막 났다. 그러나 피해를 입은 것은 아군도 마찬가지다.

엄청난 교환비로 승리했다고는 해도, 앞서 희생된 이백여 명은 전체 병력의 2할에 달했으니까.

몬스터 군단이 몇 번이나 잘라 먹어야 할 만큼 커다란 파이라면, 우리는 한입에 삼켜질 수도 있는 머핀이었다.

“신중하게 접근할 필요가 있어요. 분산해서 추격해야 합니다.”

내 말을 듣고 있던 샤오 쉔이 고개를 끄덕였다.

“저 역시 진 선생님의 말씀이 옳다고 생각합니다. 잘못된 정보로 움직였다간 함정에 빠지거나, 방향이 어긋나 몬스터들을 놓칠 수 있으니까요.”

“맞아. 차라리 병력을 나눠서 움직인다면 위험 확률을 줄일 수 있겠지.”

최 팀장이 미간을 좁히며 입을 열었다.

“분산하려는 의도는 알겠습니다만…… 반대로 각개 격파당할 위험이 있지 않겠습니까?”

지휘관이라면 충분히 우려해야 할 만한 부분이지만, 그럴 가능성은 극히 희박하다.

‘애초에 몬스터들이 도망친 방향은, 동쪽이 아닌 서쪽이니까.’

혀끝에서 맴도는 말을 삼킨 나는 망설임 없이 대답했다.

“각 부대의 간격을 좁히고 이동할 겁니다. 그렇다면 높은 마력 분포도로 인해 통신이 불안정한 것을 감안하더라도, 안정적인 통신을 확보할 수 있으니까요.”

“음. 나는 진의 제안에 동의해. 지금 얼추 계산해 보니 부대 간 간격은 100km 남짓이면 충분할 거야.”

불쑥 입을 연 매직 존슨을 말없이 바라보던 나는, 무거운 마음으로 그의 말을 받았다.

“맞아요. 추격 범위도 넓어지겠죠.”

룹 알 할리 사막.

세계에서 두 번째로 거대하다고 알려진 사막 지대답게, 그 넓이는 실로 광활하다.

의문을 제기하던 최 팀장조차 그 사실을 새삼 깨달았는지 마지못해 고개를 끄덕였다.

“각 추격대에 백 명씩 배치한다면…… 동쪽뿐만 아니라 동남, 동북까지 커버할 수 있겠군요. 알겠습니다. 그럼 지체할 시간이 없으니 빠르게 움직이도록 하죠.”

하지만 서두르려던 최 팀장은, 미처 한 걸음을 떼기도 전에 돌아서야 했다.

바로 그 순간 내가 던진 한마디 때문이었다.

“하나를 빠트리셨네요.”

“진태경 씨, 그게 무슨…….”

“서쪽. 저는 서쪽으로도 추격대를 보낼 생각입니다.”

“네?”

“그곳은 정반대잖습니까.”

“맞아요.”

나는 모두를 바라보며 말을 이었다.

“하지만 여기서 서쪽으로 몇 시간만 더 이동한다면, 석유 지대가 나오죠. 선지자가 제게 남긴 전언(傳言)이 가리키는 바로 그 장소.”

“……!”

“직접 들었으니 네 입으로 말해. 맞지?”

내가 마지막에 덧붙인 물음이 향한 곳은 야마모토 겐지였다.

병력을 분산한다는 이야기가 나왔을 때부터 줄곧 울상을 짓고 있던 녀석은, 자신을 향해 쏠린 사람들의 시선에 눈치를 살피며 고개를 끄덕였다.

“어, 음. 검은 보석이 묻혀 있는 땅이라고 했으니까. 우선은 맞는 것 같긴 한데…….”

“그럼 됐어. 우리는 서쪽으로 간다.”

“잠깐. 우리요?”

“그래. 우리. 너, 나. 스켈레톤 킹. 그리고 매직 존슨까지.”

내 말을 들은 야마모토 겐지의 얼굴이 새하얗게 질렸다.

“아니, 진 사마! 그런 게 어디 있습니까!”

“여기 있어.”

“이런 말도 안 되는…… 저는 빼 주십시오! 다른 사람들과 함께 있고 싶습니다!”

“안 돼. 안 빼 줘. 빼 줄 생각 없어. 돌아가.”

단호하게 대답한 나는, 이 뜻하지 않은 상황에 눈만 깜빡이고 있는 사람들을 향해 말을 이었다.

“우리가 이곳에 온 진정한 목적은 몬스터 군단이 아니라 선지자입니다. 적어도 놈이 남긴 말을 따라 그곳까지는 가 봐야 해요. 금방 돌아갈 테니, 그때까지는 충돌을 피하면서 남은 몬스터들을 추격하십시오.”

“안 됩니다!”

멍하니 나를 바라보던 최 팀장이 버럭 외쳤다.

“상식적으로 애초에 서쪽에 선지자가 있었다면, 몬스터들이 굳이 정반대인 동쪽으로 도망칠 이유가 없지 않습니까!”

“맞아요. 하지만 앤트 라이온이 그랬듯 대부분의 몬스터들이 선지자의 존재를 모른다면, 동쪽으로 도망칠 이유는 충분하죠.”

“진태경 씨. 선지자가 정말 그곳에 있다고 믿으시는 겁니까?”

“모릅니다. 하지만 선지자가 없다고 해도 최 팀장님과 다른 사람들이 몬스터들을 추격하고 있으니 문제 될 것은 없고, 놈이 서쪽에 있다면…… 이 전력으로도 충분히 상대할 수 있을 겁니다.”

S급 헌터만 무려 셋.

아니, 스켈레톤 킹까지 포함한다면 넷이다. 더군다나 녀석이 지닌 능력이 있다면, 언데드 병사들과 함께 전투를 치를 수도 있다.

“그건…….”

최 팀장이 말꼬리를 흐린 그때.

나는 무언가 말하려는 듯, 입술을 달싹이는 그에게 결정타를 꽂았다.

“이건 명령입니다.”

“……!”

“서두르세요. 놈들이 더 멀리 도망치기 전에.”

그 말을 끝으로 나는 돌아섰다.

그리고 아까부터 줄곧 말 한마디 없이 자리를 지키던 누군가를 향해, 흘리듯 전음(傳音)을 쏘아보냈다.

- 지금부터 내가 하는 말에 어떤 대답도, 반응도 하지 말고 들어.

짧은 순간. 거세게 흔들리던 스켈레톤 킹의 눈빛이 이내 깊게 가라앉았다.



* * *



일방적인 논의가 끝난 직후, 나는 짧은 운기조식을 끝마친 뒤 서쪽을 향해 출발했다.

물론 혼자는 아니었다.

스켈레톤 킹과 매직 존슨, 그리고 야마모토 겐지까지.

비록 숫자는 넷뿐이었지만 전력은 강력했고, 이동하는 속도는 병력과 함께 움직이던 때와는 비교조차 할 수 없을 만큼 쾌속했다.

쐐애애액!

빠르게 스쳐 지나가는 풍경 사이사이로 웅덩이처럼 고여 있는 끈적한 핏물이 보인다.

굳이 자세히 확인하지 않아도 상당한 출혈과 범위.

고작 몇십 마리가 흘릴 수 있는 것이 아니다. 앤트 라이온의 했던 말은 전부 사실이었다.

‘중요한 건 따로 있지만.’

내심 중얼거린 나는 계속해서 달렸다. 언덕이 굽이진 사막 지대를 넘고, 탁 트인 황야를 지나쳤다.

그렇게 삼십여 분쯤을 달렸을까?

두 개의 절벽이 서로를 향해 마주 선 협곡 앞에 이르러서야, 서서히 발걸음을 늦췄다.

“허억. 헉. 조, 조금만 천천히 가면 안 됩니까?”

숨을 헐떡이는 야마모토 겐지의 모습에, 매직 존슨이 땀에 젖은 이마를 닦으며 내게 말했다.

“진. 여기서 잠시 쉬었다 가는 건 어때? 몬스터도 딱히 안 보이는데.”

대답 대신 완전히 발걸음을 멈춘 나는 천천히 주위를 둘러보았다.

저 멀리 이어진 절벽. 좁은 틈새. 좋은 지형이다.

주어진 공간도 좁고, 도주로도 좁다.

고개를 들어 하늘을 바라보니, 저 멀리 사막지대를 비추는 흐릿한 달빛 위로 날갯짓하는 그림자가 보였다.

‘독수리.’

내 시선을 따라 고개를 움직인 매직 존슨이 미간을 찌푸렸다.

“아직도 날짐승이 있군. 마력 분포도 때문에 서식하는 건 거의 불가능할 텐데.”

“불가능하진 않죠. 평범한 독수리가 아니라면.”

“뭐?”

매직 존슨이 그 말의 의미를 이해하지 못해 눈을 깜빡이던 그때, 나는 협곡의 입구를 막아섰다.
```

## Final English reading copy

```markdown
# Chapter 811

“East. You mean east.”

Magic Johnson turned his head to confirm the direction. For the Skeleton King, that was unfortunate.

He had to fight to hide the shock that flashed across his face.

But the shock filling his mind didn’t fade so easily.

*Why on earth?*

To the Skeleton King, a monster, the Demon Realm language was practically his mother tongue.

Unlike Magic Johnson, who had been watching the rear of the formation, he’d stayed beside Jin Taekyung at the front the whole time. He’d heard enough of the conversation to understand it perfectly.

*He definitely said most of the monsters went west. I’m sure of it.*

His thoughts tangled together in confusion.

For a moment, he wondered if Jin Taekyung’s expression—unchanged down to the color of his face—had somehow tricked him. But no. There was no mistake.

No matter how many times he went over it, his memory of what had just happened stayed the same.

*That vile human… lied.*

So what did Jin Taekyung’s lie, and this situation now, mean?

After a brief moment of thought, the Skeleton King found the answer himself.

The answer he’d already suspected, but had tried so hard to ignore.

*No way.*

Just as the Skeleton King’s pupils trembled at last as he faced an unbelievable reality, Magic Johnson’s gaze shifted from somewhere in the darkened east to him.

“Did you send your minions east to search—hey. Are you listening to me?”

“Hm? Oh. Of course.”

“What were you looking at?”

The Skeleton King had found himself looking at Jin Taekyung, but he couldn’t exactly say so.

The instant he heard Magic Johnson’s voice, his heart had lurched. He forced himself to settle down, then gestured with his chin toward the dead Ant Lion’s corpse.

“That one. I thought it might have decent mobility if I brought it back as an undead.”

“Hmm, not a bad idea. But it can burrow deep into the sand, so humans like us couldn’t ride it. And if it moved aboveground, its size would make it too conspicuous.”

“Then I’ll give up on it. Now that I think about it, controlling something like that would take a lot of magical power.”

Had he answered convincingly? Had Magic Johnson noticed anything strange about his behavior?

As Johnson slowly stroked his chin, the Skeleton King pushed down his anxiety and hurriedly continued.

“But what were you going to ask?”

“Oh, right. I was going to ask if you’d sent your minions to search the east.”

“The eagles and griffins?”

“Right. Didn’t they go out once already and come back? If the monsters fled east, I’d think they would’ve spotted them.”

Magic Johnson was right. The Skeleton King had already sent his subordinates east.

While everyone else regrouped and rested, a dozen or so eagles and griffins had taken to the sky and chased after the monster army as it fled in a panic.

Of course, the Skeleton King had soon run low on magical power, and the undead’s pursuit had ended without yielding anything. But at the very least, the Skeleton King knew there had been few monsters heading east.

“Well…”

The Skeleton King let his voice trail off. He could feel Jin Taekyung, standing beside Magic Johnson, watching him with a gaze gone dark and still.

*Damn it.*

He didn’t know whether the choice he was about to make was the right one.

But then he remembered something Jin Taekyung had once said. The words that had calmed not only him, but everyone around him.

*If you can’t trust yourself, trust me.*

He remembered. And at the same time, he repeated the words to himself.

Then, in an instant, his hesitation ended. The Skeleton King spoke evenly.

“I lost sight of them quickly, but there’s a good chance most of the monster army fled east.”

The Skeleton King trusted Jin Taekyung’s judgment—no, his friend’s judgment.

Maybe even more than he trusted his own.

* * *

Even before we met the Ant Lion, I’d already put the conflict lingering in the back of my mind far behind me.

All that remained was to pull hard on the thread I’d barely managed to grasp and find out what this mystery really was.

*But I can’t do that right away.*

I had to be meticulous. I couldn’t leave them an opening.

After quickly sorting out my thoughts, I gathered several of the people who could be considered the leaders.

“We’ll split up our forces and move out.”

My blunt opening sent a ripple of unease through the group. Team Leader Choi was the first to object.

“Weren’t we all going east together?”

Most of the monsters had headed east.

That was what everyone knew except the Skeleton King and me, so Team Leader Choi’s question made sense.

Assuming, of course, that the information they had was true.

“Team Leader Choi.”

“Yes?”

“When did I say that?”

“……But—”

“I know what you mean.”

My voice came out dry and unfamiliar, even to me. I stared at Team Leader Choi’s stiff face and continued slowly.

“But we can’t trust information we got from the Ant Lion and act on it. It’s too dangerous.”

“Do you mean it could have been an intentional trap?”

“Yes.”

It struck me again: I was pretty good at lying.

And on top of that, I knew one of the truths of the world I’d learned by living in both the Murim and the modern world.

*Authority.*

A lie told by someone with authority carries tremendous power to persuade. It calls forth the trust of the people who believe in him.

Just like now.

“They may have lost the battle and run, but they still outnumber us by more than five to one.”

Five thousand.

An army that had once numbered well over ten thousand had been cut down to a third in a single battle. But our side had taken losses, too.

Even with such an overwhelming kill ratio, we’d lost more than two hundred people. That was a fifth of our total force.

If the monster army was a pie so big it would take several slices to finish, we were a muffin someone could swallow in one bite.

“We need to proceed carefully. We should split up and pursue them.”

Xiao Shen, who’d been listening to me, nodded.

“I also believe you’re right, Sir Jin. If we act on false information, we could walk into a trap or head in the wrong direction and lose the monsters.”

“Exactly. Splitting up would lower the risk.”

Team Leader Choi furrowed his brow.

“I understand why you want to split up, but… wouldn’t that leave us vulnerable to being picked off one by one?”

It was a concern any commander should have, but the chance of that happening was extremely low.

*The monsters fled west, not east, to begin with.*

I swallowed the words hovering at the tip of my tongue and answered without hesitation.

“We’ll keep the units close together. That way, even with the unstable communications caused by the high concentration of magical power, we can maintain a reliable connection.”

“Hmm. I agree with Jin. I’ve done a rough calculation, and a hundred kilometers or so between units should be enough.”

I looked silently at Magic Johnson, who’d spoken up without warning, then replied with a heavy heart.

“That’s right. We’ll cover more ground, too.”

The Rub’ al Khali Desert.

As the world’s second-largest desert, it was truly vast.

Even Team Leader Choi seemed to realize anew how large it was. He reluctantly nodded.

“If we assign a hundred people to each pursuit unit… we could cover the southeast and northeast as well as the east. Understood. There’s no time to waste, so we should move quickly.”

But Team Leader Choi, who’d been about to hurry off, had to turn back before he could take a single step.

It was because of what I said at that very moment.

“You’ve left one thing out.”

“Mr. Jin Taekyung, what do you mean—”

“West. I plan to send a pursuit unit west, too.”

“What?”

“That’s the complete opposite direction.”

“That’s right.”

I looked around at everyone and continued.

“But if we travel a few more hours west from here, we’ll reach the oil fields. The very place the message The Prophet left for me points to.”

“……!”

“You heard it yourself, so say it. Am I right?”

My last question was directed at Yamamoto Genji.

He’d been looking miserable ever since I’d brought up splitting the forces. Now, with everyone watching him, he glanced around nervously and nodded.

“Uh, well. He said it was a land where black jewels were buried, so I think that’s probably right…”

“Good enough. We’re going west.”

“Wait. We are?”

“Yes. Us. You, me, the Skeleton King, and Magic Johnson.”

Yamamoto Genji’s face went deathly pale.

“Jin-sama! Where does that even happen?”

“Right here.”

“This is ridiculous… Leave me out of it! I want to stay with the others!”

“No. I’m not leaving you out. I have no intention of leaving you out. Go back.”

After answering firmly, I continued speaking to the people who were blinking at this unexpected turn of events.

“Our real reason for coming here wasn’t the monster army. It was The Prophet. We need to follow his message at least as far as the place it points to. We’ll be back soon. Until then, avoid any clashes and keep pursuing the remaining monsters.”

“No!”

Team Leader Choi, who’d been staring at me blankly, shouted in protest.

“Common sense says that if The Prophet were in the west to begin with, the monsters would have no reason to run in the exact opposite direction, east!”

“That’s true. But if, like the Ant Lion, most of the monsters don’t know The Prophet exists, then they have every reason to run east.”

“Mr. Jin Taekyung. Do you really believe The Prophet is there?”

“I don’t know. But even if he isn’t, you and the others will still be pursuing the monsters, so nothing will go wrong. And if he’s in the west… we’ll have enough strength to take him on.”

There were three S-rank Hunters.

No, four, if we counted the Skeleton King. And with his abilities, he could fight alongside his undead soldiers, too.

“But…”

Team Leader Choi let his words trail off.

Just as he parted his lips to say something, I delivered the final blow.

“This is an order.”

“……!”

“Hurry. Before they get any farther away.”

With that, I turned around.

Then, toward someone who’d been standing there in silence all this time, I sent a Sound Transmission so casually it might have passed for a breath.

—From now on, don’t answer or react to anything I say. Just listen.

For a brief moment, the Skeleton King’s eyes, which had been trembling violently, settled into a deep stillness.

* * *

Immediately after the one-sided discussion ended, I finished a short session circulating my qi and set out west.

Of course, I wasn’t alone.

The Skeleton King, Magic Johnson, and Yamamoto Genji came with me.

There were only four of us, but we were a powerful force, and we moved at a speed that couldn’t compare to when we’d been traveling with the army.

*Whoosh!*

Through the landscape flashing past us, I saw puddles of thick, sticky blood.

I didn’t need to look closely to know there was a lot of it, spread over a wide area.

It couldn’t have come from a few dozen monsters. Everything the Ant Lion had said was true.

*Though that isn’t the important part.*

I kept running, muttering to myself. We crossed rolling dunes and passed through an open stretch of wilderness.

After running for a little over thirty minutes, we finally reached a canyon where two cliffs faced each other. Only then did I start to slow down.

“Hah… Hah. C-could you slow down a little?”

Seeing Yamamoto Genji panting, Magic Johnson wiped his sweat-soaked forehead and spoke to me.

“Jin. How about we rest here for a bit? I don’t see any monsters around.”

Instead of answering, I came to a complete stop and slowly looked around.

Cliffs stretching into the distance. A narrow passage. Good terrain.

Little room to move. A narrow escape route.

I looked up at the sky. In the distance, I saw a shadow flapping its wings against the faint moonlight over the desert.

*An eagle.*

Following my gaze, Magic Johnson frowned.

“Still seeing birds out here, huh? With this concentration of magical power, it should be almost impossible for them to live here.”

“Not impossible, if they aren’t ordinary eagles.”

“What?”

While Magic Johnson blinked, unable to understand what I meant, I blocked the canyon entrance.
```
