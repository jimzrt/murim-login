<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0421.txt",
      "sha256": "281dc22be83580f0cf9665f3c9763f10de33b92d5c3097a08067bfe237ccb8f7",
      "bytes": 13146
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e6d032e4008d29b98407d1d73ad7d7b3e2fe14d7daf7926eb30197135b625e33",
      "bytes": 1717
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b86886be1e7715485612ee8679a0961b6d7917b8691159c8cdd0f00d4fb20687",
      "bytes": 139155
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4048a058614e8be52ba9e2dc7ab838ae3e4cf1e7acfdf332c68330277147a397",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3c86744ceb84eff8c0548bbc85c766492b672549ff66e0d980664625f18f3b30",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4cc0068de36c7f1a8432ab59052b123c4840b7d37e42192f5d15b6cdce0a59c4",
      "bytes": 128627
    }
  ],
  "estimated_tokens": 9142
}
-->

# Durable State Update — Chapter 421

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 421. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 421. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 421,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 421,
    "continuity_sources": [421],
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
    "The Arch Lich has appeared before Jin and claims authority over all undead monsters.",
    "The Arch Lich can observe Jin through Familiars and protect itself from Qi Sense with an unidentified powerful force.",
    "The Arch Lich seeks to corrupt Jin, whose soul and death energy it considers unusually powerful.",
    "Jin has launched an attack against the Arch Lich with White Flame; its outcome remains unresolved.",
    "The Arch Lich corrupted Lei Fei into the Death Knight Lord after Lei Fei's death.",
    "Choi Minwoo trusts Jin deeply and leads the allied fighters against the monsters.",
    "The city's transformation into one enormous Gate remains an active threat.",
    "The Skeleton Warlord remains intensely frightened by the Arch Lich, with the cause still unexplained.",
    "Wu Heixing is dead and Lee Jungryong has been reduced to black ash.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    420
  ],
  "open_questions": [
    "Can Jin and the allied Hunters stop the city's transformation into a Gate?",
    "What is the full extent of the Arch Lich's power and ability to observe or identify Jin?",
    "Will Jin's attack damage the Arch Lich?",
    "Why does the Skeleton Warlord react to the Arch Lich with such extreme fear?"
  ],
  "safe_through": 420,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 마계 as Demon Realm.",
    "Render 데스나이트 로드 as Death Knight Lord.",
    "Preserve Jin's profanity and the Arch Lich's archaic, taunting register.",
    "Render 바실리스크 as Basilisk."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 420
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 420
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃421화



헌터들 사이에서 오랜 격언처럼 전해지는 말이 있다.

마법사는 두 종류로 나뉜다. 대마도사. 그리고 대마도사가 아닌 자.

매직 존슨은 몸소 그 말이 사실임을 입증했다.

지구상에 존재하는 70억 인구를 통틀어 단 셋밖에 없다는 대마도사.

그중에서도 최강의 워 메이지(War Mage)인 그는 대격변 당시 셀 수 없이 많은 몬스터를 처치했고 숱한 전투를 승리로 이끌었다.

하지만 그런 엄청난 위업을 쌓은 매직 존슨조차 자존심을 굽히는 존재가 있었다.



‘이런 말은 하고 싶지 않지만…… 아크 리치의 마법은 나보다 한 수 위야. 조심해, 진.’



아크 리치는 그만큼 강대한 존재다. 놈을 상대함에 있어 한 치의 망설임도, 방심도 있어서는 안 된다.

- 인간, 어서!

나도 알아, 인마.

스켈레톤 워로드의 비명 같은 외침을 한 귀로 흘리며, 두 다리에 공력을 불어넣었다.

쩌저저적, 단단한 콘크리트 바닥이 전해지는 압력을 견디지 못하고 움푹 꺼진다. 살짝 무릎을 굽힌 뒤 힘차게 발을 굴렀다.

콰앙!

흡사 폭탄이 터지는 듯한 굉음과 함께, 나는 허공을 향해 빛살처럼 쏘아졌다.

맹렬한 바람이 전신을 스쳤고, 검은 로브를 날개처럼 펼친 아크 리치의 신형이 빠르게 가까워졌다.

- 너…….

보인다. 잘게 흔들리는 놈의 안광이.

온 힘을 다해 쏘아 보낸 백염(白炎)은 아크 리치를 둘러싼 무형의 방어막을 부수고 힘을 다해 떨어지는 중이었다.

‘와라.’

손을 뻗었다. 수 미터의 거리를 격하고 허공섭물(虛空攝物)로 끌어당긴 백염의 창대가 손아귀에 잡힌다.

‘지금!’

나는 힘차게 창을 내질렀다. 단전을 타고 솟구친 삼 갑자의 열양지기가 거침없이 내달렸다. 투명한 창날 위로 푸른 겁화와도 같은 강기가 터져 나왔다.

콰아아아!

그리고 성공을 확신한 그 순간.

- 그래비티(Gravity).

스아아악!

“흐읍!”

음산한 목소리와 함께 보이지 않는 무언가가 전신을 짓눌렀다.

아니, 후려쳤다.

숨을 삼키며 최대한 팔을 뻗었지만, 강기를 머금은 창날이 아크 리치의 발에 닿기도 전에 내 몸은 지상으로 떨어지고 있었다.

손만 뻗으면 닿을 것 같던 아크 리치의 신형이 순식간에 멀어진다.

“이런 개……!”

콰아아아앙!

굉음과 함께 유성처럼 추락한 내 머리 위로 쇠가 긁히는 듯한 웃음소리가 울려 퍼졌다.

- 제법이구나. 나름 재미있었다.

빌어먹을 해골 새끼. 나는 가래를 탁 뱉으며 마치 신처럼 굽어보는 아크 리치를 바라보았다.

“그거 잘됐네. 앞으로는 더 재밌어질 거거든.”

- 인간들은 늘 헛된 꿈을 꾸더군. 넘을 수 없는 것에 대한 분노와 열망으로 도전하고, 마침내 현실을 깨닫고 절망하는 모습을 수도 없이 보았다.

“지금까지 내 손에 뒤진 놈들이 늘어놓던 헛소리랑 비슷한데…… 혹시 너희들끼리 진태경 대응 백문백답 같은 거 공유하냐? 가끔 스터디도 열고 그래?”

- 그래 봤자 네 손에 죽은 놈들 역시 하찮은 인간. 하지만 나는 다르다.

“당연히 다르지. 이 시벌 놈아. 넌 이미 죽어 있으니까.”

- ……!

나는 순간 말문이 막힌 아크 리치를 향해 말을 이었다.

“지금 꼬라지를 보면 결국 너도 누구한테 죽었다는 얘긴데, 혹시 인간한테 죽었냐? 아까부터 왜 그렇게 자꾸 열등감 표출해?”

- 놈…….

“맞네. 이 새끼 인간한테 죽었네.”

- 닥치지 못할까!

쩌렁쩌렁한 외침과 동시에 아크 리치를 둘러싼 마력이 거세게 요동쳤다. 아까보다 훨씬 더 붉어진 안광이 나를 노려보고 있었다.

- 나는 위대한 왕을 따르는 신하. 너희와 같은 하찮은 존재에 비할 수 있는 몸이 아니다!

계속해서 쏘아붙이려던 나는 놈의 입에서 튀어나온 뜻밖의 단어에 멈칫했다.

잠깐. 왕이라고?

‘지금 내가 잘못 들은 건가?’

뇌리를 스치는 의문에, 스켈레톤 워로드가 떨리는 목소리로 대답했다.

- 보, 본 사령관도 똑똑히 들었다. 간악한 인간이여. 그, 그럼 설마…….

그럴 리가. 아니겠지. 마른 침을 꿀꺽 삼킨 내가 물었다.

“혹시 방금 말한 그 위대한 왕이라는 게, 마왕 아스모데우스냐?”

- 존귀하신 왕의 이름을 입에 담지 말라.

설마가 사람 잡는다더니. 바로 그 마왕 아스모데우스일 줄이야.

스켈레톤 워로드는 숨도 못 쉬는 주제에 헛숨을 들이켰고, 나는 도무지 믿기지 않아 작게 중얼거렸다.

“허, 진짜 아스모데우스?”

- 존귀하신 왕의 이름을…….

“하지만 아스모데우스는 분명히 소멸한 것으로 알고 있는데.”

- 존귀하신…….

“혹시 아스모데우스가 아직도 살아 있냐? 아크 마왕. 뭐 그런 걸로?”

- 존귀…….

“그래, 존나 귀여운 거 충분히 알겠으니까 대답해 봐. 아스모데우스라면 그때 죽은 거 아냐? 아니면 부활한 건가? 만약 너처럼 언데드로 부활한 거면 지금 어디서 뭐 하고 있어?”

그때 스켈레톤 워로드가 두려움 섞인 목소리로 중얼거렸다.

- 이 시간이면 주무시고 있지 않을까……?

무슨 개소리야. 너도 안 자는 주제에.

- 나야 그렇지만, 왕께서는 다르실 수도 있지.

마왕이 새 나라의 어린이냐. 해 떨어지면 TV 끄고 양치하고 자는 놈일 것 같아? 그리고 왜 극존칭 쓰냐.

- 아앗. 나도 모르게 그만…… 그런데 본 사령관 입장에서는 당연한 거 아닌가?

그건 그러네.

- 그렇지. 몬스터니까.

그러니까 쓰지 마.

- 어째서……?

마왕은 멀리 있고, 내 주먹은 가까이에 있으니까.

- 아아.

깨달음의 탄성을 토해 낸 스켈레톤 워로드가 덧붙였다.

- 그런데 인간. 잠시 후면 아크 리치의 마법이 더 가까워질 것 같은데.

빌어먹을. 그러네.

나는 황급히 몸을 날렸다. 아슬아슬하게 몸을 스친 초록빛 안개가 방금만 해도 내가 있던 자리를 덮었다.

치이이익!

돌, 강철, 콘크리트까지. 반경 수십 미터의 공간이 뻥 뚫린 것처럼 녹아 없어진다.

가공할 만한 위력의 독구름을 쏘아 보낸 아크 리치의 안광은 또렷하다 못해 횃불처럼 타오르고 있었다.

- 널 수하로 거둘 생각이었다.

“어, 갑자기?”

- 영혼과 육체를 굴복시키고, 영광스러운 언데드 군단의 선봉장으로 쓰려 했지.

“그거 연봉 얼마 주냐.”

- 하지만 생각을 고쳤다.

“아니, 연봉 얼마 주냐고. 설마 너네도 열정 페이야?”

- 네 육신은 갈기갈기 찢어질 것이며, 영혼은 죽음의 강을 영원히 떠돌게 될 것이다.

“혹시 나 어릴 때 다녔던 교회 집사님이랑 아는 사이냐. 그 양반도 나한테 비슷한 말 했었는데. 너 같은 마귀는 지옥 갈 거라고. 그때 엄마 안 말렸으면 그 교회 최초의 순교자 될 뻔했잖아.”

- 너, 하찮은 인간이여. 존귀하신 왕을 모욕하고 그분의 이름을 더럽힌 죗값을 치러라.

“모처럼 하고 싶은 말이 일치하네. 죗값. 그거 좋지.”

고개를 끄덕인 나는 백염을 비스듬히 늘어트렸다.

“그래서 나도 너한테 죗값을 받아 낼 생각인데…… 네 생각은 어때?”

다음 순간, 아크 리치가 입을 열었다.

더없이 깊고 음산한 목소리로 이루어진 네 글자는, 질문에 대한 대답이 아닌 죽음을 부르는 저주였다.

- 다크 핸드(Dark Hand).

후우웅!

짙은 안개를 뚫고 한 쌍의 검은 손이 튀어나왔다. 마치 합장을 하듯, 좌우에서 맹렬한 기세로 쇄도하는 다크 핸드를 피해 뛰어오른 나를 기다리는 것은 또 다른 마법이었다.

- 커즈(Curse).

그물처럼 덮쳐 오는 검은 안개를 피해 몸을 틀었지만, 이번에는 늦었다.

아니, 어쩌면 아크 리치는 내 움직임을 예상하고 있었을지도 모른다.

내가 다크 핸드를 피하기도 전에 안개가 덮여 오고 있었으니.

스윽.

고작 종이 한 장의 차이.

새끼손가락의 끝에 끈적한 안개가 스친 그 순간이었다.

삐빅.



- 상태이상, [저주]에 걸렸습니다!

- [저주]로 인하여 신체에 관련된 모든 능력치가 일시적으로 하락합니다!

- [근력]이 일시적으로 20 하락했습니다!

- [체력]이 일시적으로 20 하락했습니다!

- [민첩]이…….



시스템 알림이 들리기 무섭게 무거워진 신체를 느끼며, 나는 내심 혀를 찼다.

‘빌어먹을.’

포인트를 받아도 모자랄 판에 저주로 디버프가 걸려 버리다니.

1, 2도 아니고 단숨에 20씩 깎여 나가자 체감상 확실히 느껴진다.

하지만 제아무리 디버프가 걸렸다 해도 놈에게 속절없이 당할 정도는 아니었다.

바로 지금처럼.

- 다크 바인(Dark Vine).

콰직. 쏴아아아악!

지면을 뚫고 솟구친 수백 줄기의 가시넝쿨이 사방을 가득 메운 채 쏘아진다.

나는 짧게 호흡을 내뱉으며 창을 휘둘렀다. 서걱, 푸른 화염의 선이 그어지며 마력으로 이루어진 줄기가 모조리 잘려 나갔다.

- 다크 바인, 다크 바인, 다크 바인.

슈화아아악!

힘을 잃고 스러지던 가시넝쿨의 절단면에서 또 다른 넝쿨이 자라났다. 싹을 틔우고, 가시를 만들고, 더욱 거대하게 자라기까지 걸린 시간은 불과 1초 남짓.

하지만 1초라는 시간은 내게 1분이나 다름없는 시간이다.

화륵, 서걱!

수 미터의 둘레를 지닌 가시넝쿨이 단 일격에 잘렸다.

마력의 연결이 끊긴 어둠의 식물이 반쯤 무너져 있던 고층 빌딩을 덮치며 쓰러진다.

굉음과 함께 피어오른 먼지구름 사이로 심상치 않은 기의 파동이 느껴졌다.

‘마법.’

내 예상은 정확했다.

쉬쉬쉬쉬슁!

거무튀튀하게 물든 한 자루의 창. 오직 뼈로 이루어진 본 스피어(Bone Spear)가 한 줄기의 빛이 되어 나를 향해 쏘아진다.

아니. 아니다.

‘하나가 아니야.’

- 조심해라, 인간!

스켈레톤 워로드의 다급한 외침과 함께.

퍼엉!

압축된 공기와 함께 먼지구름이 터져 나갔다.

일일이 헤아릴 수 없을 만큼 많은 본 스피어가 나를 향해 쇄도했다. 어떤 것은 일직선으로. 어떤 것은 유성처럼 낙하했으며 곡선을 그리는 것도 있었다.

“허…….”

- 아.

나와 스켈레톤 워로드가 동시에 토해 낸 신음.

몇 개나 될까. 수백? 아니면 수천?

그 압도적인 광경에 나는 순간 할 말을 잃었다.

서늘한 기운이 등골이 타고 흘렀고 저절로 입이 벌어진다. 어느샌가 이마에 맺혀 있던 식은땀 한 방울이 콧날을 타고 미끄러졌다.

그리고…… 모든 것이 멈췄다.

‘이건…….’

위기의 때마다 종종 찾아왔던 바로 그 상황이다.

오감(五感)이 날카롭게 곤두서고 세상이 느려졌다. 그 사이를 비집고 낯선 무언가가 엄습해 왔다.

새로운 감각. 과학적으로 설명할 수 없는 여섯 번째 감각. 나는 그것의 이름을 알고 있다.

‘육감(六感).’

동시에 내 안의 무엇인가가 껍질을 벗었다.

수백, 수천 개의 본 스피어로 이루어진 거대한 그물을 훑던 눈동자가 천천히 느려진다.

이미 모든 것을 포기해서? 아니다. 중요한 건 본질이다. 형상은 덧씌울 수 있어도, 본질은 달라지지 않는다.

그리고 지금 이 순간, 나는 본질을 보고 있었다. 바짝 말라붙은 입술이 벌어지고 탄성이 흘러나왔다.

“아.”

그랬구나. 그런 거였어.

초절정에 올랐음에도 아직 깨닫지 못했었던 한 부분.

뇌리를 스치는 섬광 같은 깨달음과 함께, 느려진 세상이 제 시간을 찾아 움직였다.

사방을 가득 메운 채 쏟아지는 창의 비 앞에서, 나는 멍하니 창을 들었다. 보이는 길을 향해 백염을 내리그었다.

천격(天格).

콰아아아!

터져 나온 불꽃이 모든 것을 집어삼켰다. 감히 헤아릴 수조차 없었던 본 스피어가 사라졌다.

아니, 화염이 닿자마자 사라진 것은 마력으로 이루어진 허상이다. 오직 본질만이 내 일격과 부딪쳤고, 힘을 이기지 못해 타들어 갔다.

솨아아아.

어디선가 불어온 바람에 잿가루가 흩날렸다.

나는 바람 사이로 섞여 들어온 경쾌한 종소리를 들었다.

띠링. 띠링. 띠링…….

그건 나도 모르게 미소가 지어질 만큼, 듣기 좋은 소리였다.
```

## Final English reading copy

```markdown
# Chapter 421

There was an old saying passed down among Hunters.

Mages came in two kinds: archmages, and everyone else.

Magic Johnson had proven that saying true with his own body.

Among the seven billion people on Earth, there were only three archmages.

And even among those three, he was the strongest War Mage. During the Great Cataclysm, he had slain countless monsters and led innumerable battles to victory.

But even Magic Johnson, despite all those incredible achievements, had encountered someone before whom he had been forced to swallow his pride.

*I hate to say this, but the Arch Lich’s magic is a level above mine. Be careful, Jin.*

The Arch Lich was that powerful. There could be no hesitation or carelessness—not even for an instant—when facing it.

—Human, hurry!

*I know, damn it.*

I let the Skeleton Warlord’s shriek wash in one ear and out the other as I poured internal energy into both legs.

*Crack-crack-crack!*

The solid concrete floor sank beneath me, unable to withstand the pressure transmitted into it. I bent my knees slightly, then kicked off with all my strength.

*Boom!*

With a thunderous roar like an explosion, I shot into the air like a streak of light.

The fierce wind swept across my entire body, and the Arch Lich’s form rapidly drew closer, its black robe spread like wings.

—You…

I could see them.

The creature’s trembling red eyes.

White Flame, launched with all my strength, had shattered the invisible barrier surrounding the Arch Lich and was now falling with everything it had.

*Come.*

I stretched out my hand. The shaft of White Flame, pulled across several meters with Seizing an Object Through Empty Space, landed in my grasp.

*Now!*

I thrust the spear forward with all my strength. Three jiazi of Scorching Yang Qi surged up from my dantian and raced onward without restraint. Blue Force, like hellfire, erupted over the transparent spearhead.

*Fwoooooom!*

And just as I became certain of my success—

—Gravity.

*Fwoosh!*

“Hngh!”

Along with that sinister voice, something invisible pressed down on my entire body.

No.

It struck me.

I swallowed a breath and reached out as far as I could, but before the spearhead brimming with Force could touch the Arch Lich’s foot, my body was already falling toward the ground.

The Arch Lich’s form, which had seemed close enough to touch, receded in an instant.

“You fucking—”

*Booooom!*

As I crashed down like a meteor, a laugh like scraping metal rang out above my head.

—Not bad. That was rather entertaining.

*Damn skeleton bastard.*

I spat thickly and looked up at the Arch Lich looming over me as though it were a god.

“Good to hear. It’s only going to get more entertaining from here.”

—Humans are always dreaming futile dreams. I have seen it countless times: you challenge what cannot be surpassed, driven by anger and longing, only to finally realize reality and fall into despair.

“That sounds a lot like the bullshit spewed by all the guys who’ve died by my hand… Do you people share a *Hundred Questions and Answers for Dealing with Jin Taekyung* or something? Do you hold study sessions every now and then, too?”

—Even so, those who died by your hand were still insignificant humans. But I am different.

“Of course you’re different, you son of a bitch. You’re already dead.”

—…!

The Arch Lich fell silent for a moment, so I continued.

“Looking at your current state, that means someone killed you, too. Was it a human? Why have you been showing off your inferiority complex this whole time?”

—You…

“Yep. This bastard was killed by a human.”

—Will you shut your mouth!

At the thunderous shout, the magic surrounding the Arch Lich surged violently. Its red eyes had grown far brighter than before as they glared down at me.

—I am a servant who follows a great king. I am not a being who can be compared to insignificant creatures like you!

I was about to fire back again when I froze at the unexpected word that came from its mouth.

*Wait. A king?*

*Did I hear that wrong?*

A question flashed through my mind, and the Skeleton Warlord answered in a trembling voice.

—The commander heard it clearly, too. Wretched human. Th-then, could it be…

*No way. It can’t be.*

I swallowed dryly and asked,

“Is the great king you just mentioned the Demon King Asmodeus?”

—Do not speak the name of His Highness.

Never say never, I guess.

And it turned out to be the Demon King Asmodeus after all.

The Skeleton Warlord sucked in a breath despite not needing to breathe, while I muttered in disbelief,

“Huh. Asmodeus? Seriously?”

—The name of His Highness…

“But I was sure Asmodeus had been destroyed.”

—The name of His Highness…

“Is Asmodeus still alive? As an Arch Demon King or something?”

—His Highness…

“Yeah, yeah, I get it—he’s fucking adorable. Now answer me. Asmodeus died back then, didn’t he? Or did he resurrect? If he came back as an undead like you, where is he and what’s he doing now?”

At that moment, the Skeleton Warlord murmured in a fearful voice,

—If it is this time of day, he might be sleeping…

“What the fuck are you talking about? You don’t sleep, either.”

—I do not, but His Highness might be different.

“What is the Demon King, some good little schoolboy? Do you think he turns off the television, brushes his teeth, and goes to bed when the sun goes down? And why are you using such an honorific?”

—Ah! I did not realize I was doing it… But is it not natural from the commander’s perspective?

*That’s true.*

—It is. Because I am a monster.

“Then don’t use it.”

—Why not…?

“The Demon King is far away, and my fist is close.”

—Ah.

The Skeleton Warlord let out an exclamation of realization, then added,

—But, human. It seems the Arch Lich’s magic will be getting closer in a moment.

*Damn it. He’s right.*

I hurriedly threw myself aside. A green mist grazed my body by a hair and covered the spot where I had been standing only a moment before.

*Ssssssssss!*

Stone, steel, and even concrete melted away, leaving a gaping hole in a space several dozen meters wide.

The Arch Lich had fired a poison cloud of terrifying power. Its eyes were not merely clear—they burned like torches.

—I intended to take you as one of my servants.

“Uh, what brought that on all of a sudden?”

—I would have subdued your soul and body and used you as the vanguard of my glorious undead army.

“How much does it pay?”

—But I have changed my mind.

“No, I asked how much it pays. Don’t tell me you people pay in passion, too?”

—Your flesh will be torn to pieces, and your soul will wander the River of Death for all eternity.

“Are you acquainted with the deacon at the church I went to as a kid? He said something similar to me. That a devil like me would go to hell. If my mom hadn’t stopped me, he would’ve become the first martyr in that church’s history.”

—You insignificant human. Pay the price for insulting His Highness and defiling his name.

“For once, we agree on something. Paying the price. I like that.”

I nodded and lowered White Flame at an angle.

“So I’m planning to make you pay the price, too… What do you think?”

The Arch Lich opened its mouth.

The four-syllable incantation, uttered in a voice deeper and more sinister than ever, was not an answer to my question.

It was a curse that called forth death.

—Dark Hand.

*Whoooom!*

A pair of black hands burst through the thick fog. They charged fiercely from both sides, as though coming together in prayer.

I leaped to avoid the Dark Hands—and another spell was waiting for me.

—Curse.

I twisted my body to evade the black fog descending like a net, but this time, I was too late.

No.

Perhaps the Arch Lich had anticipated my movement.

The fog had already been closing in before I finished dodging the Dark Hands.

*Shhk.*

The difference was no more than a single sheet of paper.

At the instant the sticky fog grazed the tip of my little finger—

*Beep!*

> **System**
>
> - You have been afflicted with the status effect **Curse**!
> - Due to **Curse**, all physical attributes have been temporarily reduced!
> - **Strength** has temporarily decreased by 20!
> - **Stamina** has temporarily decreased by 20!
> - **Agility**…

As soon as the System notification rang out, I felt my body grow heavier and clicked my tongue inwardly.

*Damn it.*

Even when I was short on points, I had been hit with a debuff from a curse.

Not one or two points, either. With twenty points stripped away at once from each attribute, I could definitely feel the difference.

But even with a debuff, I was not so helpless that I could do nothing but take his attacks.

Just like now.

—Dark Vine.

*Crack! Whoooosh!*

Hundreds of thorny vines burst through the ground and filled the air in every direction as they shot toward me.

I exhaled briefly and swung my spear. *Shhk.* A line of blue flame traced through the air, slicing apart every vine made of magic.

—Dark Vine. Dark Vine. Dark Vine.

*Shwoooooosh!*

From the severed ends of the thorny vines, which had been collapsing after losing their strength, new vines began to grow.

They sprouted, formed thorns, and grew even larger in barely a second.

But one second was the same as a minute to me.

*Fwoom! Shhk!*

A thorny vine measuring several meters around was cut apart in a single blow.

The dark plant, severed from its magical connection, toppled over and crashed into a half-collapsed high-rise building.

Through the cloud of dust rising with the thunderous impact, I sensed an ominous wave of energy.

*Magic.*

My prediction was right.

*Shhh-shhh-shhh-shhh!*

A spear stained a dull black.

A Bone Spear made entirely of bones became a streak of light and shot toward me.

No.

That wasn’t it.

*There isn’t just one.*

—Be careful, human!

Along with the Skeleton Warlord’s desperate shout—

*Boom!*

The dust cloud exploded with compressed air.

An uncountable number of Bone Spears surged toward me.

Some flew in straight lines. Some fell like meteors. Others traced curving paths through the air.

“Huh…”

—Ah.

The Skeleton Warlord and I groaned at the same time.

*How many are there? Hundreds? No, thousands?*

The overwhelming sight left me speechless for a moment.

A chill ran down my spine, and my mouth fell open on its own. A bead of cold sweat that had formed on my forehead slid down the bridge of my nose.

And then…

Everything stopped.

*This is…*

It was the very situation that sometimes came to me in times of crisis.

My five senses grew razor-sharp, and the world slowed down. In the space between those moments, something unfamiliar came creeping toward me.

A new sense.

A sixth sense that could not be explained scientifically.

I knew its name.

*The sixth sense.*

At the same time, something inside me shed its shell.

My eyes, sweeping over the enormous net formed by hundreds—thousands—of Bone Spears, gradually slowed.

*Because I had already given up everything?*

No.

What mattered was the essence.

A form could be layered over it, but the essence itself did not change.

And at this very moment, I was seeing the essence.

My lips, cracked completely dry, parted, and an exclamation escaped me.

“Ah.”

*So that was it. That’s what it was.*

It was something I still had not realized, even after reaching the Supreme Peak.

Along with a flash of insight that streaked through my mind like lightning, the slowed world returned to its proper speed.

Before the rain of spears pouring down and filling every direction, I raised my spear absentmindedly.

I brought White Flame down along the path I could see.

*Heavenly Strike.*

*Fwoooooom!*

The flames that erupted swallowed everything.

The Bone Spears, too numerous to count, vanished.

No.

The things that vanished the instant the flames touched them were illusions made of magic.

Only the essence collided with my strike, and unable to withstand its power, it burned away.

*Shhhhhhh.*

Ash scattered in the wind that blew from somewhere.

Amid the breeze, I heard a bright, cheerful ringing.

*Ding. Ding. Ding…*

It was such a pleasant sound that I found myself smiling without realizing it.
```
